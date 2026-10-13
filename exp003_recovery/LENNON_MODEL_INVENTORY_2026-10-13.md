# LENNON MODEL INVENTORY — 2026-10-13

Purpose: verified inventory of executable/model artifacts found after GitHub access was restored. This file distinguishes code that actually exists from architecture that is only described.

## 1) Vn-2026-DC-ENSEMBLE — EXISTS / EXECUTABLE HISTORY
File: `exp003_recovery/vn2026_forward.py`
Blob SHA: `8607cde1b74114e90ced2603ca74160d13940809`

Verified characteristics:
- Mathematical parent: `V0.1R_RECOVERED` Dixon-Coles ensemble.
- Data bridge: OpenFootball through 2024-25 plus FotMob 2025-26 and 2026-27.
- Current code is explicitly Liga MX (`LEAGUE_ID=230`, `LEAGUE_SLUG=liga-mx`).
- Mandatory caller-supplied cutoff; rejects rows at/after cutoff.
- Canonical America/Mexico_City time normalization.
- Deterministic source precedence and fixture deduplication.
- SHA-256 hash of normalized training snapshot in output.
- Produces a joint score matrix and derives 1X2, double chance, BTTS, match totals and team totals.

Implication: this is a real historical Lennon goal/result engine and should be evaluated/reused for supported Liga MX work before inventing another unrelated implementation. It does NOT by itself justify applying its probabilities to other leagues.

## 2) C0.1-CORNERS-NB-ENSEMBLE — EXISTS / SHADOW ONLY
File: `exp003_recovery/corner_shadow_v0_1.py`
Blob SHA: `2fe6414bb447bade41e91d2c68636b57d5138811`

Verified characteristics:
- Separate corner process; it cannot mutate Vn goal-model parameters.
- Negative Binomial count model for overdispersed corner counts.
- Fits team corner attack, corner defense, intercept, home-corner advantage and shared dispersion k.
- Ensemble half-lives: 180 / 365 / 730 / 1460 days.
- Derives total-corner O/U, team-corner O/U and corner 3-way probabilities.
- Explicitly SHADOW_ONLY and not REAL staking eligible.

Test file: `exp003_recovery/test_corner_shadow.py` (`af5049127b9c2027d89ef41b2fe7288d75f062e6`). Tests matrix normalization, market complements, cutoff handling and FotMob corner parsing.

Implication: the current Prediction-First roadmap should reuse/audit this existing engine instead of treating Corners Engine as nonexistent.

## 3) DUAL TRACK GOVERNANCE — EXISTS / EXECUTABLE GOVERNANCE
File: `exp003_recovery/dual_track_governance.py`
Blob SHA: `863922d7a659ba9833473bad2d52fce40b0c2fbd`
Governance version: `DTL-1.2`.

Verified gates include:
- provisional forward distinct-match floor: 125 for calibration changes, 400 for architecture changes;
- minimum 75 distinct matches for CLV evidence;
- minimum calibration bucket n=20 with Wilson 95% interval consistency;
- REAL_USER_OVERRIDE structurally excluded from model-promotion evidence;
- shadow drawdown limit 20%;
- drift monitor using rolling log-loss/Brier, currently logging-only because thresholds are not historically calibrated;
- required preregistered rationale, version diff, data snapshot hash, canary plan and zero open leakage findings before promotion.

Implication: do not casually promote Poisson-v0.1, corner models or future market engines from a few daily sessions. The repository already contains stricter promotion logic.

## 4) ECONOMIC_SELECTOR_V1 — EXISTS / HISTORICAL MECHANICAL SELECTOR
File: `exp003_recovery/economic_selector_v1.py`
Blob SHA: `770e024260520c817f2d62012cc627fa8f8783fd`

Verified characteristics:
- Mechanical model-plus-pre-cutoff-price selection; cannot consume narrative context or outcomes.
- Uses a frozen model probability surface and frozen price snapshot.
- Computes market disagreement and model EV at a proxy price.
- Historical support interval hard-coded to [0.60, 0.8224852071005917].
- Designed for a specific 3x3 EXP-003 economic track, not the current daily Prediction-First workflow.

Implication: useful as leakage-resistant selection logic and historical evidence, but it should not be silently reused as the current SHADOW selector without an explicit architecture decision.

## 5) Current Prediction-First daily engine — RECENT OPERATIONAL STATE
Canonical recent ledger identifies `LENNON-PURE-POISSON-V0.1` as the model used for October daily forecasts.
This implementation is represented in the Prediction Ledger and local prospective freeze artifacts, but a matching current source-code module was NOT identified in the GitHub inventory during this restoration pass.

Known diagnostic: cross-league domestic xG without strength adjustment appears to create false underdog inflation. That remains a hypothesis/diagnostic, not a promoted parameter change.

## 6) Reconciliation rule going forward
- For Liga MX goal/result work, evaluate the existing Vn-2026 Dixon-Coles implementation alongside any newer Goals Engine rather than assuming the October Poisson baseline supersedes it.
- For corners, evaluate C0.1-CORNERS-NB-ENSEMBLE prospectively before designing a replacement.
- Preserve current Prediction-First daily forecasts as prospective evidence.
- Any new model version must have source code committed, versioned inputs, cutoff enforcement and immutable output/freeze artifacts.
- CP remains canonical learning record; MASTER remains canonical ticket/decision ledger; GitHub is the executable/model/artifact mirror.
- Never call a model 'executed' unless its code or reproducible output actually ran for the target fixture/market.