# Clausura 2025 — Tournament Audit before Claude Fiscal Review

Status: TOURNAMENT COMPLETE / HISTORICAL MONEY SIMULATED ONLY
Date of audit: 2026-09-14
Scope: Economic Track J11–J17 plus residual lessons accumulated during replay. J1–J10 remain earlier predictive experiments and are not retrofitted into this economic series.

## 1. Economic result

- Starting simulated bankroll: MXN 1,000.00
- Jornadas economically tracked: 7 (J11–J17)
- Forced stake rule during this completed tournament: MXN 200/jornada, split 80/80/40
- Total simulated stake: MXN 1,400
- Ending simulated bankroll: MXN 443.43
- Net P&L: -MXN 556.57
- ROI on simulated stake: -39.76%
- Tickets won: 5/21 = 23.81%
- Individual legs won: 40/63 = 63.49%

Jornada bankroll path:
J11 1000.00→936.10; J12→975.05; J13→775.05; J14→681.66; J15→481.66; J16→281.66; J17→443.43.

## 2. Calibration warning

Across J11–J17 selected legs, mean model confidence is approximately 74.0%, while realized hit rate is 63.5%, an overconfidence gap of roughly 10.5 percentage points.

J11–J15 diagnostic already showed 66.7% hit rate vs 74.0% mean p. J16 deteriorated to 4/9; J17 recovered to 6/9 under restored researcher blindness. Mean selected-leg Brier across J11–J17 = ~0.2411 and mean log loss = ~0.6799.

Do NOT recalibrate using these same observations and then claim improvement on them. Any recalibration must be versioned and evaluated prospectively/out-of-sample.

## 3. Market-family residuals

Approximate cumulative selected-leg results after J17:
- TEAM_SCORE_1PLUS: 18/27 = 66.7% vs mean model p ~72.6%. Mild-to-moderate overconfidence overall, not a broken market.
- TOTAL_OVER_1.5: 12/18 = 66.7% vs mean model p ~74.5%. More meaningful overconfidence.
- DOUBLE_CHANCE: 7/11 = 63.6% vs mean model p ~76.8%. Largest repeated family-level calibration concern.
- Puebla-related scoring/total assumptions J12–J17: 0/6 vs mean p ~73.6%. J17 was the first restored-blindness prospective confirmation of this warning, so the signal deserves structured testing but is still too small/team-specific for a hard-coded penalty.

## 4. Economic selector / price proxy

ECONOMIC_SELECTOR_V1 compares p_model with MARKET_PROXY_V1 prices reconstructed primarily from historical 1X2 odds using an independent-Poisson fit and source overround.

The proxy is useful as a disagreement score but has NOT been validated as accurate exact-market pricing across team totals/totals/double chance.

Counterfactual "only proxy-EV-positive tickets":
- Ending bankroll after J17: ~MXN 509.43
- Total staked: ~MXN 1,000
- Net P&L: -MXN 490.57
- ROI on stake: -49.06%

It preserved more bankroll than the forced-200 series mainly because it staked less, not because demonstrated betting efficiency improved. Treat this as evidence against promoting proxy EV as a trusted edge signal yet.

## 5. Portfolio structure

A recurrent pattern is acceptable leg accuracy with poor parlay economics. J13 had 6/9 legs and 0/3 tickets; J14 7/9 and only 1/3. One failed leg destroys the ticket. The 3-leg parlay requirement creates substantial variance and may be mismatched to a model with meaningful probability overconfidence.

User governance change after J17: participation remains mandatory every jornada, but MXN 200 becomes a ceiling rather than a quota. Future staking should be dynamic, with at least one wager each jornada, while number of tickets and total stake may vary. This rule starts with the next unfrozen tournament, Apertura 2025 J1.

## 6. Context and integrity

V0.1R itself is primarily goal-history/Dixon-Coles based; context is not numerically embedded. Context variables are being logged in shadow: recent GF/xG/SOT, home/away, opponent strength, form, defensive/tempo profile, injuries/lineups/managers/rest/tactical conditions when temporally clean.

J12–J16 researcher had accidental outcome exposure, so those jornadas are usable for deterministic bankroll/accounting and diagnosis but not clean feature promotion. J17 restored blindness using score-suppressed fixture discovery and pregame price sources before freeze.

## 7. What should NOT change without evidence

- Do not retune rho/decay/Dixon-Coles from this tournament alone.
- Do not hard-code a global penalty to team-to-score.
- Do not declare proxy EV validated.
- Do not use J12–J16 outcome-exposed observations as blind proof of contextual features.
- Do not mix historical simulated money with real forward money beginning 2026-09-13.

## 8. Candidate changes for fiscal review

External reviewer should prioritize:
1. probability calibration layer / shrinkage and how to validate it prospectively;
2. exact-market price validation versus MARKET_PROXY_V1;
3. whether three-leg parlays should remain primary vs singles/two-leg portfolio construction;
4. dynamic bankroll/stake sizing under mandatory participation;
5. formal context feature promotion tests, especially recent attacking process, opponent strength, low-tempo/rivalry and team-specific deterioration;
6. whether model update speed/decay is too slow for recent form changes;
7. whether double-chance construction is systematically miscalibrated;
8. leakage/replay integrity and score-suppressed fixture discovery as mandatory standard.

No architecture change is authorized until fiscal review is received and adjudicated.