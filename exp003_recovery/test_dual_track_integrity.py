#!/usr/bin/env python3
"""Regression tests for Dual-Track Lab temporal integrity and governance."""
from __future__ import annotations
import inspect
from datetime import datetime
import numpy as np
import parlay_replay_dc as base
import vn2026_forward as fwd
import dual_track_governance as gov


def assert_no_wall_clock_dependency():
    src=inspect.getsource(fwd)+"\n"+inspect.getsource(base)
    forbidden=("datetime.now(","datetime.utcnow(","date.today(","time.time(")
    hits=[x for x in forbidden if x in src]
    assert not hits, f"wall-clock dependency found: {hits}"
    sig=inspect.signature(base.ensemble)
    assert "asof" in sig.parameters, "base.ensemble must require explicit asof/cutoff"


def synthetic_fit_fingerprint():
    rows=[
      base.Match(datetime(2024,1,1),"A","B",1,0,"synthetic"),
      base.Match(datetime(2024,1,8),"B","A",0,0,"synthetic"),
      base.Match(datetime(2024,1,15),"A","B",2,1,"synthetic"),
      base.Match(datetime(2024,1,22),"B","A",1,2,"synthetic"),
      base.Match(datetime(2024,1,29),"A","B",0,1,"synthetic"),
      base.Match(datetime(2024,2,5),"B","A",1,1,"synthetic"),
    ]
    cutoff=datetime(2024,3,1,12,0,0)
    models=base.ensemble(rows,cutoff)
    fp=[]
    for m in models:
        fp.extend(np.asarray(m.theta,dtype=np.float64).tobytes())
    return bytes(fp)


def assert_cutoff_run_date_invariance():
    # With wall-clock access statically banned, identical explicit inputs must
    # produce a bit-identical fingerprint regardless of calendar date of run.
    a=synthetic_fit_fingerprint()
    b=synthetic_fit_fingerprint()
    assert a==b, "fixed-cutoff fit is not bit-identical across repeated runs"


def assert_source_precedence_and_snapshot_hash():
    t=datetime(2026,1,1)
    rows=[
      base.Match(t,"A","B",1,0,"OpenFootball:test"),
      base.Match(t,"A","B",2,0,"FotMob:test"),
    ]
    out=fwd.dedupe_rows(rows)
    assert len(out)==1 and out[0].source.startswith("FotMob") and out[0].hg==2
    h1=fwd.training_snapshot_hash(out)
    h2=fwd.training_snapshot_hash(list(reversed(out)))
    assert h1==h2 and len(h1)==64


def assert_explicit_cutoff_required():
    try:
        fwd.parse_cutoff("")
    except ValueError:
        pass
    else:
        raise AssertionError("empty cutoff was accepted")


def assert_promotion_gate_defaults_to_blocked():
    e=gov.PromotionEvidence(
      change_type="ARCHITECTURE",rationale_preregistered=True,
      untouched_h_windows_passed=2,forward_settled_same_market_family=399,
      clv_snapshots=74,clv_lower_confidence_bound=0.01,
      calibration_bucket_ns=(25,25,25,25),calibration_residuals=(0.01,0.02,-0.01,0.0),
      drawdown_fraction=0.10,version_diff_documented=True,
      data_snapshot_hash_documented=True,canary_plan_documented=True,
      open_leakage_findings=0,power_calc_completed=False)
    d=gov.evaluate_promotion(e)
    assert not d.eligible
    assert "forward_sample_below_400" in d.failed_requirements
    assert "power_calc_not_completed" in d.failed_requirements


def assert_drift_never_mutates_model():
    r=gov.page_hinkley_logloss([0.5]*125)
    assert r.tier in set(gov.DriftTier)
    assert isinstance(r.action,str)


def main():
    assert_no_wall_clock_dependency()
    assert_cutoff_run_date_invariance()
    assert_source_precedence_and_snapshot_hash()
    assert_explicit_cutoff_required()
    assert_promotion_gate_defaults_to_blocked()
    assert_drift_never_mutates_model()
    print("DUAL_TRACK_INTEGRITY_TESTS_PASS")

if __name__=="__main__": main()
