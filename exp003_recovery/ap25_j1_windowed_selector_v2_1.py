#!/usr/bin/env python3
"""Apertura 2025 J1 mechanical price-aware selector under Execution Policy V2.1.

J1 researcher outcome exposure is known. Therefore this script is the ONLY authority
for the production paper selections: raw V0.1R + exact archived prices. Human context
cannot add/remove/reorder J1 wagers.

Selection:
- compute all exact-priced candidates from frozen snapshot;
- positive EV required;
- within each fixture keep the candidate with highest full-Kelly fraction as a
  risk-adjusted ranking score (Kelly is NOT used as actual stake sizing);
- primary single gate: Kelly score >= 0.05;
- fixed conservative stake tiers from the MXN100 weekly risk budget:
    Kelly >= .15 -> 20 MXN
    Kelly >= .08 -> 15 MXN
    Kelly >= .05 -> 10 MXN
- one 5 MXN diagnostic 2-leg parlay per window when >=2 primary singles exist;
- 3+ leg parlays are shadow only, zero bankroll stake.
"""
from __future__ import annotations
import json
from pathlib import Path
from datetime import datetime
import numpy as np
import parlay_replay_dc as base

MODEL_CUTOFF=datetime(2025,7,11,0,0,0)
BUDGET=100.0
SNAP=Path(__file__).with_name('ap25_j1_price_snapshot_pre_cutoff.json')
FIXTURES=[
 ("AP25J1-01","2025-07-11","Puebla FC","Atlas Guadalajara"),
 ("AP25J1-02","2025-07-11","FC Juárez","CF América"),
 ("AP25J1-03","2025-07-11","Club Tijuana","Gallos Blancos"),
 ("AP25J1-04","2025-07-12","Deportivo Toluca","Club Necaxa"),
 ("AP25J1-05","2025-07-12","Santos Laguna","Pumas UNAM"),
 ("AP25J1-06","2025-07-12","Cruz Azul","Mazatlán FC"),
 ("AP25J1-07","2025-07-13","CF Pachuca","CF Monterrey"),
 ("AP25J1-08","2025-07-13","Club León","Atlético San Luis"),
]

def market_probs(M):
 n=M.shape[0]; h=float(np.tril(M,-1).sum()); d=float(np.trace(M)); a=float(np.triu(M,1).sum())
 z={"1X2_HOME":h,"1X2_DRAW":d,"1X2_AWAY":a,"DC_1X":h+d,"DC_12":h+a,"DC_X2":d+a,"BTTS_YES":float(M[1:,1:].sum()),"BTTS_NO":float(M[0,:].sum()+M[1:,0].sum())}
 for line in (1.5,2.5,3.5,4.5):
  k=int(line); u=float(sum(M[i,j] for i in range(n) for j in range(n) if i+j<=k)); z[f"TOTAL_U{line}"]=u; z[f"TOTAL_O{line}"]=1-u
 for side,marg in (("HOME",M.sum(axis=1)),("AWAY",M.sum(axis=0))):
  for line in (0.5,1.5,2.5):
   k=int(line); u=float(marg[:k+1].sum()); z[f"{side}_TG_U{line}"]=u; z[f"{side}_TG_O{line}"]=1-u
 return z

def stake_from_kelly(k):
 if k>=0.15:return 20.0
 if k>=0.08:return 15.0
 if k>=0.05:return 10.0
 return 0.0

def main():
 snap=json.loads(SNAP.read_text())
 allm=base.load_all(); tr=[m for m in allm if m.date<MODEL_CUTOFF]
 if len(tr)!=1016: raise SystemExit(f"chronology drift: expected 1016, got {len(tr)}")
 mods=base.ensemble(tr,MODEL_CUTOFF)
 probs={}
 for fid,date,home,away in FIXTURES:
  M,_=base.avg_matrix(mods,home,away)
  pp=market_probs(M)
  for market,p in pp.items(): probs[(fid,market)]=float(p)
 rows=[]
 for q in snap['markets']:
  key=(q['fixture_id'],q['market'])
  if key not in probs: continue
  p=probs[key]; o=float(q['decimal']); ev=p*o-1.0
  kelly=ev/(o-1.0) if o>1 and ev>0 else 0.0
  rows.append({**q,"p_raw":p,"break_even":1.0/o,"model_ev":ev,"kelly_score":kelly})
 by_fixture={}
 for r in rows:
  if r['model_ev']<=0: continue
  old=by_fixture.get(r['fixture_id'])
  if old is None or (r['kelly_score'],r['model_ev'])>(old['kelly_score'],old['model_ev']): by_fixture[r['fixture_id']]=r
 best=sorted(by_fixture.values(),key=lambda r:(r['window'],-r['kelly_score'],r['fixture_id']))
 singles=[]
 for r in best:
  stake=stake_from_kelly(r['kelly_score'])
  if stake>0:
   singles.append({**r,"stake_mxn_simulated":stake,"vehicle":"SINGLE_PRIMARY"})
 total=sum(x['stake_mxn_simulated'] for x in singles)
 parlays=[]
 for window in ("FRIDAY","SATURDAY","SUNDAY"):
  wr=sorted([x for x in singles if x['window']==window],key=lambda x:-x['kelly_score'])
  if len(wr)>=2 and total+5.0<=BUDGET:
   a,b=wr[:2]; odds=a['decimal']*b['decimal']; pj=a['p_raw']*b['p_raw']; stake=5.0
   parlays.append({"window":window,"vehicle":"PARLAY_2_SECONDARY","stake_mxn_simulated":stake,"legs":[{"fixture_id":a['fixture_id'],"market":a['market']},{"fixture_id":b['fixture_id'],"market":b['market']}],"decimal":odds,"p_joint_independence":pj,"model_ev":pj*odds-1.0})
   total+=stake
 out={"experiment":"EXP-003","tournament":"Apertura 2025","jornada":"J1","policy":"V2.1_WINDOWED_100","money_type":"SIMULATED_PAPER_ONLY","integrity_class":"MECHANICAL_REPLAY_RESEARCHER_OUTCOME_EXPOSED","promotion_eligibility":False,"opening_bankroll_mxn_simulated":443.4282159211471,"weekly_risk_budget_mxn":BUDGET,"training_count":len(tr),"all_exact_price_candidates":sorted(rows,key=lambda r:-r['kelly_score']),"best_positive_candidate_per_fixture":best,"primary_singles":singles,"secondary_two_leg_parlays":parlays,"total_stake_mxn_simulated":total,"held_cash_from_weekly_budget":BUDGET-total,"notes":["Kelly fraction is used only as a risk-adjusted ranking/gate, not literal bankroll sizing.","CAL_SHRINK_GLOBAL_V0_1 remains shadow and does not alter J1 selection/stake.","Human context cannot alter J1 because researcher outcome exposure occurred before selection.","Returns from early windows cannot replenish the MXN100 risk budget."]}
 print("AP25_J1_WINDOWED_SELECTION",json.dumps(out,ensure_ascii=False,sort_keys=True),flush=True)

if __name__=='__main__': main()
