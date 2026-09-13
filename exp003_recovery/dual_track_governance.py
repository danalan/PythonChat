#!/usr/bin/env python3
"""Executable governance for the 1000 a 100000 Dual-Track Laboratory.

This module does NOT fit/predict football. It governs architecture promotion,
forward evidence, calibration, risk circuit-breaking and concept-drift state.
All constants are explicit and versioned so they cannot move after outcomes.
"""
from __future__ import annotations
from dataclasses import dataclass, asdict
from enum import Enum
from typing import Iterable
import hashlib, json, math

GOVERNANCE_VERSION="DTL-1.2"

# Provisional floors only. A completed power calculation remains mandatory.
MIN_FORWARD_DISTINCT_MATCHES={"CALIBRATION":125,"ARCHITECTURE":400}
MIN_CLV_DISTINCT_MATCHES=75
MIN_CALIBRATION_BUCKET_N=20
WILSON_Z=1.959963984540054
MIN_UNTOUCHED_H_WINDOWS=2

# Shadow risk definition. Flat-unit is frozen until a future architecture gate.
SHADOW_STAKING_RULE="FLAT_1_UNIT_PER_TICKET"
MAX_SHADOW_DRAWDOWN_FRACTION=0.20

# Drift settings are provisional and LOGGING-ONLY until historically calibrated.
DRIFT_WINDOW=125
PAGE_HINKLEY_DELTA=0.005
PAGE_HINKLEY_REVIEW_THRESHOLD=4.0
PAGE_HINKLEY_HALT_THRESHOLD=8.0
DRIFT_THRESHOLDS_HISTORICALLY_CALIBRATED=False

PROMOTION_EVIDENCE_STAKE_TYPES=frozenset({"SHADOW_MODEL","SIM_MODEL"})
NON_PROMOTION_STAKE_TYPES=frozenset({"REAL_USER_OVERRIDE"})

SCORE_MATRIX_SIGNAL_FAMILIES=frozenset({
    "1X2","DOUBLE_CHANCE","BTTS","TOTALS","TEAM_TOTALS",
    "CLEAN_SHEET","WIN_TO_NIL","MARGINS","EXACT_SCORE"
})

class DriftTier(str,Enum):
    NORMAL="NORMAL"
    WATCH="WATCH"
    REVIEW="REVIEW"
    HALT="HALT"

@dataclass(frozen=True)
class PromotionEvidence:
    change_type: str  # CALIBRATION or ARCHITECTURE
    rationale_preregistered: bool
    rationale_hash: str
    rationale_timestamp_precedes_validation: bool
    untouched_h_windows_passed: int
    forward_distinct_matches_same_market_family: int
    clv_distinct_matches: int
    clv_lower_confidence_bound: float
    calibration_bucket_ns: tuple[int,...]
    calibration_bucket_predicted_means: tuple[float,...]
    calibration_bucket_successes: tuple[int,...]
    drawdown_fraction: float
    shadow_staking_rule: str
    drawdown_limit_backtested: bool
    version_diff_documented: bool
    data_snapshot_hash_documented: bool
    canary_plan_documented: bool
    open_leakage_findings: int
    power_calc_completed: bool
    evidence_scope_excludes_real_user_override: bool

@dataclass(frozen=True)
class PromotionDecision:
    governance_version: str
    eligible: bool
    failed_requirements: tuple[str,...]
    evidence: dict

def rationale_fingerprint(parent_version: str, timestamp_iso: str, rationale_text: str) -> str:
    """Stable hash for append-only architecture proposal files.

    Storage convention: governance/proposals/<timestamp>_<first12sha>.json
    Files are created once, never updated in place.
    """
    payload={"parent_version":parent_version,"timestamp":timestamp_iso,"rationale":rationale_text}
    raw=json.dumps(payload,ensure_ascii=False,sort_keys=True,separators=(",",":")).encode("utf-8")
    return hashlib.sha256(raw).hexdigest()

def promotion_record_eligible(stake_type: str) -> bool:
    """REAL_USER_OVERRIDE is structurally excluded from promotion evidence."""
    return str(stake_type).upper() in PROMOTION_EVIDENCE_STAKE_TYPES

def wilson_interval(successes: int, n: int, z: float=WILSON_Z) -> tuple[float,float]:
    if n<=0 or successes<0 or successes>n:
        raise ValueError("invalid binomial bucket")
    p=successes/n
    den=1+(z*z)/n
    center=(p+(z*z)/(2*n))/den
    half=(z/den)*math.sqrt((p*(1-p)/n)+(z*z)/(4*n*n))
    return max(0.0,center-half),min(1.0,center+half)

def calibration_bucket_passes(predicted_mean: float, successes: int, n: int) -> bool:
    """Size-aware calibration gate: model bucket mean must lie in Wilson 95% CI."""
    if n<MIN_CALIBRATION_BUCKET_N or not (0.0<=predicted_mean<=1.0):
        return False
    lo,hi=wilson_interval(successes,n)
    return lo<=predicted_mean<=hi

def evaluate_promotion(e: PromotionEvidence) -> PromotionDecision:
    kind=e.change_type.upper()
    if kind not in MIN_FORWARD_DISTINCT_MATCHES:
        raise ValueError("change_type must be CALIBRATION or ARCHITECTURE")
    failures=[]
    required_n=MIN_FORWARD_DISTINCT_MATCHES[kind]
    if not e.rationale_preregistered:
        failures.append("rationale_not_preregistered")
    if len(e.rationale_hash)!=64 or any(c not in "0123456789abcdef" for c in e.rationale_hash.lower()):
        failures.append("rationale_hash_missing_or_malformed")
    if not e.rationale_timestamp_precedes_validation:
        failures.append("rationale_not_provably_pre_validation")
    if e.untouched_h_windows_passed<MIN_UNTOUCHED_H_WINDOWS:
        failures.append("fewer_than_two_untouched_track_h_windows")
    if e.forward_distinct_matches_same_market_family<required_n:
        failures.append(f"forward_distinct_match_sample_below_{required_n}")
    if e.clv_distinct_matches<MIN_CLV_DISTINCT_MATCHES:
        failures.append(f"clv_distinct_matches_below_{MIN_CLV_DISTINCT_MATCHES}")
    if not math.isfinite(e.clv_lower_confidence_bound) or e.clv_lower_confidence_bound<=0:
        failures.append("clv_lower_bound_not_positive")
    calib=(e.calibration_bucket_ns,e.calibration_bucket_predicted_means,e.calibration_bucket_successes)
    if not all(calib) or not (len(calib[0])==len(calib[1])==len(calib[2])):
        failures.append("calibration_evidence_missing")
    else:
        for n,p,s in zip(*calib):
            if n<MIN_CALIBRATION_BUCKET_N:
                failures.append("calibration_bucket_under_supported")
                break
            if not calibration_bucket_passes(float(p),int(s),int(n)):
                failures.append("calibration_wilson_inconsistency")
                break
    if e.shadow_staking_rule!=SHADOW_STAKING_RULE:
        failures.append("shadow_staking_rule_mismatch")
    if not e.drawdown_limit_backtested:
        failures.append("shadow_drawdown_limit_not_empirically_calibrated")
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
    if not e.power_calc_completed:
        failures.append("power_calc_not_completed")
    if not e.evidence_scope_excludes_real_user_override:
        failures.append("real_user_override_not_hard_excluded")
    return PromotionDecision(GOVERNANCE_VERSION,not failures,tuple(dict.fromkeys(failures)),asdict(e))

@dataclass(frozen=True)
class DriftResult:
    tier: DriftTier
    logloss_statistic: float
    brier_statistic: float
    n: int
    thresholds_calibrated: bool
    action: str

def _winsorize_upper(xs: list[float], q: float=0.95) -> list[float]:
    if not xs:
        return []
    ys=sorted(xs)
    idx=min(len(ys)-1,max(0,int(math.ceil(q*len(ys)))-1))
    cap=ys[idx]
    return [min(x,cap) for x in xs]

def _page_hinkley_stat(xs: list[float], delta: float) -> float:
    mean=0.0; cumulative=0.0; minimum=0.0; maximum_stat=0.0
    for i,x in enumerate(xs,1):
        mean += (x-mean)/i
        cumulative += x-mean-delta
        minimum=min(minimum,cumulative)
        maximum_stat=max(maximum_stat,cumulative-minimum)
    return maximum_stat

def monitor_drift(log_losses: Iterable[float], brier_scores: Iterable[float], thresholds_calibrated: bool=DRIFT_THRESHOLDS_HISTORICALLY_CALIBRATED) -> DriftResult:
    """Logging-only drift monitor until thresholds are calibrated on Track H.

    Log loss is upper-winsorized inside the rolling window and Brier is monitored
    in parallel as a bounded cross-check. No statistic mutates model parameters.
    """
    ll=[float(x) for x in log_losses if math.isfinite(float(x))][-DRIFT_WINDOW:]
    br=[float(x) for x in brier_scores if math.isfinite(float(x))][-DRIFT_WINDOW:]
    n=min(len(ll),len(br))
    if n<MIN_CALIBRATION_BUCKET_N:
        return DriftResult(DriftTier.NORMAL,0.0,0.0,n,thresholds_calibrated,"insufficient_support_keep_logging")
    ll=_winsorize_upper(ll[-n:]); br=br[-n:]
    ll_stat=_page_hinkley_stat(ll,PAGE_HINKLEY_DELTA)
    br_stat=_page_hinkley_stat(br,PAGE_HINKLEY_DELTA)
    stat=max(ll_stat,br_stat)
    if stat>=PAGE_HINKLEY_HALT_THRESHOLD:
        tier=DriftTier.HALT
    elif stat>=PAGE_HINKLEY_REVIEW_THRESHOLD:
        tier=DriftTier.REVIEW
    elif stat>=PAGE_HINKLEY_REVIEW_THRESHOLD/2:
        tier=DriftTier.WATCH
    else:
        tier=DriftTier.NORMAL
    if not thresholds_calibrated:
        action=f"logging_only_provisional_{tier.value.lower()}_no_staking_or_parameter_action"
    elif tier==DriftTier.HALT:
        action="suspend_real_staking_for_market_family_keep_shadow_logging"
    elif tier==DriftTier.REVIEW:
        action="open_architecture_proposal_full_promotion_gate_required"
    elif tier==DriftTier.WATCH:
        action="log_watch_no_parameter_change"
    else:
        action="no_action"
    return DriftResult(tier,ll_stat,br_stat,n,thresholds_calibrated,action)

def market_signal_status(family: str, model_status: str="SHADOW") -> dict:
    """Computable signal != eligible real-money market."""
    fam=str(family).upper()
    computable=fam in SCORE_MATRIX_SIGNAL_FAMILIES
    return {
        "family":fam,
        "signal_computable":computable,
        "real_stake_eligible":bool(computable and str(model_status).upper()=="PRODUCTION-ELIGIBLE")
    }

if __name__=="__main__":
    print({
      "governance_version":GOVERNANCE_VERSION,
      "min_forward_distinct_matches":MIN_FORWARD_DISTINCT_MATCHES,
      "min_clv_distinct_matches":MIN_CLV_DISTINCT_MATCHES,
      "calibration_gate":"Wilson 95% interval; no flat residual tolerance",
      "min_calibration_bucket_n":MIN_CALIBRATION_BUCKET_N,
      "shadow_staking_rule":SHADOW_STAKING_RULE,
      "max_shadow_drawdown_fraction":MAX_SHADOW_DRAWDOWN_FRACTION,
      "drift_window":DRIFT_WINDOW,
      "drift_thresholds_historically_calibrated":DRIFT_THRESHOLDS_HISTORICALLY_CALIBRATED,
      "real_user_override_counts_for_promotion":promotion_record_eligible("REAL_USER_OVERRIDE"),
    })
