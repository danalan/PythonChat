#!/usr/bin/env python3
"""Clausura 2025 J9 expanded replay screen.

Temporal contract:
- One slate freeze before the first remaining J9 match on 2025-02-25.
- OpenFootball stores only match dates, not reliable kickoff times, so goal-model
  training cutoff is 2025-02-25 00:00. This deliberately excludes ALL Feb-25
  target results rather than risking same-day leakage.
- Context cutoff is handled outside this script and must be <= 2025-02-25 18:59
  America/Mexico_City.
- No J9 target outcome is used here.

The canonical V0.1R identities remain separately identifiable. Expanded score-
matrix readouts are EXPERIMENTAL_SIGNAL until enough walk-forward evidence exists.
"""
from __future__ import annotations
import json
from datetime import datetime
import numpy as np
import parlay_replay_dc as base

MODEL_CUTOFF=datetime(2025,2,25,0,0,0)
CONTEXT_CUTOFF="2025-02-25T18:59:00-06:00"
ERR_ENVELOPE=0.003

FIXTURES=[
 ("J9R-01","2025-02-25","UANL Tigres","FC Juárez"),
 ("J9R-02","2025-02-25","Mazatlán FC","CF Monterrey"),
 ("J9R-03","2025-02-25","Club Tijuana","Pumas UNAM"),
 ("J9R-04","2025-02-26","CF Pachuca","Puebla FC"),
 ("J9R-05","2025-02-26","Deportivo Toluca","Gallos Blancos"),
 ("J9R-06","2025-02-26","Atlético San Luis","Deportivo Guadalajara"),
]

# Historical aggregate absolute errors available from the recovered calibration
# packet. Readouts without a known historical error remain experimental only.
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
    # Descriptive portfolio label, not an edge/profitability claim.
    if p>=0.78: return "CONSERVATIVE_CANDIDATE"
    if 0.55<=p<0.70 and (market.startswith("1X2_") or market in {"BTTS_YES","BTTS_NO","TOTAL_O2.5","TOTAL_U2.5"}):
        return "AGGRESSIVE_CANDIDATE"
    return "STANDARD"


def main():
    allm=base.load_all()
    tr=[m for m in allm if m.date<MODEL_CUTOFF]
    # J8 training count was 913. Nine J8 fixtures occurred Feb21-23, so J9
    # pre-slate chronology should contain 922 rows. Fail closed if upstream data drifts.
    if len(tr)!=922:
        raise SystemExit(f"J9 chronology drift: expected 922 training rows, got {len(tr)}")
    mods=base.ensemble(tr,MODEL_CUTOFF)
    rows=[]
    matrices={}
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
      "track":"HISTORICAL_J9_SECOND_SLATE",
      "model":"V0.1R_RECOVERED",
      "model_cutoff":MODEL_CUTOFF.isoformat(),
      "context_cutoff":CONTEXT_CUTOFF,
      "training_count":len(tr),
      "fixtures":[{"fixture_id":f[0],"date":f[1],"home":f[2],"away":f[3]} for f in FIXTURES],
      "canonical_pool":canonical,
      "expanded_top30":ranked[:30],
      "score_matrices_0_7":matrices,
      "warning":"Expanded markets are probability read-outs only; historical Caliente odds are unavailable, so no historical EV/ROI claim is permitted.",
    }
    print("J9_EXPANDED_OUTPUT",json.dumps(out,ensure_ascii=False,sort_keys=True),flush=True)

if __name__=="__main__": main()
