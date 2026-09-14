#!/usr/bin/env python3
"""Apertura 2025 J10 mechanical V2.1 selector + V2.2 fractional-Kelly shadows."""
from __future__ import annotations
import json
from pathlib import Path
ROOT=Path(__file__).resolve().parent
MODEL_OUT=ROOT/'ap25_j10_model_output.txt'
PRICE_SNAPSHOT=ROOT/'ap25_j10_price_snapshot_pre_cutoff.json'
BUDGET=100.0
CANONICAL_OPENING=457.3012159211471
SHADOW_OPENINGS={'FK15':484.17507281219184,'FK20':482.3624371369899,'FK25':480.28051643649303}
SHADOW_MULT={'FK15':0.15,'FK20':0.20,'FK25':0.25}

def stake_from_kelly(k:float)->float:
    if k>=0.15:return 20.0
    if k>=0.08:return 15.0
    if k>=0.05:return 10.0
    return 0.0

def load_model():
    text=MODEL_OUT.read_text(encoding='utf-8').strip(); prefix='AP25_J10_MODEL_ONLY '
    if not text.startswith(prefix): raise SystemExit('Unexpected J10 model output format')
    obj=json.loads(text[len(prefix):])
    if obj['training_count']!=1097: raise SystemExit('J10 training-count drift')
    if obj['jornada']!='J10': raise SystemExit('Wrong model output')
    return obj

def main():
    model=load_model(); snap=json.loads(PRICE_SNAPSHOT.read_text(encoding='utf-8'))
    pmap={}; fixture_meta={}
    for f in model['fixtures']:
        fixture_meta[f['fixture_id']]={k:f[k] for k in ('date','home','away')}
        for market,data in f['markets'].items(): pmap[(f['fixture_id'],market)]=float(data['p_raw'])
    rows=[]
    for f in snap['fixtures']:
        fid=f['fixture_id']
        for market,decimal in f['prices'].items():
            p=pmap[(fid,market)]; o=float(decimal); ev=p*o-1.0; k=ev/(o-1.0) if ev>0 else 0.0
            rows.append({'fixture_id':fid,**fixture_meta[fid],'market':market,'decimal':o,'p_raw':p,'break_even':1.0/o,
                         'model_ev':ev,'kelly_score':k,'source':f['source'],'source_url':f['source_url']})
    best=[]
    for fid in fixture_meta:
        positives=[r for r in rows if r['fixture_id']==fid and r['model_ev']>0]
        if positives: best.append(max(positives,key=lambda r:(r['kelly_score'],r['model_ev'])))
    best=sorted(best,key=lambda r:(r['date'],-r['kelly_score'],r['fixture_id']))
    singles=[]
    for r in best:
        stake=stake_from_kelly(r['kelly_score'])
        if stake>0: singles.append({**r,'vehicle':'SINGLE_PRIMARY','stake_mxn_simulated':stake})
    canonical_total=sum(x['stake_mxn_simulated'] for x in singles); parlays=[]
    for date in sorted(set(x['date'] for x in singles)):
        wr=sorted([x for x in singles if x['date']==date],key=lambda x:-x['kelly_score'])
        if len(wr)>=2 and canonical_total+5.0<=BUDGET:
            a,b=wr[:2]; odds=a['decimal']*b['decimal']; pj=a['p_raw']*b['p_raw']
            parlays.append({'execution_date':date,'vehicle':'PARLAY_2_SECONDARY','stake_mxn_simulated':5.0,
                            'legs':[a['fixture_id']+'|'+a['market'],b['fixture_id']+'|'+b['market']],
                            'decimal':odds,'p_joint_independence':pj,'model_ev':pj*odds-1.0})
            canonical_total+=5.0
    shadows={}
    for sid,bank in SHADOW_OPENINGS.items():
        mult=SHADOW_MULT[sid]
        raw=[{'fixture_id':x['fixture_id'],'stake_mxn_simulated':bank*x['kelly_score']*mult} for x in singles]
        pt=5.0*len(parlays); st=sum(x['stake_mxn_simulated'] for x in raw); scale=1.0
        if st+pt>BUDGET and st>0:
            scale=(BUDGET-pt)/st
            for x in raw:x['stake_mxn_simulated']*=scale
        shadows[sid]={'opening_bankroll_mxn':bank,'fraction_of_full_kelly':mult,'single_stakes':raw,
                      'same_fixed_parlays_total_mxn':pt,'total_stake_mxn':sum(x['stake_mxn_simulated'] for x in raw)+pt,
                      'risk_ceiling_scale_factor':scale}
    out={'experiment':'EXP-003','tournament':'Apertura 2025','jornada':'J10',
         'integrity_class':'MECHANICAL_REPLAY_EXTERNAL_PACKET_OUTCOME_EXPOSURE_BEFORE_SELECTION_FREEZE','promotion_eligibility':False,
         'canonical_policy':'V2.1_WINDOWED_100','shadow_policy':'V2.2_FRACTIONAL_KELLY_SHADOW',
         'canonical_opening_bankroll_mxn':CANONICAL_OPENING,'training_count':model['training_count'],
         'all_exact_price_candidates':sorted(rows,key=lambda r:-r['kelly_score']),
         'best_positive_candidate_per_fixture':best,'canonical_primary_singles':singles,
         'canonical_secondary_parlays':parlays,'canonical_total_stake_mxn_simulated':canonical_total,
         'canonical_held_cash_from_budget':BUDGET-canonical_total,'fractional_kelly_shadows':shadows,
         'excluded_price_rows':snap['excluded_price_rows'],
         'notes':['No J10 outcome is used in the calculations.','Only three fixtures have accepted complete pre-kickoff 1X2 rows from the supplied firewall packet.',
                  'Chivas-Necaxa was excluded because temporal provenance of its price row was ambiguous.',
                  'Canonical V2.1 uses Kelly only for ranking/gating and fixed stake bands.','V2.2 shadows inherit the exact canonical qualifying singles and fixed secondary parlays; only single sizing changes.']}
    print('AP25_J10_SELECTION '+json.dumps(out,ensure_ascii=False,sort_keys=True),flush=True)
if __name__=='__main__':main()
