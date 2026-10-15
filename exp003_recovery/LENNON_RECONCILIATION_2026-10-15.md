# LENNON reconciliation — 2026-10-15

Settled **9** original 14-Oct Champions League prospective forecasts, append-only in CP `LENNON Prediction Ledger!A164:AE172`. Original 14-Oct freeze CP rows 154–162 unchanged. Official results: https://www.uefa.com/uefachampionsleague/news/02a8-2174c9e9019d-f909a77bd77a-1000--2026-27-champions-league-all-the-league-phase-fixtures-a/

| Original fixture | Final | Status |
|---|---|---|
| 2026-10-14|UCL-FEY-COM | 3-2 | SETTLED_FORECAST_ONLY |
| 2026-10-14|UCL-LASK-LIV | 3-6 | SETTLED_FORECAST_ONLY |
| 2026-10-14|UCL-ROM-RMA | 3-4 | SETTLED_FORECAST_ONLY |
| 2026-10-14|UCL-AVL-FEN | 6-0 | SETTLED_FORECAST_ONLY |
| 2026-10-14|UCL-SHA-AEK | 3-1 | SETTLED_FORECAST_ONLY |
| 2026-10-14|UCL-BOG-BVB | 1-0 | SETTLED_FORECAST_ONLY |
| 2026-10-14|UCL-MCI-PSG | 2-4 | SETTLED_FORECAST_ONLY |
| 2026-10-14|UCL-BET-POR | 3-2 | SETTLED_FORECAST_ONLY |
| 2026-10-14|UCL-SLO-STU | 0-3 | SETTLED_FORECAST_ONLY |

14-Oct n=9: top-1X2 correct 4/9, multiclass Brier 0.635058, log loss 1.033670, O2.5 Brier 0.171287, BTTS Brier 0.226708, goal-count MAE 1.645278 and RMSE 2.059089 (per team). All 14-Oct FORECAST_ONLY; no SHADOW/REAL to settle.

Cumulative n=64 unique probabilistic forecasts (prior 55 + 9): top 31/64, Brier 0.652078, log loss 1.077243, O2.5 Brier 0.234576, BTTS Brier 0.228962, goal MAE 1.115430 and RMSE 1.406723. Prior paired 08-Oct market no-vig n=5: market Brier 0.446919 vs Lennon 0.616772, tiny sample. Historical 24 SHADOW settled: 5 wins, 19 losses, -115 MXN simulated on 600 MXN diagnostic staked; quoted odds timestamps not independently validated, so no validated ROI or CLV.

No model retuning on a single session. Separate cross-league strength bias and feature provenance (domestic-season vs mixed last10) before interpreting new scores. Master tickets untouched: no 14-Oct SHADOW or REAL, and no 15-Oct new ticket. 15-Oct forecast mirror: `LENNON_FREEZE_2026-10-15_PREDICTION_FIRST.md`.
