#!/usr/bin/env python3
"""C0.1 CORNERS SHADOW model for project 1000 a 100000.

Architecture status: SHADOW ONLY. This module is a separate corner process and
MUST NOT mutate Vn-2026 goal-model parameters. It is intentionally modeled with
Negative Binomial counts because corner counts are overdispersed relative to a
simple Poisson in football data.

State variables fit at explicit cutoff:
- team corner attack
- team corner defense
- global intercept
- home-corner advantage
- shared NB dispersion k

Architecture choices frozen for C0.1 shadow:
- literal half-life decay ensemble: 180 / 365 / 730 / 1460 days
- home and away corner counts conditionally independent in C0.1
- market probabilities are read-outs from the joint corner-count matrix
- no real staking eligibility; signals are logging/shadow only

Any future correlation structure, covariates, feature set, different half-lives,
or staking eligibility is an ARCHITECTURE UPDATE and must clear DTL promotion.
"""
from __future__ import annotations
from dataclasses import dataclass
from datetime import datetime
import math
import numpy as np
from scipy.optimize import minimize
from scipy.stats import nbinom

HALF_LIVES=(180,365,730,1460)
MAX_CORNERS=25

@dataclass(frozen=True)
class CornerMatch:
    date: datetime
    home: str
    away: str
    home_corners: int
    away_corners: int
    source: str="FotMob"

@dataclass(frozen=True)
class CornerFit:
    teams: tuple[str,...]
    theta: np.ndarray
    half_life: int
    cutoff: datetime

    @property
    def n(self): return len(self.teams)

    def unpack(self):
        n=self.n
        attack=self.theta[:n]
        defense=self.theta[n:2*n]
        intercept=float(self.theta[2*n])
        home_adv=float(self.theta[2*n+1])
        log_k=float(self.theta[2*n+2])
        return attack,defense,intercept,home_adv,math.exp(log_k)


def _weights(rows,cutoff,half_life):
    ages=np.array([max(0.0,(cutoff-r.date).total_seconds()/86400.0) for r in rows])
    return np.power(0.5,ages/float(half_life))


def _nb_logpmf(y,mu,k):
    p=k/(k+mu)
    return nbinom.logpmf(y,k,p)


def fit_corner_model(rows:list[CornerMatch],cutoff:datetime,half_life:int)->CornerFit:
    eligible=[r for r in rows if r.date<cutoff]
    if not eligible:
        raise ValueError("no corner matches before cutoff")
    teams=tuple(sorted({r.home for r in eligible}|{r.away for r in eligible}))
    idx={t:i for i,t in enumerate(teams)}
    n=len(teams)
    h=np.array([idx[r.home] for r in eligible],dtype=int)
    a=np.array([idx[r.away] for r in eligible],dtype=int)
    yc_h=np.array([r.home_corners for r in eligible],dtype=float)
    yc_a=np.array([r.away_corners for r in eligible],dtype=float)
    w=_weights(eligible,cutoff,half_life)

    # empirical initialization
    mean_c=max(0.1,float(np.mean(np.r_[yc_h,yc_a])))
    x0=np.zeros(2*n+3,dtype=float)
    x0[2*n]=math.log(mean_c)
    x0[2*n+1]=0.05
    x0[2*n+2]=math.log(8.0)

    def objective(x):
        attack=x[:n]; defense=x[n:2*n]
        intercept=x[2*n]; home_adv=x[2*n+1]; k=math.exp(x[2*n+2])
        mu_h=np.exp(intercept+home_adv+attack[h]+defense[a])
        mu_a=np.exp(intercept+attack[a]+defense[h])
        ll=_nb_logpmf(yc_h,mu_h,k)+_nb_logpmf(yc_a,mu_a,k)
        # Identifiability only. Not predictive regularization.
        penalty=1000.0*(float(attack.sum())**2+float(defense.sum())**2)
        return -float(np.sum(w*ll))+penalty

    res=minimize(objective,x0,method="L-BFGS-B",options={"maxiter":1200,"ftol":1e-11})
    if not res.success:
        raise RuntimeError(f"corner fit failed: {res.message}")
    return CornerFit(teams,np.asarray(res.x,dtype=float),half_life,cutoff)


def means(model:CornerFit,home:str,away:str):
    if home not in model.teams or away not in model.teams:
        raise KeyError("team missing from corner fit")
    i=model.teams.index(home); j=model.teams.index(away)
    attack,defense,intercept,home_adv,k=model.unpack()
    mu_h=math.exp(intercept+home_adv+attack[i]+defense[j])
    mu_a=math.exp(intercept+attack[j]+defense[i])
    return mu_h,mu_a,k


def joint_matrix(model:CornerFit,home:str,away:str,max_corners:int=MAX_CORNERS):
    mu_h,mu_a,k=means(model,home,away)
    xs=np.arange(max_corners+1)
    ph=nbinom.pmf(xs,k,k/(k+mu_h))
    pa=nbinom.pmf(xs,k,k/(k+mu_a))
    # C0.1 conditional-independence assumption; tracked as a shadow limitation.
    M=np.outer(ph,pa)
    M=M/M.sum()
    return M,{"mu_home_corners":mu_h,"mu_away_corners":mu_a,"dispersion_k":k}


def ensemble(rows:list[CornerMatch],cutoff:datetime):
    return [fit_corner_model(rows,cutoff,h) for h in HALF_LIVES]


def avg_matrix(models,home,away,max_corners:int=MAX_CORNERS):
    mats=[]; meta=[]
    for m in models:
        M,z=joint_matrix(m,home,away,max_corners)
        mats.append(M); meta.append({"half_life":m.half_life,**z})
    A=np.mean(np.stack(mats),axis=0)
    return A/A.sum(),meta


def market_probs(M):
    n=M.shape[0]
    home_m=M.sum(axis=1); away_m=M.sum(axis=0)
    out={
      "CORNERS_HOME_MORE":float(np.tril(M,-1).sum()),
      "CORNERS_TIE":float(np.trace(M)),
      "CORNERS_AWAY_MORE":float(np.triu(M,1).sum()),
    }
    for line in (7.5,8.5,9.5,10.5,11.5,12.5):
        k=int(line)
        u=float(sum(M[i,j] for i in range(n) for j in range(n) if i+j<=k))
        out[f"TOTAL_CORNERS_U{line}"]=u
        out[f"TOTAL_CORNERS_O{line}"]=1-u
    for side,marg in (("HOME",home_m),("AWAY",away_m)):
        for line in (2.5,3.5,4.5,5.5,6.5,7.5):
            k=int(line); u=float(marg[:k+1].sum())
            out[f"{side}_CORNERS_U{line}"]=u
            out[f"{side}_CORNERS_O{line}"]=1-u
    return out


def extract_corner_pair(match_details:dict):
    """Best-effort FotMob matchDetails parser.

    Finds a stat object whose title/key/name normalizes to 'corners' and whose
    values resolve to a home/away pair. Schema changes must fail closed rather
    than silently returning invented zeros.
    """
    hits=[]
    def walk(x):
        if isinstance(x,dict):
            label=str(x.get("title") or x.get("key") or x.get("name") or "").strip().lower()
            if label in {"corners","corner kicks","corner"}:
                hits.append(x)
            for v in x.values(): walk(v)
        elif isinstance(x,list):
            for v in x: walk(v)
    walk(match_details)

    def as_int(v):
        if isinstance(v,(int,float)) and float(v).is_integer(): return int(v)
        if isinstance(v,str):
            s=v.strip().replace("%","")
            try: return int(float(s))
            except Exception: return None
        if isinstance(v,dict):
            for key in ("value","statValue","displayValue"):
                if key in v:
                    q=as_int(v[key])
                    if q is not None: return q
        return None

    for h in hits:
        candidate_pairs=[
          (h.get("home"),h.get("away")),
          (h.get("homeValue"),h.get("awayValue")),
          (h.get("homeStat"),h.get("awayStat")),
        ]
        vals=h.get("stats") or h.get("values")
        if isinstance(vals,list) and len(vals)>=2:
            candidate_pairs.append((vals[0],vals[1]))
        for x,y in candidate_pairs:
            a,b=as_int(x),as_int(y)
            if a is not None and b is not None and 0<=a<=40 and 0<=b<=40:
                return a,b
    raise ValueError("FotMob Corners stat not found or unsupported schema")


if __name__=="__main__":
    print({"model":"C0.1-CORNERS-NB-ENSEMBLE","status":"SHADOW_ONLY","half_lives":HALF_LIVES})
