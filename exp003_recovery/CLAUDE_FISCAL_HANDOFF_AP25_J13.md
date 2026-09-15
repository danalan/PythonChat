# Claude Fiscal Handoff — Apertura 2025 replay through J13

Status: AUDIT_INPUT
Prepared: 2026-09-14
Scope: current historical replay architecture and implementation state through Apertura 2025 J13.

## Auditor role

Act as an adversarial independent reviewer. Do not optimize for agreement with the current architecture. Your job is to find invalid assumptions, leakage paths, fragile rules, duplicated machinery, unjustified thresholds, misleading metrics and simpler alternatives.

Do not propose changes merely because a recent bet won or lost. Separate structural flaws from outcome variance.

## Current architecture

Canonical historical execution architecture: `V2.1_WINDOWED_100`.

Model signal:
- raw `V0.1R` Dixon-Coles ensemble;
- half-lives 180 / 365 / 730 / 1460 days;
- raw probability is canonical for selection;
- `CAL_SHRINK_GLOBAL_V0_1`, k=0.5620833333, is shadow calibration only.

Selection:
- require positive EV;
- within each fixture choose outcome with highest full-Kelly fraction;
- full-Kelly gate >= 0.05;
- fixed stakes: >=0.15 → MXN20, >=0.08 → MXN15, >=0.05 → MXN10;
- one MXN5 two-leg parlay per qualifying execution window when >=2 primary singles qualify; top two by Kelly;
- risk ceiling MXN100 per jornada; unused risk is allowed.

Shadow staking:
- `V2.2_FRACTIONAL_KELLY_SHADOW` with FK15, FK20, FK25;
- same candidate set/gate as V2.1;
- remains non-canonical.

## Mandatory historical replay chronology

Active order from J14 preparation onward:

`INTERNAL LEDGER → MODEL FREEZE → EXTERNAL RESEARCH → PRICE SNAPSHOT → SELECTOR → SELECTION FREEZE → RESULTS → SETTLEMENT`

Internal ledger owns endogenous data: prior results, standings, W-D-L, GF/GA, form, home/away splits and training chronology.

External research is restricted to fixtures/times, injuries, suspensions, player availability, probable lineups, coach/roster/institutional news, press/community context and historical pre-kickoff odds.

Context does not numerically modify `p_model` and does not veto a pick without a preregistered rule.

If a Jn result becomes visible before selection freeze, Jn becomes permanently `NO-PROMOTION`; mechanical replay may continue, but the contaminated slice cannot justify architecture promotion.

## Known contamination record

Historical replay J1–J13 contains multiple outcome-exposed / `NO-PROMOTION` jornadas.

J13 specifically:
- model code and training set were frozen before external J13 research;
- during historical-price web research, a J13 result became visible before selection freeze;
- the revealed result was not used to alter probabilities, odds, EV, Kelly or selections;
- nevertheless J13 is classified `NO-PROMOTION`.

The audit should determine whether this observer-exposure classification is sufficient or whether contamination should be classified more granularly.

## J13 exact state

Model training count: 1124.
Canonical opening bankroll: MXN437.3012159211471.

Accepted Bet365 rows produced three canonical singles:
1. Tijuana ML @3.05, p=0.4946296299, EV=+0.5086203713, full Kelly=0.2481074982, stake MXN20.
2. Pachuca ML @2.75, p=0.3959809216, EV=+0.0889475345, full Kelly=0.0508271626, stake MXN10.
3. Guadalajara–Mazatlán DRAW @5.25, p=0.2552227423, EV=+0.3399193969, full Kelly=0.0799810346, stake MXN10.

Secondary parlay:
- Pachuca ML + Guadalajara–Mazatlán DRAW @14.4375;
- independence joint p=0.1010633367;
- stake MXN5.

Total risk MXN45.
All four tickets lost.
Canonical J13 P&L: -MXN45.
Canonical close: MXN392.3012159211471.

Shadow closes approximately:
- FK15 MXN443.0890;
- FK20 MXN429.6736;
- FK25 MXN416.2316.

Cumulative selected-single calibration J1–J13, n=39:
- raw Brier ≈0.18489;
- shrink Brier ≈0.20591;
- raw log loss ≈0.55596;
- shrink log loss ≈0.60335.

Do not treat raw's lead as promotion evidence without accounting for conditioning, contamination and sample size.

## J14 starting state

Canonical bankroll: MXN392.3012159211471.
Completed Apertura matches: 117.
Expected model training count: 1133.

## Price provenance issue requiring explicit verdict

For J13, complete same-book Bet365 1X2 rows were recovered from contemporaneous SportyTrader prediction pages whose original publication timestamp was pre-kickoff, but whose pages may have been modified later.

Audit whether this is acceptable historical-price evidence.

Return one of:
- `ACCEPT_CANONICAL_PRICE_EVIDENCE`
- `ACCEPT_WITH_DOWNGRADE`
- `SHADOW_ONLY_PRICE_EVIDENCE`
- `REJECT_PRICE_EVIDENCE`

Explain the minimum provenance standard that should apply prospectively to historical replay.

## Questions Claude must attack

1. Is the raw Dixon-Coles probability construction temporally clean and correctly implemented?
2. Are the 180/365/730/1460 half-lives justified or merely inherited? What test would validate them without data snooping?
3. Is averaging the four model matrices/probabilities mathematically coherent and correctly coded?
4. Is the full-Kelly gate of 0.05 defensible?
5. Are fixed stake buckets compatible with Kelly ranking, or do they throw away useful information?
6. Should bankroll level affect canonical stakes instead of fixed MXN10/15/20 buckets?
7. Is 'highest Kelly outcome per fixture' the correct within-match candidate rule?
8. Is the MXN100 risk ceiling meaningfully connected to drawdown control?
9. Is the two-leg parlay layer adding expected value or merely variance and multiple-testing surface area?
10. Is multiplying cross-match probabilities for the parlay acceptable, and what dependence risks remain?
11. Is selected-bet Brier/log loss an interpretable calibration metric after selection conditioning?
12. Should calibration evaluation include all generated probabilities rather than only selected singles?
13. Is the shrink shadow a meaningful calibration challenger or an arbitrary transform?
14. Is `NO-PROMOTION` adequate, or should contamination be split by where leakage happened?
15. Could the web-research sequence be redesigned to materially reduce observer exposure?
16. Does using modern webpages with historical original timestamps create hidden revision risk?
17. Are team aliases and fixture reschedules robustly normalized and tested?
18. Are there scripts/workflows that can diverge because constants are copied rather than centralized?
19. Does GitHub CI genuinely enforce freeze-before-result ordering, or is that mostly procedural convention?
20. Which active components should be KEEP / REVISE / REMOVE / TEST before J14 onward?

## Required repository artifacts to inspect first

- `CP_BRIDGE_MANIFEST_V1.md`
- `ap25_j13_model_only_replay.py`
- `ap25_j13_model_output.txt`
- `ap25_j13_price_snapshot_pre_cutoff.json`
- `ap25_j13_selection_output.json`
- `ap25_j13_selection_freeze.json`
- `ap25_j13_settlement.json`
- `ap25_j14_internal_pre_jornada_snapshot.json`
- current J13 model and selector GitHub Actions workflows
- prior J10–J12 price/freeze/settlement artifacts to test whether rules were applied consistently

## Required output

Return:

1. `EXECUTIVE VERDICT`: HEALTHY / HEALTHY_WITH_MATERIAL_FIXES / UNSAFE_TO_CONTINUE / REBUILD_REQUIRED.
2. Top findings ordered CRITICAL / HIGH / MEDIUM / LOW.
3. Direct answer on historical odds provenance.
4. Leakage and temporal-integrity audit.
5. Model-math audit.
6. Staking/risk/parlay audit.
7. Calibration/metrics audit.
8. Code/CI/reproducibility audit.
9. Data-normalization/reschedule audit.
10. List of rules that are genuinely justified vs merely conventional.
11. Exact action list, maximum 12 items, each tagged KEEP / REVISE / REMOVE / ADD / TEST.
12. Explicit section `DO NOT CHANGE YET` to prevent hindsight overfitting.
13. For every proposed change, specify whether it can apply immediately to J14 or must be preregistered and tested on a later untouched window.

Do not build a larger framework unless it solves a demonstrated failure. Prefer deletion and simplification when two layers do the same job.
