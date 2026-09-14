#!/usr/bin/env python3
"""Apertura 2025 J5 canonical V2.1 selector + independent-bankroll V2.2 shadows.

J5 is NO-PROMOTION because the researcher became outcome-exposed before selection
freeze. Selection remains mechanical from frozen J5 model inputs and frozen prices.
"""
from __future__ import annotations
import json
from pathlib import Path
import ap25_j5_model_only_replay as mdl

BUDGET=100.0
KELLY_GATE=0.05
PARLAY_STAKE=5.0
CANONICAL_OPEN=508.8012159211471
SHADOW_OPENS={
    "FK15":517.5288384645028,
    "FK20":517.3547126456212,
    "FK25":517.1805868267398,
}
SHADOW_FRACTIONS={"FK15":0.15,"FK20":0.20,"FK25":0.25}
SNAP=Path(__file__).with_name("ap25_j5_price_snapshot_pre_cutoff.json")

def stake_from_kelly(k):
    if k>=0.15:return 20.0
    if k>=0.08:return 15.0
    if k>=0.05:return 10.0
    return 0.0

def main():
    snap=json.loads(SNAP.read_text(encoding="utf-8"))
    hist=[m for m in mdl.base.load_all() if m.date < mdl.datetime(2025,7,11)]
    if len(hist)!=1016: raise SystemExit(f"chronology drift pre-J1: {len(hist)}")
    tr=sorted(hist+mdl.J1_FROZEN+mdl.J2_FROZEN+mdl.J3_FROZEN+mdl.J4_FROZEN,key=lambda m:(m.date,m.home,m.away,m.hg,m.ag))
    if len(tr)!=1051: raise SystemExit(f"J5 training count drift: expected 1051, got {len(tr)}")
    if any(m.date>=mdl.MODEL_CUTOFF for m in tr): raise SystemExit("J5 leakage detected")
    mods=mdl.base.ensemble(tr,mdl.MODEL_CUTOFF)
    probs={}; fixture_meta={}
    for fid,date,home,away in mdl.FIXTURES:
        M,_=mdl.base.avg_matrix(mods,home,away); pp=mdl.market_probs(M)
        fixture_meta[fid]={"date":date,"home":home,"away":away}
        for market,p in pp.items(): probs[(fid,market)]=float(p)

    rows=[]
    for f in snap["fixtures"]:
        fid=f["fixture_id"]
        for market,o in f["prices"].items():
            key=(fid,market)
            if key not in probs: continue
            p=probs[key]; o=float(o); ev=p*o-1.0
            k=ev/(o-1.0) if o>1 and ev>0 else 0.0
            rows.append({
                "fixture_id":fid,**fixture_meta[fid],"market":market,"decimal":o,
                "source":f["source"],"published":f["published"],"p_raw":p,
                "p_cal_shadow":mdl.cal(p),"break_even":1.0/o,"model_ev":ev,"kelly_score":k
            })

    by_fixture={}
    for r in rows:
        if r["model_ev"]<=0: continue
        old=by_fixture.get(r["fixture_id"])
        if old is None or (r["kelly_score"],r["model_ev"])>(old["kelly_score"],old["model_ev"]):
            by_fixture[r["fixture_id"]]=r
    best=sorted(by_fixture.values(),key=lambda r:(r["date"],-r["kelly_score"],r["fixture_id"]))

    singles=[]
    for r in best:
        stake=stake_from_kelly(r["kelly_score"])
        if stake>0: singles.append({**r,"stake_mxn_simulated":stake,"vehicle":"SINGLE_PRIMARY"})
    single_total=sum(x["stake_mxn_simulated"] for x in singles)
    if single_total>BUDGET: raise SystemExit(f"Canonical singles exceed budget: {single_total}")

    parlays=[]; running=single_total
    for date in sorted({x["date"] for x in singles}):
        wr=sorted([x for x in singles if x["date"]==date],key=lambda x:-x["kelly_score"])
        if len(wr)>=2 and running+PARLAY_STAKE<=BUDGET:
            a,b=wr[:2]; odds=a["decimal"]*b["decimal"]; pj=a["p_raw"]*b["p_raw"]
            parlays.append({"window":date,"vehicle":"PARLAY_2_SECONDARY","stake_mxn_simulated":PARLAY_STAKE,
                            "legs":[{"fixture_id":a["fixture_id"],"market":a["market"]},{"fixture_id":b["fixture_id"],"market":b["market"]}],
                            "decimal":odds,"p_joint_independence":pj,"model_ev":pj*odds-1.0})
            running+=PARLAY_STAKE

    parlay_total=sum(x["stake_mxn_simulated"] for x in parlays)
    shadow={}
    for sid,mult in SHADOW_FRACTIONS.items():
        bank=SHADOW_OPENS[sid]
        sr=[]
        for x in singles:
            sr.append({"fixture_id":x["fixture_id"],"date":x["date"],"home":x["home"],"away":x["away"],"market":x["market"],
                       "decimal":x["decimal"],"p_raw":x["p_raw"],"kelly_score":x["kelly_score"],
                       "stake_mxn_simulated":bank*x["kelly_score"]*mult})
        raw_total=sum(x["stake_mxn_simulated"] for x in sr); capacity=BUDGET-parlay_total
        scale=min(1.0,capacity/raw_total) if raw_total>0 else 1.0
        for x in sr: x["stake_mxn_simulated"]*=scale
        shadow[sid]={"opening_bankroll_mxn":bank,"fraction_of_full_kelly":mult,"single_stakes":sr,
                     "single_scale_factor_for_risk_ceiling":scale,"single_stake_total_mxn":sum(x["stake_mxn_simulated"] for x in sr),
                     "same_fixed_secondary_parlays":parlays,"total_stake_mxn":sum(x["stake_mxn_simulated"] for x in sr)+parlay_total}

    out={"experiment":"EXP-003","tournament":"Apertura 2025","jornada":"J5",
         "canonical_policy":"V2.1_WINDOWED_100","shadow_policy":"V2.2_FRACTIONAL_KELLY_SHADOW",
         "integrity_class":"MECHANICAL_REPLAY_RESEARCHER_OUTCOME_EXPOSED","promotion_eligibility":False,
         "training_count":len(tr),"canonical_opening_bankroll_mxn":CANONICAL_OPEN,
         "shadow_opening_bankrolls_mxn":SHADOW_OPENS,"jornada_risk_budget_mxn":BUDGET,
         "all_exact_price_candidates":sorted(rows,key=lambda r:-r["kelly_score"]),
         "best_positive_candidate_per_fixture":best,"canonical_primary_singles":singles,
         "canonical_secondary_two_leg_parlays":parlays,"canonical_total_stake_mxn":running,"canonical_held_cash_mxn":BUDGET-running,
         "fractional_kelly_shadows":shadow,
         "notes":["No J5 outcome is used by the mechanical selector.","V2.1 remains canonical; V2.2 changes sizing only.",
                  "Each V2.2 shadow begins J5 from its own J4 closing bankroll.","CORE/VALUE/LONGSHOT has no selection or stake authority."]}
    print("AP25_J5_SELECTION",json.dumps(out,ensure_ascii=False,sort_keys=True),flush=True)

if __name__=="__main__": main()
