# LENNON TEST 07 — 2026-09-22 — PRE-MATCH FREEZE

Status: FROZEN_SHADOW / SIMULATED ONLY
Formal cutoff: 2026-09-22T04:07:45+06:00 (captured after slate identification and before candidate research)
Stake unit: MXN25 SIM per ticket
Tickets: exactly 20 x 3 legs = 60 portfolio slots
Total SIM exposure: MXN500
REAL exposure: MXN0
Governance: REAL requires explicit written Carlos authorization, ticket-by-ticket, before kickoff.

## Slate verification
No Liga MX fixture was found in the usable 22-Sep slate. Priority therefore moved to UEFA Women's Champions League, EFL Trophy, Scottish Challenge Cup, with controlled KNVB Beker / Colombia exploration. EFL Trophy and UWCL fixtures/1X2 prices were independently visible in current bookmaker/odds-comparison pages. The slate contains substantially more youth/reserve/cup uncertainty than a normal top-flight board; that is recorded as CONTEXT_RISK rather than hidden.

## Probability nomenclature
- No internal LENNON core model was executed for this freeze. Therefore p_model LENNON = NULL for every leg.
- MODEL_SIGNAL means a named external algorithm/model actually published a probability/pick.
- MARKET means bookmaker price / implied probability only.
- CONTEXT means non-model pre-match evidence.
- EXPERIMENTAL means family coverage without sufficient price/model maturity; it is not eligible for edge claims.

## Research Ledger — 30 unique legs (each counted once)

L01 | Walsall-Stevenage | DRAW @3.30 | FAMILY result | MODEL_SIGNAL: Forebet draw 38%; WinComparator draw 45.63%. MARKET implied 30.30%. Reason: model disagreement with market creates diagnostic value. Contradiction: Stevenage market favourite ~2.2. Rejected: Stevenage ML because model panel is materially split. Portfolio role: high-variance model-v-market probe.
L02 | Walsall-Stevenage | Under 2.5 @1.70 | FAMILY goals | MODEL_SIGNAL: Forebet Under 54%; WinComparator Under 57.01%. MARKET implied 58.82%. Reason: lower-score consensus but price is not proven value. Contradiction: market alternatives show O2.5 around 2.0. Rejected: BTTS No because its external probability/price edge is similarly marginal. Role: calibration probe, LOW_EDGE.
L03 | Luton-Ipswich U21 | Luton ML @1.25 | FAMILY result | MARKET implied 80.0%; no trusted external model probability frozen. Context: senior side vs U21 but cup rotation risk. Rejected: 1.20 early-payout variant because semantics differ. Role: LOW_ODDS_BAND audit; LOW_EVIDENCE.
L04 | Luton-Ipswich U21 | Over 2.5 @1.20 | FAMILY goals | MARKET implied 83.33%; price verified. Context: youth/reserve cup environment. Contradiction: no independent calibrated probability captured. Rejected: O3.5 @1.57 because higher tail. Role: LOW_ODDS_BAND / goals audit; LOW_EVIDENCE.
L05 | Accrington-Sunderland U21 | Accrington ML @1.72 | FAMILY result | MARKET implied 58.14%. No p_model. Contradiction: reserve-team variance. Rejected: Sunderland ML @3.70. Role: cup senior-v-youth market probe; LOW_EVIDENCE.
L06 | York-Rotherham | York ML @2.05 | FAMILY result | MARKET implied 48.78%. No validated model probability. Contradiction: Rotherham higher-tier pedigree may matter. Rejected: Rotherham ML @3.15 because market prefers York. Role: mid-odds band probe; LOW_EVIDENCE.
L07 | Rochdale-Liverpool U21 | Rochdale ML @1.97 | FAMILY result | MARKET implied 50.76%. Context: senior side vs U21; youth variance remains. Rejected: Liverpool U21 ML @3.20. Role: senior-v-youth probe; LOW_EVIDENCE.
L08 | Notts County-Grimsby | Notts County ML @2.12 | FAMILY result | MARKET implied 47.17%. No external probability frozen. Contradiction: relatively balanced 1X2. Rejected: draw/Grimsby because no stronger signal. Role: balanced-price diagnostic; LOW_EVIDENCE.
L09 | Crewe-Aston Villa U21 | Crewe ML @1.48 | FAMILY result | MARKET implied 67.57%. Context: senior-v-U21 structural advantage, but rotation uncertainty. Rejected: Villa U21 @5.20. Role: 1.40-1.59 odds-band audit; LOW_EVIDENCE.
L10 | Tranmere-Shrewsbury | Tranmere ML @2.08 | FAMILY result | MARKET implied 48.08%. Balanced game; no external calibrated probability. Rejected: Shrewsbury @3.40. Role: mid-price selection audit; LOW_EVIDENCE.
L11 | MK Dons-Crawley | MK Dons ML @1.68 | FAMILY result | MARKET implied 59.52%. Context: Crawley currently bottom of League Two and only one win from seven reported in current press. Contradiction: cup rotation. Rejected: Crawley @4.10. Role: MARKET+CONTEXT candidate.
L12 | Peterborough-Colchester | Peterborough ML @1.92 | FAMILY result | MARKET implied 52.08%. No external probability frozen. Rejected: Colchester @3.22. Role: mid-odds market probe; LOW_EVIDENCE.
L13 | Swindon-Newport | Over 7.5 corners | FAMILY corners | EXPERIMENTAL. External corner model/tip publishes O7.5 with 82% signal; Swindon corner profile baseline ~10.0 recent combined. ODDS_UNVERIFIED at freeze, therefore no edge/P&L-quality claim. Contradiction: small recent sample. Rejected: inventing a price. Role: CORNER_SPECIFIC_GATE learning only.
L14 | Walsall-Stevenage | Under 4.5 cards | FAMILY cards | EXPERIMENTAL. Forebet card model publishes Under 4.5 at 71% and projected 1-2 cards. ODDS_UNVERIFIED. Contradiction: cup officiating/lineup uncertainty. Rejected: any fabricated bookmaker price. Role: cards-family prospecting only.
L15 | Bayern Women-Man City Women | Bayern ML @2.02 | FAMILY result | MODEL_SIGNAL: Sports Mole Bayern 54.65%, fair ~1.83; MARKET implied 49.50%. Context: City entered with six straight wins per Sports Mole; contradiction is meaningful. Rejected: City ML ~2.95. Role: external-model vs market test.
L16 | Bayern Women-Man City Women | Under 3.5 @1.65 | FAMILY goals | MODEL_SIGNAL Sports Mole Under3.5 63.48%, fair ~1.575; MARKET implied 60.61%. Contradiction: both are elite attacking teams and opening-round volatility. Rejected: O2.5 because price not captured in same source. Role: totals model-price probe.
L17 | Juventus Women-Benfica Women | Juventus ML @1.79 | FAMILY result | MARKET implied 55.87%. No trusted model probability frozen. Contradiction: continental opener uncertainty. Rejected Benfica @3.75. Role: familiar competition / mid-band probe; LOW_EVIDENCE.
L18 | Real Madrid Women-PSG Women | Real Madrid ML @1.80 | FAMILY result | MARKET implied 55.56%. No trusted model probability frozen. Contradiction: PSG quality. Rejected PSG ~3.8. Role: familiar competition / mid-band probe; LOW_EVIDENCE.
L19 | Inter Women-Hacken Women | Inter ML @2.27 | FAMILY result | MARKET implied 44.05%. Market relatively balanced. Rejected Hacken @2.90 because no stronger signal. Role: high-uncertainty UWCL diagnostic; LOW_EVIDENCE.
L20 | Gala Fairydean-Spartans | Spartans ML @1.14 | FAMILY result | MARKET implied 87.72%; WinDrawWin predicts Spartans away win, 46% on its displayed 1X2 probability, a severe probability/price inconsistency. Reason INCLUDED specifically to audit why low odds must not be called safe. Rejected as REAL candidate. Role: LOW_ODDS_BAND stress test / CONTRADICT_HIGH.
L21 | Bonnyrigg-Airdrie | Airdrie ML @1.88 | FAMILY result | MARKET implied 53.19%; form display 2.00 vs 2.00. No p_model. Rejected home @3.50. Role: Scottish cup exploration; LOW_EVIDENCE.
L22 | Forfar-Peterhead | Peterhead ML @1.75 | FAMILY result | MARKET implied 57.14%; form display 0.50 vs 3.00 supports away side contextually. Rejected home @3.75. Role: MARKET+CONTEXT.
L23 | Stirling-Cumbernauld | Stirling ML @1.48 | FAMILY result | MARKET implied 67.57%; form display 3.00 vs 0.33 supports home. Rejected away @5.56. Role: MARKET+CONTEXT / odds-band audit.
L24 | Clachnacuddin-Ross County | Ross County ML @1.15 | FAMILY result | MARKET implied 86.96%; form 1.00 vs2.00. No calibrated model. Role: LOW_ODDS_BAND audit, not safety claim.
L25 | Fraserburgh-Cove Rangers | Cove ML @1.37 | FAMILY result | MARKET implied 72.99%; form 0.33 vs2.00 supports away. Role: MARKET+CONTEXT.
L26 | Formartine-Montrose | Montrose ML @1.57 | FAMILY result | MARKET implied 63.69%; form 1.50 vs3.00 supports away. Role: MARKET+CONTEXT.
L27 | East Kilbride-Celtic II | East Kilbride ML @1.25 | FAMILY result | MARKET implied 80.0%; form 3.00 vs2.33. Contradiction: reserve-side variance. Role: LOW_ODDS_BAND audit.
L28 | Queen of the South-Annan | Queen of the South ML @2.00 | FAMILY result | MARKET implied 50.0%; form 2.33 vs1.33. Role: MARKET+CONTEXT.
L29 | Koninklijke HFC-Dovo | Koninklijke HFC ML @1.625 (5/8) | FAMILY result | MODEL_SIGNAL ScorelineAI home 56% (fair ~1.79); MARKET implied 61.54%, so model does NOT clear price. TACTIX free pick is Home-or-Away rather than home win, adding contradiction. Included as negative-edge diagnostic, not value. Rejected: calling it a pass. Role: PRICE failure training.
L30 | Santa Fe-Deportivo Cali | Santa Fe AH -0.25 @1.741 (-135) | FAMILY handicap | MARKET only. Moneyline +108 and away +270 show modest home lean; AH protects half stake on draw. No p_model. Rejected: Santa Fe ML because AH better trains protection family. Role: handicap/protection probe; LOW_EVIDENCE.

## Portfolio Ledger — exactly 20 x 3
Each unique leg is used exactly twice. Thus 60 slots = 30 unique predictive observations x2 portfolio exposures. Reuse = 2/20 tickets (10%) per leg; no leg exceeds V2.1 reuse cap. No ticket contains two legs from the same fixture. No repeated leg pair.

P01: L01 + L03 + L05 | MXN25 SIM
P02: L02 + L04 + L06 | MXN25 SIM
P03: L07 + L08 + L09 | MXN25 SIM
P04: L10 + L11 + L12 | MXN25 SIM
P05: L13 + L14 + L15 | MXN25 SIM | EXPERIMENTAL_PRICE_INCOMPLETE
P06: L16 + L17 + L18 | MXN25 SIM
P07: L19 + L20 + L21 | MXN25 SIM
P08: L22 + L23 + L24 | MXN25 SIM
P09: L25 + L26 + L27 | MXN25 SIM
P10: L28 + L29 + L30 | MXN25 SIM
P11: L01 + L08 + L17 | MXN25 SIM
P12: L02 + L09 + L18 | MXN25 SIM
P13: L03 + L10 + L19 | MXN25 SIM
P14: L04 + L11 + L20 | MXN25 SIM
P15: L05 + L12 + L21 | MXN25 SIM
P16: L06 + L13 + L22 | MXN25 SIM | EXPERIMENTAL_PRICE_INCOMPLETE
P17: L07 + L14 + L23 | MXN25 SIM | EXPERIMENTAL_PRICE_INCOMPLETE
P18: L15 + L24 + L28 | MXN25 SIM
P19: L16 + L25 + L29 | MXN25 SIM
P20: L26 + L27 + L30 | MXN25 SIM

## Concentration / correlation audit
- Max leg reuse: 2 tickets = PASS.
- Same-fixture double-leg within a ticket: 0 = PASS.
- Repeated leg-pair: 0 = PASS.
- EFL Trophy exposure is intentionally large because it is the deepest verified same-day slate; flag COMPETITION_CONCENTRATION.
- Youth/reserve fixtures create a shared ROTATION_UNCERTAINTY failure mode; flag PORTFOLIO_DAMAGE_RISK even though individual legs are diversified.
- L13/L14 are EXPERIMENTAL and price-incomplete. They may train family-specific hit-rate/evidence quality but cannot produce valid price-edge, CLV or ticket P&L claims until a contemporaneous equivalent price is captured. Tickets containing them are excluded from headline P&L.

## Odds-band audit buckets
1.01-1.29: L03,L04,L20,L24,L27
1.30-1.49: L09,L23,L25
1.50-1.69: L11,L16,L26,L29
1.70-1.99: L05,L07,L12,L17,L18,L21,L22,L30
2.00-2.49: L01,L06,L08,L10,L15,L19,L28
Unpriced: L13,L14

## Family audit plan
Result/protection: n unique, hit rate vs raw implied; Brier/log loss only where an actual external probability was frozen; SIM P&L and CLV when closing equivalent available.
Goals: same metrics; no conversion of market probability into p_model.
Handicap: settlement-aware grading for -0.25; no binary Brier shortcut for half-win/half-loss structures.
Corners: L13 only; hit-rate/evidence diagnostic, no price metrics until price exists.
Cards: L14 only; hit-rate/evidence diagnostic, no price metrics until price exists.

## Post-result protocol
Settle unique legs first, then tickets. Compare frozen entry reason against outcome. Failure labels allowed: MODEL / EVIDENCE / CONTEXT / PRICE / SELECTION / PORTFOLIO / VARIANCE; subflags TAIL_BLOWOUT / SCORE_STATE / PORTFOLIO_AMPLIFICATION where applicable. No parameter/weight/probability retuning from TEST07 alone.

## Compact Fiscal/Claude packet
Audit focus: (1) whether low-odds legs are overrepresented despite weak independent probability support; (2) whether cup/youth rotation creates hidden common-mode risk; (3) whether L15/L16 external-model price comparisons are semantically valid; (4) whether experimental corners/cards should remain outside headline P&L; (5) whether 30 unique legs x2 reuse is materially safer than prior concentrated slates. Fiscal is auditor only, never predictive signal.

## Source freeze
Current web sources used: EFL Trophy fixture/odds boards (Stake variants, SportyTrader, Oddschecker, Sportingbet); UEFA Women's Champions League odds (Oddschecker/Stake variants); Sports Mole Bayern-Man City model; Forebet and WinComparator Walsall-Stevenage; TotalCorner/CornerEdge Walsall-Stevenage; KillerBetTips corner/card-family discovery; FootyStats Scottish Challenge Cup; PredictZ/WinDrawWin Scottish Challenge Cup; ScorelineAI/TACTIX/OddsDigger KNVB Beker; BetUS Santa Fe-Cali. All were accessed after the formal cutoff and before results. No post-match result is admitted into this freeze.