# LENNON reconciliation 2026-10-14

Verified append-only settlements in Cerebro Portátil, `LENNON Prediction Ledger!A133:AE153`. Original forecast and ticket freezes remain unchanged. 09-Oct backlog: 7 fixture outcomes and 5 SHADOW settlements; 13-Oct: 9 UCL outcomes. Master Decision Log D031 readback confirmed; original T023-T027 remain as frozen historical rows. REAL=0.

|Settlement ID|Original fixture/ticket|Outcome|Status/PnL|
|---|---|---|---|
|LEN14-SET09-01|2026-10-09|MEX|PUE-LEO|1-1|SETTLED_FORECAST_ONLY|
|LEN14-SET09-02|2026-10-09|MEX|TIG-TOL|3-2|SETTLED_FORECAST_ONLY|
|LEN14-SET09-03|2026-10-09|GER|BVB-WER|2-2|SETTLED_FORECAST_ONLY|
|LEN14-SET09-04|2026-10-09|ESP|MAL-ESP|1-1|SETTLED_FORECAST_ONLY|
|LEN14-SET09-05|2026-10-09|FRA|LEN-LYO|2-1|SETTLED_FORECAST_ONLY|
|LEN14-SET09-06|2026-10-09|POR|BRA-SPO|1-3|SETTLED_FORECAST_ONLY|
|LEN14-SET09-07|2026-10-09|POR|MOR-GIL|0-1|SETTLED_FORECAST_ONLY|
|LEN14-SET09-S1|2026-10-09|GER|BVB-WER / DRAW|2-2|WIN +112.50 SIM|
|LEN14-SET09-S2|2026-10-09|GER|BVB-WER / Werder ML|2-2|LOSS -25.00 SIM|
|LEN14-SET09-S3|2026-10-09|ESP|MAL-ESP / Espanyol ML|1-1|LOSS -25.00 SIM|
|LEN14-SET09-S4|2026-10-09|POR|BRA-SPO / Braga ML|1-3|LOSS -25.00 SIM|
|LEN14-SET09-S5|2026-10-09|POR|MOR-GIL / Gil Vicente ML|0-1|WIN +28.75 SIM|
|LEN14-SET13-01|2026-10-13|UCL-LEN-SPO|0-2|SETTLED_FORECAST_ONLY|
|LEN14-SET13-02|2026-10-13|UCL-SAB-SLA|2-0|SETTLED_FORECAST_ONLY|
|LEN14-SET13-03|2026-10-13|UCL-ARS-LIL|3-0|SETTLED_FORECAST_ONLY|
|LEN14-SET13-04|2026-10-13|UCL-ATM-MUN|2-0|SETTLED_FORECAST_ONLY|
|LEN14-SET13-05|2026-10-13|UCL-GAL-BAR|1-4|SETTLED_FORECAST_ONLY|
|LEN14-SET13-06|2026-10-13|UCL-INT-BRU|3-4|SETTLED_FORECAST_ONLY|
|LEN14-SET13-07|2026-10-13|UCL-RBL-PSV|1-0|SETTLED_FORECAST_ONLY|
|LEN14-SET13-08|2026-10-13|UCL-VIK-BAY|3-3|SETTLED_FORECAST_ONLY|
|LEN14-SET13-09|2026-10-13|UCL-VIL-NAP|3-1|SETTLED_FORECAST_ONLY|

09-Oct 5 SHADOW: 2 wins / 3 losses, +66.25 MXN SIM on 125 simulated stake; odds origin lacks independently verified timestamp, so PnL is DIAGNOSTIC, not validated ROI/CLV. Historical tally previously 19 settled singles (3W/16L, -181.25/475 SIM); after this reconciliation 24 settled singles (5W/19L, -115.00/600 SIM), subject to historical reconciliation.

Verified unique probabilistic forecast metrics from CP, 55 settled with frozen p (08,09,10,11,12,13 Oct): top 1X2 27/55, Brier 0.654864, log loss 1.084373, O2.5 Brier 0.244932, BTTS Brier 0.229331, goal count MAE 1.028727, RMSE 1.268421. 07-Oct 3 historical settlements and 06-Oct missing full p snapshots excluded from these metrics. Matched market no-vig comparison only for 08-Oct n=5: model Brier 0.616772 vs market 0.446919, model log loss 1.040981 vs market 0.783472. Do NOT generalize from tiny sample. No valid CLV due missing closing odds.

13-Oct UCL n=9: top 5/9, Brier 0.618982, log loss 1.016003, O2.5 Brier 0.241498, BTTS Brier 0.266458, goal MAE 1.213056, RMSE 1.356403. 09-Oct n=7: top 3/7, Brier 0.677933, log loss 1.125221.

Sources: individual links in CP settlement rows; match results independently checked before settlement. No retrofreeze; no parameter change based on this one day. 14-Oct prospective 9-fixture freeze is in `LENNON_FREEZE_2026-10-14_PREDICTION_FIRST.md`.
