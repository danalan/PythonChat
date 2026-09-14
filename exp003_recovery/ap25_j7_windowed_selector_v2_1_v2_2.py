#!/usr/bin/env python3
"""Apertura 2025 J7 mechanical V2.1 selector + V2.2 fractional-Kelly shadows.

Authoritative probabilities come from the already-frozen J7 model output text.
J7 is NO-PROMOTION because researcher outcome exposure occurred before selection freeze.
"""
from __future__ import annotations
import json
from pathlib import Path

ROOT=Path(__file__).resolve().parent
MODEL_OUT=ROOT/'ap25_j7_model_output.txt'
PRICE_SNAPSHOT=ROOT/'ap25_j7_price_snapshot_pre_cutoff.json'
BUDGET=100.0
CANONICAL_OPENING=510.3012159211471
SHADOW_OPENINGS={'FK15':511.20159944558327,'FK20':513.9092776017159,'FK25':516.6124019445112}
SHADOW_MULT={'FK15':0.15,'FK20':0.20,'FK25':0.25}

MARKET_TO_SIDE={'1X2_HOME':'home','1X2_DRAW':'draw','1X2_AWAY':'away'}

def stake_from_kelly(k:float)->float:
    if k>=0.15:return 20.0
    if k>=0.08:return 15.0
    if k>=0.05:return 10.0
    return 0.0

def load_model():
    text=MODEL_OUT.read_text(encoding='utf-8').strip()
    prefix='AP25_J7_MODEL_ONLY '
    if not text.startswith(prefix):
        raise SystemExit('Unexpected J7 model output format')
    obj=json.loads(text[len(prefix):])
    if obj['training_count']!=1069: raise SystemExit('J7 training-count drift')
    if obj['jornada']!='J7': raise SystemExit('Wrong model output')
    return obj

def main():
    model=load_model(); snap=json.loads(PRICE_SNAPSHOT.read_text(encoding='utf-8'))
    pmap={}
    fixture_meta={}
    for f in model['fixtures']:
        fixture_meta[f['fixture_id']]={k:f[k] for k in ('date','home','away')}
        for market,data in f['markets'].items():
            pmap[(f['fixture_id'],market)]=float(data['p_raw'])
    rows=[]
    for f in snap['markets']:
        fid=f['fixture_id']
        for market,decimal in f['quotes'].items():
            p=pmap[(fid,market)]; o=float(decimal); ev=p*o-1.0
            k=ev/(o-1.0) if ev>0 else 0.0
            rows.append({
                'fixture_id':fid,**fixture_meta[fid],'market':market,'decimal':o,
                'p_raw':p,'break_even':1.0/o,'model_ev':ev,'kelly_score':k,
                'source':f['source'],'source_url':f['source_url']
            })
    best=[]
    for fid in fixture_meta:
        positives=[r for r in rows if r['fixture_id']==fid and r['model_ev']>0]
        if positives:
            best.append(max(positives,key=lambda r:(r['kelly_score'],r['model_ev'])))
    best=sorted(best,key=lambda r:(r['date'],-r['kelly_score'],r['fixture_id']))
    singles=[]
    for r in best:
        stake=stake_from_kelly(r['kelly_score'])
        if stake>0:
            singles.append({**r,'vehicle':'SINGLE_PRIMARY','stake_mxn_simulated':stake})
    canonical_single_total=sum(x['stake_mxn_simulated'] for x in singles)
    parlays=[]; canonical_total=canonical_single_total
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
        raw_stakes=[{'fixture_id':x['fixture_id'],'stake_mxn_simulated':bank*x['kelly_score']*mult} for x in singles]
        parlay_total=5.0*len(parlays)
        single_total=sum(x['stake_mxn_simulated'] for x in raw_stakes)
        scale=1.0
        if single_total+parlay_total>BUDGET and single_total>0:
            scale=(BUDGET-parlay_total)/single_total
            for x in raw_stakes:x['stake_mxn_simulated']*=scale
        shadows[sid]={'opening_bankroll_mxn':bank,'fraction_of_full_kelly':mult,'single_stakes':raw_stakes,
                      'same_fixed_parlays_total_mxn':parlay_total,
                      'total_stake_mxn':sum(x['stake_mxn_simulated'] for x in raw_stakes)+parlay_total,
                      'risk_ceiling_scale_factor':scale}
    out={
        'experiment':'EXP-003','tournament':'Apertura 2025','jornada':'J7',
        'integrity_class':'MECHANICAL_REPLAY_RESEARCHER_OUTCOME_EXPOSED_BEFORE_SELECTION_FREEZE','promotion_eligibility':False,
        'canonical_policy':'V2.1_WINDOWED_100','shadow_policy':'V2.2_FRACTIONAL_KELLY_SHADOW',
        'canonical_opening_bankroll_mxn':CANONICAL_OPENING,'training_count':model['training_count'],
        'all_exact_price_candidates':sorted(rows,key=lambda r:-r['kelly_score']),
        'best_positive_candidate_per_fixture':best,'canonical_primary_singles':singles,
        'canonical_secondary_parlays':parlays,'canonical_total_stake_mxn_simulated':canonical_total,
        'canonical_held_cash_from_budget':BUDGET-canonical_total,'fractional_kelly_shadows':shadows,
        'notes':[
            'No J7 outcome is used in the calculations.',
            'J7 is NO-PROMOTION due to researcher outcome exposure during fixture-source lookup.',
            'Canonical V2.1 uses Kelly only for ranking/gating and fixed stake bands.',
            'V2.2 shadows inherit the exact canonical qualifying singles and fixed secondary parlays; only single sizing changes.',
            'CORE/VALUE/LONGSHOT labels have no admission or capital-allocation authority.'
        ]}
    print('AP25_J7_SELECTION '+json.dumps(out,ensure_ascii=False,sort_keys=True),flush=True)

if __name__=='__main__':main()
