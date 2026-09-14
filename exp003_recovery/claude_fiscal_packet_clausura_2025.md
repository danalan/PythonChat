# CLAUDE FISCAL PACKET — Clausura 2025 betting-lab audit

You are an external fiscal/auditor. Do NOT redesign everything. Your job is to identify the smallest high-value changes for the next tournament and call out where the current system is fooling itself.

## System
Historical replay of Liga MX using V0.1R: Dixon-Coles/goals model with time decay, home advantage and frozen pre-match probabilities. Economic selector compares model probabilities with historical market prices. Historical money is SIMULATED only. Real-money track is separate.

Context such as xG, shots/SOT, recent form, injuries, opponent strength, managers, fatigue and tactical conditions is currently shadow research, not numerically embedded in V0.1R.

## Completed tournament evidence
Economic Track covers Clausura 2025 J11–J17 only. Earlier J1–J10 were different predictive experiments and are not retrofitted into this bankroll series.

Starting bankroll: MXN 1,000 simulated.
Rule used during completed tournament: mandatory 3 parlays/jornada, 3 legs each, stake split 80/80/40 = MXN 200/jornada.
Total stake: MXN 1,400.
Ending bankroll: MXN 443.43.
Net P&L: -556.57.
ROI/stake: -39.76%.
Tickets won: 5/21 = 23.81%.
Legs won: 40/63 = 63.49%.

Bankroll path: 1000 → 936.10 → 975.05 → 775.05 → 681.66 → 481.66 → 281.66 → 443.43.

Selected-leg model confidence averaged about 74.0%, while actual hit rate was 63.5%. Approximate overconfidence gap: -10.5 percentage points. Mean Brier across J11–J17 ~0.2411; mean log loss ~0.6799.

Market-family residuals:
- Team scores 1+: 18/27 = 66.7% vs mean model p ~72.6%.
- Total O1.5: 12/18 = 66.7% vs mean p ~74.5%.
- Double chance: 7/11 = 63.6% vs mean p ~76.8%.
- Puebla-related scoring/total assumptions J12–J17: 0/6 vs mean p ~73.6%. J17 provided the first clean prospective confirmation after this warning had been registered.

Repeated pattern: decent leg accuracy does not translate to parlay economics. J13 = 6/9 legs but 0/3 parlays. J14 = 7/9 but only 1/3. One leg miss kills a 3-leg ticket.

## Price/EV issue
MARKET_PROXY_V1 often derives target-market prices from historical 1X2 odds through an independent-Poisson fit plus the source's observed overround. This is not yet validated against enough exact archived odds.

Counterfactual that only bets tickets with positive proxy EV ended at ~MXN 509.43 vs forced track 443.43, but it staked only ~1,000 vs 1,400. Its ROI on money actually staked was about -49.1%, worse than forced track -39.8%. So it mostly preserved cash by betting less; it did NOT demonstrate that proxy EV identifies genuine edge.

## Integrity
J12–J16 had accidental researcher exposure to some outcomes through search snippets. Selection was mechanical and frozen before settlement, so they remain valid for deterministic bankroll/accounting and diagnosis, but NOT for blind feature promotion. J17 restored researcher blindness using score-suppressed fixture discovery plus pregame-only price sources.

## Governance already changed for next tournament
Participation remains mandatory every jornada. However MXN 200 becomes a CEILING, not a quota. At least one wager must be placed each jornada. Number of tickets and total stake may vary dynamically. This starts next tournament; do not rewrite Clausura 2025 results.

## Do not assume these proposed fixes are correct
We are considering: probability calibration/shrinkage; validating exact-market prices; reducing reliance on 3-leg parlays; dynamic stake sizing; faster-response recent-form features; formal context promotion; double-chance recalibration; team-specific deterioration signals.

## Your task
Return ONLY:
1. VERDICT: KEEP / REVISE / KILL for the current architecture.
2. Top 5 failures ranked CRITICAL/HIGH/MEDIUM, each with evidence from the numbers above.
3. Top 5 changes for Apertura 2025, ranked by expected value of learning, not complexity.
4. Which changes may be implemented immediately vs which require a prospective A/B or shadow test first.
5. A concrete staking rule under mandatory participation, with MXN 200 maximum, that avoids bankroll suicide.
6. Whether the 3-leg parlay structure should remain primary, secondary, or be retired; justify mathematically.
7. What ONE thing are we most likely missing that could explain the 74% predicted vs 63.5% realized gap?

Be adversarial. Do not praise the system. Do not suggest changing rho/decay/model parameters unless the evidence specifically supports it. Maximum 900 words.