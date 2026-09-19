# LENNON TEST 04 — PARTIAL SETTLEMENT — 2026-09-18 19:00 CDMX

Status: PARTIAL / NOT FINAL
Parent: LENNON_TEST_04_2026-09-18_MARKET_CONTEXT_FREEZE.md

Completed fixtures at checkpoint:
- Espanyol 1-3 Elche
- Monaco 2-1 Lens
- Monza 2-1 Sassuolo
- Bayern Munich 7-0 Union Berlin

Pending fixtures:
- Puebla vs Atlante
- FC Juárez vs Tigres UANL

Resolved unique legs so far: 21
- WIN: 15
- LOSS: 6
- Hit rate: 71.43%

By fixture:
- Espanyol–Elche: 2/5
- Monaco–Lens: 6/6
- Monza–Sassuolo: 3/5
- Bayern–Union: 4/5

Resolved tickets so far:
- WON: P03 only
- LOST: P01, P02, P06, P09, P10, P12, P14, P15, P18, P19
- Still live/pending: P04, P05, P07, P08, P11, P13, P16, P17, P20

Accounting at checkpoint (MXN25 SIM per ticket):
- Settled tickets: 11
- Settled stake: MXN275
- Return: MXN59.875
- Realized P&L: -MXN215.125
- Remaining open exposure: MXN225

Diagnostics:
- MODEL_SIGNAL was NONE for TEST 04, so this checkpoint does not score Vn model quality.
- Portfolio amplification is visible: 6 losing unique legs have already killed 10 of 11 settled tickets.
- Espanyol cluster is the main selection/context weakness so far: C1, C3, C5 lost.
- Bayern 7-0 triggered the intended blowout-tail lesson: F3 Under 6.5 lost while F1/F2/F4/F5 won.
- Monaco cluster was perfect at 6/6.
- Do not retune from this partial session. Final settlement waits for both Liga MX matches.
