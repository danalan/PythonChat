#!/usr/bin/env python3
"""Apertura 2025 J7 model-only replay under frozen V0.1R + calibration shadow.

J7 is permanently NO-PROMOTION because the researcher saw one J7 result snippet
while recovering the preseason schedule article. No J7 result is used here.
Training contains only the frozen historical seasons plus completed Apertura 2025 J1-J6.
"""
from __future__ import annotations
import json
from datetime import datetime
import ap25_j6_model_only_replay as prev

base=prev.base
MODEL_CUTOFF=datetime(2025,8,29,0,0,0)

J6_FROZEN=[
base.Match(datetime(2025,8,22),"FC Juárez","Santos Laguna",2,1,"AP25_J6_FROZEN"),
base.Match(datetime(2025,8,22),"Gallos Blancos","Atlético San Luis",3,2,"AP25_J6_FROZEN"),
base.Match(datetime(2025,8,22),"Mazatlán FC","UANL Tigres",2,2,"AP25_J6_FROZEN"),
base.Match(datetime(2025,8,22),"Club Tijuana","Deportivo Guadalajara",3,3,"AP25_J6_FROZEN"),
base.Match(datetime(2025,8,23),"Club León","CF Pachuca",1,1,"AP25_J6_FROZEN"),
base.Match(datetime(2025,8,23),"CF Monterrey","Club Necaxa",3,0,"AP25_J6_FROZEN"),
base.Match(datetime(2025,8,23),"Cruz Azul","Deportivo Toluca",1,0,"AP25_J6_FROZEN"),
base.Match(datetime(2025,8,24),"Pumas UNAM","Puebla FC",0,0,"AP25_J6_FROZEN"),
base.Match(datetime(2025,8,24),"Atlas Guadalajara","CF América",2,4,"AP25_J6_FROZEN")]

FIXTURES=[
("AP25J7-01","2025-08-29","FC Juárez","Mazatlán FC"),
("AP25J7-02","2025-08-29","Atlético San Luis","Deportivo Toluca"),
("AP25J7-03","2025-08-29","Puebla FC","CF Monterrey"),
("AP25J7-04","2025-08-30","Club León","Gallos Blancos"),
("AP25J7-05","2025-08-30","Deportivo Guadalajara","Cruz Azul"),
("AP25J7-06","2025-08-30","Santos Laguna","UANL Tigres"),
("AP25J7-07","2025-08-30","CF América","CF Pachuca"),
("AP25J7-08","2025-08-31","Pumas UNAM","Atlas Guadalajara"),
("AP25J7-09","2025-08-31","Club Tijuana","Club Necaxa")]

def main():
    hist=[m for m in base.load_all() if m.date<datetime(2025,7,11)]
    if len(hist)!=1016: raise SystemExit(f"chronology drift pre-J1: {len(hist)}")
    tr=sorted(hist+prev.J1_FROZEN+prev.J2_FROZEN+prev.J3_FROZEN+prev.J4_FROZEN+prev.J5_FROZEN+J6_FROZEN,
              key=lambda m:(m.date,m.home,m.away,m.hg,m.ag))
    if len(tr)!=1069: raise SystemExit(f"J7 training count drift: expected 1069, got {len(tr)}")
    if any(m.date>=MODEL_CUTOFF for m in tr): raise SystemExit("J7 leakage detected")
    mods=base.ensemble(tr,MODEL_CUTOFF); rows=[]
    for fid,date,home,away in FIXTURES:
        M,meta=base.avg_matrix(mods,home,away); pp=prev.market_probs(M)
        rows.append({"fixture_id":fid,"date":date,"home":home,"away":away,
                     "markets":{k:{"p_raw":float(v),"p_cal_shadow":float(prev.cal(v))} for k,v in pp.items()},
                     "model_meta":meta})
    out={"experiment":"EXP-003","tournament":"Apertura 2025","jornada":"J7","model":"V0.1R_DC_ENSEMBLE",
         "calibration_shadow":"CAL_SHRINK_GLOBAL_V0_1","model_cutoff":"2025-08-29T00:00:00-06:00",
         "training_count":len(tr),"training_includes":"Apertura 2025 J1-J6 completed fixtures",
         "integrity_class":"MODEL_SIGNAL_FROZEN_WITH_NO_J7_OUTCOME_INPUTS_RESEARCHER_OUTCOME_EXPOSED",
         "promotion_eligibility":False,"fixtures":rows,
         "notes":["No J7 result is an input.","Raw V0.1R remains canonical for V2.1 selection.",
                  "J7 is permanently NO-PROMOTION because a J7 result snippet was seen during fixture-source lookup before selection freeze."]}
    print("AP25_J7_MODEL_ONLY",json.dumps(out,ensure_ascii=False,sort_keys=True),flush=True)
if __name__=="__main__": main()
