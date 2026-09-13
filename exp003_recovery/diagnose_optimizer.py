import json, math
from datetime import datetime
import numpy as np
from scipy.optimize import minimize
from scipy.special import gammaln
import parlay_replay_dc as p

ALL=p.load_all(); TR=[m for m in ALL if m.date < datetime(2025,1,10)]; ASOF=datetime(2025,1,10)
FIX={'J1-01':('Gallos Blancos','CF América'),'J1-03':('Club Tijuana','Deportivo Toluca'),'J1-05':('CF Monterrey','Puebla FC'),'J1-06':('Deportivo Guadalajara','Santos Laguna'),'J1-08':('Pumas UNAM','Club Necaxa')}
REF={
'J1-01':{'HOME':.1528465072043198,'DRAW':.2448419924548112,'AWAY':.6023115003408691,'OVER_2.5':.4804085691075246},
'J1-03':{'HOME':.2815287030638931,'DRAW':.2482744414842101,'AWAY':.4701968554518968,'OVER_2.5':.6083459289781771},
'J1-05':{'HOME':.7678854037252519,'DRAW':.1525191559096011,'AWAY':.0795954403651469,'OVER_2.5':.6720335112737199},
'J1-06':{'HOME':.6301823415365048,'DRAW':.2340571514348059,'AWAY':.1357605070286892,'OVER_2.5':.4854615882568141},
'J1-08':{'HOME':.5738052229420694,'DRAW':.2427365839689352,'AWAY':.1834581930889955,'OVER_2.5':.5333926985861029}}

def mprobs(M):
    return {'HOME':float(np.tril(M,-1).sum()),'DRAW':float(np.trace(M)),'AWAY':float(np.triu(M,1).sum()),'OVER_2.5':float(sum(M[i,j] for i in range(M.shape[0]) for j in range(M.shape[1]) if i+j>=3))}

def fit_one(hl, method='L-BFGS-B', rho_mode='free', rho_fixed=-0.07762):
    teams=sorted({m.home for m in TR}|{m.away for m in TR}); idx={t:i for i,t in enumerate(teams)}; n=len(teams)
    # Common DC parameterization: attack all n with explicit sum-to-n constraint (mean attack=1 in multiplicative space equivalent sum log=0), defense n, home, intercept, rho.
    # Use log-scale additive attack/defense to stay comparable to frozen outputs.
    if rho_mode=='free': size=2*n+3
    else: size=2*n+2
    x0=np.zeros(size); x0[2*n]=math.log(np.mean([m.hg+m.ag for m in TR])/2); x0[2*n+1]=0.15
    if rho_mode=='free': x0[-1]=-0.05
    def unpack(x):
        a=x[:n]; d=x[n:2*n]; b=x[2*n]; h=x[2*n+1]; r=(x[-1] if rho_mode=='free' else rho_fixed); return a,d,b,h,r
    def obj(x):
        a,d,b,h,r=unpack(x); z=0.
        for q in TR:
            l=math.exp(b+h+a[idx[q.home]]+d[idx[q.away]]); mu=math.exp(b+a[idx[q.away]]+d[idx[q.home]])
            tt=p.dc_tau(q.hg,q.ag,l,mu,r)
            if tt<=1e-12 or not math.isfinite(tt): return 1e12
            age=max(0.,(ASOF-q.date).total_seconds()/86400.); w=0.5**(age/hl)
            z-=w*(q.hg*math.log(l)-l-gammaln(q.hg+1)+q.ag*math.log(mu)-mu-gammaln(q.ag+1)+math.log(tt))
        return z
    cons={'type':'eq','fun':lambda x: np.sum(x[:n])}
    if method=='SLSQP':
        bounds=[(None,None)]*(size-1)+([(-0.3,0.3)] if rho_mode=='free' else [(None,None)])
        # if fixed rho, last parameter is h, so use unbounded all.
        if rho_mode!='free': bounds=[(None,None)]*size
        res=minimize(obj,x0,method='SLSQP',constraints=[cons],bounds=bounds,options={'maxiter':4000,'ftol':1e-12,'disp':False})
    else:
        # eliminate constraint not possible here; trust-constr would be overkill, use SLSQP alias.
        raise ValueError(method)
    a,d,b,h,r=unpack(res.x)
    def matrix(home,away):
        l=math.exp(b+h+a[idx[home]]+d[idx[away]]); mu=math.exp(b+a[idx[away]]+d[idx[home]])
        xs=np.arange(20); ph=np.exp(xs*np.log(l)-l-gammaln(xs+1)); pa=np.exp(xs*np.log(mu)-mu-gammaln(xs+1)); M=np.outer(ph,pa)
        for xx,yy in [(0,0),(0,1),(1,0),(1,1)]: M[xx,yy]*=p.dc_tau(xx,yy,l,mu,r)
        M/=M.sum(); return M
    return matrix, {'success':bool(res.success),'fun':float(res.fun),'rho':float(r)}

def eval_variant(rho_mode,rho_fixed=None):
    mods=[]; metas=[]
    for hl in p.HALF_LIVES:
        f,m=fit_one(hl,'SLSQP',rho_mode,-0.07762 if rho_fixed is None else rho_fixed);mods.append(f);metas.append(m)
    errs=[]; rows={}
    for fid,(h,a) in FIX.items():
        A=sum(f(h,a) for f in mods)/len(mods); g=mprobs(A); rows[fid]={}
        for k,t in REF[fid].items(): rows[fid][k]=g[k]; errs.append(abs(g[k]-t))
    return {'mae':float(np.mean(errs)),'maxae':float(np.max(errs)),'meta':metas,'rows':rows}

out={
'SLSQP_free_rho':eval_variant('free'),
'SLSQP_fixed_rho_-0.07762':eval_variant('fixed',-0.07762),
'SLSQP_fixed_rho_0':eval_variant('fixed',0.0),
}
print(json.dumps(out,ensure_ascii=False,indent=2))
