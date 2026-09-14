#!/usr/bin/env python3
"""Clausura 2025 J10 expanded replay screen.

Temporal contract:
- One slate freeze before the first J10 match on 2025-02-28.
- OpenFootball stores dates but this recovery path intentionally uses a date-only
  model cutoff of 2025-02-28 00:00 to exclude every J10 target result.
- Context cutoff is external and must be <= 2025-02-28 20:59 America/Mexico_City.
- No J10 target outcome is used by this script.

The legacy V0.1R comparator remains separate from the expanded score-matrix
readouts. Expanded markets are SHADOW/EXPERIMENTAL until walk-forward evidence
exists; historical Caliente odds are unavailable, so no EV/ROI claim is made.
"""
from __future__ import annotations
import json
from datetime import datetime
import numpy as np
import parlay_replay_dc as base

MODEL_CUTOFF=datetime(2025,2,28,0,0,0)
CONTEXT_CUTOFF="2025-02-28T20:59:00-06:00"
ERR_ENVELOPE=0.003

FIXTURES=[
 ("J10-01","2025-02-28","Mazatlán FC","Cruz Azul"),
 ("J10-02","2025-03-01","CF América","Deportivo Toluca"),
 ("J10-03","2025-03-01","FC Juárez","CF Pachuca"),
 ("J10-04","2025-03-01","Club Necaxa","UANL Tigres"),
 ("J10-05","2025-03-01","Club León","Club Tijuana"),
 ("J10-06","2025-03-01","Pumas UNAM","Deportivo Guadalajara"),
 ("J10-07","2025-03-02","Gallos Blancos","Puebla FC"),
 ("J10-08","2025-03-02","Atlas Guadalajara","Atlético San Luis"),
 ("J10-09","2025-03-02","CF Monterrey","Santos Laguna"),
]

KNOWN_ABS_ERROR={
 "DC_12":0.0011004523947688,
 "HOME_TG_O0.5":0.0046173990890806,
 "HOME_TG_U2.5":0.013866299032083,
 "TOTAL_O1.5":0.0321663976272116,
 "DC_1X":0.0499629373171155,
 "DC_X2":0.0510633897118843,
 "1X2_HOME":0.0510633897118843,
 "1X2_AWAY":0.0499629373171155,
}
CANONICAL={"DC_12","HOME_TG_O0.5","HOME_TG_U2.5"}

def market_probs(M):
    n=M.shape[0]
    h=float(np.tril(M,-1).sum()); d=float(np.trace(M)); a=float(np.triu(M,1).sum())
    z={
      "1X2_HOME":h,"1X2_DRAW":d,"1X2_AWAY":a,
      "DC_1X":h+d,"DC_12":h+a,"DC_X2":d+a,
      "BTTS_YES":float(M[1:,1:].sum()),
      "BTTS_NO":float(M[0,:].sum()+M[1:,0].sum()),
    }
    for line in (1.5,2.5,3.5,4.5):
        k=int(line)
        u=float(sum(M[i,j] for i in range(n) for j in range(n) if i+j<=k))
        z[f"TOTAL_U{line}"]=u; z[f"TOTAL_O{line}"]=1-u
    for side,marg in (("HOME",M.sum(axis=1)),("AWAY",M.sum(axis=0))):
        for line in (0.5,1.5,2.5):
            k=int(line); u=float(marg[:k+1].sum())
            z[f"{side}_TG_U{line}"]=u; z[f"{side}_TG_O{line}"]=1-u
    return z

def risk_band(market,p):
    if p>=0.78: return "CONSERVATIVE_CANDIDATE"
    if 0.55<=p<0.70 and (market.startswith("1X2_") or market in {"BTTS_YES","BTTS_NO","TOTAL_O2.5","TOTAL_U2.5"}):
        return "AGGRESSIVE_CANDIDATE"
    return "STANDARD"

def main():
    allm=base.load_all()
    tr=[m for m in allm if m.date<MODEL_CUTOFF]
    # J9 pre-slate had 922 rows; the six Feb25-26 J9 matches become eligible.
    if len(tr)!=928:
        raise SystemExit(f"J10 chronology drift: expected 928 training rows, got {len(tr)}")
    mods=base.ensemble(tr,MODEL_CUTOFF)
    rows=[]; matrices={}
    for fid,date,home,away in FIXTURES:
        M,meta=base.avg_matrix(mods,home,away)
        matrices[fid]=[[round(float(M[i,j]),10) for j in range(8)] for i in range(8)]
        for market,p in market_probs(M).items():
            err=KNOWN_ABS_ERROR.get(market)
            rows.append({
              "fixture_id":fid,"date":date,"home":home,"away":away,
              "market":market,"p_model":float(p),
              "known_abs_error":err,
              "research_score":None if err is None else float(p-err),
              "canonical_v01r":market in CANONICAL,
              "signal_status":"CANONICAL_ELIGIBILITY_TEST" if market in CANONICAL else "EXPERIMENTAL_SIGNAL",
              "risk_band":risk_band(market,float(p)),
              "ensemble_meta":meta,
            })
    ranked=sorted(rows,key=lambda r:(-r["p_model"],r["fixture_id"],r["market"]))
    canonical=[r for r in rows if r["canonical_v01r"] and r["p_model"]>=0.60 and base.SUPPORT_LOW<=r["p_model"]<=base.SUPPORT_HIGH]
    canonical=sorted(canonical,key=lambda r:(-(r["research_score"] or -99),r["fixture_id"]))
    out={
      "track":"HISTORICAL_J10",
      "model":"V0.1R_RECOVERED",
      "model_cutoff":MODEL_CUTOFF.isoformat(),
      "context_cutoff":CONTEXT_CUTOFF,
      "training_count":len(tr),
      "fixtures":[{"fixture_id":f[0],"date":f[1],"home":f[2],"away":f[3]} for f in FIXTURES],
      "canonical_pool":canonical,
      "expanded_top40":ranked[:40],
      "score_matrices_0_7":matrices,
      "warning":"Expanded markets are probability read-outs only; historical Caliente odds are unavailable, so no historical EV/ROI claim is permitted.",
    }
    print("J10_EXPANDED_OUTPUT",json.dumps(out,ensure_ascii=False,sort_keys=True),flush=True)

if __name__=="__main__": main()
