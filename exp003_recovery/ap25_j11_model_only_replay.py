#!/usr/bin/env python3
"""Apertura 2025 J11 model-only replay under frozen V0.1R + calibration shadow.

J11 is permanently NO-PROMOTION because the supplied external firewall packet visibly exposed
J11 outcomes in its source list before selection freeze. No J11 outcome is used here.
Training contains completed Liga MX through J10 only.
"""
from __future__ import annotations
import json
from datetime import datetime
import ap25_j10_model_only_replay as prev

base=prev.base
MODEL_CUTOFF=datetime(2025,9,26,0,0,0)

J10_FROZEN=[
base.Match(datetime(2025,9,23),"Deportivo Guadalajara","Club Necaxa",3,1,"AP25_J10_FROZEN"),
base.Match(datetime(2025,9,23),"Puebla FC","CF Pachuca",2,2,"AP25_J10_FROZEN"),
base.Match(datetime(2025,9,23),"Club León","Mazatlán FC",2,2,"AP25_J10_FROZEN"),
base.Match(datetime(2025,9,23),"FC Juárez","Pumas UNAM",3,1,"AP25_J10_FROZEN"),
base.Match(datetime(2025,9,24),"Cruz Azul","Gallos Blancos",2,2,"AP25_J10_FROZEN"),
base.Match(datetime(2025,9,24),"UANL Tigres","Atlas Guadalajara",2,0,"AP25_J10_FROZEN"),
base.Match(datetime(2025,9,24),"Deportivo Toluca","CF Monterrey",6,2,"AP25_J10_FROZEN"),
base.Match(datetime(2025,9,24),"Atlético San Luis","CF América",0,1,"AP25_J10_FROZEN"),
base.Match(datetime(2025,9,24),"Santos Laguna","Club Tijuana",1,0,"AP25_J10_FROZEN")]

FIXTURES=[
("AP25J11-01","2025-09-26","FC Juárez","Club León"),
("AP25J11-02","2025-09-26","Puebla FC","Deportivo Guadalajara"),
("AP25J11-03","2025-09-27","CF Pachuca","Atlético San Luis"),
("AP25J11-04","2025-09-27","Atlas Guadalajara","Club Necaxa"),
("AP25J11-05","2025-09-27","CF Monterrey","Santos Laguna"),
("AP25J11-06","2025-09-27","Deportivo Toluca","Mazatlán FC"),
("AP25J11-07","2025-09-27","CF América","Pumas UNAM"),
("AP25J11-08","2025-09-28","Gallos Blancos","UANL Tigres"),
("AP25J11-09","2025-09-28","Club Tijuana","Cruz Azul")]

def main():
    hist=[m for m in base.load_all() if m.date<datetime(2025,7,11)]
    if len(hist)!=1016: raise SystemExit(f"chronology drift pre-J1: {len(hist)}")
    p=prev.prev
    tr=sorted(hist+p.prev.prev.prev.prev.J1_FROZEN+p.prev.prev.prev.prev.J2_FROZEN+p.prev.prev.prev.prev.J3_FROZEN+p.prev.prev.prev.prev.J4_FROZEN+p.prev.prev.prev.prev.J5_FROZEN+p.prev.prev.prev.J6_FROZEN+p.prev.prev.J7_FROZEN+p.prev.J8_FROZEN+p.J1_BACKFILL+prev.J9_FROZEN+J10_FROZEN,
              key=lambda m:(m.date,m.home,m.away,m.hg,m.ag))
    if len(tr)!=1106: raise SystemExit(f"J11 training count drift: expected 1106, got {len(tr)}")
    if any(m.date>=MODEL_CUTOFF for m in tr): raise SystemExit("J11 leakage detected")
    mods=base.ensemble(tr,MODEL_CUTOFF); rows=[]
    market_probs=p.prev.prev.prev.prev.market_probs
    cal=p.prev.prev.prev.prev.cal
    for fid,date,home,away in FIXTURES:
        M,meta=base.avg_matrix(mods,home,away); pp=market_probs(M)
        rows.append({"fixture_id":fid,"date":date,"home":home,"away":away,
                     "markets":{k:{"p_raw":float(v),"p_cal_shadow":float(cal(v))} for k,v in pp.items()},
                     "model_meta":meta})
    out={"experiment":"EXP-003","tournament":"Apertura 2025","jornada":"J11","model":"V0.1R_DC_ENSEMBLE",
         "calibration_shadow":"CAL_SHRINK_GLOBAL_V0_1","model_cutoff":"2025-09-26T00:00:00-06:00",
         "training_count":len(tr),"training_includes":"Apertura 2025 completed fixtures through J10 plus Sep.17 J1 backfill",
         "integrity_class":"MODEL_SIGNAL_FROZEN_WITH_NO_J11_OUTCOME_INPUTS_EXTERNAL_PACKET_VISIBLE_J11_OUTCOME_EXPOSURE",
         "promotion_eligibility":False,"fixtures":rows,
         "notes":["No J11 result is an input.","Raw V0.1R remains canonical for V2.1 selection.",
                  "External packet statistics that contradicted frozen history were not used.",
                  "J11 is permanently NO-PROMOTION because the external packet visibly exposed J11 outcomes before selection freeze."]}
    print("AP25_J11_MODEL_ONLY "+json.dumps(out,ensure_ascii=False,sort_keys=True),flush=True)
if __name__=='__main__':main()
