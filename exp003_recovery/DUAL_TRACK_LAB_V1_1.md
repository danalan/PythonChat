# Dual-Track Laboratory V1.1 — Fiscal Patch

Status: SHADOW-ONLY pending re-audit and production gate.
Parent mathematical core: `V0.1R_RECOVERED`.
Forward candidate: `Vn-2026-DC-ENSEMBLE`.

## 1. Two clocks, one mathematical core

Track H (historical replay) and Track F (live forward) share model code but never share a wall clock, freeze table, or mutable state. Every fit receives an explicit `cutoff` argument. No fitting/eligibility function may consult `now()`, `today()`, or system time.

Track H may only admit matches whose kickoff is strictly before its historical cutoff. Track F may admit every actually completed Liga MX match strictly before the real forward cutoff even when Track H has not replayed that period yet.

## 2. Immutable freezes

Freeze identity is `(model_version, parent_version, cutoff, fixture, market, selection, line)`.

Freezes are create-only. No overwrite/update path is permitted. Corrections create a new record with a correction reference while preserving the original.

Every freeze must record model version, parent, explicit cutoff, training snapshot SHA-256, source precedence, fixture/kickoff, market/line, p_model, odds/timestamp when available, de-vig probability, edge/EV when available, context signal/veto, minimum acceptable odds, and separate SIM/REAL execution fields.

## 3. Source precedence and deduplication

Fixture identity for source deduplication: `(date, home, away)` after canonical team-name normalization.

Precedence is fixed and versioned:
- FotMob: 20
- OpenFootball: 10

When sources overlap, higher precedence wins. Conflicts are auditable through the normalized training snapshot hash.

## 4. State update vs architecture update

STATE UPDATE may run after each newly eligible completed match using the same frozen architecture. It may refit attack, defense, intercept, home advantage and rho against the eligible aggregate training set at the caller-supplied cutoff.

ARCHITECTURE UPDATE includes model family, half-lives, features, calibration, context weights, eligible markets, thresholds, priors, parlay construction, staking and risk rules. It requires a new version and the promotion gate below. A single win/loss can open a diagnostic hypothesis only.

## 5. Promotion gate Vn -> Vn+1

All requirements are mandatory:
1. Change rationale pre-registered before validation results are inspected.
2. At least two disjoint untouched Track-H validation windows pass.
3. Track-F shadow sample for the same market family reaches the pre-registered minimum.
4. Calibration buckets have adequate support and residuals remain inside tolerance.
5. CLV lower confidence bound is positive, with adequate closing-line snapshots.
6. Shadow drawdown remains below the risk circuit-breaker.
7. Full version diff is documented.
8. Training data snapshot hash is documented.
9. Canary overlap plan is documented.
10. No open leakage findings.
11. Power calculation based on observed Track-H score variance is complete.

Provisional sample policy pending the power calculation:
- calibration-only: 125 settled forward picks per market family;
- architecture/model-family/half-life/feature changes: 400 settled forward picks per market family;
- CLV early-read minimum: 75 closing-line snapshots.

Provisional calibration/risk policy pending re-audit:
- minimum 20 observations per evaluated calibration bucket;
- max absolute calibration residual 0.05;
- max shadow drawdown 20% of the designated shadow bankroll.

These thresholds may only change through an architecture-version change, never after viewing a single ticket outcome.

## 6. Concept drift

Drift is monitored per market family on a rolling 125-observation log-loss stream using one-sided Page-Hinkley.

Tiers:
- NORMAL: no action.
- WATCH: log only; no parameter change.
- REVIEW: open architecture proposal; full promotion gate still required.
- HALT: suspend REAL staking for that market family; continue SHADOW logging.

Current preregistered Page-Hinkley parameters in code:
- delta = 0.005
- REVIEW threshold = 4.0
- HALT threshold = 8.0

Drift detection never mutates model parameters directly.

## 7. Combining evidence without double counting

Track H and Track F are never pooled into a single IID sample size.

Track H answers: would the architecture survive untouched historical windows?
Track F answers: does it survive real execution, current regime, odds, market friction and closing-line comparison?

A retrospective discovery from Track H is contaminated on the slice that generated it. It must be tested on a different untouched historical slice and then clear the forward shadow requirement before production promotion.

## 8. Correlation

Same-game combinations whose legs are functions of the final score must derive joint probability by summing score-matrix cells satisfying every leg. Marginal multiplication is prohibited.

Cross-match legs may use independence as a first-order joint-probability assumption, while repeated structural exposure across matches/weeks remains a portfolio-risk issue and is governed separately.

## 9. Metrics

- Brier: primary scalar probability score where applicable.
- Log loss: secondary proper score, especially sensitive to confident misses and used for drift monitoring.
- Calibration residuals: diagnostic by probability bucket/market family.
- CLV: leading real-market indicator; lower confidence bound matters more than point estimate.
- ROI/P&L: lagging and noisy; never the sole promotion trigger.
- Drawdown: risk circuit-breaker; never a direct model-tuning trigger.

## 10. Current status

`Vn-2026-DC-ENSEMBLE` remains `SHADOW MODEL SIGNAL`. It is not production-cleared and its outputs do not automatically authorize REAL wagers.

The December MXN 100,000 objective is not part of model validation and cannot relax any gate.
