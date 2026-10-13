# LENNON PREDICTION-FIRST PROTOCOL V1

Effective: 2026-10-05
GitHub sync restored: 2026-10-13
Project: 1000→100000
Mode: SHADOW / PREDICTION-FIRST
Canonical operational records: Cerebro Portátil + MASTER BET LEDGER
REAL execution: forbidden unless Carlos gives explicit written authorization per ticket before kickoff.

## Primary learning unit
The primary predictive learning unit is a UNIQUE pre-match market forecast, not a parlay and not a repeated leg slot.

NO BET never means NO PREDICTION.

Every eligible same-day fixture with sufficient data should receive prospective model forecasts before kickoff, even when no positive edge exists, no SHADOW bet is created, and no parlay is built.

Parlays remain downstream portfolio stress-tests only.

## Required chronology
1. Read Cerebro Portátil and MASTER BET LEDGER.
2. Reconcile and settle prior forecasts/SHADOW where results are verifiable.
3. Fix a real America/Mexico_City cutoff BEFORE same-day research.
4. Identify eligible fixtures.
5. Execute only models that genuinely run.
6. Freeze p_model, features/provenance, timestamp and observed price when available.
7. Separate LENNON PURE, LENNON MARKET-AWARE, MARKET no-vig, EXTERNAL_MODEL_SIGNAL and CONTEXT.
8. Classify each prediction as FORECAST_ONLY, SHADOW_EDGE or REAL_CANDIDATE.
9. Settle prospectively frozen forecasts later.
10. Append learning; never rewrite a historical freeze.

## Engines
### CORE — Goals Engine
Target joint home/away scoring distribution and derive 1X2, double chance/DNB, Asian result handicaps, match O/U, BTTS and team totals.
Current experimental implementation in the Prediction Ledger: LENNON PURE Poisson-v0.1.

### SECONDARY — Corners Engine
Separate market-specific engine. Never infer corners from favoritism, possession or goal expectation alone. Prefer overdispersed count models when data support them.

### SECONDARY — Team Shots / SOT
Separate count/ML engine once reliable team-shot datasets and temporal coverage are available.

### EXPERIMENTAL — Cards
Do not promote until referee, team discipline and match-context features plus valid prices are available.

### RESEARCH ONLY
Player props, fouls, offsides, throw-ins and goal-kicks remain research-only until their data and price coverage are proven.

## Signal provenance
MODEL_SIGNAL means an actual executed Lennon model output.
EXTERNAL_MODEL_SIGNAL is a third-party probability/model.
MARKET is bookmaker/market information.
CONTEXT is injuries, suspensions, lineups, rest, travel, tactics, form, etc.
Never relabel external or implied probabilities as Lennon p_model.

## Validation
Use strict temporal / walk-forward evaluation.
Benchmark forecasts against no-vig market probability and closing price when available.
Report Brier score, log loss, calibration, MAE/RMSE and distributional calibration for count targets, CLV only with valid frozen prices, and SHADOW ROI only from genuinely frozen executable prices.
Segment by market family, league, odds band and provenance.
One session never promotes or retunes a model.

## SHADOW / REAL
SHADOW rules must be frozen prospectively before outcomes.
REAL remains fully separate and requires explicit written Carlos authorization for each ticket before kickoff.
This daily task never authorizes REAL.

## Portfolio layer
P01-P20 may be constructed only when portfolio quality/diversity permits. They are optional for predictive learning.
Retain SAME_DAY, BLOWOUT_TAIL, CORNER_SPECIFIC, PORTFOLIO_CONTAMINATION, FREEZE_QUALITY and PORTFOLIO_DAMAGE gates for portfolio tests.

## Storage and sync
Cerebro Portátil is the canonical learning record.
MASTER BET LEDGER stores betting/ticket decisions where applicable.
GitHub stores model/protocol artifacts, immutable freezes, settlements, audit files and periodic canonical snapshots.
After every GitHub write, verify by reading the resulting file/commit before claiming sync.