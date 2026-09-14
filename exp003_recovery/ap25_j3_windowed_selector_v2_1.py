#!/usr/bin/env python3
"""Apertura 2025 J3 mechanical price-aware selector under frozen Execution Policy V2.1.

J3 researcher outcome exposure occurred before the final price snapshot. Therefore:
- selection is purely mechanical from frozen V0.1R probabilities + archived prices;
- human/context input cannot add, remove, reorder, or resize wagers;
- J3 is permanently NO-PROMOTION regardless of settlement.
"""
from __future__ import annotations
import json
from pathlib import Path
import ap25_j3_model_only_replay as mdl

BUDGET=100.0
OPENING_BANKROLL=549.8012159211471
SNAP=Path(__file__).with_name('ap25_j3_price_snapshot_pre_cutoff.json')
WINDOW_ORDER={"FRIDAY":0,"SATURDAY":1}

def stake_from_kelly(k):
    if k>=0.15:return 20.0
    if k>=0.08:return 15.0
    if k>=0.05:return 10.0
    return 0.0

def main():
    snap=json.loads(SNAP.read_text())
    hist=[m for m in mdl.base.load_all() if m.date < mdl.datetime(2025,7,11)]
    if len(hist)!=1016: raise SystemExit(f"chronology drift: expected pre-J1 1016, got {len(hist)}")
    tr=sorted(hist+mdl.J1_FROZEN+mdl.J2_FROZEN,key=lambda m:(m.date,m.home,m.away,m.hg,m.ag))
    if len(tr)!=1033: raise SystemExit(f"J3 training count drift: expected 1033, got {len(tr)}")
    mods=mdl.base.ensemble(tr,mdl.MODEL_CUTOFF)
    probs={}
    for fid,date,home,away in mdl.FIXTURES:
        M,_=mdl.base.avg_matrix(mods,home,away)
        pp=mdl.market_probs(M)
        for market,p in pp.items(): probs[(fid,market)]=float(p)
    rows=[]
    for q in snap['markets']:
        key=(q['fixture_id'],q['market'])
        if key not in probs: continue
        p=probs[key]; o=float(q['decimal']); ev=p*o-1.0
        kelly=ev/(o-1.0) if o>1 and ev>0 else 0.0
        rows.append({**q,"p_raw":p,"p_cal_shadow":mdl.cal(p),"break_even":1.0/o,"model_ev":ev,"kelly_score":kelly})
    by_fixture={}
    for r in rows:
        if r['model_ev']<=0: continue
        old=by_fixture.get(r['fixture_id'])
        if old is None or (r['kelly_score'],r['model_ev'])>(old['kelly_score'],old['model_ev']):
            by_fixture[r['fixture_id']]=r
    best=sorted(by_fixture.values(),key=lambda r:(WINDOW_ORDER[r['window']],-r['kelly_score'],r['fixture_id']))
    singles=[]
    for r in best:
        stake=stake_from_kelly(r['kelly_score'])
        if stake>0:
            singles.append({**r,"stake_mxn_simulated":stake,"vehicle":"SINGLE_PRIMARY"})
    total=sum(x['stake_mxn_simulated'] for x in singles)
    if total>BUDGET: raise SystemExit(f"Singles exceed frozen weekly budget: {total}")
    parlays=[]
    for window in ("FRIDAY","SATURDAY"):
        wr=sorted([x for x in singles if x['window']==window],key=lambda x:-x['kelly_score'])
        if len(wr)>=2 and total+5.0<=BUDGET:
            a,b=wr[:2]; odds=a['decimal']*b['decimal']; pj=a['p_raw']*b['p_raw']
            parlays.append({"window":window,"vehicle":"PARLAY_2_SECONDARY","stake_mxn_simulated":5.0,
                            "legs":[{"fixture_id":a['fixture_id'],"market":a['market']},{"fixture_id":b['fixture_id'],"market":b['market']}],
                            "decimal":odds,"p_joint_independence":pj,"model_ev":pj*odds-1.0})
            total+=5.0
    out={
        "experiment":"EXP-003","tournament":"Apertura 2025","jornada":"J3",
        "policy":"V2.1_WINDOWED_100","money_type":"SIMULATED_PAPER_ONLY",
        "integrity_class":"MECHANICAL_REPLAY_RESEARCHER_OUTCOME_EXPOSED","promotion_eligibility":False,
        "opening_bankroll_mxn_simulated":OPENING_BANKROLL,"weekly_risk_budget_mxn":BUDGET,
        "training_count":len(tr),"price_snapshot_status":snap['status'],
        "all_exact_price_candidates":sorted(rows,key=lambda r:-r['kelly_score']),
        "best_positive_candidate_per_fixture":best,"primary_singles":singles,
        "secondary_two_leg_parlays":parlays,"total_stake_mxn_simulated":total,
        "held_cash_from_weekly_budget":BUDGET-total,
        "notes":[
            "Kelly is ranking/gating only, not literal bankroll sizing.",
            "CAL_SHRINK_GLOBAL_V0_1 remains shadow-only and cannot alter selection or stake.",
            "Human/statistical context is logged separately and cannot alter J3 selection after researcher outcome exposure.",
            "Only explicitly archived pre-kickoff prices in the frozen snapshot are eligible.",
            "Pachuca-Mazatlan has no eligible timestamped price snapshot and is excluded from economic selection, not from model/statistical analysis.",
            "Returns from early windows cannot replenish the MXN100 risk budget."
        ]
    }
    print("AP25_J3_WINDOWED_SELECTION",json.dumps(out,ensure_ascii=False,sort_keys=True),flush=True)

if __name__=='__main__': main()
