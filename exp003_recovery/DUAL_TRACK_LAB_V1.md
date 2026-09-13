# DUAL-TRACK LAB V1 — 1000 a 100000

## Goal
Build a Liga MX prediction/parlay system that can be used prospectively now while the historical walk-forward replay continues from Clausura 2025. The two tracks share a mathematical core and evaluation framework, but never share information across a forbidden temporal boundary.

## Track H — Historical walk-forward replay
- Start from the frozen pre-jornada state.
- Use only matches and public context available before the jornada cutoff.
- Generate model probabilities, apply predeclared selection rules, freeze, then reveal outcomes.
- Settled outcomes may update only later historical states and research diagnostics.
- Never rewrite an earlier frozen probability, ticket, or verdict.
- Historical results are retrospective evidence and may not directly justify a production model change without an untouched validation segment or forward evidence.

## Track F — Forward production test
- At each real cutoff, use every completed Liga MX match that truly occurred before that cutoff, even if Track H has not replayed that date yet.
- Current parent engine: V0.1R_RECOVERED Dixon-Coles ensemble with half-lives 180/365/730/1460.
- Current data bridge: OpenFootball through 2024-25 plus FotMob for 2025-26 and current 2026-27.
- A match enters training only when kickoff < cutoff AND status=finished.
- Generate the full score matrix first; derive 1X2, double chance, totals, BTTS and team totals from it.
- Same-game joint probabilities must be computed directly from the score matrix, never by multiplying correlated marginals.
- Compare p_model with de-vig market probabilities. No official edge claim without a valid mapped price.

## Two meanings of learning
### A. State update — automatic and allowed
After a newly completed match becomes eligible, append it and refit the fixed model specification. Team attack/defense, intercept, home advantage and rho may therefore change naturally.

### B. Architecture update — gated
Changes to half-lives, model family, calibration method, market eligibility, context weights, thresholds, parlay construction, priors or risk rules require a new model version and an explicit promotion gate. One winning or losing ticket is never sufficient evidence.

## Information firewall
- Forward outcomes never leak into a historical prediction whose cutoff precedes them.
- Historical outcomes are revealed only after that historical freeze.
- Forward Track F may use all real matches that occurred before its actual cutoff; it does NOT wait for Track H to catch up.
- No frozen prediction is recalculated after the result is known.
- Every dataset row is deduplicated by date/fixture/score/source mapping before fitting.

## Freeze record required for every prediction
- model_version
- parent_version
- cutoff timestamp + timezone
- data snapshot/source counts and ideally hash
- fixture and kickoff
- market/selection/line
- p_model
- quoted odds and timestamp
- raw implied p and de-vig p when possible
- model edge and EV
- score-matrix reference for correlated selections
- context signal and any veto
- minimum acceptable odds
- SIM stake / REAL stake stored separately

## Settlement diagnostics
At leg and ticket level track at minimum:
- result
- Brier score
- log loss where applicable
- calibration residual by market family and probability bucket
- ROI and drawdown where authentic odds exist
- CLV when closing price can be captured
- cause-of-error tags, kept descriptive rather than retroactively changing the model

## Promotion gate for a new architecture
A candidate version may be promoted only when it beats the incumbent on predeclared metrics across an untouched validation segment and/or sufficient forward observations. It must not be promoted solely because recent parlays won. Promotion decision and evidence are append-only.

## Context layer
For now context remains outside numeric p_model. Pre-kickoff injuries, suspensions, lineup changes, rest, tactical changes and reliable news may issue a material veto or confidence warning. Narrative/support alone may not inflate model probability. If context is later encoded numerically, that is an architecture change requiring a new version and validation.

## Bankroll separation
SIM and REAL share hypotheses but remain separate executions, odds, stake, P&L and timestamps. Current experimental SIM unit remains 10 MXN. User-directed REAL stake does not change model quality or constitute validation.

## Current bridge snapshot — 2026-09-13
Vn-2026-DC-ENSEMBLE parent=V0.1R_RECOVERED.
Cutoff=2026-09-13T16:10:00 America/Mexico_City.
Training matches=1416.
Last admitted match=2026-09-12 21:15 local.
Sources: OpenFootball through 2024-25; FotMob 2025/26 Apertura; FotMob 2025/26 Clausura; FotMob 2026/27 Apertura.
Today's target matches are excluded from training until after they finish.
