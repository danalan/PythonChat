# Clausura 2025 Claude Fiscal Review — Adjudication

Status: ACCEPTED WITH MATERIAL QUALIFICATIONS
Date: 2026-09-14
Scope: decisions for Apertura 2025 historical replay; no rewrite of settled Clausura 2025.

## Overall verdict

ACCEPT REVISE.

However, two Claude claims are narrowed:

1. `63.5% > 50%` does NOT by itself prove real betting signal. The selected markets are not 50/50 propositions; evidence of edge must be measured against contemporaneous market prices / calibrated baselines, not a coin flip.
2. `74.0% mean p vs 63.5% realized` proves overconfidence in the SELECTED-LEG layer over J11-J17. It does not yet prove that the entire V0.1R probability engine is globally miscalibrated because selection itself is non-random and some prices are reconstructed proxies.

## Decisions

### ACCEPT NOW — governance / process

- Mandatory 3-leg parlays are retired as the PRIMARY bankroll vehicle.
- Singles become the primary economic vehicle.
- Two-leg parlays remain secondary diagnostic bets only.
- Three-leg parlays may be logged in shadow for continuity/research, but receive no primary bankroll allocation.
- Score-suppressed fixture discovery is mandatory for every historical replay.
- Mandatory participation each jornada remains in force.
- MXN 200 remains an absolute ceiling, never a quota.
- Historical SIMULATED money remains fully separated from forward REAL money.

### ACCEPT AS SHADOW TEST — not production-calibrated yet

- Probability calibration/shrinkage is a priority experiment.
- Do not fit on J11-J17 and then score improvement on J11-J17 as evidence.
- Clausura J11-J17 may be used as TRAINING evidence for a calibration candidate, but Apertura 2025 must be untouched prospective/forward historical validation for that candidate.
- Raw V0.1R probability and calibrated-shadow probability must both be frozen each jornada.
- Calibration does not change the underlying Dixon-Coles score matrix; it is an output-layer candidate.

### ACCEPT AS REQUIRED VALIDATION

- MARKET_PROXY_V1 is demoted from `edge estimator` to `market-disagreement diagnostic` until validated against exact archived target-market odds.
- Where an exact target-market historical price exists, use it for economic accounting and compare proxy error.
- Where exact target-market price cannot be recovered, proxy-derived EV cannot be the sole reason to size up a wager.

### SHADOW ONLY

- Double-chance family recalibration.
- Puebla/team-specific deterioration flags.
- Recent form, xG, shots/SOT, injuries, opponent strength, manager changes, rest, fatigue, rivalry/tempo and tactical context.
- These context variables may SUPPORT / NEUTRAL / CONTRADICT_LOW / CONTRADICT_HIGH a candidate, but do not numerically alter p_model until prospective evidence exists.

### REJECT / DO NOT DO

- Do not infer edge from 63.5% hit rate vs 50%.
- Do not globally penalize team-to-score markets.
- Do not hard-code a Puebla penalty from six observations.
- Do not retune rho, decay or the Dixon-Coles core from this tournament.
- Do not promote proxy EV despite the cash-preservation counterfactual.

## Why the parlay decision changes now

Observed selected-leg hit rate J11-J17 = 40/63 = 63.49%.
A rough independent 3-leg conversion is 0.6349^3 ~= 25.6%, close to the observed 5/21 = 23.8% ticket rate. Independence is only an approximation, but the order of magnitude is correct: compounding three uncertain legs makes the ticket inherently fragile.

Therefore the system will no longer require three-leg parlays to carry the bankroll.

## Apertura 2025 learning agenda

Ranked:
1. Out-of-sample calibration/shrinkage shadow.
2. Singles-primary vs two-leg-secondary portfolio economics.
3. Exact-price audit of MARKET_PROXY_V1.
4. Double-chance residual calibration.
5. Context/deterioration shadow tags, especially recent attacking process and opponent strength.

No architecture/model-family promotion is authorized yet.