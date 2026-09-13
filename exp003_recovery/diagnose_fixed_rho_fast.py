import json, math
from datetime import datetime
import numpy as np
from scipy.optimize import minimize
from scipy.special import gammaln
import parlay_replay_dc as p
ALL=p.load_all(); TR=[m for m in ALL if m.date<datetime(2025,1,10)]; ASOF=datetime(2025,1,10)
FIX={'J1-01':('Gallos Blancos','CF América'),'J1-03':('Club Tijuana','Deportivo Toluca'),'J1-05':('CF Monterrey','Puebla FC'),'J1-06':('Deportivo Guadalajara','Santos Laguna'),'J1-08':('Pumas UNAM','Club Necaxa')}
REF={'J1-01':(.1528465072043198,.2448419924548112,.6023115003408691,.4804085691075246),'J1-03':(.2815287030638931,.2482744414842101,.4701968554518968,.6083459289781771),'J1-05':(.7678854037252519,.1525191559096011,.0795954403651469,.6720335112737199),'J1-06':(.6301823415365048,.2340571514348059,.1357605070286892,.4854615882568141),'J1-08':(.5738052229420694,.2427365839689352,.1834581930889955,.5333926985861029)}

def fit(hl,rho):
    teams=sorted({m.home for m in TR}|{m.away for m in TR});idx={t:i for i,t in enumerate(teams)};n=len(teams)
    # attacks n-1 sum0; defenses n; intercept; home. rho fixed
    size=(n-1)+n+2;x0=np.zeros(size);x0[-2]=math.log(np.mean([m.hg+m.ag for m in TR])/2);x0[-1]=.15
    def unpack(x):
        a=np.r_[x[:n-1],-np.sum(x[:n-1])];d=x[n-1:n-1+n];return a,d,x[-2],x[-1]
    def obj(x):
        a,d,b,h=unpack(x);z=0.
        for q in TR:
            l=math.exp(b+h+a[idx[q.home]]+d[idx[q.away]]);mu=math.exp(b+a[idx[q.away]]+d[idx[q.home]]);tt=p.dc_tau(q.hg,q.ag,l,mu,rho)
            if tt<=1e-10:return 1e12
            age=max(0.,(ASOF-q.date).total_seconds()/86400.);w=.5**(age/hl)
            z-=w*(q.hg*math.log(l)-l-gammaln(q.hg+1)+q.ag*math.log(mu)-mu-gammaln(q.ag+1)+math.log(tt))
        return z
    res=minimize(obj,x0,method='L-BFGS-B',options={'maxiter':3000,'ftol':1e-12,'gtol':1e-8,'maxls':50});a,d,b,h=unpack(res.x)
    def mat(home,away):
        l=math.exp(b+h+a[idx[home]]+d[idx[away]]);mu=math.exp(b+a[idx[away]]+d[idx[home]]);xs=np.arange(16);ph=np.exp(xs*np.log(l)-l-gammaln(xs+1));pa=np.exp(xs*np.log(mu)-mu-gammaln(xs+1));M=np.outer(ph,pa)
        for xx,yy in [(0,0),(0,1),(1,0),(1,1)]:M[xx,yy]*=p.dc_tau(xx,yy,l,mu,rho)
        return M/M.sum()
    return mat

def score(rho):
    mods=[fit(h,rho) for h in p.HALF_LIVES];errs=[]
    for fid,(h,a) in FIX.items():
        M=sum(f(h,a) for f in mods)/4;home=float(np.tril(M,-1).sum());draw=float(np.trace(M));away=float(np.triu(M,1).sum());o25=float(sum(M[i,j] for i in range(M.shape[0]) for j in range(M.shape[1]) if i+j>=3));got=(home,draw,away,o25)
        errs += [abs(x-y) for x,y in zip(got,REF[fid])]
    return {'mae':float(np.mean(errs)),'maxae':float(np.max(errs))}
print(json.dumps({str(r):score(r) for r in [-.12,-.10,-.07762,-.06,-.04,-.02,0.0]},indent=2))
