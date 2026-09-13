#!/usr/bin/env python3
"""Vn-2026 forward bridge for project 1000 a 100000.

Uses the recovered V0.1R Dixon-Coles ensemble as the mathematical base, then
appends Liga MX 2025-26 and 2026-27 results strictly before an explicit cutoff.
Historical replay and forward evaluation remain separate: this file never writes
forward outcomes into historical freeze artifacts.
"""
from __future__ import annotations
import io, json, math, re, sys
from datetime import datetime
import requests
import pandas as pd
import numpy as np
import parlay_replay_dc as base

CUTOFF = datetime.fromisoformat(sys.argv[1] if len(sys.argv) > 1 else "2026-09-13T16:10:00")
FBREF = [
    ("2025-26", "https://fbref.com/en/comps/31/2025-2026/schedule/2025-2026-Liga-MX-Scores-and-Fixtures"),
    ("2026-27", "https://fbref.com/en/comps/31/schedule/Liga-MX-Scores-and-Fixtures"),
]
TARGETS = [
    ("Santos Laguna", "FC Juárez"),
    ("Deportivo Guadalajara", "Pumas UNAM"),
]
TEAM_MAP = {
    "América":"CF América", "Club América":"CF América",
    "Atlas":"Atlas Guadalajara", "Atlas FC":"Atlas Guadalajara",
    "Atlético San Luis":"Atlético San Luis", "San Luis":"Atlético San Luis",
    "Cruz Azul":"Cruz Azul", "FC Juárez":"FC Juárez", "Juárez":"FC Juárez",
    "Guadalajara":"Deportivo Guadalajara", "Chivas":"Deportivo Guadalajara", "CD Guadalajara":"Deportivo Guadalajara",
    "León":"Club León", "Monterrey":"CF Monterrey", "Necaxa":"Club Necaxa",
    "Pachuca":"CF Pachuca", "Puebla":"Puebla FC", "UNAM":"Pumas UNAM", "Pumas UNAM":"Pumas UNAM",
    "Querétaro":"Gallos Blancos", "Querétaro FC":"Gallos Blancos",
    "Santos Laguna":"Santos Laguna", "UANL":"UANL Tigres", "Tigres UANL":"UANL Tigres",
    "Tijuana":"Club Tijuana", "Toluca":"Deportivo Toluca", "Mazatlán":"Mazatlán FC", "Mazatlán FC":"Mazatlán FC",
    "Atlante":"Atlante FC", "Atlante FC":"Atlante FC",
}

def canon(x):
    s=str(x).strip()
    return TEAM_MAP.get(s, s)

def fetch_fbref(tag, url):
    r=requests.get(url, headers={"User-Agent":"Mozilla/5.0 research/1.0"}, timeout=30)
    r.raise_for_status()
    tabs=pd.read_html(io.StringIO(r.text))
    tab=None
    for t in tabs:
        cols=[str(c[-1] if isinstance(c,tuple) else c) for c in t.columns]
        if all(x in cols for x in ["Date","Home","Score","Away"]):
            t=t.copy(); t.columns=cols; tab=t; break
    if tab is None: raise RuntimeError(f"schedule table not found: {tag}")
    out=[]
    for _,row in tab.iterrows():
        score=str(row.get("Score",""))
        sm=re.search(r"(\d+)\s*[–-]\s*(\d+)", score)
        if not sm: continue
        date=str(row.get("Date","")).strip(); tm=str(row.get("Time","")).strip()
        if not date or date.lower()=="nan": continue
        if not tm or tm.lower()=="nan": tm="00:00"
        try: dt=datetime.fromisoformat(f"{date}T{tm[:5]}")
        except Exception: dt=pd.to_datetime(f"{date} {tm}").to_pydatetime()
        # Strict forward cutoff. A scored match after cutoff is forbidden even if source already knows it.
        if dt >= CUTOFF: continue
        home,away=canon(row["Home"]),canon(row["Away"])
        hg,ag=int(sm.group(1)),int(sm.group(2))
        notes=str(row.get("Notes",""))
        # Exclude shoot-out score contamination; ordinary playoff legs remain usable.
        if "penalty shoot" in notes.lower(): continue
        out.append(base.Match(dt,home,away,hg,ag,f"FBref:{tag}"))
    return out

def load_training():
    old=base.load_all()
    rows=list(old)
    source_counts={"openfootball_through_2024_25":len(old)}
    for tag,url in FBREF:
        rr=fetch_fbref(tag,url); rows.extend(rr); source_counts[tag]=len(rr)
    # Dedup on fixture/date/score after canonicalization.
    seen=set(); ded=[]
    for m in sorted(rows,key=lambda z:(z.date,z.home,z.away,z.hg,z.ag,z.source)):
        k=(m.date.date().isoformat(),m.home,m.away,m.hg,m.ag)
        if k in seen: continue
        seen.add(k); ded.append(m)
    ded=[m for m in ded if m.date < CUTOFF]
    return ded,source_counts

def market_probs(M):
    n=M.shape[0]
    home=float(np.tril(M,-1).sum()); draw=float(np.trace(M)); away=float(np.triu(M,1).sum())
    d={
      "1X2_HOME":home,"1X2_DRAW":draw,"1X2_AWAY":away,
      "DC_1X":home+draw,"DC_12":home+away,"DC_X2":draw+away,
      "BTTS_YES":float(M[1:,1:].sum()),"BTTS_NO":float(M[0,:].sum()+M[1:,0].sum()),
    }
    for line in [1.5,2.5,3.5,4.5]:
        k=int(math.floor(line))
        under=float(sum(M[i,j] for i in range(n) for j in range(n) if i+j<=k))
        d[f"TOTAL_U{line}"]=under; d[f"TOTAL_O{line}"]=1-under
    for side,axis in [("HOME",0),("AWAY",1)]:
        marg=M.sum(axis=1-axis)
        for line in [0.5,1.5,2.5]:
            k=int(math.floor(line)); under=float(marg[:k+1].sum())
            d[f"{side}_TG_U{line}"]=under; d[f"{side}_TG_O{line}"]=1-under
    return d

def matrix_small(M,cap=7):
    return [[round(float(M[i,j]),10) for j in range(min(cap+1,M.shape[1]))] for i in range(min(cap+1,M.shape[0]))]

def main():
    rows,counts=load_training()
    print("VN_SOURCE_COUNTS",json.dumps(counts,ensure_ascii=False),flush=True)
    print("VN_CUTOFF",CUTOFF.isoformat(),"TRAINING",len(rows),"LAST_MATCH",max(m.date for m in rows).isoformat(),flush=True)
    teams=sorted({m.home for m in rows}|{m.away for m in rows})
    missing=sorted({x for f in TARGETS for x in f if x not in teams})
    if missing: raise SystemExit("missing target teams: "+repr(missing))
    models=base.ensemble(rows,CUTOFF)
    output={"model":"Vn-2026-DC-ENSEMBLE","parent":"V0.1R_RECOVERED","cutoff":CUTOFF.isoformat(),"training_count":len(rows),"fixtures":[]}
    for home,away in TARGETS:
        M,meta=base.avg_matrix(models,home,away)
        output["fixtures"].append({"home":home,"away":away,"markets":market_probs(M),"score_matrix_0_7":matrix_small(M),"ensemble_meta":meta})
    print("VN_FORWARD_OUTPUT",json.dumps(output,ensure_ascii=False,sort_keys=True),flush=True)

if __name__=="__main__": main()
