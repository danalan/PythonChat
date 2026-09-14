# Apertura 2025 Execution Policy V2.1 — Windowed MXN 100 Risk Budget

Effective: Apertura 2025 J1 historical replay
Status: ACTIVE GOVERNANCE
Historical money: SIMULATED/PAPER only
Supersedes: V2 staking amount / window handling only. All integrity, calibration, context and price-quality rules remain.

## 1. Weekly/jornada budget

- Primary historical economic track starts Apertura 2025 with the carried simulated bankroll from Clausura: MXN 443.43.
- There is NO external weekly deposit. MXN 100 is a risk budget/cap drawn from the existing simulated bankroll.
- At the start of each jornada, `weekly_risk_budget = min(MXN 100, opening bankroll)`.
- Cumulative stakes placed across all windows of that jornada may not exceed the starting weekly risk budget.
- Returns/winnings from an earlier window do NOT replenish or expand the same jornada's risk budget.
- Losses from an earlier window do NOT authorize chasing or adding capital.
- Unused budget from an earlier window may be used in a later window of the SAME jornada.
- Unused budget at jornada end stays as cash in bankroll; it is not a failure and is not added to next jornada's MXN 100 cap.
- At least one wager must be placed every jornada while bankroll > 0.

## 2. Time windows

- Build/freeze wagers by natural kickoff windows (normally Friday / Saturday / Sunday, or other actual schedule blocks).
- Before each window's first kickoff: freeze model probabilities, prices available by that time, context tags and stake for that window.
- Later windows may use genuinely new pre-kickoff information such as confirmed lineups or market movement.
- Earlier realized results may update bankroll accounting but may NOT alter model parameters, calibration candidate or context-feature definitions inside the same jornada.
- Later-window stake may be lower for risk control, but never increased beyond remaining predeclared weekly budget because of earlier wins or losses.

## 3. Portfolio hierarchy

PRIMARY = singles.
SECONDARY = 2-leg parlays using different fixtures; diagnostic/limited stake.
SHADOW ONLY = 3+ leg parlays for continuity/research, no primary bankroll allocation.

- Prefer one primary single per fixture to reduce hidden concentration.
- A 2-leg parlay should normally use <=5% of the MXN 100 weekly cap per ticket during this first Apertura validation phase.
- Total 2-leg parlay stake should normally remain <=20% of weekly risk budget.
- No same-game correlated parlays unless explicitly modeled and classified as diagnostic.

## 4. Price and selection

- Exact archived target-market prices (Class A/B) are preferred for primary economic stakes.
- MARKET_PROXY_V1 Class C is diagnostic and may not be the sole reason for a primary stake.
- Raw V0.1R remains the production comparator for J1; `CAL_SHRINK_GLOBAL_V0_1` remains shadow only and may not alter primary selection or stake until its preregistered checkpoint.
- For outcome-exposed historical jornadas, human context may be logged but cannot alter mechanical selection or promote features.

## 5. Parallel counterfactual

Track A (primary): windowed MXN 100 risk-budget policy above.
Track B (counterfactual only): prior dynamic bankroll rule using up to 10% of bankroll.

No additional simulated money is required for Track B. It is calculated in parallel so the tournament can compare a fixed practical weekly budget with bankroll-proportional sizing.
