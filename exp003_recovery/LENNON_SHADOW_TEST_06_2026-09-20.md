# LENNON SHADOW TEST 06 — 2026-09-20

## Governance freeze
- CUTOFF: 2026-09-20 15:36 CDMX. Research and ticket construction occur only after this timestamp was fixed.
- Mode: SHADOW/SIM only. 20 parlays x MXN25 SIM = MXN500 simulated exposure. NO REAL MONEY authorized.
- Upcoming verified Liga MX slate after cutoff is unusually thin: Toluca–Santos (18:00 CDMX) and Querétaro–León (20:10 CDMX; some feeds round to 20:00). Most major European Sunday matches had already started/finished; club football is entering an unusual international break. Rather than backfill with already-started games, TEST06 is explicitly LOW_DIVERSITY.
- MODEL_SIGNAL is reserved for probabilities from named executed/public models (Dimers, PoissonFC, ProfeGol). These are EXTERNAL model signals, not LENNON p_model. LENNON internal p_model was NOT executed in this run.
- Market prices are contemporaneous published snapshots, not claimed Caliente prices unless explicitly named. Sources: Oddschecker, Legalbet, SportsGambler, FOX, Squawka/Kalshi. Price drift is possible.

## Research Ledger — unique candidates, frozen before results

TOL-ML | Toluca ML | MARKET 1.22–1.25; MODEL_SIGNAL Dimers 78.2%, PoissonFC 87%, ProfeGol 70%, Squawka Signal 73%. Data: Toluca 19 pts/8, 18:6; Santos 4 pts/8, 6:13; Santos lost all four away league matches. Contradiction: market raw implied at 1.25=80%, so Dimers/ProfeGol do NOT show edge; only PoissonFC clears. Chosen as portfolio anchor, not assumed value. Rejected alternative: Santos upset due extreme low model support.
TOL-1.5 | Toluca -1.5 | MARKET ~1.70 (Legalbet). CONTEXT: Toluca 2.43 goals/game; recent 4-0 Juárez, 5-2 Atlas; Santos weak away. Contradiction: no clean named probability for -1.5; Golista estimates win by 2+ only 39%. EXPERIMENTAL/MARKET, not p_model. Included to test handicap family.
TOL-O2.5 | Match Over 2.5 | MARKET around 1.34–1.57 depending source/snapshot; MODEL_SIGNAL PoissonFC 77%, ProfeGol 71%, Squawka/Kalshi 70%. Contradiction: Dimers most likely scores include 2-0; TipMan gives only 57%. Included for goals-family disagreement test.
TOL-O3.5 | Match Over 3.5 | MARKET ~1.83–2.00. MODEL_SIGNAL ProfeGol 49.8%; MARKET roughly 50%. Contradiction substantial; LOW-EVIDENCE. Included only as controlled experimental high line.
TOL-BTTS-Y | BTTS Yes | MARKET ~1.61. MODEL_SIGNAL Dimers 53.6%, ProfeGol 61%, PoissonFC 49%, Squawka/Kalshi 56%. Contradiction high; market implies 62.1% raw, so no obvious model edge. Included as calibration test, not value claim.
TOL-U3.5 | Under 3.5 | MARKET ~1.82–1.88. MODEL_SIGNAL ProfeGol 50.2%; market near coin flip. Contradiction: attacking/home trend points Over. LOW-EVIDENCE counter-thesis.
TOL-C-O8.5 | Over 8.5 corners | EXPERIMENTAL. TipMan projects 13.4 total corners and 88% 8.5+; no contemporaneous verified bookmaker price captured. Included only in experimental tickets; price=N/A, excluded from price/P&L quality claims until price obtained.
TOL-C-O9.5 | Over 9.5 corners | EXPERIMENTAL. TipMan 82% 9.5+; same price limitation. Tests corner threshold sensitivity.

QRO-DNB | Querétaro DNB | MARKET ~1.72–1.75. SportsGambler bet-builder uses Querétaro 0.0 +108 in its snapshot, while Legalbet has 1.75. MODEL_SIGNAL conflict: Dimers QRO 33.7/D 25.4/LEO 40.9; PredictNext QRO 40/D26/LEO34. Reason: test market/model disagreement. Contradiction is central, not hidden.
LEO-X2 | León or draw | MARKET ~1.50. MODEL_SIGNAL Dimers gives X2 66.3%; raw implied 66.7%, essentially fair before vig. Included as protection benchmark, not edge.
QRO-U2.5 | Under 2.5 goals | MARKET ~1.76–2.10 depending book; SportsGambler bet-builder recommends Under 2.5 +110. MODEL_SIGNAL PredictNext 56% Under; TipMan 52% Under. Contradiction: BetClan 58% Over and market often leans Over. Included for disagreement test.
QRO-BTTS-Y | BTTS Yes | MARKET ~1.60. MODEL_SIGNAL Dimers 56%, TipMan 54%, BetClan 63%. Raw implied 62.5%; only BetClan roughly supports price. LOW-EVIDENCE/value-negative candidate retained for calibration.
QRO-U3.5 | Under 3.5 goals | MARKET ~1.45. Context/model distribution strongly favors avoiding 4+; PredictNext central 1-1/1-2; SportsGambler prefers U2.5. No named exact probability frozen. MARKET/CONTEXT.
QRO-C-U10.5 | Under 10.5 corners | MARKET -114 (~1.88) SportsGambler. SportsGambler: five straight León away matches below line; León away total corners avg 9.2. Contradiction: Querétaro home total avg 12.0. EXPERIMENTAL corner family, but priced.
QRO-C-O8.5 | Over 8.5 corners | EXPERIMENTAL. TipMan: 8.5 corners/match and 60% 8.5+; no clean current price frozen. Directly conflicts with U10.5 only if total lands outside 9–10; used to test middle corridor.
QRO-C-O9.5 | Over 9.5 corners | EXPERIMENTAL. TipMan 54% 9.5+; no clean current price frozen. Low evidence.
QRO-CARDS-O4.5 | Over 4.5 cards | EXPERIMENTAL. TipMan projects 6.4 cards/match; team card averages QRO 3.4, León 2.3. No verified current price captured, so excluded from price-edge claims.
QRO-CARDS-O5.5 | Over 5.5 cards | EXPERIMENTAL. Same 6.4 baseline; no verified price. Higher-variance threshold test.
LEO+1.5 | León +1.5 | MARKET ~1.17 (Legalbet). Protection line; low price is not called safe. Included specifically for odds-band audit.
QRO+1.5 | Querétaro +1.5 | MARKET ~1.13. Same purpose: low-odds tail-risk audit.

## Candidate ordering before ticket construction
A: TOL-ML, TOL-O2.5, QRO-C-U10.5, QRO-U3.5, LEO-X2.
B: TOL-1.5, QRO-DNB, QRO-U2.5, TOL-BTTS-Y, LEO+1.5, QRO+1.5.
C/EXPERIMENTAL: TOL-O3.5, TOL-U3.5, TOL-C-O8.5, TOL-C-O9.5, QRO-BTTS-Y, QRO-C-O8.5, QRO-C-O9.5, QRO-CARDS-O4.5, QRO-CARDS-O5.5.

## Portfolio Ledger — exactly 20 x 3
P01 TOL-ML / QRO-C-U10.5 / QRO-U3.5
P02 TOL-O2.5 / LEO-X2 / QRO-C-U10.5
P03 TOL-1.5 / QRO-U2.5 / QRO-C-U10.5
P04 TOL-ML / QRO-DNB / QRO-U3.5
P05 TOL-O2.5 / LEO+1.5 / QRO-C-U10.5
P06 TOL-BTTS-Y / QRO-U2.5 / QRO+1.5
P07 TOL-ML / QRO-BTTS-Y / QRO-C-U10.5
P08 TOL-1.5 / LEO-X2 / QRO-U3.5
P09 TOL-O2.5 / QRO-DNB / QRO-C-O8.5
P10 TOL-U3.5 / LEO-X2 / QRO-C-U10.5
P11 TOL-C-O8.5 / QRO-U2.5 / LEO+1.5
P12 TOL-C-O9.5 / QRO-U3.5 / QRO+1.5
P13 TOL-O3.5 / QRO-CARDS-O4.5 / LEO-X2
P14 TOL-ML / QRO-CARDS-O5.5 / QRO-U3.5
P15 TOL-BTTS-Y / QRO-C-O8.5 / LEO+1.5
P16 TOL-1.5 / QRO-C-O9.5 / QRO+1.5
P17 TOL-O2.5 / QRO-CARDS-O4.5 / QRO-DNB
P18 TOL-C-O8.5 / QRO-BTTS-Y / QRO-U2.5
P19 TOL-C-O9.5 / QRO-CARDS-O5.5 / LEO-X2
P20 TOL-O3.5 / QRO-C-O9.5 / QRO-DNB

## Concentration audit
- 60 slots are NOT 60 independent observations. Only 20 unique legs across 2 fixtures.
- Fixture exposure is necessarily extreme: every ticket touches both fixtures and at least one fixture contributes 2 legs. This FAILS the normal PORTFOLIO_DAMAGE_GATE and is explicitly tagged LOW_DIVERSITY / CONCENTRATION_STRESS_TEST.
- Reuse is visible: TOL-ML 4; TOL-O2.5 4; TOL-1.5 3; TOL-BTTS-Y 3; TOL-O3.5 2; TOL-U3.5 1; TOL-C-O8.5 2; TOL-C-O9.5 2. QRO-C-U10.5 6; QRO-U3.5 6; LEO-X2 5; QRO-U2.5 4; QRO-DNB 4; LEO+1.5 3; QRO+1.5 3; QRO-BTTS-Y 2; QRO-C-O8.5 2; QRO-C-O9.5 2; QRO-CARDS-O4.5 2; QRO-CARDS-O5.5 2.
- Highest concentration: QRO-C-U10.5 and QRO-U3.5 each kill 30% of tickets if they fail. This sits exactly at the 6/20 ceiling, but fixture-level damage is far above it because slate breadth is only two games.
- Correlation warning: same-game totals/corners/cards are not assumed independent. Portfolio P&L will be descriptive only; predictive training uses unique legs.

## Settlement protocol
After final results: settle each unique leg once; classify failure MODEL/EVIDENCE/CONTEXT/PRICE/SELECTION/PORTFOLIO/VARIANCE; then settle 20 tickets at MXN25 SIM each. Track family n/hit-rate vs implied, Brier/log loss only where genuine probabilities were frozen, odds bands, SIM P&L only for legs/tickets with captured prices, and CLV only where a closing quote is obtainable. No retuning from TEST06 alone.

## Fiscal packet
Question for audit: given only two eligible Liga MX fixtures after cutoff, was it better to (a) run exactly 20 as a declared concentration stress test, or (b) violate the user's exact-20 instruction? TEST06 chooses (a) while refusing to pretend the portfolio is diversified. Audit focus: duplicated thesis risk, unpriced experimental legs, and whether low-odds protection legs add information or merely cosmetically increase hit rate.
