#!/usr/bin/env python3
"""EXP-003 Apertura 2025 J1 model-only replay.

Temporal contract
-----------------
- Target slate: Apertura 2025 Jornada 1, 11-13 July 2025.
- Chivas-Tigres is excluded from the July betting window because it was postponed.
- Global model freeze: 2025-07-11 00:00. No J1 result is eligible.
- Context/price windows: Friday before 18:59, Saturday before 18:59, Sunday before 16:59 America/Mexico_City.
- Researcher outcome exposure occurred during schedule verification; therefore selection must remain mechanical and this jornada is not feature-promotion eligible.
"""
from __future__ import annotations
import json
from datetime import datetime
import numpy as np
import parlay_replay_dc as base

MODEL_CUTOFF=datetime(2025,7,11,0,0,0)
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
K_SHRINK=0.5620833333

def p_cal(p):
 return 0.5 + K_SHRINK*(p-0.5)

def market_probs(M):
 n=M.shape[0]; h=float(np.tril(M,-1).sum()); d=float(np.trace(M)); a=float(np.triu(M,1).sum())
 z={"1X2_HOME":h,"1X2_DRAW":d,"1X2_AWAY":a,"DC_1X":h+d,"DC_12":h+a,"DC_X2":d+a,"BTTS_YES":float(M[1:,1:].sum()),"BTTS_NO":float(M[0,:].sum()+M[1:,0].sum())}
 for line in (1.5,2.5,3.5,4.5):
  k=int(line); u=float(sum(M[i,j] for i in range(n) for j in range(n) if i+j<=k)); z[f"TOTAL_U{line}"]=u; z[f"TOTAL_O{line}"]=1-u
 for side,marg in (("HOME",M.sum(axis=1)),("AWAY",M.sum(axis=0))):
  for line in (0.5,1.5,2.5):
   k=int(line); u=float(marg[:k+1].sum()); z[f"{side}_TG_U{line}"]=u; z[f"{side}_TG_O{line}"]=1-u
 return z

def main():
 allm=base.load_all(); tr=[m for m in allm if m.date<MODEL_CUTOFF]
 mods=base.ensemble(tr,MODEL_CUTOFF)
 rows=[]
 for fid,date,home,away in FIXTURES:
  M,meta=base.avg_matrix(mods,home,away)
  for market,p in market_probs(M).items():
   rows.append({"fixture_id":fid,"date":date,"home":home,"away":away,"market":market,"p_raw":float(p),"p_cal_shadow":float(p_cal(float(p))),"ensemble_meta":meta})
 rows=sorted(rows,key=lambda r:(-r["p_raw"],r["fixture_id"],r["market"]))
 out={"track":"APERTURA_2025_J1_MODEL_ONLY_PRE_PRICE_CONTEXT","model":"V0.1R_RECOVERED","model_cutoff":MODEL_CUTOFF.isoformat(),"training_count":len(tr),"fixtures":[{"fixture_id":f[0],"date":f[1],"home":f[2],"away":f[3]} for f in FIXTURES],"postponed_excluded":"Deportivo Guadalajara vs UANL Tigres (played later; not part of July J1 betting window)","calibration_shadow":{"candidate":"CAL_SHRINK_GLOBAL_V0_1","k":K_SHRINK,"production_use":False},"expanded_candidates":rows,"warning":"Researcher saw J1 score snippets during schedule verification. This output is deterministic/model-only and J1 cannot promote context features."}
 print("AP25_J1_MODEL_ONLY_OUTPUT",json.dumps(out,ensure_ascii=False,sort_keys=True),flush=True)
if __name__=="__main__": main()
