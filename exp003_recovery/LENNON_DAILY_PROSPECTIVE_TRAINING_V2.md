# LENNON Daily Prospective Training V2

Effective: 2026-09-16
Updated: 2026-09-17
Status: SHADOW / SIMULATED training protocol

## Primary training mode
LENNON's primary learning loop is prospective pre-match evidence. Historical replay remains preserved as prior evidence but is no longer the primary training path because retrospective web research creates result-leakage risk.

## Daily portfolio
- Exactly 20 SHADOW parlays per daily cycle.
- Exactly 3 legs per parlay.
- Accounting stake: MXN 25 SIM per ticket, MXN 500 total daily simulated exposure.
- REAL money is never implied by the simulation. A ticket becomes REAL only after explicit written authorization from Carlos before kickoff.
- Prioritize Liga MX and major/known leagues. Include controlled exploratory leagues to discover repeatable patterns and calibration opportunities.

## Market-universe-first
Scan and freeze the actual available market universe before constructing the portfolio. Five primary market families are tracked separately:
1. RESULT: 1X2, double chance, DNB.
2. GOALS: totals, BTTS, team totals.
3. HANDICAP: Asian handicap and equivalent lines.
4. CORNERS: totals, team corners, corner handicaps.
5. CARDS: totals, team cards, card handicaps.

Halves, player props and specials may be explored when available, but are secondary to the five primary families. Do not force equal counts if the slate does not support them.

## Signal provenance
Never invent model capability. MODEL_SIGNAL requires an actual executed model output for that league/market. Otherwise label the leg MARKET, CONTEXT, EXPERIMENTAL or LOW-EVIDENCE as appropriate. Market-implied or contextual probability must never be called p_model.

## Mandatory pre-match selection audit
Before any parlay is constructed, every candidate leg must have a frozen rationale created before the result is known. Record:
- fixture, competition and kickoff;
- market family, market and line;
- odds, source and observation time;
- signal provenance;
- probability and the nature/source of that probability when one is legitimately available;
- market-specific statistical evidence;
- relevant pre-match context, injuries, suspensions and lineup information available at cutoff;
- why this market was preferred over plausible alternatives;
- material contradictory evidence and risks;
- alternatives rejected and why;
- why the leg deserves inclusion in the portfolio.

This rationale is immutable evidence for the postmortem. The result may update the learning record, never the original explanation. This is an explicit control against hindsight bias and retrospective rationalization.

## Learning units
A unique forecast/leg is the predictive learning unit. Repeating a leg in multiple parlays does not multiply predictive n. Research Ledger stores unique legs. Portfolio Ledger stores tickets, repetitions, concentration, correlation, odds, simulated stake, settlement and P&L.

### Concentration cost
Repeated use of the same leg creates portfolio dependency. Every reuse must be visible and justified. Exposure concentration is audited separately from predictive quality because one bad forecast can destroy several tickets without representing several independent forecasting errors.

Low odds are not synonymous with safety. Performance must also be segmented by odds band so repeated short-priced failures cannot hide behind nominal hit rate.

## Workflow
1. Identify upcoming eligible fixtures and freeze the pre-research cutoff.
2. Research pre-match data, model outputs, injuries/suspensions, lineups when available, form/statistics, market prices, press and relevant external signals.
3. Scan the real market universe.
4. Build the candidate-leg universe.
5. Complete and freeze the mandatory pre-match selection audit for every leg that can enter a ticket.
6. Rank/evaluate candidates and rejected alternatives.
7. Construct exactly 20 three-leg SHADOW parlays, controlling correlation and concentration.
8. Freeze portfolio composition and prices.
9. Settle after results.
10. Postmortem by unique leg and by portfolio.

## Postmortem and diagnostics
For each unique leg compare the frozen pre-match rationale with the actual outcome. Classify failure or weakness as one or more of:
- MODEL
- EVIDENCE
- CONTEXT
- PRICE
- SELECTION
- PORTFOLIO
- VARIANCE

Track the five primary market families separately using prospective sample size, hit rate versus implied probability, calibration/Brier or log loss when applicable, SIM P&L and closing-line value when obtainable. Also segment by league, odds band and signal provenance.

Parlay outcomes measure portfolio construction. They do not create additional independent predictive observations.

## Anti-overfit rule
No model probability, parameter, weight or structural rule may be changed merely because of one daily slate or one 20-parlay session. Quantitative retuning requires accumulated prospective evidence sufficient to distinguish repeatable error from variance. A single result can create a hypothesis or flag, not a fitted correction.

## Existing 20-parlay freeze
The LENNON MARKET-UNIVERSE TEST 02 frozen on 2026-09-16 remains unchanged: 20 SHADOW parlays x 3 legs, MXN 25 SIM each, MXN 500 total. Its frozen candidate legs and tickets must not be rewritten retroactively to fit this V2 taxonomy. V2 applies prospectively to new cycles.

## Governance
Preserve all prior canon and records append-only. Fiscal/Claude is an adversarial governance reviewer, not a predictive signal. The purpose is not daily hit-rate maximization. The purpose is clean prospective evidence about which leagues, market families, signals and portfolio constructions LENNON can predict reliably.