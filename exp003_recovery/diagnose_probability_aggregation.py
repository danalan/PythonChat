import json, math
from datetime import datetime
import numpy as np
from scipy.special import gammaln
import parlay_replay_dc as p

# use exp(-age/HL), which best matched the frozen J6 targets so far

def objective_exp(self, theta):
    a,d,b,h,rho=self.unpack(theta); total=0.0
    for m in self.matches:
        i=self.idx[m.home]; j=self.idx[m.away]
        lam=math.exp(b+h+a[i]+d[j]); mu=math.exp(b+a[j]+d[i])
        tau=p.dc_tau(m.hg,m.ag,lam,mu,rho)
        if tau<=1e-10 or not math.isfinite(tau): return 1e12
        age=max(0.0,(self.asof-m.date).total_seconds()/86400.0)
        w=math.exp(-age/self.half_life)
        ll=(m.hg*math.log(lam)-lam-gammaln(m.hg+1)+m.ag*math.log(mu)-mu-gammaln(m.ag+1)+math.log(tau))
        total -= w*ll
    return total
p.DCModel.objective=objective_exp

allm=p.load_all(); tr=p.training_for(allm,'2025-02-07',True); models=p.ensemble(tr,datetime(2025,2,7))
fixtures={x[0]:x for x in p.J6_FIXTURES}

def matrix_from_params(lam,mu,rho,max_goals=20):
    xs=np.arange(max_goals+1)
    ph=np.exp(xs*np.log(lam)-lam-gammaln(xs+1)); pa=np.exp(xs*np.log(mu)-mu-gammaln(xs+1))
    M=np.outer(ph,pa)
    for x,y in [(0,0),(0,1),(1,0),(1,1)]: M[x,y]*=p.dc_tau(x,y,lam,mu,rho)
    M/=M.sum(); return M

def evaluate(fid, contract):
    _,_,home,away=fixtures[fid]
    mats=[]; params=[]
    for m in models:
        M,meta=m.score_matrix(home,away,max_goals=20); mats.append(M); params.append(meta)
    # 1 avg probabilities/matrices
    A=sum(mats)/len(mats); A/=A.sum(); pav=p.probs(A)[contract]
    # 2 average lambda, mu, rho then one matrix
    lam=np.mean([x['lambda'] for x in params]); mu=np.mean([x['mu'] for x in params]); rho=np.mean([x['rho'] for x in params])
    P2=matrix_from_params(lam,mu,rho); plam=p.probs(P2)[contract]
    # 3 geometric-average intensities then matrix
    glam=math.exp(np.mean([math.log(x['lambda']) for x in params])); gmu=math.exp(np.mean([math.log(x['mu']) for x in params])); grho=rho
    P3=matrix_from_params(glam,gmu,grho); pgeo=p.probs(P3)[contract]
    return {'avg_matrix':pav,'avg_lambda':plam,'geo_lambda':pgeo,'params':params}

out={}
for fid,c,t in p.J6_TARGET:
    out[fid+'|'+c]={'target':t,**evaluate(fid,c)}
out['PUMAS_U2.5']={'target':0.7421193625777459,**evaluate('J6-08','TEAM_TOTALS|HOME_UNDER_2.5')}
out['PUMAS_O0.5']={'target_hint':'should be outside primary in original',**evaluate('J6-08','TEAM_TOTALS|HOME_OVER_0.5')}
print(json.dumps(out,ensure_ascii=False,indent=2))
