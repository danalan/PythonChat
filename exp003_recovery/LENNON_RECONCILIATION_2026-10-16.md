# LENNON reconciliation — 16 Oct 2026 (settlement of 15 Oct)

Original 17 pre-kickoff forecasts: CP `LENNON Prediction Ledger!A173:AE189`, freeze 2026-10-15 08:29–08:31 CDMX. Append-only settlement: CP `A191:AE207`, readback verified. **No retrofreeze.**

Results: UEFA official 2026/27 Europa League Matchday 2: https://www.uefa.com/uefaeuropaleague/news/02a8-2174cafa5bb6-82bbc20c9b92-1000--2026-27-europa-league-all-the-league-phase-fixtures-and-re/

| Original forecast | Final | Top 1X2 hit | Brier 1X2 | Log loss |
|---|---|---|---:|---:|
| LEN15-UEL-AZ-HBS | 2-1 | ✓ | 0.3999 | 0.7235 |
| LEN15-UEL-CEL-OMO | 0-3 | ✓ | 0.4903 | 0.8433 |
| LEN15-UEL-LEC-B04 | 0-4 | ✗ | 0.5841 | 0.9634 |
| LEN15-UEL-LYO-CRY | 3-2 | ✓ | 0.4118 | 0.7402 |
| LEN15-UEL-SAL-MIL | 0-4 | ✗ | 0.6958 | 1.1178 |
| LEN15-UEL-TOR-SUN | 1-2 | ✓ | 0.4466 | 0.7872 |
| LEN15-UEL-USG-RSO | 1-1 | ✗ | 0.9298 | 1.5110 |
| LEN15-UEL-JAG-AVA | 3-1 | ✗ | 0.7292 | 1.1589 |
| LEN15-UEL-BOU-STU | 3-0 | ✓ | 0.5593 | 0.9314 |
| LEN15-UEL-HOF-BES | 2-3 | ✓ | 0.5410 | 0.9067 |
| LEN15-UEL-NEC-LEV | 1-1 | ✗ | 0.8435 | 1.3758 |
| LEN15-UEL-BEN-CELT | 4-1 | ✓ | 0.4049 | 0.7297 |
| LEN15-UEL-CELTA-JUV | 1-2 | ✓ | 0.3958 | 0.7206 |
| LEN15-UEL-REN-OFI | 2-1 | ✓ | 0.4504 | 0.7899 |
| LEN15-UEL-FER-PLZ | 2-1 | ✓ | 0.5263 | 0.8863 |
| LEN15-UEL-DIN-AND | 1-0 | ✓ | 0.5024 | 0.8589 |
| LEN15-UEL-MAR-OLY | 0-1 | ✓ | 0.3761 | 0.6936 |

**17 unique forecasts; top 1X2 12/17; multiclass Brier 0.546313; log loss 0.925778; Over 2.5 Brier 0.208826; BTTS Brier 0.227167; mean absolute goals error per team 0.941029; goals RMSE per team 1.150724.**

Notes: independent Poisson on unadjusted xG/xGA; no validated same-bookmaker time-stamped odds; no ROI/CLV. 17 matches contain large mismatches and a few strong results; no model retune on one day. 0 prior SHADOW tickets associated with these 17, 0 REAL. Master BET LEDGER unchanged, since no new tickets/decisions. Results in CP settlement notes preserve original provenance.