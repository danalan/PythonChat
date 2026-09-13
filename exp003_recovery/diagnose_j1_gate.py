import math, json
from datetime import datetime
import numpy as np
from scipy.optimize import minimize
from scipy.special import gammaln
import parlay_replay_dc as p

ALL=p.load_all(); TR=[m for m in ALL if m.date < datetime(2025,1,10)]; ASOF=datetime(2025,1,10)
FIX=[
('J1-01','Gallos Blancos','CF América'),('J1-02','Mazatlán FC','FC Juárez'),('J1-03','Club Tijuana','Deportivo Toluca'),('J1-04','Atlético San Luis','UANL Tigres'),('J1-05','CF Monterrey','Puebla FC'),('J1-06','Deportivo Guadalajara','Santos Laguna'),('J1-07','Cruz Azul','Atlas Guadalajara'),('J1-08','Pumas UNAM','Club Necaxa')]
# frozen reference subset from all_markets.csv, enough to identify 1X2 and total-goal shape
REF={
'J1-01':{'HOME':.1528465072043198,'DRAW':.2448419924548112,'AWAY':.6023115003408691,'OVER_2.5':.4804085691075246},
'J1-03':{'HOME':.2815287030638931,'DRAW':.2482744414842101,'AWAY':.4701968554518968,'OVER_2.5':.6083459289781771},
'J1-05':{'HOME':.7678854037252519,'DRAW':.1525191559096011,'AWAY':.0795954403651469,'OVER_2.5':.6720335112737199},
'J1-06':{'HOME':.6301823415365048,'DRAW':.2340571514348059,'AWAY':.1357605070286892,'OVER_2.5':.4854615882568141},
'J1-08':{'HOME':.5738052229420694,'DRAW':.2427365839689352,'AWAY':.1834581930889955,'OVER_2.5':.5333926985861029}}

def fit_models(decay):
    old=p.DCModel.objective
    def obj(self,theta):
        a,d,b,h,rho=self.unpack(theta); z=0.
        for q in self.matches:
            i=self.idx[q.home];j=self.idx[q.away]
            l=math.exp(b+h+a[i]+d[j]);m=math.exp(b+a[j]+d[i]);tt=p.dc_tau(q.hg,q.ag,l,m,rho)
            if tt<=1e-10:return 1e12
            age=max(0.,(self.asof-q.date).total_seconds()/86400.)
            w=(0.5**(age/self.half_life)) if decay=='half' else math.exp(-age/self.half_life)
            z-=w*(q.hg*math.log(l)-l-gammaln(q.hg+1)+q.ag*math.log(m)-m-gammaln(q.ag+1)+math.log(tt))
        return z
    p.DCModel.objective=obj
    mods=p.ensemble(TR,ASOF)
    p.DCModel.objective=old
    return mods

def market_probs(M):
    home=float(np.tril(M,-1).sum()); draw=float(np.trace(M)); away=float(np.triu(M,1).sum())
    o25=float(sum(M[i,j] for i in range(M.shape[0]) for j in range(M.shape[1]) if i+j>=3))
    return {'HOME':home,'DRAW':draw,'AWAY':away,'OVER_2.5':o25}

def run(decay):
    mods=fit_models(decay); out={}; errs=[]
    for fid,home,away in FIX:
        if fid not in REF: continue
        A,_=p.avg_matrix(mods,home,away); got=market_probs(A); row={}
        for k,t in REF[fid].items():
            e=got[k]-t; errs.append(abs(e)); row[k]={'got':got[k],'target':t,'err':e}
        out[fid]=row
    return {'mae':float(np.mean(errs)),'maxae':float(np.max(errs)),'rows':out}
print(json.dumps({'training_count':len(TR),'half_life_literal':run('half'),'exp_tau':run('exp')},ensure_ascii=False,indent=2))
