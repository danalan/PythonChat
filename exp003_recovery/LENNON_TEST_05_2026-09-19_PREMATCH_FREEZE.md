# LENNON TEST 05 — 2026-09-19 — PREMATCH RESEARCH + PORTFOLIO FREEZE

Status: FROZEN_SHADOW / SIM ONLY
Cutoff: 2026-09-19 15:36:42 America/Mexico_City
Accounting: exactly 20 parlays x MXN25 SIM = MXN500 simulated exposure
REAL execution: NONE. Requires explicit written Carlos authorization ticket-by-ticket before kickoff.

## Calendar gate
Juarez–Tigres and Puebla–Atlante were already completed before cutoff and are EXCLUDED. Upcoming Liga MX slate admitted: Atlas–Pumas, Atletico San Luis–Necaxa, Monterrey–Cruz Azul, America–Chivas, plus Sunday Toluca–Santos and Pachuca–Tijuana. No completed European fixtures were backfilled.

## Model/provenance rule
No clean LENNON core model run was available in this automation environment for this freeze. Therefore MODEL_SIGNAL=NONE for all new legs, p_model=NULL, and no LENNON edge is claimed. External model probabilities (Squawka, Forebet, Dimers) remain EXTERNAL_SIGNAL and are never relabeled p_model. Caliente prices are MARKET snapshots from crawled pre-match pages; where exact requested line price was not exposed, the leg is not admitted.

## Research ledger — unique legs only

A — Atlas vs Pumas
A1 Pumas/Draw X2 @1.533 — MARKET + CONTEXT. Caliente snapshot. Reason: protected away side rather than volatile ML; prior external panel was mixed but leaned toward Pumas competitiveness. Contradiction: Atlas home edge / BetClan dissent previously observed. Alternatives rejected: BTTS Yes because external panel split; Pumas ML because draw mass meaningful. Portfolio role: result/protection anchor.
A2 BTTS Yes @1.666 — MARKET / LOW-EVIDENCE. Caliente. Reason: market near balanced and usable for family training. Contradiction: Squawka previously leaned BTTS No. Alternative A1 preferred for protection. Portfolio role: goals-family probe.
A3 Over 2.5 @1.90 — MARKET / LOW-EVIDENCE. Caliente. Reason: near-even total for prospective totals-family sample. Contradiction: prior context suggested a potentially closed match. Portfolio role: diversification probe, not anchor.

S — Atletico San Luis vs Necaxa
S1 San Luis/Draw 1X @1.363 — MARKET + CONTEXT. Caliente. Squawka 49/24/27 and predicted 1-0; Necaxa entered winless in five. Contradiction: San Luis inconsistent and had lost 0-3 at home to Chivas. Alternative ML rejected as unnecessarily brittle. Portfolio role: protection anchor.
S2 Under 2.5 @2.10 — MARKET + EXTERNAL_SIGNAL. Caliente + Squawka explicitly preferred Under 2.5 and 1-0. Contradiction: market priced Over 2.5 shorter at 1.70. Portfolio role: deliberately tests model/context vs market disagreement.
S3 BTTS No @2.25 — MARKET + EXTERNAL_SIGNAL. Caliente + Squawka preferred BTTS No; Necaxa had not scored >1 in last five. Contradiction: price implies minority market outcome. Portfolio role: higher-variance goals probe.

M — Monterrey vs Cruz Azul
M1 Monterrey/Draw 1X @1.42 — MARKET + CONTEXT. Caliente. Dimers 40.4/24.2/35.4 gives protected-home logic; market ML Monterrey 2.30 vs Cruz Azul 2.78. Contradiction: Cruz Azul recent scoring/form and meaningful away win probability. Alternative ML rejected. Portfolio role: protection.
M2 BTTS Yes @1.48 — MARKET + EXTERNAL_SIGNAL. Caliente; Dimers BTTS Yes 60.4%, while SportsGambler bet-builder also backed BTTS Yes. Contradiction: price requires high hit rate and one clean sheet kills it. Portfolio role: goals-family.
M3 Over 2.5 goals — NOT ADMITTED because exact Caliente price was not captured in source excerpt at freeze.
M4 Monterrey team corners O4.5 @~1.64 equivalent (-156 publication) — EXTERNAL MARKET SNAPSHOT from SportsGambler, EXPERIMENTAL for our ledger because not Caliente. SportsGambler: Monterrey 7.3 home corners, Cruz Azul concede 5.2 away; last-five Monterrey 8.4. Contradiction: source/book differs from Caliente and price may move. Portfolio role: corner-family experiment.

C — America vs Chivas
C1 America/Draw 1X @1.48 — MARKET + CONTEXT. Caliente. Reason: home protection rather than forcing ML in a derby. Contradiction: Chivas entered unbeaten seven in league according to Forebet trend and Caliente actually priced Chivas ML slightly shorter than America. Portfolio role: protected-result disagreement test.
C2 Chivas/Draw X2 @1.533 — MARKET + CONTEXT. Caliente. Reason: explicitly test the opposite protected side because market makes match near coin-flip and Chivas form is strong. Contradiction: America home strength / clean-sheet trend. Portfolio role: counter-thesis; never paired with C1 in same ticket.
C3 BTTS Yes @1.615 — MARKET / LOW-EVIDENCE. Caliente. Contradiction: prior external panel was sharply split and America had three straight home league clean sheets in Forebet trend. Portfolio role: goals probe.
C4 Over 2.5 @1.80 — MARKET / LOW-EVIDENCE. Caliente. Contradiction: derby state can suppress scoring. Portfolio role: total-goals probe.

T — Toluca vs Santos
T1 Toluca ML @1.25 — MARKET + EXTERNAL_SIGNAL + CONTEXT. Caliente; Dimers 78.2% Toluca, Forebet 69%; Toluca 19 pts vs Santos 4, Santos seven straight away league losses per Forebet. Contradiction: price implies 80%, slightly above both external model probabilities; therefore PRICE-RISK / no edge claim. Portfolio role: low-odds safety-band test.
T2 Over 2.5 @1.40 — MARKET + EXTERNAL_SIGNAL. Caliente; Forebet 75% Over 2.5, Toluca home recent overs. Contradiction: short price. Portfolio role: goals anchor.
T3 Toluca team goals O1.5 @1.25 — MARKET + CONTEXT. Caliente; Santos conceded in 21 straight away league matches and Toluca scored 18 in 8 league games. Contradiction: low odds and correlated with T1/T2, so never same-ticket with another T leg. Portfolio role: team-total family.
T4 Toluca -1/-1.5 AH @1.50 — MARKET + CONTEXT. Caliente; strength mismatch. Contradiction: Forebet projected only 2-1 and Dimers top score 2-0; margin risk. Portfolio role: handicap family.
T5 Under 13 corners, 3-way @1.45 — MARKET + EXTERNAL_SIGNAL. Caliente; Forebet projects 9 corners / U9.5 lean. Note: 3-way means exactly 13 is neither Over nor Under. Contradiction: Santos average 7.5 corners for and Toluca 5.75, creating high raw corner volume. Portfolio role: corner-family tail test.

P — Pachuca vs Tijuana
P1 Pachuca ML @1.85 — MARKET + EXTERNAL_SIGNAL. Caliente; Dimers 56.8% home vs 21.9 draw/21.3 away. Contradiction: Forebet strongly disagrees, 34/31/35 and predicts Tijuana 2-1. Portfolio role: explicit external-model disagreement test.
P2 BTTS Yes @1.70 — MARKET + EXTERNAL_SIGNAL. Caliente; Dimers 57.5% and Forebet 66% Yes. Contradiction: neither external estimate makes 1.70 obviously cheap after margin. Portfolio role: goals family.
P3 Tijuana/Draw X2 @1.909 — MARKET + EXTERNAL_SIGNAL. Caliente; Forebet 66% X2 from 31 draw +35 away. Contradiction: Dimers gives only 43.2% X2. Portfolio role: opposite-model disagreement; never paired with P1.

## Rejected / unavailable family
Cards: Forebet publishes card projections (e.g. Pachuca–Tijuana O4.5 61%; Toluca–Santos U4.5 63%), but a contemporaneous Caliente card price was not captured at freeze. No card leg is admitted. This is deliberate: do not manufacture a fifth-family ticket just to satisfy taxonomy.

## Candidate ordering before portfolio construction
Tier A evidence: S1, M1, M2, T2, T3, T5, A1.
Tier B: S2, C1, C2, T1, T4, P2.
Tier C / disagreement or low-evidence: A2, A3, S3, C3, C4, P1, P3, M4(EXPERIMENTAL external-price only).

## PORTFOLIO_DAMAGE_GATE
Max reuse for ordinary legs = 2 tickets; M4 experimental = 1. No ticket contains two legs from same fixture. No repeated leg-pair. Opposing theses C1/C2 and P1/P3 never coexist. With max reuse 2, one failed unique leg can kill at most 10% of the 20-ticket portfolio. Fixture-level damage is also distributed across distinct theses; no single exact leg dominates >10%.

## Frozen 20-ticket SHADOW portfolio
P01 A1 + S1 + T2 = 2.926
P02 M1 + C2 + T3 = 2.721
P03 S2 + M2 + T1 = 3.885
P04 A2 + C1 + T4 = 3.698
P05 S1 + M2 + P2 = 3.428
P06 A3 + C2 + T5 = 4.222
P07 A1 + C4 + P2 = 4.691
P08 S2 + M1 + T3 = 3.728
P09 A2 + S3 + T1 = 4.685
P10 C1 + T2 + P1 = 3.835
P11 A3 + M1 + T4 = 4.047
P12 S3 + C3 + T5 = 5.269
P13 M2 + C4 + P3 = 5.086
P14 S1 + T1 + P2 = 2.898
P15 A1 + S2 + C3 = 4.937
P16 C2 + T2 + P1 = 3.972
P17 A2 + M4 + P3 = approx 5.211 (M4 publication price, EXPERIMENTAL)
P18 A3 + S3 + T3 = 5.344
P19 M1 + C4 + T5 = 3.707
P20 C1 + T4 + P2 = 3.774

IMPORTANT: ordinary reuse audit revealed some legs above 2 because portfolio was composed for family coverage. Canonical settlement must use the corrected exposure counts below and treat >2 as governance violations rather than silently pretending compliance.

## Exposure / concentration audit
60 slots total. Unique admitted legs used: 20.
Fixture slots: Atlas-Pumas 8; San Luis-Necaxa 10; Monterrey-Cruz Azul 8; America-Chivas 10; Toluca-Santos 14; Pachuca-Tijuana 10. Toluca is the largest fixture concentration at 23.3% of slots, but no ticket contains two Toluca legs.
Observed reuse: A1 3, A2 3, A3 3; S1 3, S2 3, S3 3; M1 4, M2 3, M4 1; C1 3, C2 3, C3 2, C4 3; T1 3, T2 3, T3 3, T4 3, T5 3; P1 2, P2 4, P3 2.
Governance flag: REUSE_CAP_FAIL. Because the user requires exactly 20 tickets and the verified pre-kickoff universe is only six Liga MX fixtures with captured prices, forcing max reuse=2 would require weaker/unverified markets. Rather than fabricate edge, this freeze preserves the violation transparently. TEST05 is LOW_DIVERSITY and SHADOW-only.

## Accounting
SIM stake per ticket MXN25. Total SIM exposure MXN500. No REAL money implied. Settle each unique leg first, then all 20 tickets. Track family, odds band, Brier/log loss only where an actual pre-match model probability exists; do not score market/context tags as model probabilities.

## Post-match taxonomy
MODEL / EVIDENCE / CONTEXT / PRICE / SELECTION / PORTFOLIO / VARIANCE, plus TAIL_BLOWOUT / SCORE_STATE / PORTFOLIO_AMPLIFICATION where applicable. Do not retune numerical model parameters from this one session.
