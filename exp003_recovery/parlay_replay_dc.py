#!/usr/bin/env python3
"""EXP-003 Dixon-Coles recovery adapter.

Purpose: reproduce the frozen V0.1 engine before it is allowed to generate J8.
This is a reconstruction from the canonical model contract, NOT a claim that the
lost transient source file was byte-identical. Acceptance is determined only by
the preregistered J6 reproduction gate.
"""
from __future__ import annotations
import json, math, re, sys
from dataclasses import dataclass
from datetime import datetime
from urllib.request import urlopen

import numpy as np
from scipy.optimize import minimize
from scipy.special import gammaln

RAW_BASE = "https://raw.githubusercontent.com/openfootball/world/master/north-america/mexico/"
FILES = ["2022-23_mx1.txt", "2023-24_mx1.txt", "2024-25_mx1.txt"]
HALF_LIVES = (180.0, 365.0, 730.0, 1460.0)
MAX_GOALS = 12

MONTHS = {m:i for i,m in enumerate(["Jan","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct","Nov","Dec"],1)}
DATE_RE = re.compile(r"^\s*(?:Mon|Tue|Wed|Thu|Fri|Sat|Sun)\s+([A-Z][a-z]{2})\s+(\d{1,2})(?:\s+(\d{4}))?\s*$")
MATCH_RE = re.compile(r"^\s*(?:(\d{1,2}:\d{2})\s+)?(.+?)\s{2,}v\s+(.+?)\s{2,}(\d+)-(\d+)(.*)$")

@dataclass(frozen=True)
class Match:
    date: datetime
    home: str
    away: str
    hg: int
    ag: int
    source: str


def fetch_text(name: str) -> str:
    with urlopen(RAW_BASE + name, timeout=30) as r:
        return r.read().decode("utf-8-sig")


def parse_openfootball(text: str, source: str) -> list[Match]:
    # season is encoded in filename, e.g. 2024-25
    mseason = re.search(r"(20\d{2})-(\d{2})", source)
    start_year = int(mseason.group(1))
    end_year = 2000 + int(mseason.group(2))
    current_date = None
    out: list[Match] = []
    for raw in text.splitlines():
        dm = DATE_RE.match(raw)
        if dm:
            mon, day, explicit_year = dm.groups()
            month = MONTHS[mon]
            year = int(explicit_year) if explicit_year else (start_year if month >= 6 else end_year)
            current_date = datetime(year, month, int(day))
            continue
        mm = MATCH_RE.match(raw)
        if not mm or current_date is None:
            continue
        _time, home, away, hg, ag, tail = mm.groups()
        # Shootout-decided matches are excluded from training. Openfootball marks
        # them in the trailing annotation (penalties / pen.).
        tl = tail.lower()
        if "pen" in tl or "shoot" in tl:
            continue
        out.append(Match(current_date, home.strip(), away.strip(), int(hg), int(ag), source))
    return out


def load_all() -> list[Match]:
    rows=[]
    for f in FILES:
        rows.extend(parse_openfootball(fetch_text(f), f))
    # exact de-duplication by effective date + teams + regulation score
    seen=set(); ded=[]
    for r in sorted(rows, key=lambda x:(x.date,x.home,x.away,x.hg,x.ag)):
        k=(r.date.date().isoformat(),r.home,r.away,r.hg,r.ag)
        if k not in seen:
            seen.add(k); ded.append(r)
    return ded


def dc_tau(x, y, lam, mu, rho):
    if x == 0 and y == 0: return 1.0 - lam*mu*rho
    if x == 0 and y == 1: return 1.0 + lam*rho
    if x == 1 and y == 0: return 1.0 + mu*rho
    if x == 1 and y == 1: return 1.0 - rho
    return 1.0

class DCModel:
    def __init__(self, matches: list[Match], asof: datetime, half_life: float):
        self.matches=matches; self.asof=asof; self.half_life=half_life
        self.teams=sorted({m.home for m in matches}|{m.away for m in matches})
        self.idx={t:i for i,t in enumerate(self.teams)}
        self.n=len(self.teams)
        self.theta=None

    def unpack(self, theta):
        n=self.n
        a=np.empty(n)
        a[:-1]=theta[:n-1]
        a[-1]=-np.sum(a[:-1])
        d=theta[n-1:n-1+n]
        intercept=theta[-3]
        home_adv=theta[-2]
        rho=theta[-1]
        return a,d,intercept,home_adv,rho

    def objective(self, theta):
        a,d,b,h,rho=self.unpack(theta)
        total=0.0
        for m in self.matches:
            i=self.idx[m.home]; j=self.idx[m.away]
            lam=math.exp(b+h+a[i]+d[j])
            mu=math.exp(b+a[j]+d[i])
            tau=dc_tau(m.hg,m.ag,lam,mu,rho)
            if tau <= 1e-10 or not math.isfinite(tau):
                return 1e12
            age=max(0.0,(self.asof-m.date).total_seconds()/86400.0)
            w=0.5**(age/self.half_life)
            ll=(m.hg*math.log(lam)-lam-gammaln(m.hg+1) +
                m.ag*math.log(mu)-mu-gammaln(m.ag+1) + math.log(tau))
            total -= w*ll
        return total

    def fit(self):
        n=self.n
        mean_goals=np.mean([m.hg+m.ag for m in self.matches])/2.0
        x0=np.zeros((n-1)+n+3)
        x0[-3]=math.log(max(mean_goals,0.2))
        x0[-2]=0.15
        x0[-1]=-0.05
        bounds=[(None,None)]*((n-1)+n)+[(None,None),(-1.0,1.0),(-0.30,0.30)]
        res=minimize(self.objective,x0,method="L-BFGS-B",bounds=bounds,
                     options={"maxiter":3000,"ftol":1e-12,"gtol":1e-8,"maxls":50})
        if not res.success:
            # one deterministic retry from the first optimum; this often resolves
            # line-search termination without changing the target optimum.
            res2=minimize(self.objective,res.x,method="L-BFGS-B",bounds=bounds,
                          options={"maxiter":5000,"ftol":1e-13,"gtol":1e-9,"maxls":100})
            if res2.fun < res.fun: res=res2
        self.theta=res.x
        self.fit_result={"success":bool(res.success),"fun":float(res.fun),"message":str(res.message)}
        return self

    def score_matrix(self, home, away, max_goals=MAX_GOALS):
        a,d,b,h,rho=self.unpack(self.theta)
        i=self.idx[home]; j=self.idx[away]
        lam=math.exp(b+h+a[i]+d[j]); mu=math.exp(b+a[j]+d[i])
        xs=np.arange(max_goals+1)
        ph=np.exp(xs*np.log(lam)-lam-gammaln(xs+1))
        pa=np.exp(xs*np.log(mu)-mu-gammaln(xs+1))
        M=np.outer(ph,pa)
        M[0,0]*=dc_tau(0,0,lam,mu,rho)
        M[0,1]*=dc_tau(0,1,lam,mu,rho)
        M[1,0]*=dc_tau(1,0,lam,mu,rho)
        M[1,1]*=dc_tau(1,1,lam,mu,rho)
        M=M/M.sum()
        return M,{"lambda":lam,"mu":mu,"rho":rho}


def ensemble(matches, asof):
    models=[]
    for hl in HALF_LIVES:
        models.append(DCModel(matches,asof,hl).fit())
    return models


def avg_matrix(models,home,away):
    mats=[]; meta=[]
    for m in models:
        M,mm=m.score_matrix(home,away); mats.append(M); meta.append(mm)
    A=np.mean(mats,axis=0); A=A/A.sum()
    return A,meta


def probs(M):
    home=float(np.tril(M,-1).sum())
    draw=float(np.trace(M))
    away=float(np.triu(M,1).sum())
    home_o05=float(M[1:,:].sum())
    home_u25=float(M[:3,:].sum())
    return {
        "DOUBLE_CHANCE|12": home+away,
        "TEAM_TOTALS|HOME_OVER_0.5": home_o05,
        "TEAM_TOTALS|HOME_UNDER_2.5": home_u25,
        "1X2|HOME":home,"1X2|DRAW":draw,"1X2|AWAY":away,
    }

AGG_ERR={
    "DOUBLE_CHANCE|12":-0.0011004523947688,
    "TEAM_TOTALS|HOME_OVER_0.5":-0.0046173990890806,
    "TEAM_TOTALS|HOME_UNDER_2.5":0.013866299032083,
}
SUPPORT_LOW=0.1775147928994082
SUPPORT_HIGH=0.8224852071005917

J6_FIXTURES=[
("J6-01","2025-02-07","Club Necaxa","Santos Laguna"),
("J6-02","2025-02-07","Gallos Blancos","Atlético San Luis"),
("J6-03","2025-02-07","Puebla FC","CF América"),
("J6-04","2025-02-08","Club León","Deportivo Toluca"),
("J6-05","2025-02-08","UANL Tigres","Atlas Guadalajara"),
("J6-06","2025-02-08","FC Juárez","CF Monterrey"),
("J6-07","2025-02-08","Cruz Azul","CF Pachuca"),
("J6-08","2025-02-09","Pumas UNAM","Mazatlán FC"),
("J6-09","2025-02-09","Deportivo Guadalajara","Club Tijuana"),
]
J8_FIXTURES=[
("J8-01","2025-02-21","Club Necaxa","Mazatlán FC"),
("J8-02","2025-02-21","Puebla FC","Club Tijuana"),
("J8-03","2025-02-22","FC Juárez","Deportivo Toluca"),
("J8-04","2025-02-22","Club León","UANL Tigres"),
("J8-05","2025-02-22","CF Monterrey","Atlético San Luis"),
("J8-06","2025-02-22","Deportivo Guadalajara","CF Pachuca"),
("J8-07","2025-02-22","Pumas UNAM","CF América"),
("J8-08","2025-02-23","Santos Laguna","Atlas Guadalajara"),
("J8-09","2025-02-23","Cruz Azul","Gallos Blancos"),
]
J6_TARGET=[
("J6-09","TEAM_TOTALS|HOME_OVER_0.5",0.8220553875146782),
("J6-03","DOUBLE_CHANCE|12",0.7839386689301153),
("J6-05","DOUBLE_CHANCE|12",0.7634132457400761),
]


def training_for(all_matches, cutoff_date, reproduce_j6=False):
    cutoff=datetime.fromisoformat(cutoff_date)
    rows=[m for m in all_matches if m.date < cutoff]
    if reproduce_j6:
        # Frozen J6 snapshot contained 891 rows and omitted this rescheduled game.
        rows=[m for m in rows if not (m.date.date().isoformat()=="2025-02-05" and
             m.home=="CF Pachuca" and m.away=="Club León" and m.hg==1 and m.ag==2)]
    return rows


def make_candidates(models,fixtures):
    rows=[]
    for fid,date,home,away in fixtures:
        M,meta=avg_matrix(models,home,away)
        pp=probs(M)
        for contract,err in AGG_ERR.items():
            p=pp[contract]
            primary=(p>=0.60 and SUPPORT_LOW<=p<=SUPPORT_HIGH)
            rows.append({"fixture_id":fid,"date":date,"home":home,"away":away,
                         "contract":contract,"probability":p,"aggregate_error":err,
                         "research_score":p-abs(err),"primary_gate":primary,
                         "model_meta":meta})
    rows.sort(key=lambda r:r["research_score"],reverse=True)
    return rows


def select_three(rows):
    selected=[]; used=set(); family_count={}
    for r in rows:
        if not r["primary_gate"] or r["fixture_id"] in used: continue
        fam=r["contract"].split("|")[0]
        if family_count.get(fam,0)>=2: continue
        selected.append(r); used.add(r["fixture_id"]); family_count[fam]=family_count.get(fam,0)+1
        if len(selected)==3: break
    return selected


def main():
    all_matches=load_all()
    base=[m for m in all_matches if m.date < datetime(2025,1,10)]
    print("COUNTS",json.dumps({"all":len(all_matches),"pre_2025_01_10":len(base)}),flush=True)

    # J6 reproduction gate
    tr6=training_for(all_matches,"2025-02-07",True)
    print("J6_TRAINING_COUNT",len(tr6),flush=True)
    m6=ensemble(tr6,datetime(2025,2,7))
    c6=make_candidates(m6,J6_FIXTURES)
    s6=select_three(c6)
    by={(r["fixture_id"],r["contract"]):r for r in c6}
    gate=[]
    for fid,contract,target in J6_TARGET:
        got=by[(fid,contract)]["probability"]
        gate.append({"fixture_id":fid,"contract":contract,"target":target,"got":got,"abs_error":abs(got-target)})
    joint_target=np.prod([x[2] for x in J6_TARGET])
    joint_got=np.prod([g["got"] for g in gate])
    gate_pass=(max(g["abs_error"] for g in gate)<=0.005 and abs(joint_got-joint_target)<=0.01 and
               [(r["fixture_id"],r["contract"]) for r in s6]==[(x[0],x[1]) for x in J6_TARGET])
    print("J6_GATE",json.dumps({"pass":gate_pass,"legs":gate,"selected":[{k:r[k] for k in ("fixture_id","home","away","contract","probability","research_score")} for r in s6],"joint_target":joint_target,"joint_got":joint_got},ensure_ascii=False),flush=True)
    if not gate_pass:
        print("STOP: J6 reproduction gate failed; J8 forbidden.",flush=True)
        sys.exit(2)

    # J8 only after gate passes. Effective-date chronology, no nominal-round filter.
    tr8=training_for(all_matches,"2025-02-21")
    print("J8_TRAINING_COUNT",len(tr8),flush=True)
    if len(tr8)!=913:
        print("STOP: J8 chronology count != 913; J8 forbidden.",flush=True)
        sys.exit(3)
    m8=ensemble(tr8,datetime(2025,2,21))
    c8=make_candidates(m8,J8_FIXTURES)
    s8=select_three(c8)
    out={"training_count":len(tr8),"selected":[{k:r[k] for k in ("fixture_id","date","home","away","contract","probability","aggregate_error","research_score")} for r in s8],"joint_probability":float(np.prod([r["probability"] for r in s8])),"top_candidates":[{k:r[k] for k in ("fixture_id","home","away","contract","probability","research_score","primary_gate")} for r in c8[:15]]}
    print("J8_MODEL_SIGNAL",json.dumps(out,ensure_ascii=False),flush=True)

if __name__=="__main__":
    main()
