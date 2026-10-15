# LENNON prospective freeze — 15 Oct 2026

Run: LENNON-2026-10-15-PREDICTION-FIRST. Pre-research cutoff: **2026-10-15 08:26:06 CDMX**. All freezes 08:29–08:31 CDMX, before earliest 10:45 kickoff. **PAPER ONLY; REAL=0; SHADOW=0**.

Engine actually calculated: `LENNON-PURE-GOALS-POISSON-V0.1-JS-REPRO`, same deterministic independent-Poisson math as `LENNON_PURE_GOALS_POISSON_REPRO_V0_1.mjs`. Features: FootyStats last 10 matches across competitions (mixed); distinct from earlier domestic-season inputs. xG/xGA overall, no strength-of-league adjustment, no model retune. Outputs 1X2, DC, DNB, Asian home -1, O/U2.5, BTTS, team O/U1.5.

17/18 Europa League fixtures frozen; Sparta Praha–Lillestrøm omitted because Sparta xG/xGA could not be independently extracted. EFL League One Mansfield–Oxford and global leagues not fully screened. FootyStats displayed 1X2 prices have **unknown bookmaker and publication timestamp**: stored as aggregator MARKET diagnostic, not validated executable prices. No validated edge, no CLV/ROI, no SHADOW. All forecasts classified FORECAST_ONLY.

| Fixture | Kickoff CDMX | λH/λA | P(1/X/2) | P(O2.5) | P(BTTS) | Aggregator 1/X/2 |
|---|---|---|---|---|---|---|
| UEL-AZ-HBS | 10:45 | 1.870/1.405 | 48.5/22.5/29.0 | 63.6 | 63.8 | 1.3/5.6/8.5 |
| UEL-CEL-OMO | 10:45 | 1.360/1.595 | 32.6/24.3/43.0 | 56.7 | 59.3 | 2.4/3.35/2.53 |
| UEL-LEC-B04 | 10:45 | 1.570/1.570 | 38.2/23.7/38.2 | 60.7 | 62.7 | 4.6/4.33/1.62 |
| UEL-LYO-CRY | 10:45 | 1.750/1.315 | 47.7/23.4/28.9 | 59.1 | 60.4 | 2.2/3.55/3.05 |
| UEL-SAL-MIL | 10:45 | 1.565/1.340 | 42.7/24.6/32.7 | 55.5 | 58.4 | 3.1/3.7/1.99 |
| UEL-TOR-SUN | 10:45 | 1.240/1.590 | 29.8/24.7/45.5 | 53.8 | 56.6 | 8/4.8/1.4 |
| UEL-USG-RSO | 10:45 | 1.930/1.460 | 48.7/22.1/29.3 | 65.8 | 65.6 | 2.45/3.6/2.65 |
| UEL-JAG-AVA | 13:00 | 1.385/1.700 | 31.4/23.6/45.0 | 59.6 | 61.3 | 1.4/5/7.25 |
| UEL-BOU-STU | 13:00 | 1.585/1.525 | 39.4/23.8/36.8 | 60.1 | 62.2 | 1.1/7.5/11 |
| UEL-HOF-BES | 13:00 | 1.535/1.635 | 36.1/23.5/40.4 | 61.4 | 63.2 | 1.95/3.85/3.41 |
| UEL-NEC-LEV | 13:00 | 1.265/1.500 | 32.0/25.3/42.7 | 52.2 | 55.8 | 1.85/3.9/3.8 |
| UEL-BEN-CELT | 13:00 | 1.890/1.440 | 48.2/22.3/29.5 | 64.7 | 64.8 | 1.24/6/10 |
| UEL-CELTA-JUV | 13:00 | 1.140/1.625 | 26.7/24.6/48.6 | 52.2 | 54.6 | 3.3/3.25/2.15 |
| UEL-REN-OFI | 13:00 | 1.725/1.395 | 45.4/23.4/31.2 | 60.3 | 61.8 | 1.22/6.75/12 |
| UEL-FER-PLZ | 13:00 | 1.705/1.575 | 41.2/23.1/35.7 | 63.7 | 64.9 | 1.9/3.8/3.45 |
| UEL-DIN-AND | 13:00 | 1.585/1.380 | 42.4/24.3/33.3 | 56.9 | 59.5 | 2/3.5/3.6 |
| UEL-MAR-OLY | 13:00 | 1.270/1.805 | 27.0/23.1/50.0 | 59.3 | 60.1 | 2.35/3.61/3 |

Full-precision probabilities, xG features, individual source URLs, market no-vig, diagnostic differences and per-fixture freeze timestamps are verified in Cerebro Portátil `LENNON Prediction Ledger!A173:AE189`. Historical 14-Oct settlements in rows 164–172. Do not retrofreeze or call aggregator disagreements edge. Corners, Team Shots/SOT and Cards were NOT executed.
