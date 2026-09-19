# LENNON TEST 05 — 2026-09-19 — DAILY SHADOW FREEZE

Status: FROZEN_SHADOW / MARKET_CONTEXT + EXTERNAL_MODEL_EXPERIMENT
Cutoff: 2026-09-19 08:12 America/Mexico_City
Canonical count: exactly 20 parlays x 3 legs = 60 slots
Accounting: MXN25 SIM each = MXN500 simulated exposure
REAL execution: NONE

## Integrity
Only fixtures not kicked off at cutoff are eligible. p_model Lennon is NULL for every leg: Lennon does not yet have a validated native probability model for these selections. Third-party model probabilities are recorded only as EXTERNAL_MODEL evidence and must never be relabeled p_model Lennon. Where contemporaneous bookmaker odds were not verifiable, odds remain NULL and the ticket is excluded from official ROI/CLV; W/L diagnostic settlement remains valid.

## Unique leg registry
A NFO-COV Forest or Draw — EPL — context: Coventry 0 points/0 goals after 4; Wright out, Awoniyi suspended; Forest unbeaten 8/10 home. External model Forest win 49%. Odds NULL.
B NFO-COV Under 3.5 — EPL — Coventry goalless in 4; external model most likely 1-0. Odds NULL.
C CEL-RAC Under 2.5 — LaLiga — Celta only 4 goals in 6 league games; Aspas out; Racing expected more conservative after 7-2 Barcelona loss. Odds NULL.
D CEL-RAC BTTS No — LaLiga — same low-output Celta mechanism; deliberately correlated at fixture level but never paired with C in same ticket. Odds NULL.
E ROM-INT Over 1.5 — Serie A — market 1.21; reported team xG 3.1/2.9 and high shot volume. Lennon p_model NULL.
F ROM-INT BTTS Yes — Serie A — market 1.50; Inter BTTS 67% sample; Roma/Inter corners 5.7/6.3 avg. Lennon p_model NULL.
G ROM-INT Over 8.5 corners — Serie A — ACTIVE_TRAINING CORNERS; combined listed corner averages ~12.0. Odds NULL. Score-state risk explicit.
H STU-DOR Over 2.5 — Bundesliga — market ~1.42; external models 55%-65%; both attacks active. Lennon p_model NULL.
I STU-DOR BTTS Yes — Bundesliga — market ~1.36; external model 58%-67%. Lennon p_model NULL.
J STU-DOR Over 8.5 corners — Bundesliga — ACTIVE_TRAINING CORNERS; Stuttgart listed 6.5 corners/game, Dortmund 3.0. Odds NULL.
K LYO-REN Over 2.5 — Ligue 1 — market reported 1.57; external Poisson 63%; last 5 H2H over 2.5. Lennon p_model NULL.
L LYO-REN Over 8.5 corners — Ligue 1 — ACTIVE_TRAINING CORNERS; listed averages Lyon 5.5, Rennes 4.25. Odds NULL.
M MET-STE Over 2.5 — Ligue 2 — EXPLORATORY SECOND TIER; external models ~63%; Saint-Etienne 17 goals in 6, Metz striker Fall 5. Odds NULL.
N MET-STE BTTS Yes — Ligue 2 — external ensemble ~65%; tests lower-tier goals hypothesis prospectively. Odds NULL.
O MET-STE Over 7.5 corners — Ligue 2 — ACTIVE_TRAINING CORNERS; listed averages Metz 4.8, Saint-Etienne 4.2. Odds NULL.
P DRE-HER X2 — 2. Bundesliga — EXPLORATORY SECOND TIER; Hertha leader 5 wins/5, Dresden 4 pts/5; external model X2 67.1%. Odds NULL.
Q DRE-HER Over 2.5 — 2. Bundesliga — market ~1.55; external models 62.7%-67%; league source avg 3.44 goals. Lennon p_model NULL.
R DRE-HER BTTS Yes — 2. Bundesliga — market ~1.42; external models 61.5%-67%. Lennon p_model NULL.
S SEV-BAR Barcelona win — LaLiga — market ~1.20-1.23; Barcelona 28 goals/6 and perfect league start; Sevilla 13 pts/6. Lennon p_model NULL.
T SEV-BAR Over 3.5 — LaLiga — market ~1.65-1.76; Barcelona attacking output extreme, but Sevilla recent defensive solidity is contradictory evidence. Lennon p_model NULL.
U SEV-BAR Barcelona over 4.5 team corners — LaLiga — ACTIVE_TRAINING CORNERS; Barcelona listed 6.5 corners/game vs Sevilla 3.6. Odds NULL.

## 20 frozen parlays
P01 A + E + J
P02 B + H + L
P03 C + F + O
P04 D + I + U
P05 K + P + G
P06 M + S + J
P07 N + Q + L
P08 A + R + O
P09 B + T + U
P10 C + E + G
P11 D + H + L
P12 F + M + J
P13 I + P + O
P14 K + Q + U
P15 N + S + G
P16 A + T + L
P17 B + R + J
P18 C + M + O
P19 D + Q + U
P20 H + N + G

## Portfolio audit
- 20 tickets, 60 slots.
- No ticket contains two legs from the same fixture.
- Corner legs: 20/60 = 33.3%, within experimental 25%-35% target.
- Corner families represented: Serie A, Bundesliga, Ligue 1, Ligue 2, LaLiga.
- Second-tier experimental exposure: Ligue 2 + 2. Bundesliga; no claim that second tiers are inherently high scoring.
- Concentration: most unique legs reused 2-4 times; no single leg dominates portfolio.
- No REAL bet created.

## Evidence snapshot
Fixtures: 19-Sep-2026 slate verified from same-day schedules. Key sources at freeze: Guardian/Yahoo for EPL team news; Oddschecker/Forebet for Celta-Racing; Predictobets for Roma-Inter, Stuttgart-Dortmund, Sevilla-Barcelona market snapshots; Fixture360/Forebet for Lyon-Rennes; Sport.fr/MatchPulse/FullTimeStats for Metz-Saint-Etienne; Fairoddsfootball/BILD/Fixture360 for Dresden-Hertha.

## Settlement protocol
Settle unique legs first, then P01-P20. Report by competition, market family and odds-availability band. Corner legs receive SCORE_STATE review. Ligue 2 and 2. Bundesliga goals hypotheses are analyzed separately. Do not compute official ROI for tickets containing NULL odds; diagnostic hit rate only. Do not retune parameters from one slate.