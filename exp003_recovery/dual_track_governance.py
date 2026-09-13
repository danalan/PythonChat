#!/usr/bin/env python3
"""Executable governance for the 1000 a 100000 Dual-Track Laboratory.

This module does NOT fit/predict football. It governs architecture promotion,
forward sample requirements, risk circuit-breaking and concept-drift state.
All constants are explicit and versioned so they cannot move after outcomes.
"""
from __future__ import annotations
from dataclasses import dataclass, asdict
from enum import Enum
from typing import Iterable
import math

GOVERNANCE_VERSION="DTL-1.1"

# Fiscal ranges were 100-150 and 300-500. We pre-register the mid/conservative
# points below pending a power calculation from observed Track-H score variance.
MIN_FORWARD_SETTLED={"CALIBRATION":125,"ARCHITECTURE":400}
MIN_CLV_SNAPSHOTS=75
MIN_CALIBRATION_BUCKET_N=20
MAX_ABS_CALIBRATION_RESIDUAL=0.05
MAX_SHADOW_DRAWDOWN_FRACTION=0.20
MIN_UNTOUCHED_H_WINDOWS=2

# Drift policy: monitored on rolling log loss by market family.
DRIFT_WINDOW=125
PAGE_HINKLEY_DELTA=0.005
PAGE_HINKLEY_REVIEW_THRESHOLD=4.0
PAGE_HINKLEY_HALT_THRESHOLD=8.0

class DriftTier(str,Enum):
    NORMAL="NORMAL"
    WATCH="WATCH"
    REVIEW="REVIEW"
    HALT="HALT"

@dataclass(frozen=True)
class PromotionEvidence:
    change_type: str  # CALIBRATION or ARCHITECTURE
    rationale_preregistered: bool
    untouched_h_windows_passed: int
    forward_settled_same_market_family: int
    clv_snapshots: int
    clv_lower_confidence_bound: float
    calibration_bucket_ns: tuple[int,...]
    calibration_residuals: tuple[float,...]
    drawdown_fraction: float
    version_diff_documented: bool
    data_snapshot_hash_documented: bool
    canary_plan_documented: bool
    open_leakage_findings: int
    power_calc_completed: bool

@dataclass(frozen=True)
class PromotionDecision:
    governance_version: str
    eligible: bool
    failed_requirements: tuple[str,...]
    evidence: dict

def evaluate_promotion(e: PromotionEvidence) -> PromotionDecision:
    kind=e.change_type.upper()
    if kind not in MIN_FORWARD_SETTLED:
        raise ValueError("change_type must be CALIBRATION or ARCHITECTURE")
    failures=[]
    required_n=MIN_FORWARD_SETTLED[kind]
    if not e.rationale_preregistered:
        failures.append("rationale_not_preregistered")
    if e.untouched_h_windows_passed<MIN_UNTOUCHED_H_WINDOWS:
        failures.append("fewer_than_two_untouched_track_h_windows")
    if e.forward_settled_same_market_family<required_n:
        failures.append(f"forward_sample_below_{required_n}")
    if e.clv_snapshots<MIN_CLV_SNAPSHOTS:
        failures.append(f"clv_snapshots_below_{MIN_CLV_SNAPSHOTS}")
    if not math.isfinite(e.clv_lower_confidence_bound) or e.clv_lower_confidence_bound<=0:
        failures.append("clv_lower_bound_not_positive")
    if not e.calibration_bucket_ns or not e.calibration_residuals or len(e.calibration_bucket_ns)!=len(e.calibration_residuals):
        failures.append("calibration_evidence_missing")
    else:
        if any(n<MIN_CALIBRATION_BUCKET_N for n in e.calibration_bucket_ns):
            failures.append("calibration_bucket_under_supported")
        if any(abs(r)>MAX_ABS_CALIBRATION_RESIDUAL for r in e.calibration_residuals):
            failures.append("calibration_residual_outside_tolerance")
    if e.drawdown_fraction>MAX_SHADOW_DRAWDOWN_FRACTION:
        failures.append("shadow_drawdown_limit_breached")
    if not e.version_diff_documented:
        failures.append("version_diff_missing")
    if not e.data_snapshot_hash_documented:
        failures.append("snapshot_hash_missing")
    if not e.canary_plan_documented:
        failures.append("canary_plan_missing")
    if e.open_leakage_findings>0:
        failures.append("open_leakage_findings")
    # The Fiscal explicitly requested a power calculation rather than treating
    # sample ranges as eternal constants. Until completed, promotion is blocked.
    if not e.power_calc_completed:
        failures.append("power_calc_not_completed")
    return PromotionDecision(GOVERNANCE_VERSION,not failures,tuple(failures),asdict(e))

@dataclass(frozen=True)
class DriftResult:
    tier: DriftTier
    statistic: float
    n: int
    action: str

def page_hinkley_logloss(log_losses: Iterable[float]) -> DriftResult:
    """One-sided Page-Hinkley monitor for deterioration in log loss.

    Uses only the most recent DRIFT_WINDOW settled observations supplied by the
    caller for ONE market family. It never changes model parameters directly.
    """
    xs=[float(x) for x in log_losses if math.isfinite(float(x))][-DRIFT_WINDOW:]
    if len(xs)<MIN_CALIBRATION_BUCKET_N:
        return DriftResult(DriftTier.NORMAL,0.0,len(xs),"insufficient_support_keep_logging")
    mean=0.0
    cumulative=0.0
    minimum=0.0
    maximum_stat=0.0
    for i,x in enumerate(xs,1):
        mean += (x-mean)/i
        cumulative += x-mean-PAGE_HINKLEY_DELTA
        minimum=min(minimum,cumulative)
        maximum_stat=max(maximum_stat,cumulative-minimum)
    if maximum_stat>=PAGE_HINKLEY_HALT_THRESHOLD:
        return DriftResult(DriftTier.HALT,maximum_stat,len(xs),"suspend_real_staking_for_market_family_keep_shadow_logging")
    if maximum_stat>=PAGE_HINKLEY_REVIEW_THRESHOLD:
        return DriftResult(DriftTier.REVIEW,maximum_stat,len(xs),"open_architecture_proposal_full_promotion_gate_required")
    if maximum_stat>=PAGE_HINKLEY_REVIEW_THRESHOLD/2:
        return DriftResult(DriftTier.WATCH,maximum_stat,len(xs),"log_watch_no_parameter_change")
    return DriftResult(DriftTier.NORMAL,maximum_stat,len(xs),"no_action")

if __name__=="__main__":
    print({
      "governance_version":GOVERNANCE_VERSION,
      "min_forward_settled":MIN_FORWARD_SETTLED,
      "min_clv_snapshots":MIN_CLV_SNAPSHOTS,
      "max_abs_calibration_residual":MAX_ABS_CALIBRATION_RESIDUAL,
      "max_shadow_drawdown_fraction":MAX_SHADOW_DRAWDOWN_FRACTION,
      "drift_window":DRIFT_WINDOW,
      "page_hinkley_review":PAGE_HINKLEY_REVIEW_THRESHOLD,
      "page_hinkley_halt":PAGE_HINKLEY_HALT_THRESHOLD,
    })
