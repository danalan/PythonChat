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
    forbidden=("datetime.now(","datetime.utcnow(","date.today(","time.time(","Timestamp.now(")
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
    a=synthetic_fit_fingerprint(); b=synthetic_fit_fingerprint()
    assert a==b, "fixed-cutoff fit is not bit-identical across repeated runs"


def assert_runtime_cutoff_guard():
    cutoff=datetime(2026,9,13,16,10)
    safe=[base.Match(datetime(2026,9,12,20,0),"A","B",1,0,"synthetic")]
    fwd.assert_rows_before_cutoff(safe,cutoff)
    bad=safe+[base.Match(datetime(2026,9,13,16,10),"B","A",0,0,"synthetic")]
    try:
        fwd.assert_rows_before_cutoff(bad,cutoff)
    except AssertionError:
        pass
    else:
        raise AssertionError("runtime cutoff guard accepted row at/after cutoff")


def assert_source_precedence_timezone_and_snapshot_hash():
    t=datetime(2026,1,1,23,30)
    rows=[
      base.Match(t,"A","B",1,0,"OpenFootball:test"),
      base.Match(t,"A","B",2,0,"FotMob:test"),
    ]
    out=fwd.dedupe_rows(rows)
    assert len(out)==1 and out[0].source.startswith("FotMob") and out[0].hg==2
    assert fwd.fixture_key(out[0])[0]=="2026-01-01"
    h1=fwd.training_snapshot_hash(out); h2=fwd.training_snapshot_hash(list(reversed(out)))
    assert h1==h2 and len(h1)==64


def assert_explicit_cutoff_required():
    try:
        fwd.parse_cutoff("")
    except ValueError:
        pass
    else:
        raise AssertionError("empty cutoff was accepted")


def assert_size_aware_calibration_gate():
    # n=20 with observed 10/20 should accept a predicted bucket mean of .50;
    # the old flat +/- .05 rule would have been an inappropriate noise test.
    assert gov.calibration_bucket_passes(0.50,10,20)
    assert not gov.calibration_bucket_passes(0.90,10,20)
    lo,hi=gov.wilson_interval(10,20)
    assert lo<0.50<hi and (hi-lo)>0.05


def assert_promotion_gate_defaults_to_blocked():
    rh="a"*64
    e=gov.PromotionEvidence(
      change_type="ARCHITECTURE",rationale_preregistered=True,rationale_hash=rh,
      rationale_timestamp_precedes_validation=True,untouched_h_windows_passed=2,
      forward_distinct_matches_same_market_family=399,
      clv_distinct_matches=74,clv_lower_confidence_bound=0.01,
      calibration_bucket_ns=(25,25,25,25),
      calibration_bucket_predicted_means=(0.20,0.40,0.60,0.80),
      calibration_bucket_successes=(5,10,15,20),
      drawdown_fraction=0.10,shadow_staking_rule=gov.SHADOW_STAKING_RULE,
      drawdown_limit_backtested=False,version_diff_documented=True,
      data_snapshot_hash_documented=True,canary_plan_documented=True,
      open_leakage_findings=0,power_calc_completed=False,
      evidence_scope_excludes_real_user_override=True)
    d=gov.evaluate_promotion(e)
    assert not d.eligible
    assert "forward_distinct_match_sample_below_400" in d.failed_requirements
    assert "power_calc_not_completed" in d.failed_requirements
    assert "shadow_drawdown_limit_not_empirically_calibrated" in d.failed_requirements


def assert_user_override_excluded():
    assert not gov.promotion_record_eligible("REAL_USER_OVERRIDE")
    assert gov.promotion_record_eligible("SHADOW_MODEL")


def assert_drift_logging_only_until_calibrated():
    r=gov.monitor_drift([0.5]*125,[0.20]*125)
    assert r.tier in set(gov.DriftTier)
    assert r.thresholds_calibrated is False
    assert "logging_only" in r.action


def assert_computable_market_not_real_eligible_in_shadow():
    s=gov.market_signal_status("TEAM_TOTALS","SHADOW")
    assert s["signal_computable"] and not s["real_stake_eligible"]


def main():
    assert_no_wall_clock_dependency()
    assert_cutoff_run_date_invariance()
    assert_runtime_cutoff_guard()
    assert_source_precedence_timezone_and_snapshot_hash()
    assert_explicit_cutoff_required()
    assert_size_aware_calibration_gate()
    assert_promotion_gate_defaults_to_blocked()
    assert_user_override_excluded()
    assert_drift_logging_only_until_calibrated()
    assert_computable_market_not_real_eligible_in_shadow()
    print("DUAL_TRACK_INTEGRITY_TESTS_PASS_DTL_1_2")

if __name__=="__main__": main()
