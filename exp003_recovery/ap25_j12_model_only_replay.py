#!/usr/bin/env python3
"""Apertura 2025 J12 model-only replay under frozen V0.1R + calibration shadow.

J12 is permanently NO-PROMOTION because the supplied external firewall packet visibly exposed
J12 outcomes in its source list before selection freeze. No J12 outcome is used here.
Training contains completed Liga MX through J11 only.
"""
from __future__ import annotations
import json
from datetime import datetime
import ap25_j11_model_only_replay as prev
import ap25_j6_model_only_replay as j6

base=prev.base
MODEL_CUTOFF=datetime(2025,10,3,0,0,0)

J11_FROZEN=[
base.Match(datetime(2025,9,26),"FC Juárez","Club León",2,0,"AP25_J11_FROZEN"),
base.Match(datetime(2025,9,26),"Puebla FC","Deportivo Guadalajara",0,2,"AP25_J11_FROZEN"),
base.Match(datetime(2025,9,27),"CF Pachuca","Atlético San Luis",2,1,"AP25_J11_FROZEN"),
base.Match(datetime(2025,9,27),"Atlas Guadalajara","Club Necaxa",3,2,"AP25_J11_FROZEN"),
base.Match(datetime(2025,9,27),"CF Monterrey","Santos Laguna",1,0,"AP25_J11_FROZEN"),
base.Match(datetime(2025,9,27),"Deportivo Toluca","Mazatlán FC",3,1,"AP25_J11_FROZEN"),
base.Match(datetime(2025,9,27),"CF América","Pumas UNAM",4,1,"AP25_J11_FROZEN"),
base.Match(datetime(2025,9,28),"Gallos Blancos","UANL Tigres",0,2,"AP25_J11_FROZEN"),
base.Match(datetime(2025,9,28),"Club Tijuana","Cruz Azul",2,0,"AP25_J11_FROZEN")]

FIXTURES=[
("AP25J12-01","2025-10-03","Club Necaxa","CF Pachuca"),
("AP25J12-02","2025-10-03","Mazatlán FC","Atlético San Luis"),
("AP25J12-03","2025-10-03","Atlas Guadalajara","FC Juárez"),
("AP25J12-04","2025-10-04","Gallos Blancos","Puebla FC"),
("AP25J12-05","2025-10-04","Club León","Deportivo Toluca"),
("AP25J12-06","2025-10-04","UANL Tigres","Cruz Azul"),
("AP25J12-07","2025-10-04","CF América","Santos Laguna"),
("AP25J12-08","2025-10-05","Pumas UNAM","Deportivo Guadalajara"),
("AP25J12-09","2025-10-05","Club Tijuana","CF Monterrey")]

def main():
    hist=[m for m in base.load_all() if m.date<datetime(2025,7,11)]
    if len(hist)!=1016: raise SystemExit(f"chronology drift pre-J1: {len(hist)}")
    j10=prev.prev
    tr=sorted(
        hist+j6.J1_FROZEN+j6.J2_FROZEN+j6.J3_FROZEN+j6.J4_FROZEN+j6.J5_FROZEN+
        j10.prev.prev.prev.J6_FROZEN+j10.prev.prev.J7_FROZEN+j10.prev.J8_FROZEN+
        j10.prev.J1_BACKFILL+j10.J9_FROZEN+prev.J10_FROZEN+J11_FROZEN,
        key=lambda m:(m.date,m.home,m.away,m.hg,m.ag))
    if len(tr)!=1115: raise SystemExit(f"J12 training count drift: expected 1115, got {len(tr)}")
    if any(m.date>=MODEL_CUTOFF for m in tr): raise SystemExit("J12 leakage detected")
    mods=base.ensemble(tr,MODEL_CUTOFF); rows=[]
    for fid,date,home,away in FIXTURES:
        M,meta=base.avg_matrix(mods,home,away); pp=j6.market_probs(M)
        rows.append({"fixture_id":fid,"date":date,"home":home,"away":away,
                     "markets":{k:{"p_raw":float(v),"p_cal_shadow":float(j6.cal(v))} for k,v in pp.items()},
                     "model_meta":meta})
    out={"experiment":"EXP-003","tournament":"Apertura 2025","jornada":"J12","model":"V0.1R_DC_ENSEMBLE",
         "calibration_shadow":"CAL_SHRINK_GLOBAL_V0_1","model_cutoff":"2025-10-03T00:00:00-06:00",
         "training_count":len(tr),"training_includes":"Apertura 2025 completed fixtures through J11 plus Sep.17 J1 backfill",
         "integrity_class":"MODEL_SIGNAL_FROZEN_WITH_NO_J12_OUTCOME_INPUTS_EXTERNAL_PACKET_VISIBLE_J12_OUTCOME_EXPOSURE",
         "promotion_eligibility":False,"fixtures":rows,
         "notes":["No J12 result is an input.","Raw V0.1R remains canonical for V2.1 selection.",
                  "Internal canonical ledger is authoritative for endogenous football data.",
                  "J12 is permanently NO-PROMOTION because the external packet visibly exposed J12 outcomes before selection freeze."]}
    print("AP25_J12_MODEL_ONLY "+json.dumps(out,ensure_ascii=False,sort_keys=True),flush=True)
if __name__=='__main__':main()
