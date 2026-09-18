# LENNON — REAL CANDIDATES — 2026-09-18

Status: USER_REQUESTED_REAL_CANDIDATES / NOT_EXECUTED  
Track: MARKET_CONTEXT_ONLY  
MODEL_SIGNAL: NONE  
p_model: NULL  
Edge claim: NONE  
Objective: maximize estimated probability of cashing, not payout or expected value.

## Governance note
TEST 04 remains immutable as a SHADOW freeze. This file is a separate append-only record created because Carlos explicitly requested three REAL-money candidate parlays. These tickets are NOT model-validated Lennon production signals. Probabilities below are approximate no-vig market probabilities from contemporaneous Caliente prices, not p_model.

## Highest-probability candidate markets observed
1. Bayern Munich ML @1.04 — approx p_market no-vig 91.1%.
2. Puebla–Atlante Under 4.5 @1.133 — approx 83.5%.
3. FC Juárez–Tigres Under 4.5 @1.142 — approx 82.8%.
4. Monza–Sassuolo Under 4.5 @1.153 — approx 82.0%.
5. Espanyol–Elche Under 4.5 @1.166 — approx 81.1%.
6. Monaco–Lens Over 1.5 @1.181 — approx 80.1%.
7. Espanyol or Draw @1.20 — approx 79.3% from the 1X2 market.
8. Tigres or Draw @1.222 — approx 76.5% from the 1X2 market.
9. Bayern–Union Over 3.5 @1.25 — approx 76.0%.
10. Monza–Sassuolo Over 1.5 @1.25 — approx 75.7%.
11. Puebla–Atlante Over 1.5 @1.25 — approx 75.2%.
12. Monaco or Draw @1.285 — approx 73.8% from the 1X2 market.

## Three candidate REAL parlays
Designed as two-leg parlays because the stated objective is highest cash probability. No fixture is reused across the three tickets.

### R1 — Maximum probability
- Bayern Munich ML @1.04
- Monza–Sassuolo Under 4.5 @1.153
- Combined snapshot odds: ~1.199
- Approx joint market probability: ~74.7% assuming independence.

### R2 — Conservative
- FC Juárez–Tigres Under 4.5 @1.142
- Monaco–Lens Over 1.5 @1.181
- Combined snapshot odds: ~1.349
- Approx joint market probability: ~66.3% assuming independence.

### R3 — Conservative
- Espanyol or Draw @1.20
- Puebla–Atlante Under 4.5 @1.133
- Combined snapshot odds: ~1.360
- Approx joint market probability: ~66.2% assuming independence.

## Context audit
- Bayern: official club preview says the full squad is available; Union have multiple absences. The market heavily favors Bayern.
- Espanyol: Omar El Hilali is suspended and there are other availability questions, so the safer use is double chance rather than Espanyol ML.
- Lens changed coach days before the Monaco match. The ticket uses a broad goals threshold rather than requiring Monaco to win.
- Wide Under 4.5 lines remain exposed to blowout tails. V2.1 BLOWOUT_TAIL_GATE therefore remains active and these are not treated as certainties.

## Execution rule
NOT_EXECUTED until Carlos confirms an actual placed ticket and supplies the final odds/stake (or screenshot). Actual placement must be logged separately from this candidate record.

## Public market sources
- Caliente Puebla vs Atlante, 18-Sep-2026.
- Caliente FC Juárez vs Tigres UANL, 18-Sep-2026.
- Caliente Espanyol vs Elche, 18-Sep-2026.
- Caliente AS Monaco vs RC Lens, 18-Sep-2026.
- Caliente Monza vs Sassuolo, 18-Sep-2026.
- Caliente Bayern Munich vs Union Berlin, 18-Sep-2026.
