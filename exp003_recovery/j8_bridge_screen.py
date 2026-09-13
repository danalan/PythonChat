import json, math
from datetime import datetime
import parlay_replay_dc as p

LO=30/169
HI=1-30/169
BIAS={
 'DOUBLE_CHANCE|12':0.0011004523947688,
 'DOUBLE_1X':0.0499629373171155,
 'DOUBLE_X2':0.0510633897118843,
 'RESULT_HOME':0.0510633897118843,
 'RESULT_AWAY':0.0499629373171155,
 'TEAM_TOTALS|HOME_OVER_0.5':0.0046173990890806,
 'TEAM_TOTALS|HOME_UNDER_2.5':0.013866299032083,
 'MATCH_TOTALS|OVER_1.5':0.0321663976272116,
}
ERR_ENVELOPE=0.0030

def probs(mat):
    n=mat.shape[0]
    home=sum(mat[i,j] for i in range(n) for j in range(n) if i>j)
    draw=sum(mat[i,i] for i in range(n))
    away=1-home-draw
    h0=sum(mat[0,j] for j in range(n)); h_under25=sum(mat[i,j] for i in range(3) for j in range(n))
    over15=sum(mat[i,j] for i in range(n) for j in range(n) if i+j>=2)
    return {'RESULT_HOME':home,'RESULT_AWAY':away,'DOUBLE_1X':home+draw,'DOUBLE_X2':away+draw,'DOUBLE_CHANCE|12':home+away,'TEAM_TOTALS|HOME_OVER_0.5':1-h0,'TEAM_TOTALS|HOME_UNDER_2.5':h_under25,'MATCH_TOTALS|OVER_1.5':over15}

allm=p.load_all(); tr=p.training_for(allm,'2025-02-21',False)
mods=p.ensemble(tr,datetime(2025,2,21))
rows=[]
for fid,date,home,away in p.J8_FIXTURES:
    mat,_=p.avg_matrix(mods,home,away); q=probs(mat)
    for ident,pr in q.items():
        score=pr-BIAS[ident]
        eligible=(pr>=0.60 and LO<=pr<=HI)
        dist=min(abs(pr-0.60),abs(pr-LO),abs(pr-HI))
        robust=dist>ERR_ENVELOPE
        rows.append({'fixture_id':fid,'date':date,'home':home,'away':away,'identity':ident,'p':pr,'bias_abs':BIAS[ident],'score':score,'eligible':eligible,'gate_distance':dist,'robust_gate':robust})
pool=sorted([r for r in rows if r['eligible']],key=lambda r:(-r['score'],r['fixture_id'],r['identity']))
def fam(x):
    z=x['identity']
    if z.startswith('DOUBLE'): return 'DOUBLE_CHANCE'
    if z.startswith('TEAM_TOTALS'): return 'TEAM_TOTALS'
    if z.startswith('MATCH_TOTALS'): return 'MATCH_TOTALS'
    return '1X2'
sel=[]; used=set(); counts={}
for r in pool:
    f=fam(r)
    if r['fixture_id'] in used or counts.get(f,0)>=2: continue
    sel.append(r); used.add(r['fixture_id']); counts[f]=counts.get(f,0)+1
    if len(sel)==3: break
print('J8_TRAINING_COUNT',len(tr))
print('J8_TOP20',json.dumps(pool[:20],ensure_ascii=False,indent=2))
print('J8_SELECTION_SCREEN',json.dumps(sel,ensure_ascii=False,indent=2))
print('J8_ANY_GATE_AMBIGUITY_TOP20',any(not r['robust_gate'] for r in pool[:20]))
