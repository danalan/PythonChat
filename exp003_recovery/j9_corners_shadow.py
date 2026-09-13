#!/usr/bin/env python3
"""Clausura 2025 J9 historical corner shadow screen.

C0.1-CORNERS-NB-ENSEMBLE remains SHADOW ONLY. This script reconstructs only
pre-cutoff corner history from FotMob match pages and evaluates the six
remaining J9 fixtures without reading their outcomes.

Temporal rules:
- slate model cutoff: 2025-02-25 00:00 America/Mexico_City
- any match at/after cutoff is excluded before its match page is requested
- only 2024/2025 Apertura + pre-cutoff Clausura are used in C0.1
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
HEADERS={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 Chrome/131 Safari/537.36","Accept":"text/html,application/xhtml+xml,application/json;q=0.9,*/*;q=0.8","Accept-Language":"es-MX,es;q=0.9"}
TEAM_MAP={**fw.TEAM_MAP,
          "Atlético de San Luis":"Atlético San Luis",
          "Atletico de San Luis":"Atlético San Luis"}
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

def season_fixtures(year,tournament):
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
    out=[]; label=f"{year} - {tournament}"
    for m in raw:
        st=m.get("status") or {}; utc=st.get("utcTime") or m.get("utcTime") or m.get("date")
        if not utc: continue
        try: dt=local_dt(utc)
        except Exception: continue
        finished=bool(st.get("finished")) or str(((st.get("reason") or {}).get("short") or "")).upper() in {"FT","AET","PEN"}
        if not finished or dt>=CUTOFF: continue
        mid=m.get("id"); home=(m.get("home") or {}).get("name"); away=(m.get("away") or {}).get("name")
        page=m.get("pageUrl") or m.get("pageURL") or m.get("url")
        if mid and home and away and page:
            out.append((int(mid),dt,canon(home),canon(away),label,str(page)))
    return out

def fetch_one(row):
    mid,dt,home,away,season,page=row
    url=page if page.startswith("http") else "https://www.fotmob.com"+page
    data=fw.get_next(url)
    props=data.get("props",{}).get("pageProps",{})
    hc,ac=cm.extract_corner_pair(props)
    return cm.CornerMatch(dt,home,away,int(hc),int(ac),f"FotMobPage:{season}:{mid}")

def main():
    fixtures=[]
    for year,t in SEASONS: fixtures.extend(season_fixtures(year,t))
    fixtures=list({r[0]:r for r in fixtures}.values())
    rows=[]; failures=[]
    with ThreadPoolExecutor(max_workers=5) as ex:
        futs={ex.submit(fetch_one,r):r for r in fixtures}
        for f in as_completed(futs):
            try: rows.append(f.result())
            except Exception as e:
                r=futs[f]; failures.append({"match_id":r[0],"page":r[5],"error":str(e)[:220]})
    rows=sorted(rows,key=lambda r:(r.date,r.home,r.away))
    if any(r.date>=CUTOFF for r in rows): raise AssertionError("corner cutoff leakage")
    if len(rows)<120:
        print("J9_CORNERS_FAILURE_SAMPLE",json.dumps(failures[:10],ensure_ascii=False),flush=True)
        raise SystemExit(f"insufficient pre-cutoff corner rows: {len(rows)}; failures={len(failures)}")
    models=cm.ensemble(rows,CUTOFF)
    available=set(models[0].teams)
    target_teams={t for _,h,a in FIXTURES for t in (h,a)}
    missing=sorted(target_teams-available)
    if missing:
        print("J9_CORNERS_TEAM_DIAGNOSTIC",json.dumps({
          "training_rows":len(rows),"detail_failures":len(failures),
          "missing":missing,"available":sorted(available)
        },ensure_ascii=False,sort_keys=True),flush=True)
        raise SystemExit("corner target-team mapping incomplete")
    out=[]
    for fid,home,away in FIXTURES:
        M,meta=cm.avg_matrix(models,home,away)
        for market,p in cm.market_probs(M).items():
            if p>=0.60:
                out.append({"fixture_id":fid,"home":home,"away":away,"market":market,"p_model":float(p),"status":"C0.1_SHADOW_ONLY","meta":meta})
    out=sorted(out,key=lambda x:(-x["p_model"],x["fixture_id"],x["market"]))
    payload={
      "model":"C0.1-CORNERS-NB-ENSEMBLE","status":"SHADOW_ONLY",
      "cutoff":CUTOFF.isoformat(),"eligible_schedule_rows":len(fixtures),
      "training_rows":len(rows),"detail_failures":len(failures),
      "coverage":len(rows)/max(1,len(fixtures)),
      "seasons":[f"{a} - {b}" for a,b in SEASONS],"top30":out[:30],
      "warning":"No historical odds/EV claim; conditional home-away corner independence and incomplete source coverage are explicit C0.1 limitations."
    }
    print("J9_CORNERS_OUTPUT",json.dumps(payload,ensure_ascii=False,sort_keys=True),flush=True)
    if failures: print("J9_CORNERS_FAILURE_SAMPLE",json.dumps(failures[:10],ensure_ascii=False),flush=True)

if __name__=="__main__": main()
