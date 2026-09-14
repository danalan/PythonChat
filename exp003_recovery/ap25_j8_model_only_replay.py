#!/usr/bin/env python3
"""Apertura 2025 J8 model-only replay under frozen V0.1R + calibration shadow.

J8 is permanently NO-PROMOTION because the researcher was exposed to future-tournament
information while recovering the preseason schedule source. No J8 result is used here.
Training contains only the frozen historical seasons plus completed Apertura 2025 J1-J7.
"""
from __future__ import annotations
import json
from datetime import datetime
import ap25_j7_model_only_replay as prev

base=prev.base
MODEL_CUTOFF=datetime(2025,9,12,0,0,0)

J7_FROZEN=[
base.Match(datetime(2025,8,29),"FC Juárez","Mazatlán FC",1,0,"AP25_J7_FROZEN"),
base.Match(datetime(2025,8,29),"Atlético San Luis","Deportivo Toluca",1,3,"AP25_J7_FROZEN"),
base.Match(datetime(2025,8,29),"Puebla FC","CF Monterrey",2,4,"AP25_J7_FROZEN"),
base.Match(datetime(2025,8,30),"Club León","Gallos Blancos",3,0,"AP25_J7_FROZEN"),
base.Match(datetime(2025,8,30),"Deportivo Guadalajara","Cruz Azul",1,2,"AP25_J7_FROZEN"),
base.Match(datetime(2025,8,30),"Santos Laguna","UANL Tigres",0,1,"AP25_J7_FROZEN"),
base.Match(datetime(2025,8,30),"CF América","CF Pachuca",2,0,"AP25_J7_FROZEN"),
base.Match(datetime(2025,8,31),"Pumas UNAM","Atlas Guadalajara",1,0,"AP25_J7_FROZEN"),
base.Match(datetime(2025,8,31),"Club Tijuana","Club Necaxa",3,0,"AP25_J7_FROZEN")]

FIXTURES=[
("AP25J8-01","2025-09-12","Club Necaxa","FC Juárez"),
("AP25J8-02","2025-09-12","CF América","Deportivo Guadalajara"),
("AP25J8-03","2025-09-12","Mazatlán FC","Pumas UNAM"),
("AP25J8-04","2025-09-13","CF Pachuca","Cruz Azul"),
("AP25J8-05","2025-09-13","UANL Tigres","Club León"),
("AP25J8-06","2025-09-13","Atlas Guadalajara","Santos Laguna"),
("AP25J8-07","2025-09-13","Deportivo Toluca","Puebla FC"),
("AP25J8-08","2025-09-14","Gallos Blancos","CF Monterrey"),
("AP25J8-09","2025-09-14","Atlético San Luis","Club Tijuana")]

def main():
    hist=[m for m in base.load_all() if m.date<datetime(2025,7,11)]
    if len(hist)!=1016: raise SystemExit(f"chronology drift pre-J1: {len(hist)}")
    tr=sorted(hist+prev.prev.J1_FROZEN+prev.prev.J2_FROZEN+prev.prev.J3_FROZEN+prev.prev.J4_FROZEN+prev.prev.J5_FROZEN+prev.J6_FROZEN+J7_FROZEN,
              key=lambda m:(m.date,m.home,m.away,m.hg,m.ag))
    if len(tr)!=1078: raise SystemExit(f"J8 training count drift: expected 1078, got {len(tr)}")
    if any(m.date>=MODEL_CUTOFF for m in tr): raise SystemExit("J8 leakage detected")
    mods=base.ensemble(tr,MODEL_CUTOFF); rows=[]
    for fid,date,home,away in FIXTURES:
        M,meta=base.avg_matrix(mods,home,away); pp=prev.prev.market_probs(M)
        rows.append({"fixture_id":fid,"date":date,"home":home,"away":away,
                     "markets":{k:{"p_raw":float(v),"p_cal_shadow":float(prev.prev.cal(v))} for k,v in pp.items()},
                     "model_meta":meta})
    out={"experiment":"EXP-003","tournament":"Apertura 2025","jornada":"J8","model":"V0.1R_DC_ENSEMBLE",
         "calibration_shadow":"CAL_SHRINK_GLOBAL_V0_1","model_cutoff":"2025-09-12T00:00:00-06:00",
         "training_count":len(tr),"training_includes":"Apertura 2025 J1-J7 completed fixtures",
         "integrity_class":"MODEL_SIGNAL_FROZEN_WITH_NO_J8_OUTCOME_INPUTS_RESEARCHER_FUTURE_TOURNAMENT_EXPOSURE",
         "promotion_eligibility":False,"fixtures":rows,
         "notes":["No J8 result is an input.","Raw V0.1R remains canonical for V2.1 selection.",
                  "J8 is permanently NO-PROMOTION because future-tournament information was visible before selection freeze."]}
    print("AP25_J8_MODEL_ONLY",json.dumps(out,ensure_ascii=False,sort_keys=True),flush=True)
if __name__=="__main__": main()
