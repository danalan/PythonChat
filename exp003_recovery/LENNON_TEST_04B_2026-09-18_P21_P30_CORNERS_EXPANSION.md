# LENNON TEST 04B — 2026-09-18 — P21-P30 PROSPECTIVE ADDENDUM

Status: FROZEN_MARKET_CONTEXT_SHADOW_ADDENDUM
Local cutoff: 2026-09-18 14:40:54 -06:00
Timezone: America/Mexico_City
Purpose: extend the already-frozen P01-P20 daily training set to the newly authorized 30-parlay cadence without altering the original morning freeze.
MODEL_SIGNAL: NONE
p_model: NULL
Edge claim: NONE
Accounting: 10 additional parlays x MXN25 SIM = MXN250 additional simulated exposure.
Daily total after addendum: 30 parlays, MXN750 SIM.
All P21-P30 fixtures were scheduled later than this addendum cutoff.

## Corner-learning design
- Exactly one CORNERS leg per addendum ticket.
- 10/30 addendum leg slots are CORNERS = 33.3%.
- Corner exposure is ACTIVE_TRAINING / MARKET-CONTEXT, not REAL_ELIGIBLE.
- No ticket combines a corner leg with another leg from that same fixture.
- No corner leg is reused more than twice.
- The original P01-P20 freeze is untouched.

## Frozen leg registry

### Central Cordoba vs Defensa y Justicia
- A1 Under 3.5 goals @1.181
- A2 1H Under 1.5 goals @1.285
- A3 Defensa y Justicia or Draw @1.42

### Racing Club vs Sarmiento
- R1 Over 1.5 goals @1.444
- R2 Racing Club or Draw @1.125
- R3 Under 3.5 goals @1.20

### New York City vs New York Red Bulls
- N1 Over 1.5 goals @1.142
- N3 Corners Over 7, 3-way @1.333 [CORNERS / ACTIVE_TRAINING]
- N4 Corners Over 8, 3-way @1.55 [CORNERS / ACTIVE_TRAINING]
- N5 Corners Under 11, 3-way @1.45 [CORNERS / ACTIVE_TRAINING]
- N6 New York City first to 3 corners @1.615 [CORNERS / ACTIVE_TRAINING]

### Puebla vs Atlante
- P1 Under 4.5 goals @1.133

### FC Juarez vs Tigres UANL
- J1 Tigres UANL or Draw @1.222
- J2 Under 4.5 goals @1.133
- J3 Corners Over 8, 3-way @1.333 [CORNERS / ACTIVE_TRAINING]
- J4 Corners Over 9, 3-way @1.571 [CORNERS / ACTIVE_TRAINING]

## P21-P30 frozen portfolio

| Ticket | Legs | Approx snapshot odds |
|---|---|---:|
| P21 | N3 + A1 + R1 | 2.273 |
| P22 | N3 + A2 + J1 | 2.093 |
| P23 | N4 + A3 + P1 | 2.494 |
| P24 | N4 + R2 + J2 | 1.976 |
| P25 | N5 + A1 + R3 | 2.055 |
| P26 | N5 + A2 + J2 | 2.111 |
| P27 | J3 + A3 + N1 | 2.162 |
| P28 | J3 + R1 + P1 | 2.181 |
| P29 | J4 + R2 + N1 | 2.018 |
| P30 | N6 + R3 + J1 | 2.368 |

## Source/provenance notes
- Caliente contemporaneous pages supplied the Central Cordoba, Racing, NYCFC, Juarez/Tigres prices used above.
- Puebla Under 4.5 @1.133 and Tigres/Draw @1.222 were also independently visible in the user-confirmed Caliente slip around the cutoff.
- Same-day schedule was rechecked before freeze for Central Cordoba, NYCFC, Puebla and Tigres. Racing Club vs Sarmiento was confirmed by the Caliente event page and the user slip.
- Because this is MARKET_CONTEXT_SHADOW, market prices are not p_model.

## Settlement
Settle unique legs first, then P21-P30. Report corner-family performance separately from goals/result families. Preserve SCORE_STATE, SOURCE_QUALITY, SELECTION and PORTFOLIO flags. Do not retune quantitative corner parameters from this one slate.
