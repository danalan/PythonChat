#!/usr/bin/env python3
"""Apertura 2025 J13 model-only replay under frozen V0.1R + calibration shadow.

J13 model freezes before external J13 research. Training contains completed Liga MX through J12 only.
No J13 outcome is used here.
"""
from __future__ import annotations
import json
from datetime import datetime
import ap25_j12_model_only_replay as j12
import ap25_j6_model_only_replay as j6

base=j12.base
MODEL_CUTOFF=datetime(2025,10,17,0,0,0)

J12_FROZEN=[
base.Match(datetime(2025,10,3),"Club Necaxa","CF Pachuca",0,1,"AP25_J12_FROZEN"),
base.Match(datetime(2025,10,3),"Mazatlán FC","Atlético San Luis",2,1,"AP25_J12_FROZEN"),
base.Match(datetime(2025,10,3),"Atlas Guadalajara","FC Juárez",3,1,"AP25_J12_FROZEN"),
base.Match(datetime(2025,10,4),"Gallos Blancos","Puebla FC",3,1,"AP25_J12_FROZEN"),
base.Match(datetime(2025,10,4),"Club León","Deportivo Toluca",2,4,"AP25_J12_FROZEN"),
base.Match(datetime(2025,10,4),"UANL Tigres","Cruz Azul",1,1,"AP25_J12_FROZEN"),
base.Match(datetime(2025,10,4),"CF América","Santos Laguna",3,0,"AP25_J12_FROZEN"),
base.Match(datetime(2025,10,5),"Pumas UNAM","Deportivo Guadalajara",1,2,"AP25_J12_FROZEN"),
base.Match(datetime(2025,10,5),"Club Tijuana","CF Monterrey",2,2,"AP25_J12_FROZEN")]

FIXTURES=[
("AP25J13-01","2025-10-17","Puebla FC","Club Tijuana"),
("AP25J13-02","2025-10-17","Atlético San Luis","Atlas Guadalajara"),
("AP25J13-03","2025-10-17","UANL Tigres","Club Necaxa"),
("AP25J13-04","2025-10-18","Santos Laguna","Club León"),
("AP25J13-05","2025-10-18","FC Juárez","CF Pachuca"),
("AP25J13-06","2025-10-18","Deportivo Guadalajara","Mazatlán FC"),
("AP25J13-07","2025-10-18","CF Monterrey","Pumas UNAM"),
("AP25J13-08","2025-10-18","Cruz Azul","CF América"),
("AP25J13-09","2025-10-18","Deportivo Toluca","Gallos Blancos")]

def main():
    hist=[m for m in base.load_all() if m.date<datetime(2025,7,11)]
    if len(hist)!=1016: raise SystemExit(f"chronology drift pre-J1: {len(hist)}")
    j11=j12.prev
    j10=j11.prev
    tr=sorted(
        hist+j6.J1_FROZEN+j6.J2_FROZEN+j6.J3_FROZEN+j6.J4_FROZEN+j6.J5_FROZEN+
        j10.prev.prev.prev.J6_FROZEN+j10.prev.prev.J7_FROZEN+j10.prev.J8_FROZEN+
        j10.prev.J1_BACKFILL+j10.J9_FROZEN+j11.J10_FROZEN+j12.J11_FROZEN+J12_FROZEN,
        key=lambda m:(m.date,m.home,m.away,m.hg,m.ag))
    if len(tr)!=1124: raise SystemExit(f"J13 training count drift: expected 1124, got {len(tr)}")
    if any(m.date>=MODEL_CUTOFF for m in tr): raise SystemExit("J13 leakage detected")
    mods=base.ensemble(tr,MODEL_CUTOFF); rows=[]
    for fid,date,home,away in FIXTURES:
        M,meta=base.avg_matrix(mods,home,away); pp=j6.market_probs(M)
        rows.append({"fixture_id":fid,"date":date,"home":home,"away":away,
                     "markets":{k:{"p_raw":float(v),"p_cal_shadow":float(j6.cal(v))} for k,v in pp.items()},
                     "model_meta":meta})
    out={"experiment":"EXP-003","tournament":"Apertura 2025","jornada":"J13","model":"V0.1R_DC_ENSEMBLE",
         "calibration_shadow":"CAL_SHRINK_GLOBAL_V0_1","model_cutoff":"2025-10-17T00:00:00-06:00",
         "training_count":len(tr),"training_includes":"Apertura 2025 completed fixtures through J12 plus Sep.17 J1 backfill",
         "integrity_class":"MODEL_SIGNAL_FROZEN_BEFORE_EXTERNAL_J13_RESEARCH_NO_J13_OUTCOME_INPUTS",
         "promotion_eligibility":True,"fixtures":rows,
         "notes":["No J13 result is an input.","Raw V0.1R remains canonical for V2.1 selection.",
                  "Internal canonical ledger is authoritative for endogenous football data.",
                  "Fixture-date metadata incorporates the contemporary J13 schedule revision that moved Toluca-Queretaro to Oct.18; this does not alter training inputs or cutoff.",
                  "Promotion eligibility remains provisional until external research and selection freeze complete without visible J13 outcome exposure."]}
    print("AP25_J13_MODEL_ONLY",flush=True)
    print(json.dumps(out,ensure_ascii=False,sort_keys=True,indent=2),flush=True)
if __name__=='__main__':main()
