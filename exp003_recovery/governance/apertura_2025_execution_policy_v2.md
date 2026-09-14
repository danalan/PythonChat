# Apertura 2025 Execution Policy V2

Effective: Apertura 2025 J1 historical replay
Status: ACTIVE GOVERNANCE
Historical money: SIMULATED/PAPER only

## 1. Participation and stake

- Every jornada must contain at least one wager while simulated bankroll > 0.
- MXN 200 is the absolute jornada ceiling, not a target.
- Default total jornada exposure = min(MXN 200, 10% of current simulated bankroll).
- Exposure may be reduced when price quality / calibration confidence is weak, but never to zero while bankroll > 0.
- Reference exposure tiers, determined before outcome:
  - LOW confidence / weak price quality: 2% of bankroll.
  - MEDIUM: 5%.
  - HIGH: 8%.
  - EXCEPTIONAL: 10%.
- No individual wager may risk more than 40% of the jornada exposure budget.

## 2. Portfolio hierarchy

PRIMARY: singles.
SECONDARY: two-leg parlays, diagnostic/limited allocation only.
SHADOW ONLY: three-leg parlays for continuity/research.

- A two-leg parlay may receive at most 20% of the jornada exposure budget.
- No same-game correlated parlay unless a validated joint score-matrix calculation exists and the ticket is explicitly classified as a diagnostic experiment.
- Do not force a fixed ticket count.

## 3. Decision stack

For each fixture:
1. Freeze raw V0.1R MODEL_ONLY probabilities.
2. Retrieve temporally clean pre-cutoff prices.
3. Prefer exact target-market prices; MARKET_PROXY_V1 is diagnostic until validated.
4. Run context audit using only pre-cutoff information.
5. Freeze raw p, calibration-shadow p, price, context verdict and chosen stake before results.
6. Settle append-only.

## 4. Calibration experiment

- V0.1R raw probabilities remain canonical comparator.
- A calibration/shrinkage candidate trained only on completed Clausura 2025 selected-leg evidence may run in SHADOW.
- Apertura 2025 is the first untouched validation tournament for the calibration candidate.
- Do not use Apertura results to refit the same candidate before a preregistered evaluation checkpoint.
- Compare raw vs calibrated using Brier, log loss, calibration gap and economic decisions at exact prices where available.

## 5. Context

Context is mandatory research but not yet a numeric model feature.
Allowed tags: SUPPORT, NEUTRAL, CONTRADICT_LOW, CONTRADICT_HIGH, UNKNOWN.
Priority diagnostics: recent GF/xG/SOT, opponent defensive process, home/away, opponent strength, lineups/injuries, manager/system changes, rest/fatigue, rivalry/tempo, team-specific deterioration.

A context contradiction may reduce stake or quarantine a wager under governance, but must never secretly rewrite p_model.

## 6. Price quality

Price classes:
A = exact archived target-market price from identifiable sportsbook before cutoff.
B = exact same market/line from another clean archived book/consensus.
C = MARKET_PROXY_V1 reconstructed from 1X2; diagnostic only.

Economic performance must be segmented by price class. Proxy C may not be presented as demonstrated EV.

## 7. Integrity

- Score-suppressed fixture discovery is mandatory.
- Never search generic historical result pages before freeze.
- Any accidental outcome exposure is logged; affected jornada cannot promote features.
- Historical simulated bankroll and real forward bankroll remain separate.

## 8. Promotion gates

No change to rho, decay, Dixon-Coles core or context feature promotion without prospective evidence and versioned fiscal review.