#!/usr/bin/env python3
from datetime import datetime,timedelta
import numpy as np
import corner_shadow_v0_1 as c


def synthetic_rows():
    start=datetime(2025,1,1)
    out=[]
    vals=[(5,3),(7,4),(4,5),(6,2),(8,3),(3,6),(5,5),(9,2),(4,4),(6,5),(7,3),(5,4)]
    for i,(hc,ac) in enumerate(vals):
        home,away=("A","B") if i%2==0 else ("B","A")
        out.append(c.CornerMatch(start+timedelta(days=7*i),home,away,hc,ac,"synthetic"))
    return out


def test_fit_and_markets():
    rows=synthetic_rows(); cutoff=datetime(2025,5,1)
    models=c.ensemble(rows,cutoff)
    M,meta=c.avg_matrix(models,"A","B")
    assert M.shape==(26,26)
    assert abs(float(M.sum())-1.0)<1e-10
    assert len(meta)==4
    p=c.market_probs(M)
    assert 0<=p["TOTAL_CORNERS_O9.5"]<=1
    assert abs(p["TOTAL_CORNERS_O9.5"]+p["TOTAL_CORNERS_U9.5"]-1)<1e-10
    assert abs(p["CORNERS_HOME_MORE"]+p["CORNERS_TIE"]+p["CORNERS_AWAY_MORE"]-1)<1e-10


def test_cutoff():
    rows=synthetic_rows()+[c.CornerMatch(datetime(2030,1,1),"A","B",20,20,"future")]
    m=c.fit_corner_model(rows,datetime(2025,5,1),365)
    assert m.cutoff==datetime(2025,5,1)


def test_parser():
    payload={"content":{"stats":{"Periods":{"All":{"stats":[
      {"title":"Possession","stats":[55,45]},
      {"title":"Corners","stats":[7,4]}
    ]}}}}}
    assert c.extract_corner_pair(payload)==(7,4)


def main():
    test_fit_and_markets(); test_cutoff(); test_parser()
    print("C0_1_CORNER_SHADOW_TESTS_PASS")

if __name__=="__main__": main()
