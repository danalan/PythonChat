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
import json, time
from datetime import datetime
from concurrent.futures import ThreadPoolExecutor, as_completed
from urllib.parse import quote
from zoneinfo import ZoneInfo
import requests
import corner_shadow_v0_1 as cm
import vn2026_forward as fw

TZ=ZoneInfo("America/Mexico_City")
LEAGUE_ID=230
LEAGUE_SLUG="liga-mx"
CUTOFF=datetime(2025,2,25,0,0,0)
SEASONS=(("2024/2025","Apertura"),("2024/2025","Clausura"))
HEADERS={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 Chrome/122 Safari/537.36","Accept":"application/json,text/plain,*/*","Accept-Language":"es-MX,es;q=0.9"}
TEAM_MAP=fw.TEAM_MAP
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

def season_fixtures(year,tournament):
    """Get historical schedule from the same public page-data route used by Vn.

    The old /api/leagues route currently returns 404. We deliberately use page
    __NEXT_DATA__ only to identify match IDs and pre-cutoff kickoffs; no season
    aggregate statistics enter the corner fit.
    """
    season=quote(f"{year} - {tournament}")
    urls=[
      f"https://www.fotmob.com/es/leagues/{LEAGUE_ID}/matches/{LEAGUE_SLUG}?season={season}",
      f"https://www.fotmob.com/es/leagues/{LEAGUE_ID}/fixtures/{LEAGUE_SLUG}?season={season}",
    ]
    raw=[]; last=None
    for url in urls:
        try:
            data=fw.get_next(url)
            props=data.get("props",{}).get("pageProps",{})
            raw=fw.extract_matches(props)
            if raw: break
        except Exception as e:
            last=e; raw=[]
    if not raw:
        raise RuntimeError(f"No FotMob page fixtures for {year} {tournament}: {last}")
    out=[]
    label=f"{year} - {tournament}"
    for m in raw:
        st=m.get("status") or {}; utc=st.get("utcTime") or m.get("utcTime") or m.get("date")
        if not utc: continue
        try: dt=local_dt(utc)
        except Exception: continue
        finished=bool(st.get("finished")) or str(((st.get("reason") or {}).get("short") or "")).upper() in {"FT","AET","PEN"}
        if not finished or dt>=CUTOFF: continue
        mid=m.get("id"); home=(m.get("home") or {}).get("name"); away=(m.get("away") or {}).get("name")
        if mid and home and away:
            out.append((int(mid),dt,canon(home),canon(away),label))
    return out

def fetch_one(row):
    mid,dt,home,away,season=row
    d=get_json("https://www.fotmob.com/api/matchDetails",{"matchId":mid})
    hc,ac=cm.extract_corner_pair(d)
    return cm.CornerMatch(dt,home,away,int(hc),int(ac),f"FotMob:{season}:{mid}")

def main():
    fixtures=[]
    for year,t in SEASONS: fixtures.extend(season_fixtures(year,t))
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
      "seasons":[f"{a} - {b}" for a,b in SEASONS],"top30":out[:30],
      "warning":"No historical odds/EV claim; conditional home-away corner independence is an explicit C0.1 limitation."
    }
    print("J9_CORNERS_OUTPUT",json.dumps(payload,ensure_ascii=False,sort_keys=True),flush=True)
    if failures: print("J9_CORNERS_FAILURE_SAMPLE",json.dumps(failures[:10],ensure_ascii=False),flush=True)

if __name__=="__main__": main()
