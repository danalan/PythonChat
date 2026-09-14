#!/usr/bin/env python3
"""Apertura 2025 J4 canonical V2.1 selector + V2.2 fractional-Kelly shadows.

J4 is permanently NO-PROMOTION because the human researcher became outcome-exposed
before selection freeze. The selector itself is mechanical from frozen model output
and frozen pre-kickoff prices only.
"""
from __future__ import annotations
import json
from pathlib import Path

BUDGET = 100.0
OPENING_BANKROLL = 523.0512159211471
KELLY_GATE = 0.05
PARLAY_STAKE = 5.0
SHADOW_FRACTIONS = {"FK15":0.15,"FK20":0.20,"FK25":0.25}
HERE = Path(__file__).resolve().parent
MODEL_PATH = HERE / "ap25_j4_model_output.txt"
PRICE_PATH = HERE / "ap25_j4_price_snapshot_pre_cutoff.json"

def stake_from_kelly(k):
    if k >= 0.15: return 20.0
    if k >= 0.08: return 15.0
    if k >= 0.05: return 10.0
    return 0.0

def load_model():
    txt = MODEL_PATH.read_text(encoding="utf-8").strip()
    prefix = "AP25_J4_MODEL_ONLY "
    if not txt.startswith(prefix):
        raise SystemExit("Unexpected J4 model output prefix")
    return json.loads(txt[len(prefix):])

def main():
    mdl = load_model()
    snap = json.loads(PRICE_PATH.read_text(encoding="utf-8"))
    if mdl.get("training_count") != 1042:
        raise SystemExit(f"J4 training count drift: {mdl.get('training_count')}")
    prob = {}
    meta = {}
    for f in mdl["fixtures"]:
        fid=f["fixture_id"]
        meta[fid]={"date":f["date"],"home":f["home"],"away":f["away"]}
        for market,v in f["markets"].items():
            prob[(fid,market)] = float(v["p_raw"])

    rows=[]
    for f in snap["fixtures"]:
        fid=f["fixture_id"]
        for market,o in f["prices"].items():
            key=(fid,market)
            if key not in prob: continue
            p=prob[key]; o=float(o); ev=p*o-1.0
            k=ev/(o-1.0) if o>1 and ev>0 else 0.0
            rows.append({
                "fixture_id":fid,**meta[fid],"market":market,"decimal":o,
                "source":f["source"],"published":f["published"],
                "p_raw":p,"break_even":1.0/o,"model_ev":ev,"kelly_score":k
            })

    by_fixture={}
    for r in rows:
        if r["model_ev"] <= 0: continue
        old=by_fixture.get(r["fixture_id"])
        if old is None or (r["kelly_score"],r["model_ev"]) > (old["kelly_score"],old["model_ev"]):
            by_fixture[r["fixture_id"]]=r
    best=sorted(by_fixture.values(),key=lambda r:(r["date"],-r["kelly_score"],r["fixture_id"]))

    singles=[]
    for r in best:
        stake=stake_from_kelly(r["kelly_score"])
        if stake>0:
            singles.append({**r,"stake_mxn_simulated":stake,"vehicle":"SINGLE_PRIMARY"})
    canonical_single_total=sum(x["stake_mxn_simulated"] for x in singles)
    if canonical_single_total>BUDGET:
        raise SystemExit("Canonical singles exceed J4 budget")

    parlays=[]
    running_total=canonical_single_total
    for date in sorted({x["date"] for x in singles}):
        wr=sorted([x for x in singles if x["date"]==date],key=lambda x:-x["kelly_score"])
        if len(wr)>=2 and running_total+PARLAY_STAKE<=BUDGET:
            a,b=wr[:2]
            odds=a["decimal"]*b["decimal"]
            pj=a["p_raw"]*b["p_raw"]
            parlays.append({
                "window":date,"vehicle":"PARLAY_2_SECONDARY","stake_mxn_simulated":PARLAY_STAKE,
                "legs":[{"fixture_id":a["fixture_id"],"market":a["market"]},{"fixture_id":b["fixture_id"],"market":b["market"]}],
                "decimal":odds,"p_joint_independence":pj,"model_ev":pj*odds-1.0
            })
            running_total+=PARLAY_STAKE

    shadow={}
    parlay_total=sum(p["stake_mxn_simulated"] for p in parlays)
    single_capacity=BUDGET-parlay_total
    for sid,mult in SHADOW_FRACTIONS.items():
        raw=[]
        for x in singles:
            stake=OPENING_BANKROLL*x["kelly_score"]*mult
            raw.append({
                "fixture_id":x["fixture_id"],"date":x["date"],"home":x["home"],"away":x["away"],
                "market":x["market"],"decimal":x["decimal"],"p_raw":x["p_raw"],"kelly_score":x["kelly_score"],
                "stake_mxn_simulated":stake
            })
        raw_total=sum(x["stake_mxn_simulated"] for x in raw)
        scale=min(1.0,single_capacity/raw_total) if raw_total>0 else 1.0
        for x in raw: x["stake_mxn_simulated"]*=scale
        shadow[sid]={
            "fraction_of_full_kelly":mult,
            "single_stakes":raw,
            "single_scale_factor_for_risk_ceiling":scale,
            "single_stake_total_mxn":sum(x["stake_mxn_simulated"] for x in raw),
            "same_fixed_secondary_parlays":parlays,
            "total_stake_mxn":sum(x["stake_mxn_simulated"] for x in raw)+parlay_total
        }

    out={
        "experiment":"EXP-003","tournament":"Apertura 2025","jornada":"J4",
        "canonical_policy":"V2.1_WINDOWED_100","shadow_policy":"V2.2_FRACTIONAL_KELLY_SHADOW",
        "money_type":"SIMULATED_PAPER_ONLY",
        "integrity_class":"MECHANICAL_REPLAY_RESEARCHER_OUTCOME_EXPOSED","promotion_eligibility":False,
        "opening_bankroll_mxn_simulated":OPENING_BANKROLL,"jornada_risk_budget_mxn":BUDGET,
        "training_count":mdl["training_count"],
        "all_exact_price_candidates":sorted(rows,key=lambda r:-r["kelly_score"]),
        "best_positive_candidate_per_fixture":best,
        "canonical_primary_singles":singles,
        "canonical_secondary_two_leg_parlays":parlays,
        "canonical_total_stake_mxn_simulated":running_total,
        "canonical_held_cash_from_budget":BUDGET-running_total,
        "fractional_kelly_shadows":shadow,
        "notes":[
            "V2.1 remains the only canonical economic track; J4 cannot promote changes.",
            "V2.2 inherits the exact canonical qualifying singles and changes single-bet sizing only.",
            "No p>=65% gate, odds floor, mandatory bucket allocation, or price-only longshot penalty exists.",
            "CORE/VALUE/LONGSHOT remains reporting taxonomy only; no bucket changes admission or stake.",
            "Shadow stakes retain full decimal precision internally and are subject to the same MXN100 jornada risk ceiling.",
            "The same fixed MXN5 qualifying parlay is held constant across tracks to isolate single-stake sizing."
        ]
    }
    print("AP25_J4_SELECTION",json.dumps(out,ensure_ascii=False,sort_keys=True),flush=True)

if __name__=="__main__":
    main()
