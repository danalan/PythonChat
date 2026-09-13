import json, math
from datetime import datetime
import numpy as np
from scipy.optimize import minimize
from scipy.special import gammaln
import parlay_replay_dc as p

ALL=p.load_all(); TR=p.training_for(ALL,'2025-02-07',True); ASOF=datetime(2025,2,7)
RHO_VALUES=[-0.07762,-0.05,0.0]
TARGET={(a,b):t for a,b,t in p.J6_TARGET}
FIX={x[0]:x for x in p.J6_FIXTURES}

def fit(hl,rho):
    teams=sorted({m.home for m in TR}|{m.away for m in TR}); idx={t:i for i,t in enumerate(teams)}; n=len(teams)
    # attack n-1 sum0, defense n, intercept, home advantage; rho fixed
    x0=np.zeros((n-1)+n+2); x0[-2]=math.log(np.mean([m.hg+m.ag for m in TR])/2); x0[-1]=0.15
    def unpack(x):
        a=np.r_[x[:n-1],-np.sum(x[:n-1])]; d=x[n-1:n-1+n]; b=x[-2]; h=x[-1]; return a,d,b,h
    def obj(x):
        a,d,b,h=unpack(x); z=0.
        for q in TR:
            l=math.exp(b+h+a[idx[q.home]]+d[idx[q.away]]); m=math.exp(b+a[idx[q.away]]+d[idx[q.home]])
            tt=p.dc_tau(q.hg,q.ag,l,m,rho)
            if tt<=0:return 1e12
            age=max(0.,(ASOF-q.date).total_seconds()/86400.)
            w=math.exp(-age/hl)
            z-=w*(q.hg*math.log(l)-l-gammaln(q.hg+1)+q.ag*math.log(m)-m-gammaln(q.ag+1)+math.log(tt))
        return z
    res=minimize(obj,x0,method='L-BFGS-B',options={'maxiter':5000,'ftol':1e-13,'gtol':1e-9,'maxls':100})
    a,d,b,h=unpack(res.x)
    def matrix(home,away):
        l=math.exp(b+h+a[idx[home]]+d[idx[away]]); m=math.exp(b+a[idx[away]]+d[idx[home]])
        xs=np.arange(20); ph=np.exp(xs*np.log(l)-l-gammaln(xs+1)); pa=np.exp(xs*np.log(m)-m-gammaln(xs+1)); M=np.outer(ph,pa)
        for xx,yy in [(0,0),(0,1),(1,0),(1,1)]:M[xx,yy]*=p.dc_tau(xx,yy,l,m,rho)
        M/=M.sum(); return M
    return matrix

def eval_rho(rho):
    mods=[fit(h,rho) for h in p.HALF_LIVES]
    out={}
    for fid,c,t in p.J6_TARGET:
        _,_,home,away=FIX[fid]; M=sum(f(home,away) for f in mods)/len(mods); got=p.probs(M)[c]
        out[fid+'|'+c]={'target':t,'got':got,'err':got-t}
    _,_,home,away=FIX['J6-08']; M=sum(f(home,away) for f in mods)/len(mods)
    out['PUMAS_U2.5']={'target':0.7421193625777459,'got':p.probs(M)['TEAM_TOTALS|HOME_UNDER_2.5']}
    out['PUMAS_O0.5']={'got':p.probs(M)['TEAM_TOTALS|HOME_OVER_0.5']}
    return out
print(json.dumps({str(r):eval_rho(r) for r in RHO_VALUES},ensure_ascii=False,indent=2))
