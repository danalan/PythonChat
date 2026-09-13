#!/usr/bin/env python3
"""Vn-2026 forward bridge for project 1000 a 100000.

Mathematical parent: V0.1R_RECOVERED Dixon-Coles ensemble.
Data bridge: OpenFootball through 2024-25 + FotMob 2025-26 and 2026-27.
Every row is admitted only when kickoff < explicit local cutoff and status=finished.
Historical replay artifacts are never rewritten by this forward script.
"""
from __future__ import annotations
import json, math, re, sys
from datetime import datetime
from urllib.parse import quote
from zoneinfo import ZoneInfo
import requests
import numpy as np
import parlay_replay_dc as base

TZ=ZoneInfo("America/Mexico_City")
CUTOFF=datetime.fromisoformat(sys.argv[1] if len(sys.argv)>1 else "2026-09-13T16:10:00")
LEAGUE_ID=230
LEAGUE_SLUG="liga-mx"
HEADERS={
 "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 Chrome/122 Safari/537.36",
 "Accept-Language":"es-MX,es;q=0.9","Accept":"application/json,text/plain,*/*"}
TARGETS=[("Santos Laguna","FC Juárez"),("Deportivo Guadalajara","Pumas UNAM")]
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
 "Atlante":"Atlante FC","Atlante FC":"Atlante FC"}

def canon(x):
    s=str(x).strip(); return TEAM_MAP.get(s,s)

def get_next(url):
    r=requests.get(url,headers=HEADERS,timeout=30); r.raise_for_status()
    m=re.search(r'<script id="__NEXT_DATA__" type="application/json">(.*?)</script>',r.text,re.S)
    if not m: raise RuntimeError("FotMob __NEXT_DATA__ missing: "+url)
    return json.loads(m.group(1))

def available_seasons():
    data=get_next(f"https://www.fotmob.com/es/leagues/{LEAGUE_ID}/overview/{LEAGUE_SLUG}")
    props=data.get("props",{}).get("pageProps",{})
    names=props.get("allAvailableSeasons",[])
    links=props.get("stats",{}).get("seasonStatLinks",[])
    ids={str(x.get("Name")):x.get("TournamentId") for x in links if x.get("Name") and x.get("TournamentId")}
    out=[]
    for name in names:
        bits=name.split(" - ",1); year=bits[0].strip(); tournament=bits[1].strip() if len(bits)>1 else ""
        out.append({"name":name,"year":year,"tournament":tournament,"season_id":ids.get(year)})
    return out

def extract_matches(props):
    fixtures=props.get("fixtures") or {}
    if isinstance(fixtures,dict) and fixtures.get("allMatches"):
        return fixtures["allMatches"]
    for cand in [props.get("matches"),(props.get("overview") or {}).get("leagueOverviewMatches")]:
        if isinstance(cand,list) and cand: return cand
    return []

def kickoff_local(raw):
    if not raw: return None
    s=str(raw)
    try:
        dt=datetime.fromisoformat(s.replace("Z","+00:00"))
    except Exception:
        return None
    if dt.tzinfo is None: return dt
    return dt.astimezone(TZ).replace(tzinfo=None)

def fetch_tournament(year,tournament):
    season=quote(f"{year} - {tournament}")
    urls=[
      f"https://www.fotmob.com/es/leagues/{LEAGUE_ID}/matches/{LEAGUE_SLUG}?season={season}",
      f"https://www.fotmob.com/es/leagues/{LEAGUE_ID}/fixtures/{LEAGUE_SLUG}?season={season}"]
    last=None
    for url in urls:
        try:
            data=get_next(url); props=data.get("props",{}).get("pageProps",{}); raw=extract_matches(props)
            if raw: break
        except Exception as e: last=e; raw=[]
    if not raw: raise RuntimeError(f"No FotMob matches for {year} {tournament}: {last}")
    out=[]
    for m in raw:
        home=m.get("home") or {}; away=m.get("away") or {}; status=m.get("status") or {}
        if not home or not away or not status.get("finished",False): continue
        dt=kickoff_local(status.get("utcTime") or m.get("utcTime") or m.get("date"))
        if dt is None or dt>=CUTOFF: continue
        score=str(status.get("scoreStr") or m.get("score") or m.get("result") or "")
        sm=re.search(r'(\d+)\s*[-–]\s*(\d+)',score)
        if not sm: continue
        out.append(base.Match(dt,canon(home.get("name") or home.get("longName")),canon(away.get("name") or away.get("longName")),int(sm.group(1)),int(sm.group(2)),f"FotMob:{year}-{tournament}"))
    return out

def load_training():
    rows=list(base.load_all()); counts={"OpenFootball_through_2024_25":len(rows)}
    av=available_seasons(); names={x["name"] for x in av}
    wanted=[("2025/2026","Apertura"),("2025/2026","Clausura"),("2026/2027","Apertura")]
    for year,t in wanted:
        label=f"{year} - {t}"
        if label not in names: raise RuntimeError(f"FotMob season not advertised: {label}; available tail={sorted(names)[-8:]}")
        rr=fetch_tournament(year,t); rows.extend(rr); counts[label]=len(rr)
    seen=set(); ded=[]
    for m in sorted(rows,key=lambda z:(z.date,z.home,z.away,z.hg,z.ag,z.source)):
        k=(m.date.date().isoformat(),m.home,m.away,m.hg,m.ag)
        if k in seen: continue
        seen.add(k); ded.append(m)
    return [m for m in ded if m.date<CUTOFF],counts

def market_probs(M):
    n=M.shape[0]; h=float(np.tril(M,-1).sum()); d=float(np.trace(M)); a=float(np.triu(M,1).sum())
    z={"1X2_HOME":h,"1X2_DRAW":d,"1X2_AWAY":a,"DC_1X":h+d,"DC_12":h+a,"DC_X2":d+a,
       "BTTS_YES":float(M[1:,1:].sum()),"BTTS_NO":float(M[0,:].sum()+M[1:,0].sum())}
    for line in [1.5,2.5,3.5,4.5]:
        k=int(line); u=float(sum(M[i,j] for i in range(n) for j in range(n) if i+j<=k)); z[f"TOTAL_U{line}"]=u; z[f"TOTAL_O{line}"]=1-u
    for side,marg in [("HOME",M.sum(axis=1)),("AWAY",M.sum(axis=0))]:
        for line in [0.5,1.5,2.5]:
            k=int(line); u=float(marg[:k+1].sum()); z[f"{side}_TG_U{line}"]=u; z[f"{side}_TG_O{line}"]=1-u
    return z

def main():
    rows,counts=load_training()
    print("VN_SOURCE_COUNTS",json.dumps(counts,ensure_ascii=False),flush=True)
    print("VN_CUTOFF",CUTOFF.isoformat(),"TRAINING",len(rows),"LAST_MATCH",max(m.date for m in rows).isoformat(),flush=True)
    teams={m.home for m in rows}|{m.away for m in rows}; missing=sorted({x for f in TARGETS for x in f if x not in teams})
    if missing: raise SystemExit("Missing target teams: "+repr(missing))
    models=base.ensemble(rows,CUTOFF)
    out={"model":"Vn-2026-DC-ENSEMBLE","parent":"V0.1R_RECOVERED","cutoff":CUTOFF.isoformat(),"training_count":len(rows),"fixtures":[]}
    for home,away in TARGETS:
        M,meta=base.avg_matrix(models,home,away)
        mat=[[round(float(M[i,j]),10) for j in range(8)] for i in range(8)]
        out["fixtures"].append({"home":home,"away":away,"markets":market_probs(M),"score_matrix_0_7":mat,"ensemble_meta":meta})
    print("VN_FORWARD_OUTPUT",json.dumps(out,ensure_ascii=False,sort_keys=True),flush=True)
if __name__=="__main__": main()
