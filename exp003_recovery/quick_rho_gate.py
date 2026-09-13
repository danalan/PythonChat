import json,math
from datetime import datetime
import numpy as np
from scipy.optimize import minimize
from scipy.special import gammaln
import parlay_replay_dc as p
TR=[m for m in p.load_all() if m.date<datetime(2025,1,10)]; ASOF=datetime(2025,1,10); R=-0.07762
FIX={'J1-01':('Gallos Blancos','CF América'),'J1-03':('Club Tijuana','Deportivo Toluca'),'J1-05':('CF Monterrey','Puebla FC'),'J1-06':('Deportivo Guadalajara','Santos Laguna'),'J1-08':('Pumas UNAM','Club Necaxa')}
REF={'J1-01':(.1528465072043198,.2448419924548112,.6023115003408691,.4804085691075246),'J1-03':(.2815287030638931,.2482744414842101,.4701968554518968,.6083459289781771),'J1-05':(.7678854037252519,.1525191559096011,.0795954403651469,.6720335112737199),'J1-06':(.6301823415365048,.2340571514348059,.1357605070286892,.4854615882568141),'J1-08':(.5738052229420694,.2427365839689352,.1834581930889955,.5333926985861029)}
def fit(hl):
 t=sorted({m.home for m in TR}|{m.away for m in TR});ix={v:i for i,v in enumerate(t)};n=len(t);x=np.zeros((n-1)+n+2);x[-2]=math.log(np.mean([m.hg+m.ag for m in TR])/2);x[-1]=.15
 def up(z):return np.r_[z[:n-1],-np.sum(z[:n-1])],z[n-1:n-1+n],z[-2],z[-1]
 def f(z):
  a,d,b,h=up(z);s=0
  for q in TR:
   l=math.exp(b+h+a[ix[q.home]]+d[ix[q.away]]);u=math.exp(b+a[ix[q.away]]+d[ix[q.home]]);tt=p.dc_tau(q.hg,q.ag,l,u,R)
   if tt<=0:return 1e12
   age=(ASOF-q.date).total_seconds()/86400;w=.5**(age/hl);s-=w*(q.hg*math.log(l)-l-gammaln(q.hg+1)+q.ag*math.log(u)-u-gammaln(q.ag+1)+math.log(tt))
  return s
 r=minimize(f,x,method='L-BFGS-B',options={'maxiter':1500,'ftol':1e-10,'gtol':1e-7});a,d,b,h=up(r.x)
 def M(home,away):
  l=math.exp(b+h+a[ix[home]]+d[ix[away]]);u=math.exp(b+a[ix[away]]+d[ix[home]]);g=np.arange(15);ph=np.exp(g*np.log(l)-l-gammaln(g+1));pa=np.exp(g*np.log(u)-u-gammaln(g+1));m=np.outer(ph,pa)
  for i,j in ((0,0),(0,1),(1,0),(1,1)):m[i,j]*=p.dc_tau(i,j,l,u,R)
  return m/m.sum()
 return M
mods=[fit(h) for h in p.HALF_LIVES];errs=[]
for fid,(h,a) in FIX.items():
 M=sum(z(h,a) for z in mods)/4;got=(float(np.tril(M,-1).sum()),float(np.trace(M)),float(np.triu(M,1).sum()),float(sum(M[i,j] for i in range(M.shape[0]) for j in range(M.shape[1]) if i+j>=3)));errs += [abs(x-y) for x,y in zip(got,REF[fid])]
print(json.dumps({'rho':R,'mae':float(np.mean(errs)),'maxae':float(np.max(errs))}))
