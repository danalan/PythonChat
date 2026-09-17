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

## Same-day eligibility gate — added 2026-09-17
- A daily SHADOW training cycle may contain ONLY fixtures whose scheduled kickoff date is the same local calendar date as the training cycle, using America/Mexico_City.
- Verify fixture date and kickoff before candidate generation and again before FREEZE.
- Tomorrow's matches, future weekend matches, postponed/rescheduled matches outside the date, and stale schedule entries are INELIGIBLE.
- If any leg is later found to violate the same-day gate, the affected daily test is INVALIDATED for learning and must not receive W/L, ROI, P&L, Brier or calibration credit.
- Do not silently replace an ineligible fixture after FREEZE. Start a new prospective test/version with a new cutoff.
- The 2026-09-17 TEST 03 constructed at 15:52 CDMX violated this rule by including future-date fixtures. It is retained append-only as INVALIDATED_CALENDAR_ERROR and is not predictive evidence.

## Market-universe-first
Scan and freeze the actual available market universe before constructing the portfolio. Five primary market families are tracked separately:
1. RESULT: 1X2, double chance, DNB.
2. GOALS: totals, BTTS, team totals.
3. HANDICAP: Asian handicap and equivalent lines.
4. CORNERS: totals, team corners, corner handicaps.
5. CARDS: historical taxonomy only. Cards remain OUT_OF_SCOPE for active model expansion per 2026-09-13 governance decision.

Halves and player props may be explored when available, but are secondary. Active expansion remains corners and first-half markets; full-time goals remain the core. Do not force equal counts if the slate does not support them.

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

## Real-money execution gate — added 2026-09-17
A football opinion is not a wager-ready forecast. Before Lennon can recommend a leg for REAL execution, the record must contain:
1. legitimate p_model when the model actually supports that league/market;
2. contemporaneous market odds and no-vig market probability where calculable;
3. estimated edge versus market;
4. explicit tail-risk / blowout-risk check for totals and BTTS;
5. lineup/context audit available before cutoff;
6. comparison against plausible alternative markets;
7. Fiscal/adversarial review;
8. immutable FREEZE before kickoff.

If this chain is incomplete, the candidate may remain SHADOW/EXPERIMENTAL but is not model-validated for REAL money. A high-looking probability is not evidence of edge.

## Learning units
A unique forecast/leg is the predictive learning unit. Repeating a leg in multiple parlays does not multiply predictive n. Research Ledger stores unique legs. Portfolio Ledger stores tickets, repetitions, concentration, correlation, odds, simulated stake, settlement and P&L.

### Concentration cost
Repeated use of the same leg creates portfolio dependency. Every reuse must be visible and justified. Exposure concentration is audited separately from predictive quality because one bad forecast can destroy several tickets without representing several independent forecasting errors.

Low odds are not synonymous with safety. Performance must also be segmented by odds band so repeated short-priced failures cannot hide behind nominal hit rate.

## Workflow
1. Identify eligible SAME-DAY fixtures and freeze the pre-research cutoff.
2. Verify date/kickoff in America/Mexico_City.
3. Research pre-match data, model outputs, injuries/suspensions, lineups when available, form/statistics, market prices, press and relevant external signals.
4. Scan the real market universe.
5. Build the candidate-leg universe.
6. Complete and freeze the mandatory pre-match selection audit for every leg that can enter a ticket.
7. Rank/evaluate candidates and rejected alternatives.
8. Construct exactly 20 three-leg SHADOW parlays, controlling correlation and concentration.
9. Re-verify SAME-DAY eligibility, freeze portfolio composition and prices.
10. Settle after results.
11. Postmortem by unique leg and by portfolio.

## Postmortem and diagnostics
For each unique leg compare the frozen pre-match rationale with the actual outcome. Classify failure or weakness as one or more of:
- MODEL
- EVIDENCE
- CONTEXT
- PRICE
- SELECTION
- PORTFOLIO
- VARIANCE
- CALENDAR/DATASET

Track active market families separately using prospective sample size, hit rate versus implied probability, calibration/Brier or log loss when applicable, SIM P&L and closing-line value when obtainable. Also segment by league, odds band and signal provenance.

Parlay outcomes measure portfolio construction. They do not create additional independent predictive observations.

## 2026-09-17 real-money postmortem
Confirmed REAL history must remain separate from SHADOW training.

### 2026-09-16 — REAL — WIN
- Stake: MXN 50.
- Combined odds: 2.821.
- Return: MXN 139.78.
- Net P&L: +MXN 89.78.
- Barcelona vs Racing Santander: Over 9 corners — WIN.
- Levante vs Athletic Bilbao: Asian Over 2/2.5 goals — VOID after match suspension/modification.
- Atletico Madrid vs Osasuna: Atletico Madrid ML — WIN / early payout shown by bookmaker.
Interpretation: profitable ticket, but one void leg reduced the number of forecasts that actually had to survive. Do not use the win as proof of calibration or edge.

### 2026-09-17 — REAL — LOSS
Four-leg parlay:
- Betis vs Getafe: Under 3.5 — WIN; final 1-0.
- Crystal Palace vs Lech Poznan: BTTS Yes — LOSS; final 4-0.
- Juventus vs NEC: Under 3.5 — LOSS; final 5-0.
- Malaga vs Villarreal: Over 1.5 — WIN; final 1-3.
Result: 2/4 legs won; parlay lost.
Primary diagnostic: the two losing legs failed on blowout/one-sided tail scenarios. The pre-bet probabilities presented for those legs were not demonstrated as calibrated p_model outputs. Treat this as a governance and tail-risk flag, not as evidence sufficient for parameter retuning.

## 2026-09-17 SHADOW TEST 03
- Constructed/frozen around 15:52 CDMX as 20 parlays x 3 legs, MXN 25 SIM each, MXN 500 simulated exposure.
- 15 unique legs, each reused four times.
- It included fixtures scheduled on later dates, including NYCFC vs NY Red Bulls, Bayern vs Union Berlin and Brentford vs Chelsea, and therefore did not satisfy a same-day training definition.
- Status: INVALIDATED_CALENDAR_ERROR.
- Settlement: NONE for learning purposes.
- W/L, P&L, ROI, Brier/calibration: NOT SCORED.
- Preserve the artifact append-only to document the process failure.

## Anti-overfit rule
No model probability, parameter, weight or structural rule may be changed merely because of one daily slate, one winning REAL ticket, one losing REAL ticket or one 20-parlay session. Quantitative retuning requires accumulated prospective evidence sufficient to distinguish repeatable error from variance. A single result can create a hypothesis or flag, not a fitted correction.

## Existing valid training evidence
The LENNON MARKET-UNIVERSE TEST 02 frozen on 2026-09-16 remains unchanged and valid as prior SHADOW evidence. Preserve its original freeze and settlement. Do not rewrite it retroactively to fit later taxonomy.

## Governance
Preserve all prior canon and records append-only. Fiscal/Claude is an adversarial governance reviewer, not a predictive signal. REAL and SIMULATED records must never be merged. The purpose is not daily hit-rate maximization. The purpose is clean prospective evidence about which leagues, market families, signals and portfolio constructions LENNON can predict reliably.