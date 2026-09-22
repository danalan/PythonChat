# LENNON Daily Prospective Training V2

Effective: 2026-09-16
Updated: 2026-09-18
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

## 2026-09-18 correction — valid 17-Sep same-day batch (TEST 03V)

This section is append-only and corrects the scope interpretation of the earlier 2026-09-17 TEST 03 entry without deleting it.

Two distinct 17-Sep artifacts must be kept separate:
- the mixed-date artifact described above remains `INVALIDATED_CALENDAR_ERROR`;
- a separate same-day SHADOW batch existed and is now registered as `TEST_03V_VALID_SAME_DAY`.

### TEST 03V settlement summary
- 20 SHADOW parlays x 3 legs.
- MXN 25 SIM per ticket; MXN 500 total simulated exposure.
- 30 unique forecast legs.
- Parlay result: 8/20 won, 12/20 lost.
- Unique-leg result: 23/30 won, 7/30 lost = 76.7% hit rate.
- Winning tickets: P03, P07, P08, P10, P14, P15, P17, P19.
- Losing unique legs:
  1. Hoffenheim ML.
  2. OFI–Hoffenheim BTTS Yes.
  3. Besiktas–Marseille Under 3.5.
  4. Juventus–NEC Under 3.5.
  5. Lillestrøm ML.
  6. Manchester City Over 4.5 corners.
  7. Málaga/Draw double chance.
- The proposed-odds settlement implies MXN 751.25 return, +MXN 251.25 diagnostic P&L and +50.25% diagnostic ROI on MXN 500. These are `DIAGNOSTIC_COUNTERFACTUAL`, NOT official ROI/P&L, because final bookmaker odds were not frozen.

The predictive learning unit remains the unique leg. The 8/20 parlay result measures construction and dependency; it must not be treated as 20 independent forecasting observations.

## V2.1 prospective safeguards — effective 2026-09-18

No numerical model weight, probability parameter, decay constant or calibration transform is retuned from TEST 03V alone. The session creates prospective safeguards and hypotheses only.

### 1. BLOWOUT_TAIL_GATE
For totals and BTTS candidates, explicitly audit one-sided and blowout score paths before selection, especially 3-0, 4-0, 4-1 and 5-0 type outcomes.

A totals/BTTS leg must record:
- whether a strong favorite can win comfortably without the market condition surviving;
- whether an under is vulnerable to one team's scoring ceiling rather than only the combined mean;
- whether BTTS depends too heavily on the weaker side scoring;
- a comparison with ML/DNB/AH/team-total alternatives when the matchup is asymmetric.

If the tail audit materially contradicts the leg, downgrade or reject it. This is a selection gate, not a retrospective probability adjustment.

### 2. CORNER_SPECIFIC_GATE
Never infer a corner over from expected dominance, possession, shots, goals, or win probability alone.

A corner leg requires corner-specific evidence or a legitimate corner-model output, plus a score-state sensitivity check. Early leads can reduce attacking pressure and corner accumulation; therefore game-state risk must be recorded explicitly.

Until the separate corner model clears its promotion criteria, unsupported corner opinions remain `EXPERIMENTAL` or `MARKET/CONTEXT`, not `MODEL_SIGNAL`.

### 3. PORTFOLIO_CONTAMINATION_GATE
Beginning with the next daily SHADOW freeze:
- max reuse of any unique leg: 2 tickets;
- `EXPERIMENTAL` or `LOW_EVIDENCE` leg: max 1 ticket;
- never repeat the same pair of legs across two parlays;
- max one tail-sensitive/experimental leg per parlay;
- do not place two legs from the same fixture in one parlay unless the test is explicitly designed as a correlation experiment;
- track fixture-level exposure separately from leg-level exposure.

This gate is intended to stop one forecast error from mechanically destroying a large share of the portfolio.

### 4. FREEZE_QUALITY_GATE
Official SHADOW ROI/P&L requires final frozen odds before kickoff. If only proposed odds exist, settlement may be reported only as `DIAGNOSTIC_COUNTERFACTUAL`.

Where mathematically legitimate, freeze:
- p_model and model version;
- contemporaneous odds;
- no-vig p_market;
- edge versus market;
- signal provenance;
- cutoff timestamp;
- closing odds/CLV when later obtainable.

Missing p_model must remain missing. Market-implied probability is never relabeled as model probability.

### 5. New diagnostic subflags
In addition to the existing postmortem taxonomy, record:
- `TAIL_BLOWOUT`: the selected market failed through an asymmetric/high-score tail;
- `SCORE_STATE`: game-state evolution invalidated the pre-match mechanism, especially for corners;
- `PORTFOLIO_AMPLIFICATION`: one unique-leg miss damaged multiple tickets.

### 6. Hypotheses opened from TEST 03V
- `H17-01`: Under/BTTS selections in asymmetric fixtures are under-audited for blowout and one-sided tails.
- `H17-02`: Expected team dominance is an unreliable proxy for team-corner overs without corner-specific and score-state evidence.
- `H17-03`: Portfolio construction is amplifying a small number of unique-leg errors into too many ticket losses.

These hypotheses are NOT promoted rules about predictive probabilities. They must be evaluated prospectively and by market family. Minimum evidence target before quantitative promotion: 50 unique prospective legs in the affected family, with calibration/market comparison where probabilities and odds are available.


## 2026-09-18 operating terminology + 30-parlay cadence override

Effective from this instruction forward:

### Canonical user terminology
- "Entrenamiento de Lennon", "Lennon modo entrenamiento", or equivalent means the DAILY SHADOW training portfolio.
- The DAILY SHADOW training portfolio is now exactly 30 parlays, normally 3 legs each.
- Default accounting remains MXN 25 SIM per SHADOW ticket unless a future explicit instruction changes it. At 30 tickets this equals MXN 750 simulated daily exposure.
- "Apuesta con Lennon" means a REAL-money wager that Carlos confirms he actually placed. REAL wagers remain in a separate ledger and never merge with SHADOW results.

### Corner-market expansion
Corners remain a distinct model family and must not be inferred from possession, favoritism, shots or goals alone.
Beginning with the next clean daily freeze:
- scan corners as an active training family on every supported slate;
- target roughly 25%-35% of SHADOW leg slots as CORNERS when same-day market availability and evidence quality support it;
- do not force a corner quota when the market/data are poor;
- every corner leg requires corner-specific evidence plus score-state sensitivity;
- corner legs may be tagged ACTIVE_TRAINING once source quality, line semantics and corner-specific evidence are adequate for prospective learning;
- ACTIVE_TRAINING does NOT mean REAL_ELIGIBLE;
- REAL execution still requires the full Real-money execution gate, including legitimate model support, contemporaneous odds, no-vig market comparison where calculable, estimated edge, context audit, Fiscal review and immutable pre-kickoff freeze.

C0.1-CORNERS-NB-ENSEMBLE remains unpromoted for REAL use until source-of-record, missingness, mapping and prospective calibration requirements are satisfied.

### 2026-09-18 transition
TEST 04 P01-P20 remains immutable at its original morning cutoff. To honor the new 30-ticket cadence without rewriting history, a separate prospective addendum TEST 04B P21-P30 was frozen later on 18-Sep using only fixtures that had not kicked off at that second cutoff. The two sub-freezes must always retain their distinct timestamps.


## 2026-09-18 correction — cadence restored to 20 SHADOW parlays

This section supersedes the immediately prior "30-parlay cadence override" for all future operation.

### Canonical cadence
- "Entrenamiento de Lennon", "Lennon modo entrenamiento", or equivalent = exactly 20 DAILY SHADOW parlays.
- Default structure remains 3 legs per parlay unless a future explicit test says otherwise.
- Default accounting returns to MXN25 SIM per ticket = MXN500 simulated daily exposure.
- "Apuesta con Lennon" continues to mean a REAL-money wager Carlos confirms he actually placed. REAL and SHADOW remain strictly separate.

### Training competition universe
Daily SHADOW training must deliberately explore beyond Liga MX:
- core known leagues: Liga MX, Argentina Primera, Premier League, LaLiga, Serie A, Bundesliga, Ligue 1, Champions League, Europa League and other major UEFA competitions when scheduled;
- exploratory European tiers: second divisions and comparable lower professional tiers such as Championship, Segunda División, 2. Bundesliga, Serie B, Ligue 2 and other data-supported leagues;
- the purpose of lower-tier inclusion is hypothesis discovery by league/market family, not an assumption that they "have more goals";
- segment all learning by competition, market family and odds band so high-scoring or low-scoring hypotheses can be tested prospectively rather than assumed.

### REAL-money league scope
For now, REAL "Apuesta con Lennon" candidates are restricted to competitions Carlos knows and can independently read:
- Liga MX;
- Argentina Primera;
- LaLiga;
- Premier League;
- UEFA Champions League;
- UEFA Europa League;
- other major UEFA competitions explicitly familiar to Carlos.
Unknown/lower-tier competitions remain SHADOW-only unless Carlos later expands the REAL scope.

### Explanation standard for REAL candidates
Every REAL candidate must explain separately:
1. model evidence and model version, when a legitimate model output exists;
2. statistical evidence;
3. contextual evidence: injuries, suspensions, lineups, rest, tactical/manager changes and relevant current form;
4. market evidence: contemporaneous odds, no-vig p_market where possible and plausible alternatives;
5. explicit contradictory evidence and failure paths;
6. why the selected market beats the alternatives.
If p_model does not exist, state that explicitly. Never replace it with market probability or narrative confidence.

### Corners
Corners remain ACTIVE_TRAINING and should receive meaningful representation in SHADOW portfolios when data quality supports them. The target of roughly 25%-35% of leg slots remains an experiment, not a forced quota. Promotion to REAL still requires the full REAL execution gate and sufficient prospective validation.

### TEST 04B disposition
The later P21-P30 addendum created under the mistaken 30-ticket instruction is retained for audit history but is EXCLUDED from the canonical "training of Lennon" count and from the daily 20-parlay performance headline. It may be analyzed only as a separate AUXILIARY_CORNERS_EXPERIMENT and must never be merged with TEST 04 P01-P20.


## 2026-09-18 external-consult standard — Squawka + context separation

Effective immediately for all user-facing LENNON prediction reports.

### Mandatory prediction report blocks
When a current prediction is presented, report the evidence in separate blocks:
1. **LENNON** — actual executed model name/version, p_model only when the model was genuinely run, fair odds, bookmaker price and price-gate result.
2. **SQUAWKA** — current Squawka prediction/probability or model signal when available, with source timestamp/URL when practical. This is EXTERNAL_SIGNAL:SQUAWKA, never LENNON p_model.
3. **CONTEXT** — injuries, suspensions, expected/confirmed lineups, rest, travel, tactical/manager changes, current form and other pre-cutoff evidence, tagged SUPPORT / NEUTRAL / CONTRADICT_LOW / CONTRADICT_HIGH / UNKNOWN.
4. **MARKET** — contemporaneous bookmaker odds, raw implied probability and no-vig estimate when feasible.
5. **SYNTHESIS** — explain agreement or disagreement among model, Squawka, context and market. Do not average probabilities merely because multiple sources exist.

### Squawka role
- Squawka is an external benchmark/consult, not a training target and not a predictive feature inside Vn-2026 unless a future validated architecture change explicitly adds it.
- Agreement with LENNON is corroboration, not proof.
- Disagreement opens a diagnostic question: identify whether the difference comes from current context, market price, model scope, sample/data differences or methodological assumptions.
- Squawka output never overwrites LENNON probability and never receives automatic numeric weight.
- Post-match learning is still based on frozen pre-match evidence and actual outcomes, not on whether LENNON agreed with Squawka.

### Current context usage in LENNON
The LENNON system **does use context**, but the current Vn-2026-DC-ENSEMBLE core probability model does **not** numerically ingest narrative context such as injuries, lineup news, motivation, travel or tactical changes. Context is a separate decision layer applied after p_model is frozen. It may SUPPORT, downgrade, quarantine or veto a candidate, but it must not add/subtract arbitrary percentage points from p_model.

This separation remains mandatory until a context feature is formally specified, prospectively validated and promoted through governance.


## 2026-09-18 prospective portfolio lesson — damage concentration gate

Effective for the next LENNON training cycle. This is a portfolio-governance update, NOT a probability/model retune.

### Evidence from TEST 04 partial settlement
- At the 19:00 CDMX checkpoint, 21 unique legs were resolved: 15W-6L (71.43%).
- Yet 10 of 11 settled parlays had already lost.
- The main mechanism was PORTFOLIO_AMPLIFICATION: a small number of losing forecasts, especially clustered around the same fixture/thesis, contaminated many tickets.

### New mandatory PORTFOLIO_DAMAGE_GATE
Before freezing any 20-parlay SHADOW portfolio:
1. Build a fixture-exposure map and a failure-thesis map for every candidate leg.
2. Tag each leg with its principal plausible failure mode(s), e.g. FAVORITE_COLLAPSE, EARLY_GOAL, BLOWOUT_HIGH, WEAK_SIDE_NO_SCORE, SCORE_STATE, LOW_ODDS_TAIL, LINEUP_SHOCK, or other explicit mechanisms.
3. Run an adverse-scenario stress test before freeze: for each fixture, evaluate plausible score-state outcomes and count how many tickets would die.
4. No single plausible fixture outcome should be able to destroy more than 30% of the 20-ticket portfolio (max 6 tickets) unless the entire slate is explicitly labeled LOW_DIVERSITY and kept SHADOW-only.
5. No single failure thesis should dominate more than 30% of ticket exposure. If it does, diversify by fixture, market family, or thesis before freeze.
6. Distinct legs from the same fixture are NOT automatically diversified if they depend on the same underlying match thesis.
7. Preserve the existing max leg reuse = 2 and no repeated leg-pair rule; the new gate sits above those controls rather than replacing them.
8. Prefer broader fixture coverage over manufacturing extra markets from a small number of matches. Scan more leagues/fixtures first.

### Learning rule
TEST 04 creates a portfolio hypothesis, not a predictive parameter change. The hypothesis is: high unique-leg hit rate can still produce poor parlay performance when failure modes are clustered. Future sessions must track whether PORTFOLIO_DAMAGE_GATE reduces ticket-loss amplification while preserving unique-leg calibration.


## 2026-09-22 mandatory user-facing portfolio transparency — TRAIN + SETTLE

Effective immediately. This is a reporting/governance rule and does not retune model probabilities.

### When LENNON trains
Every completed daily SHADOW training response shown to Carlos MUST include the exact 20 frozen parlays, P01-P20, with all three legs visible per ticket. When frozen odds exist, show the ticket odds and MXN 25 SIM stake. Also show the unique-leg identifiers or enough market detail to map each ticket back to the Research Ledger. A training cycle is not considered user-facing complete if only aggregate counts or a summary are shown.

### When LENNON settles
Every settlement/closure response shown to Carlos MUST display those same P01-P20 tickets and grade each ticket explicitly as WON / LOST / PUSH / VOID / PENDING as applicable. For a lost ticket, visibly identify the losing leg(s); for a winning ticket, show that all required legs survived. Preserve the original frozen rationale and composition. Never reconstruct or silently substitute a leg after results are known.

### Required settlement summary
After the ticket-by-ticket table, report: unique-leg W/L/P/V first; parlay W/L/P/V second; SIM stake/return/P&L/ROI only where freeze-quality permits; concentration/amplification observations; and failure taxonomy MODEL / EVIDENCE / CONTEXT / PRICE / SELECTION / PORTFOLIO / VARIANCE. Unique legs remain the predictive learning unit and parlays remain the portfolio-learning unit.

### Auditability
The purpose is human auditability: Carlos must be able to see what LENNON actually entered before kickoff and later see exactly which tickets won or lost. Aggregate hit rate may supplement this display but never replace it.
