# LENNON TEST 04 — 2026-09-18 — MARKET/CONTEXT SHADOW FREEZE

Status: FROZEN_MARKET_CONTEXT_SHADOW  
Local date: 2026-09-18  
Timezone: America/Mexico_City  
Portfolio freeze: 2026-09-18 10:17:50 -06:00  
Odds observation window: same morning before portfolio freeze; Caliente pages crawled 2026-09-18  
Accounting: 20 parlays x MXN25 SIM = MXN500 simulated exposure  
Legs per parlay: 3  
Predictive learning units: 32 unique legs  
MODEL_SIGNAL: NONE for this test  
p_model: NULL  
Edge claim: NONE  
REAL execution: NONE implied or authorized

## Why MODEL_SIGNAL is withheld

External market information was observed before a clean model-only freeze for this daily cycle. Therefore this test cannot honestly be labeled MODEL_SIGNAL. It trains market selection, context audit, tail-risk discipline and portfolio construction only. Market-implied probability must not be relabeled p_model.

## V2.1 controls applied

- SAME_DAY_GATE: PASS. Only 18-Sep fixtures admitted.
- BLOWOUT_TAIL_GATE: active for totals and BTTS.
- CORNER_SPECIFIC_GATE: active. Two corner legs remain one-shot EXPERIMENTAL probes only.
- PORTFOLIO_CONTAMINATION_GATE: active.
  - maximum normal reuse = 2 tickets per unique leg;
  - EXPERIMENTAL reuse = 1 ticket;
  - no repeated leg-pair across tickets;
  - no two legs from the same fixture in one ticket;
  - maximum one EXPERIMENTAL leg per ticket.
- FREEZE_QUALITY_GATE: odds below are frozen as the observed SHADOW snapshot. p_model and edge remain blank because no legitimate clean model forecast exists for this cycle.

## Rejected candidate worth preserving

NYCFC ML was rejected from the training universe despite an attractive market price because the official New York Red Bulls status report listed multiple NYCFC absences, including Maxi Moralez, Keaton Parks, Kai Trewin, Talles Magno, Drew Baiera and Arnau Farnós. This is a CONTEXT_CONFLICT rejection, not a forecast that NYCFC will lose.

## Leg registry

| ID | Fixture | Selection | Odds | Provenance / flag |
|---|---|---:|---:|---|
| A1 | Puebla–Atlante | Over 1.5 goals | 1.25 | MARKET |
| A2 | Puebla–Atlante | Under 3.5 goals | 1.38 | MARKET / TAIL_AUDIT |
| A3 | Puebla–Atlante | BTTS Yes | 1.65 | MARKET / TAIL_AUDIT |
| A4 | Puebla–Atlante | Corners Over 8, 3-way | 1.50 | EXPERIMENTAL / SCORE_STATE |
| A5 | Puebla–Atlante | Puebla or Draw | 1.333 | MARKET |
| A6 | Puebla–Atlante | 1H Under 1.5 goals | 1.48 | MARKET / single-use diversification |
| B1 | Juárez–Tigres | Tigres or Draw | 1.25 | MARKET / CONTEXT |
| B2 | Juárez–Tigres | Over 1.5 goals | 1.25 | MARKET |
| B3 | Juárez–Tigres | Under 3.5 goals | 1.38 | MARKET / TAIL_AUDIT |
| B4 | Juárez–Tigres | BTTS Yes | 1.70 | MARKET / TAIL_AUDIT |
| B5 | Juárez–Tigres | Tigres ML | 1.85 | MARKET / higher-variance result leg |
| C1 | Espanyol–Elche | Espanyol or Draw | 1.20 | MARKET |
| C2 | Espanyol–Elche | Over 1.5 goals | 1.25 | MARKET |
| C3 | Espanyol–Elche | Under 3.5 goals | 1.42 | MARKET / TAIL_AUDIT |
| C4 | Espanyol–Elche | BTTS Yes | 1.65 | MARKET / TAIL_AUDIT |
| C5 | Espanyol–Elche | 1H Under 1.5 goals | 1.48 | MARKET |
| D1 | Monaco–Lens | Monaco or Draw | 1.285 | MARKET |
| D2 | Monaco–Lens | Over 1.5 goals | 1.20 | MARKET |
| D3 | Monaco–Lens | Under 3.5 goals | 1.533 | MARKET / TAIL_AUDIT |
| D4 | Monaco–Lens | BTTS Yes | 1.50 | MARKET / TAIL_AUDIT |
| D5 | Monaco–Lens | Over 2.5 goals | 1.60 | MARKET |
| D6 | Monaco–Lens | Under 4.5 goals | 1.20 | MARKET / single-use diversification |
| E1 | Monza–Sassuolo | Sassuolo or Draw | 1.444 | MARKET |
| E2 | Monza–Sassuolo | Over 1.5 goals | 1.25 | MARKET |
| E3 | Monza–Sassuolo | Under 3.5 goals | 1.42 | MARKET / TAIL_AUDIT |
| E4 | Monza–Sassuolo | BTTS Yes | 1.571 | MARKET / TAIL_AUDIT |
| E5 | Monza–Sassuolo | Under 2.5 goals | 2.05 | MARKET / higher variance |
| F1 | Bayern–Union | Bayern ML | 1.04 | MARKET / LOW_ODDS_SAFETY_TEST |
| F2 | Bayern–Union | Over 3.5 goals | 1.25 | MARKET / TAIL_AUDIT |
| F3 | Bayern–Union | Under 6.5 goals | 1.30 | MARKET / TAIL_AUDIT |
| F4 | Bayern–Union | Corners Over 9, 3-way | 1.40 | EXPERIMENTAL / SCORE_STATE |
| F5 | Bayern–Union | 1H Over 1.5 goals | 1.363 | MARKET |

## Frozen 20-ticket portfolio

| Ticket | Legs | Combined proposed/frozen snapshot odds |
|---|---|---:|
| P01 | A1 + C5 + F3 | 2.405 |
| P02 | B2 + C1 + D5 | 2.400 |
| P03 | C2 + D3 + E2 | 2.395 |
| P04 | B1 + D2 + E4 | 2.357 |
| P05 | A2 + D1 + F5 | 2.417 |
| P06 | B3 + C3 + E1 | 2.830 |
| P07 | A5 + B4 + E3 | 3.218 |
| P08 | A3 + C4 + F2 | 3.403 |
| P09 | B5 + D4 + E5 | 5.689 |
| P10 | C5 + D4 + F1 | 2.309 |
| P11 | A6 + D6 + F5 | 2.421 |
| P12 | C3 + D1 + F2 | 2.281 |
| P13 | A2 + B3 + E2 | 2.380 |
| P14 | B1 + E3 + F3 | 2.308 |
| P15 | D5 + E1 + F1 | 2.403 |
| P16 | A5 + B2 + D3 | 2.554 |
| P17 | A1 + B4 + C2 | 2.656 |
| P18 | C4 + D2 + E5 | 4.059 |
| P19 | A4 + C1 + E4 | 2.828 |
| P20 | A3 + B5 + F4 | 4.273 |

## Exposure audit

- Total leg slots: 60.
- Unique legs: 32.
- A4 and F4 EXPERIMENTAL corner probes appear exactly once.
- A6 and D6 appear once as deliberate diversification legs.
- Every other admitted leg appears exactly twice.
- No ticket contains two legs from the same fixture.
- No pair of legs is repeated across the 20 tickets.
- No ticket contains more than one EXPERIMENTAL leg.

## Settlement rules

After all matches finish:
1. Settle each unique leg first.
2. Label misses with MODEL / EVIDENCE / CONTEXT / PRICE / SELECTION / PORTFOLIO / VARIANCE / CALENDAR-DATASET plus V2.1 subflags TAIL_BLOWOUT, SCORE_STATE and PORTFOLIO_AMPLIFICATION where applicable.
3. Then settle 20 tickets.
4. Record official SHADOW P&L only against the frozen odds above, preserving any voids.
5. Do not alter the pre-match rationale after results.
6. Do not retune numerical model parameters from this one daily cycle.
7. Compare TEST 04 to TEST 03V primarily at unique-leg level and portfolio amplification, not raw parlay hit rate alone.

## Public source set used at freeze

- Caliente: Puebla vs Atlante, Liga MX, 18-Sep-2026.
- Caliente: FC Juárez vs Tigres UANL, Liga MX, 18-Sep-2026.
- Caliente: Espanyol vs Elche, La Liga, 18-Sep-2026.
- Caliente: AS Monaco vs RC Lens, Ligue 1, 18-Sep-2026.
- Caliente: Monza vs Sassuolo, Serie A, 18-Sep-2026.
- Caliente: Bayern Munich vs Union Berlin, Bundesliga, 18-Sep-2026.
- New York Red Bulls official status report, 18-Sep-2026, used only for the NYCFC ML rejection.

This file contains no private account details, screenshots, Drive IDs or credentials.
