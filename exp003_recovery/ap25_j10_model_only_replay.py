#!/usr/bin/env python3
"""Apertura 2025 J10 model-only replay under frozen V0.1R + calibration shadow.

The external J10 context packet was supplied through a Perplexity firewall. The packet itself
contained result-revealing post-J10 source titles, so J10 is permanently NO-PROMOTION.
No J10 outcome is used in this model. Training includes completed Liga MX through J9.
"""
from __future__ import annotations
import json
from datetime import datetime
import ap25_j9_model_only_replay as prev
base=prev.base
MODEL_CUTOFF=datetime(2025,9,23,0,0,0)

J9_FROZEN=[
base.Match(datetime(2025,9,19),"Club Necaxa","Puebla FC",1,0,"AP25_J9_FROZEN"),
base.Match(datetime(2025,9,19),"Cruz Azul","FC Juárez",3,2,"AP25_J9_FROZEN"),
base.Match(datetime(2025,9,19),"Club Tijuana","Club León",5,0,"AP25_J9_FROZEN"),
base.Match(datetime(2025,9,19),"Mazatlán FC","Atlas Guadalajara",1,1,"AP25_J9_FROZEN"),
base.Match(datetime(2025,9,20),"CF Pachuca","Gallos Blancos",0,2,"AP25_J9_FROZEN"),
base.Match(datetime(2025,9,20),"Deportivo Guadalajara","Deportivo Toluca",0,3,"AP25_J9_FROZEN"),
base.Match(datetime(2025,9,20),"Pumas UNAM","UANL Tigres",1,1,"AP25_J9_FROZEN"),
base.Match(datetime(2025,9,20),"CF Monterrey","CF América",2,2,"AP25_J9_FROZEN"),
base.Match(datetime(2025,9,21),"Santos Laguna","Atlético San Luis",1,4,"AP25_J9_FROZEN")]

FIXTURES=[
("AP25J10-01","2025-09-23","Deportivo Guadalajara","Club Necaxa"),
("AP25J10-02","2025-09-23","Puebla FC","CF Pachuca"),
("AP25J10-03","2025-09-23","Club León","Mazatlán FC"),
("AP25J10-04","2025-09-23","FC Juárez","Pumas UNAM"),
("AP25J10-05","2025-09-24","Cruz Azul","Gallos Blancos"),
("AP25J10-06","2025-09-24","UANL Tigres","Atlas Guadalajara"),
("AP25J10-07","2025-09-24","Deportivo Toluca","CF Monterrey"),
("AP25J10-08","2025-09-24","Atlético San Luis","CF América"),
("AP25J10-09","2025-09-24","Santos Laguna","Club Tijuana")]

def main():
    hist=[m for m in base.load_all() if m.date<datetime(2025,7,11)]
    if len(hist)!=1016: raise SystemExit(f"chronology drift pre-J1: {len(hist)}")
    tr=sorted(hist+prev.prev.prev.prev.J1_FROZEN+prev.prev.prev.prev.J2_FROZEN+prev.prev.prev.prev.J3_FROZEN+prev.prev.prev.prev.J4_FROZEN+prev.prev.prev.prev.J5_FROZEN+prev.prev.prev.J6_FROZEN+prev.prev.J7_FROZEN+prev.J8_FROZEN+prev.J1_BACKFILL+J9_FROZEN,
              key=lambda m:(m.date,m.home,m.away,m.hg,m.ag))
    if len(tr)!=1097: raise SystemExit(f"J10 training count drift: expected 1097, got {len(tr)}")
    if any(m.date>=MODEL_CUTOFF for m in tr): raise SystemExit("J10 leakage detected")
    mods=base.ensemble(tr,MODEL_CUTOFF); rows=[]
    for fid,date,home,away in FIXTURES:
        M,meta=base.avg_matrix(mods,home,away); pp=prev.prev.prev.prev.market_probs(M)
        rows.append({"fixture_id":fid,"date":date,"home":home,"away":away,
                     "markets":{k:{"p_raw":float(v),"p_cal_shadow":float(prev.prev.prev.prev.cal(v))} for k,v in pp.items()},
                     "model_meta":meta})
    out={"experiment":"EXP-003","tournament":"Apertura 2025","jornada":"J10","model":"V0.1R_DC_ENSEMBLE",
         "calibration_shadow":"CAL_SHRINK_GLOBAL_V0_1","model_cutoff":"2025-09-23T00:00:00-06:00",
         "training_count":len(tr),"training_includes":"Apertura 2025 J1-J9 plus completed Sep.17 J1 backfill",
         "integrity_class":"MODEL_SIGNAL_FROZEN_WITH_NO_J10_OUTCOME_INPUTS_EXTERNAL_PACKET_OUTCOME_EXPOSURE",
         "promotion_eligibility":False,"fixtures":rows,
         "notes":["No J10 result is an input.","Raw V0.1R remains canonical for V2.1 selection.",
                  "J10 is permanently NO-PROMOTION because the supplied external packet exposed post-J10 result information before selection freeze."]}
    print("AP25_J10_MODEL_ONLY",json.dumps(out,ensure_ascii=False,sort_keys=True),flush=True)
if __name__=="__main__":main()
