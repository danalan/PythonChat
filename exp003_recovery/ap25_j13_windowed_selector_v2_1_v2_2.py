#!/usr/bin/env python3
from __future__ import annotations
import json
from pathlib import Path

ROOT=Path(__file__).resolve().parent
MODEL_PATH=ROOT/'ap25_j13_model_output.txt'
PRICE_PATH=ROOT/'ap25_j13_price_snapshot_pre_cutoff.json'
OPEN_CANON=437.3012159211471
SHADOW_OPEN={'FK15':475.09201602517317,'FK20':470.3155484227055,'FK25':465.30994244189486}
FRACTIONS={'FK15':0.15,'FK20':0.20,'FK25':0.25}
MAX_RISK=100.0

def kelly(p,o):
    ev=p*o-1.0
    return ev, ev/(o-1.0)

def canonical_stake(k):
    if k>=0.15:return 20.0
    if k>=0.08:return 15.0
    if k>=0.05:return 10.0
    return 0.0

def load_model():
    text=MODEL_PATH.read_text(encoding='utf-8')
    if not text.startswith('AP25_J13_MODEL_ONLY\n'):
        raise SystemExit('Unexpected J13 model output header')
    return json.loads(text.split('\n',1)[1])

def main():
    model=load_model(); prices=json.loads(PRICE_PATH.read_text(encoding='utf-8'))
    mrows={r['fixture_id']:r for r in model['fixtures']}
    evaluations=[]; approved=[]
    labels=[('HOME','1X2_HOME','home'),('DRAW','1X2_DRAW','draw'),('AWAY','1X2_AWAY','away')]
    for row in prices['rows']:
        mr=mrows[row['fixture_id']]
        outcomes=[]
        for label,mkey,okey in labels:
            p=mr['markets'][mkey]['p_raw']; o=float(row[okey]); ev,k=kelly(p,o)
            outcomes.append({'outcome':label,'p_raw':p,'odds':o,'ev':ev,'full_kelly':k})
        positive=[x for x in outcomes if x['ev']>0]
        cand=max(positive,key=lambda x:x['full_kelly']) if positive else None
        evrow={'fixture_id':row['fixture_id'],'date':mr['date'],'home':mr['home'],'away':mr['away'],'outcomes':outcomes,'risk_adjusted_candidate':cand}
        evaluations.append(evrow)
        if cand and cand['full_kelly']>=0.05:
            ticket={k:cand[k] for k in ('outcome','p_raw','odds','ev','full_kelly')}
            ticket.update({'fixture_id':row['fixture_id'],'date':mr['date'],'home':mr['home'],'away':mr['away'],'stake_mxn':canonical_stake(cand['full_kelly'])})
            approved.append(ticket)
    parlays=[]
    for date in sorted(set(t['date'] for t in approved)):
        legs=sorted([t for t in approved if t['date']==date],key=lambda x:x['full_kelly'],reverse=True)
        if len(legs)>=2:
            a,b=legs[:2]; parlay_odds=a['odds']*b['odds']; p_joint=a['p_raw']*b['p_raw']
            parlays.append({'date':date,'stake_mxn':5.0,'legs':[a['fixture_id']+' '+a['outcome'],b['fixture_id']+' '+b['outcome']],
                            'odds':parlay_odds,'p_joint_independence':p_joint,'ev':p_joint*parlay_odds-1.0})
    canonical_risk=sum(t['stake_mxn'] for t in approved)+sum(p['stake_mxn'] for p in parlays)
    if canonical_risk>MAX_RISK+1e-9: raise SystemExit('Canonical risk cap breached')
    shadows={}
    for name,bank in SHADOW_OPEN.items():
        frac=FRACTIONS[name]
        sts=[]
        for t in approved:
            st=bank*t['full_kelly']*frac
            sts.append({'fixture_id':t['fixture_id'],'outcome':t['outcome'],'odds':t['odds'],'p_raw':t['p_raw'],'full_kelly':t['full_kelly'],'stake_mxn':st})
        risk=sum(x['stake_mxn'] for x in sts)+sum(p['stake_mxn'] for p in parlays)
        scale=1.0
        if risk>MAX_RISK:
            single_total=sum(x['stake_mxn'] for x in sts); fixed=sum(p['stake_mxn'] for p in parlays)
            scale=(MAX_RISK-fixed)/single_total
            for x in sts:x['stake_mxn']*=scale
            risk=MAX_RISK
        shadows[name]={'opening_bankroll':bank,'fraction':frac,'single_tickets':sts,'parlays':parlays,'risk_mxn':risk,'single_scale_if_cap':scale}
    out={'experiment':'EXP-003','jornada':'J13','architecture':'V2.1_WINDOWED_100','promotion_eligibility':False,
         'integrity_class':'MECHANICAL_REPLAY_RESEARCHER_VISIBLE_J13_OUTCOME_EXPOSURE_DURING_PRICE_RESEARCH',
         'model_training_count':model['training_count'],'canonical_opening_bankroll':OPEN_CANON,'evaluations':evaluations,
         'canonical_primary_singles':approved,'canonical_secondary_parlays':parlays,'canonical_total_risk_mxn':canonical_risk,
         'canonical_hold_mxn':MAX_RISK-canonical_risk,'fractional_kelly_v2_2_shadow':shadows,
         'notes':['Selection is mechanical from the model output frozen before external research and the timestamp-verified Bet365 price snapshot.',
                  'Visible J13 outcome exposure occurred during price research; J13 is permanently NO-PROMOTION.',
                  'No exposed outcome affects selection, odds choice, EV, Kelly, gate, stake or parlay composition.']}
    print(json.dumps(out,ensure_ascii=False,sort_keys=True,indent=2))
if __name__=='__main__':main()
