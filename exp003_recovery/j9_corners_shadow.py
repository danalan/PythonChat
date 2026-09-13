#!/usr/bin/env python3
"""Clausura 2025 J9 historical corner shadow screen.

C0.1-CORNERS-NB-ENSEMBLE remains SHADOW ONLY. This script reconstructs only
pre-cutoff corner history from FotMob match reports and evaluates the six
remaining J9 fixtures without reading their outcomes.

Temporal rules:
- slate model cutoff: 2025-02-25 00:00 America/Mexico_City
- any match at/after cutoff is excluded before its match details are requested
- only 2024/2025 Apertura + pre-cutoff Clausura are used in C0.1; this is a
  deliberately narrow first shadow sample, not a claim of production readiness
- no current/future season aggregate statistics are used
"""
from __future__ import annotations
import json, re, time
from datetime import datetime
from concurrent.futures import ThreadPoolExecutor, as_completed
from zoneinfo import ZoneInfo
import requests
import corner_shadow_v0_1 as cm

TZ=ZoneInfo("America/Mexico_City")
LEAGUE_ID=230
CUTOFF=datetime(2025,2,25,0,0,0)
SEASONS=("2024/2025 - Apertura","2024/2025 - Clausura")
HEADERS={"User-Agent":"Mozilla/5.0","Accept":"application/json,text/plain,*/*","Accept-Language":"es-MX,es;q=0.9"}
TEAM_MAP={
 "CF America":"CF América","América":"CF América","America":"CF América",
 "Atlas":"Atlas Guadalajara","Atlas FC":"Atlas Guadalajara",
 "Atletico de San Luis":"Atlético San Luis","Atlético San Luis":"Atlético San Luis","San Luis":"Atlético San Luis",
 "Cruz Azul":"Cruz Azul","FC Juarez":"FC Juárez","FC Juárez":"FC Juárez","Juarez":"FC Juárez","Juárez":"FC Juárez",
 "Chivas":"Deportivo Guadalajara","Guadalajara":"Deportivo Guadalajara","CD Guadalajara":"Deportivo Guadalajara",
 "Leon":"Club León","León":"Club León","Monterrey":"CF Monterrey","Necaxa":"Club Necaxa",
 "Pachuca":"CF Pachuca","Puebla":"Puebla FC","Pumas":"Pumas UNAM","Pumas UNAM":"Pumas UNAM","UNAM":"Pumas UNAM",
 "Queretaro FC":"Gallos Blancos","Querétaro FC":"Gallos Blancos","Queretaro":"Gallos Blancos","Querétaro":"Gallos Blancos",
 "Santos Laguna":"Santos Laguna","Tigres":"UANL Tigres","Tigres UANL":"UANL Tigres","UANL":"UANL Tigres",
 "Tijuana":"Club Tijuana","Toluca":"Deportivo Toluca","Mazatlan FC":"Mazatlán FC","Mazatlán FC":"Mazatlán FC",
}
FIXTURES=[
 ("J9R-01","UANL Tigres","FC Juárez"),
 ("J9R-02","Mazatlán FC","CF Monterrey"),
 ("J9R-03","Club Tijuana","Pumas UNAM"),
 ("J9R-04","CF Pachuca","Puebla FC"),
 ("J9R-05","Deportivo Toluca","Gallos Blancos"),
 ("J9R-06","Atlético San Luis","Deportivo Guadalajara"),
]

def canon(x): return TEAM_MAP.get(str(x).strip(),str(x).strip())

def local_dt(raw):
    dt=datetime.fromisoformat(str(raw).replace("Z","+00:00"))
    return dt.astimezone(TZ).replace(tzinfo=None)

def get_json(url,params=None,tries=3):
    last=None
    for attempt in range(tries):
        try:
            r=requests.get(url,params=params,headers=HEADERS,timeout=30)
            r.raise_for_status(); return r.json()
        except Exception as e:
            last=e; time.sleep(0.5*(attempt+1))
    raise RuntimeError(f"request failed {url} {params}: {last}")

def season_fixtures(season):
    data=get_json("https://www.fotmob.com/api/leagues",{"id":LEAGUE_ID,"season":season})
    raw=((data.get("fixtures") or {}).get("allMatches") or [])
    out=[]
    for m in raw:
        st=m.get("status") or {}; utc=st.get("utcTime") or m.get("utcTime")
        if not utc: continue
        try: dt=local_dt(utc)
        except Exception: continue
        finished=bool(st.get("finished")) or str(((st.get("reason") or {}).get("short") or "")).upper() in {"FT","AET","PEN"}
        if not finished or dt>=CUTOFF: continue
        mid=m.get("id"); home=(m.get("home") or {}).get("name"); away=(m.get("away") or {}).get("name")
        if mid and home and away:
            out.append((int(mid),dt,canon(home),canon(away),season))
    return out

def fetch_one(row):
    mid,dt,home,away,season=row
    d=get_json("https://www.fotmob.com/api/matchDetails",{"matchId":mid})
    hc,ac=cm.extract_corner_pair(d)
    return cm.CornerMatch(dt,home,away,int(hc),int(ac),f"FotMob:{season}:{mid}")

def main():
    fixtures=[]
    for s in SEASONS: fixtures.extend(season_fixtures(s))
    # Deduplicate by match id before detail calls.
    fixtures=list({r[0]:r for r in fixtures}.values())
    rows=[]; failures=[]
    with ThreadPoolExecutor(max_workers=6) as ex:
        futs={ex.submit(fetch_one,r):r for r in fixtures}
        for f in as_completed(futs):
            try: rows.append(f.result())
            except Exception as e: failures.append({"match_id":futs[f][0],"error":str(e)[:180]})
    rows=sorted(rows,key=lambda r:(r.date,r.home,r.away))
    if any(r.date>=CUTOFF for r in rows): raise AssertionError("corner cutoff leakage")
    if len(rows)<120:
        raise SystemExit(f"insufficient pre-cutoff corner rows: {len(rows)}; failures={len(failures)}")
    models=cm.ensemble(rows,CUTOFF)
    out=[]
    for fid,home,away in FIXTURES:
        M,meta=cm.avg_matrix(models,home,away)
        for market,p in cm.market_probs(M).items():
            if p>=0.60:
                out.append({"fixture_id":fid,"home":home,"away":away,"market":market,"p_model":float(p),"status":"C0.1_SHADOW_ONLY","meta":meta})
    out=sorted(out,key=lambda x:(-x["p_model"],x["fixture_id"],x["market"]))
    payload={
      "model":"C0.1-CORNERS-NB-ENSEMBLE","status":"SHADOW_ONLY",
      "cutoff":CUTOFF.isoformat(),"training_rows":len(rows),"detail_failures":len(failures),
      "seasons":SEASONS,"top30":out[:30],
      "warning":"No historical odds/EV claim; conditional home-away corner independence is an explicit C0.1 limitation."
    }
    print("J9_CORNERS_OUTPUT",json.dumps(payload,ensure_ascii=False,sort_keys=True),flush=True)
    if failures: print("J9_CORNERS_FAILURE_SAMPLE",json.dumps(failures[:10],ensure_ascii=False),flush=True)

if __name__=="__main__": main()
