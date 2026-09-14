#!/usr/bin/env python3
"""Apertura 2025 J4 model-only replay under frozen V0.1R + calibration shadow.

Integrity note: researcher became outcome-exposed to J4 during schedule research on
2026-09-14. Therefore J4 is permanently NO-PROMOTION. No J4 outcome is used as
an input. Training includes only matches prior to 2025-08-08, including completed
Apertura 2025 J1-J3 fixtures.
"""
from __future__ import annotations
import json
from datetime import datetime
import numpy as np
import parlay_replay_dc as base

MODEL_CUTOFF = datetime(2025, 8, 8, 0, 0, 0)
CAL_K = 0.5620833333

J1_FROZEN = [
    base.Match(datetime(2025,7,11), "Puebla FC", "Atlas Guadalajara", 2, 3, "AP25_J1_FROZEN"),
    base.Match(datetime(2025,7,11), "FC Juárez", "CF América", 1, 1, "AP25_J1_FROZEN"),
    base.Match(datetime(2025,7,11), "Club Tijuana", "Gallos Blancos", 1, 0, "AP25_J1_FROZEN"),
    base.Match(datetime(2025,7,12), "Deportivo Toluca", "Club Necaxa", 3, 1, "AP25_J1_FROZEN"),
    base.Match(datetime(2025,7,12), "Santos Laguna", "Pumas UNAM", 3, 0, "AP25_J1_FROZEN"),
    base.Match(datetime(2025,7,12), "Cruz Azul", "Mazatlán FC", 0, 0, "AP25_J1_FROZEN"),
    base.Match(datetime(2025,7,13), "CF Pachuca", "CF Monterrey", 3, 0, "AP25_J1_FROZEN"),
    base.Match(datetime(2025,7,13), "Club León", "Atlético San Luis", 0, 1, "AP25_J1_FROZEN"),
]

J2_FROZEN = [
    base.Match(datetime(2025,7,16), "CF América", "Club Tijuana", 3, 1, "AP25_J2_FROZEN"),
    base.Match(datetime(2025,7,16), "Santos Laguna", "Deportivo Toluca", 2, 4, "AP25_J2_FROZEN"),
    base.Match(datetime(2025,7,18), "Club Necaxa", "Gallos Blancos", 3, 1, "AP25_J2_FROZEN"),
    base.Match(datetime(2025,7,18), "Atlético San Luis", "CF Monterrey", 0, 1, "AP25_J2_FROZEN"),
    base.Match(datetime(2025,7,18), "Mazatlán FC", "Puebla FC", 2, 1, "AP25_J2_FROZEN"),
    base.Match(datetime(2025,7,19), "Club León", "Deportivo Guadalajara", 1, 0, "AP25_J2_FROZEN"),
    base.Match(datetime(2025,7,19), "UANL Tigres", "FC Juárez", 1, 0, "AP25_J2_FROZEN"),
    base.Match(datetime(2025,7,19), "Atlas Guadalajara", "Cruz Azul", 3, 3, "AP25_J2_FROZEN"),
    base.Match(datetime(2025,7,20), "Pumas UNAM", "CF Pachuca", 2, 3, "AP25_J2_FROZEN"),
]

J3_FROZEN = [
    base.Match(datetime(2025,7,25), "Gallos Blancos", "Pumas UNAM", 0, 2, "AP25_J3_FROZEN"),
    base.Match(datetime(2025,7,25), "Puebla FC", "Santos Laguna", 1, 0, "AP25_J3_FROZEN"),
    base.Match(datetime(2025,7,25), "Club Tijuana", "FC Juárez", 1, 1, "AP25_J3_FROZEN"),
    base.Match(datetime(2025,7,26), "CF Pachuca", "Mazatlán FC", 1, 0, "AP25_J3_FROZEN"),
    base.Match(datetime(2025,7,26), "Deportivo Guadalajara", "Atlético San Luis", 4, 3, "AP25_J3_FROZEN"),
    base.Match(datetime(2025,7,26), "Cruz Azul", "Club León", 4, 1, "AP25_J3_FROZEN"),
    base.Match(datetime(2025,7,26), "Deportivo Toluca", "UANL Tigres", 3, 4, "AP25_J3_FROZEN"),
    base.Match(datetime(2025,7,26), "CF Monterrey", "Atlas Guadalajara", 3, 1, "AP25_J3_FROZEN"),
    base.Match(datetime(2025,7,26), "Club Necaxa", "CF América", 1, 1, "AP25_J3_FROZEN"),
]

FIXTURES = [
    ("AP25J4-01","2025-08-08","UANL Tigres","Puebla FC"),
    ("AP25J4-02","2025-08-09","CF América","Gallos Blancos"),
    ("AP25J4-03","2025-08-09","Mazatlán FC","Club Tijuana"),
    ("AP25J4-04","2025-08-09","Atlas Guadalajara","CF Pachuca"),
    ("AP25J4-05","2025-08-10","Pumas UNAM","Club Necaxa"),
    ("AP25J4-06","2025-08-10","Santos Laguna","Deportivo Guadalajara"),
    ("AP25J4-07","2025-08-11","Club León","CF Monterrey"),
    ("AP25J4-08","2025-08-11","FC Juárez","Deportivo Toluca"),
    ("AP25J4-09","2025-08-11","Atlético San Luis","Cruz Azul"),
]

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

def cal(p):
    return 0.5 + CAL_K*(p-0.5)

def main():
    hist=[m for m in base.load_all() if m.date < datetime(2025,7,11)]
    if len(hist)!=1016:
        raise SystemExit(f"chronology drift: expected pre-J1 1016, got {len(hist)}")
    tr=sorted(hist + J1_FROZEN + J2_FROZEN + J3_FROZEN, key=lambda m:(m.date,m.home,m.away,m.hg,m.ag))
    if len(tr)!=1042:
        raise SystemExit(f"J4 training count drift: expected 1042, got {len(tr)}")
    if any(m.date >= MODEL_CUTOFF for m in tr):
        raise SystemExit("J4 leakage detected")
    mods=base.ensemble(tr,MODEL_CUTOFF)
    rows=[]
    for fid,date,home,away in FIXTURES:
        M,meta=base.avg_matrix(mods,home,away)
        pp=market_probs(M)
        rows.append({
            "fixture_id":fid,"date":date,"home":home,"away":away,
            "markets":{k:{"p_raw":float(v),"p_cal_shadow":float(cal(v))} for k,v in pp.items()},
            "model_meta":meta,
        })
    out={
        "experiment":"EXP-003",
        "tournament":"Apertura 2025",
        "jornada":"J4",
        "model":"V0.1R_DC_ENSEMBLE",
        "calibration_shadow":"CAL_SHRINK_GLOBAL_V0_1",
        "model_cutoff":"2025-08-08T00:00:00-06:00",
        "training_count":len(tr),
        "training_includes":"Apertura 2025 J1 + J2 + J3 completed fixtures",
        "integrity_class":"DETERMINISTIC_REPLAY_RESEARCHER_OUTCOME_EXPOSED",
        "promotion_eligibility":False,
        "fixtures":rows,
        "notes":[
            "No J4 result is an input.",
            "Raw V0.1R remains canonical for V2.1 selection; calibration remains shadow-only.",
            "J4 cannot promote model/context/calibration/staking changes because researcher saw J4 outcome information during schedule research.",
            "V2.2 fractional-Kelly variants are shadow-only and inherit the canonical qualifying candidate set."
        ]
    }
    print("AP25_J4_MODEL_ONLY", json.dumps(out, ensure_ascii=False, sort_keys=True), flush=True)

if __name__ == "__main__":
    main()
