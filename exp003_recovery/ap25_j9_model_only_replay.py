#!/usr/bin/env python3
"""Apertura 2025 J9 model-only replay under frozen V0.1R + calibration shadow."""
from __future__ import annotations
import json
from datetime import datetime
import ap25_j8_model_only_replay as prev
base=prev.base
MODEL_CUTOFF=datetime(2025,9,19,0,0,0)
J8_FROZEN=[
base.Match(datetime(2025,9,12),"Club Necaxa","FC Juárez",1,1,"AP25_J8_FROZEN"),
base.Match(datetime(2025,9,13),"CF América","Deportivo Guadalajara",1,2,"AP25_J8_FROZEN"),
base.Match(datetime(2025,9,12),"Mazatlán FC","Pumas UNAM",1,4,"AP25_J8_FROZEN"),
base.Match(datetime(2025,9,13),"CF Pachuca","Cruz Azul",0,1,"AP25_J8_FROZEN"),
base.Match(datetime(2025,9,13),"UANL Tigres","Club León",0,0,"AP25_J8_FROZEN"),
base.Match(datetime(2025,9,13),"Atlas Guadalajara","Santos Laguna",2,2,"AP25_J8_FROZEN"),
base.Match(datetime(2025,9,13),"Deportivo Toluca","Puebla FC",3,1,"AP25_J8_FROZEN"),
base.Match(datetime(2025,9,14),"Gallos Blancos","CF Monterrey",0,1,"AP25_J8_FROZEN"),
base.Match(datetime(2025,9,14),"Atlético San Luis","Club Tijuana",1,1,"AP25_J8_FROZEN")]
J1_BACKFILL=[base.Match(datetime(2025,9,17),"Deportivo Guadalajara","UANL Tigres",0,0,"AP25_J1_BACKFILL_PRE_J9")]
FIXTURES=[
("AP25J9-01","2025-09-19","Club Necaxa","Puebla FC"),
("AP25J9-02","2025-09-19","Cruz Azul","FC Juárez"),
("AP25J9-03","2025-09-19","Club Tijuana","Club León"),
("AP25J9-04","2025-09-19","Mazatlán FC","Atlas Guadalajara"),
("AP25J9-05","2025-09-20","CF Pachuca","Gallos Blancos"),
("AP25J9-06","2025-09-20","Deportivo Guadalajara","Deportivo Toluca"),
("AP25J9-07","2025-09-20","Pumas UNAM","UANL Tigres"),
("AP25J9-08","2025-09-20","CF Monterrey","CF América"),
("AP25J9-09","2025-09-21","Santos Laguna","Atlético San Luis")]
def main():
    hist=[m for m in base.load_all() if m.date<datetime(2025,7,11)]
    if len(hist)!=1016: raise SystemExit(f"chronology drift pre-J1: {len(hist)}")
    tr=sorted(hist+prev.prev.prev.J1_FROZEN+prev.prev.prev.J2_FROZEN+prev.prev.prev.J3_FROZEN+prev.prev.prev.J4_FROZEN+prev.prev.prev.J5_FROZEN+prev.prev.J6_FROZEN+prev.J7_FROZEN+J8_FROZEN+J1_BACKFILL,key=lambda m:(m.date,m.home,m.away,m.hg,m.ag))
    if len(tr)!=1088: raise SystemExit(f"J9 training count drift: expected 1088, got {len(tr)}")
    if any(m.date>=MODEL_CUTOFF for m in tr): raise SystemExit("J9 leakage detected")
    mods=base.ensemble(tr,MODEL_CUTOFF); rows=[]
    for fid,date,home,away in FIXTURES:
        M,meta=base.avg_matrix(mods,home,away); pp=prev.prev.prev.market_probs(M)
        rows.append({"fixture_id":fid,"date":date,"home":home,"away":away,"markets":{k:{"p_raw":float(v),"p_cal_shadow":float(prev.prev.prev.cal(v))} for k,v in pp.items()},"model_meta":meta})
    out={"experiment":"EXP-003","tournament":"Apertura 2025","jornada":"J9","model":"V0.1R_DC_ENSEMBLE","calibration_shadow":"CAL_SHRINK_GLOBAL_V0_1","model_cutoff":"2025-09-19T00:00:00-06:00","training_count":len(tr),"training_includes":"Apertura 2025 J1-J8 plus completed Sep.17 J1 backfill","integrity_class":"MODEL_SIGNAL_FROZEN_WITH_NO_J9_OUTCOME_INPUTS_RESEARCHER_J9_OUTCOME_EXPOSED","promotion_eligibility":False,"fixtures":rows,"notes":["No J9 result is an input.","Sep.17 Guadalajara-Tigres 0-0 is a legitimate pre-J9 input.","J9 remains permanently NO-PROMOTION due to researcher J9 outcome exposure during backfill verification."]}
    print("AP25_J9_MODEL_ONLY",json.dumps(out,ensure_ascii=False,sort_keys=True),flush=True)
if __name__=="__main__":main()
