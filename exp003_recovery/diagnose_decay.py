import math, json
from datetime import datetime
from scipy.special import gammaln
import parlay_replay_dc as p

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
allm=p.load_all(); tr=p.training_for(allm,'2025-02-07',True)
mods=p.ensemble(tr,datetime(2025,2,7)); cand=p.make_candidates(mods,p.J6_FIXTURES); sel=p.select_three(cand)
by={(r['fixture_id'],r['contract']):r for r in cand}
legs=[]
for fid,c,t in p.J6_TARGET:
    got=by[(fid,c)]['probability']; legs.append({'fixture_id':fid,'contract':c,'target':t,'got':got,'abs_error':abs(got-t)})
all_focus=[]
for fid,date,home,away in p.J6_FIXTURES:
    row={'fixture_id':fid,'home':home,'away':away}
    for c in ['DOUBLE_CHANCE|12','TEAM_TOTALS|HOME_OVER_0.5','TEAM_TOTALS|HOME_UNDER_2.5']:
        r=by[(fid,c)]
        row[c]={'p':r['probability'],'gate':r['primary_gate'],'score':r['research_score']}
    all_focus.append(row)
print('EXP_DECAY_DIAGNOSTIC',json.dumps({'legs':legs,'selected':[(r['fixture_id'],r['contract'],r['probability']) for r in sel],'focus':all_focus},ensure_ascii=False),flush=True)
