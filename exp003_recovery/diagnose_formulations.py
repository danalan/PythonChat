import math, json
from datetime import datetime
import numpy as np
from scipy.optimize import minimize
from scipy.special import gammaln
import parlay_replay_dc as p

ALL=p.load_all(); TR=p.training_for(ALL,'2025-02-07',True)
TARGET={(a,b):t for a,b,t in p.J6_TARGET}

def tau(x,y,l,m,r): return p.dc_tau(x,y,l,m,r)

def fit_variant(hl, variant):
    teams=sorted({m.home for m in TR}|{m.away for m in TR}); idx={t:i for i,t in enumerate(teams)}; n=len(teams)
    # variant A: intercept + attack constrained sum0 + defense free (current)
    # B: no intercept + attack constrained sum0 + defense free
    # C: intercept + attack sum0 + defense sum0
    if variant=='A': size=(n-1)+n+3
    elif variant=='B': size=(n-1)+n+2
    elif variant=='C': size=(n-1)+(n-1)+3
    else: raise ValueError
    x0=np.zeros(size)
    if variant in ('A','C'):
        x0[-3]=math.log(np.mean([m.hg+m.ag for m in TR])/2); x0[-2]=0.15; x0[-1]=-0.05
    else:
        x0[-2]=0.15; x0[-1]=-0.05
    def unpack(x):
        if variant=='A':
            a=np.r_[x[:n-1],-np.sum(x[:n-1])]; d=x[n-1:n-1+n]; b=x[-3]; h=x[-2]; r=x[-1]
        elif variant=='B':
            a=np.r_[x[:n-1],-np.sum(x[:n-1])]; d=x[n-1:n-1+n]; b=0.; h=x[-2]; r=x[-1]
        else:
            a=np.r_[x[:n-1],-np.sum(x[:n-1])]; off=n-1; d=np.r_[x[off:off+n-1],-np.sum(x[off:off+n-1])]; b=x[-3]; h=x[-2]; r=x[-1]
        return a,d,b,h,r
    def obj(x):
        a,d,b,h,r=unpack(x); z=0.
        for q in TR:
            l=math.exp(b+h+a[idx[q.home]]+d[idx[q.away]]); m=math.exp(b+a[idx[q.away]]+d[idx[q.home]])
            tt=tau(q.hg,q.ag,l,m,r)
            if tt<=0: return 1e12
            age=(datetime(2025,2,7)-q.date).days
            w=math.exp(-age/hl)
            z-=w*(q.hg*math.log(l)-l-gammaln(q.hg+1)+q.ag*math.log(m)-m-gammaln(q.ag+1)+math.log(tt))
        return z
    bounds=[(None,None)]*(size-2)+[(-1,1),(-.3,.3)]
    if variant in ('A','C'):
        bounds=[(None,None)]*(size-3)+[(None,None),(-1,1),(-.3,.3)]
    res=minimize(obj,x0,method='L-BFGS-B',bounds=bounds,options={'maxiter':8000,'ftol':1e-14,'gtol':1e-10,'maxls':100})
    a,d,b,h,r=unpack(res.x)
    def matrix(home,away):
        l=math.exp(b+h+a[idx[home]]+d[idx[away]]); m=math.exp(b+a[idx[away]]+d[idx[home]])
        xs=np.arange(16); ph=np.exp(xs*np.log(l)-l-gammaln(xs+1)); pa=np.exp(xs*np.log(m)-m-gammaln(xs+1)); M=np.outer(ph,pa)
        for xx,yy in [(0,0),(0,1),(1,0),(1,1)]: M[xx,yy]*=tau(xx,yy,l,m,r)
        M/=M.sum(); return M
    return matrix,res.fun

def eval_variant(v):
    models=[fit_variant(h,v)[0] for h in p.HALF_LIVES]
    vals={}
    fixtures={x[0]:x for x in p.J6_FIXTURES}
    for fid,c,t in p.J6_TARGET:
        _,_,home,away=fixtures[fid]; Ms=[f(home,away) for f in models]; M=sum(Ms)/len(Ms)
        pr=p.probs(M)[c]; vals[fid+'|'+c]={'got':pr,'target':t,'err':pr-t}
    # diagnostics for Pumas under and all target ranking contracts
    fid='J6-08'; _,_,home,away=fixtures[fid]; M=sum(f(home,away) for f in models)/len(models)
    vals['PUMAS_U2.5']={'got':p.probs(M)['TEAM_TOTALS|HOME_UNDER_2.5'],'target':0.7421193625777459}
    return vals

out={}
for v in ['A','B','C']:
    try: out[v]=eval_variant(v)
    except Exception as e: out[v]={'error':repr(e)}
print(json.dumps(out,ensure_ascii=False,indent=2))
