# Full-System Audit Scope — 1000 → 100000

Date frozen for audit scope: 2026-09-13
Status: AUDIT_INPUT
Purpose: give an adversarial auditor enough structure to review the project as a system, not merely inspect one ticket.

## Audit objective

Determine what is actually working, what is merely plausible, what is redundant or obsolete, what is missing, and what must be tested before further promotion. The audit must prefer fewer justified components over more framework.

## Systems in scope

### Models
- `V0.1_LEGACY`
- `V0.1R_RECOVERED`
- current forward Vn-2026 goal model artifacts
- `C0.1-CORNERS-NB-ENSEMBLE`

### Core computational files
Inspect all files under `exp003_recovery/`, with particular attention to:
- goal model/replay code
- recovery diagnostics
- context/portfolio policy
- J8/J9 freeze manifests and settlements
- corner model and corner replay
- current forward model
- architecture proposals
- GitHub Actions workflows that execute or validate these paths

### Historical experiment
EXP-003 Clausura 2025, effective-date chronology, J1–J9 currently settled.

Legacy descriptive record through J9:
- 23/27 selected legs correct
- 6/9 parlays correct
- retrospective/outcome-exposed; not evidence of ROI, EV or prospective profitability

J9 expanded shadow:
- 4/6 atomic legs
- 1/3 two-leg parlays
- mean atomic Brier 0.164330
- mean parlay Brier 0.258308
- sample far too small for broad conclusions

### Context layer
Current flow: `MODEL_SIGNAL → CONTEXT_AUDIT → FREEZE`.
Context labels: SUPPORT / NEUTRAL / CONTRADICT_LOW / CONTRADICT_HIGH / UNKNOWN.
Context must not numerically alter p_model without validated incremental evidence.

### Corner model data quality
J9 historical corner source reconstruction:
- 242 eligible schedule rows
- 132 usable corner rows
- 54.55% coverage
- exact-count disagreement observed across providers for Toluca–Querétaro, although binary O3.5 settlement agreed

C0.1 must remain SHADOW_ONLY until source coverage, missingness, mapping and walk-forward calibration are resolved.

## Questions the auditor must answer

1. Is temporal integrity genuinely fail-closed everywhere, or can any script/source path leak results or post-cutoff aggregates?
2. Is `V0.1R_RECOVERED` close enough to the legacy implementation for its intended bridge role, and are ±0.003 quarantine rules defensible?
3. Does the project overfit process rules to individual jornadas despite its stated safeguards?
4. Does `research_score = probability - abs(aggregate_error)` still reward high raw p too strongly or duplicate information already embedded in p?
5. Which market families have credible calibration evidence, which only inherit a score matrix, and which should be removed from candidate generation?
6. Are the selected-leg hit rates being used anywhere, explicitly or implicitly, as if they were unbiased performance estimates?
7. Does the expanded two-leg portfolio create a fair forward hypothesis, or is it another flexible search layer that needs preregistered selection rules?
8. Does context add incremental predictive information after the numerical model, or merely tell persuasive stories? Design an ablation test.
9. Are injury/suspension/rest/venue/H2H/form/media variables encoded consistently enough to test, or should some remain narrative-only?
10. Is the corner Negative Binomial architecture appropriate given coverage and possible non-random missingness? What is the minimum data protocol for promotion?
11. Are same-game and cross-event dependence assumptions treated consistently and conservatively?
12. Are there duplicated scripts, dead diagnostics, stale architecture files, or hard-coded values that should be archived/parameterized?
13. Do CI workflows actually test cutoff integrity, reproducibility, deterministic seeds, mapping, and freeze-before-settlement ordering?
14. Are source/provider disagreements persisted and testable, or only mentioned in prose?
15. Is club-name normalization centralized and tested, or can aliases still silently fragment training histories?
16. Are GitHub, Cerebro Portátil, and the Master Bet Ledger synchronized by an explicit source-of-truth contract?
17. What should be deleted from active use, what should merely be archived, and what genuinely needs to be added?
18. Which variables/features should undergo ablation, and what metric/sample/promotion threshold should each use?
19. Is the 200 MXN weekly / 80-80-40 real-money guide compatible with the existing bankroll/governance rules, or should it remain user-execution policy outside model governance?
20. What are the five highest-leverage changes that reduce error without creating more unnecessary machinery?

## Required variable audit

Classify each as one of:
- `ESTABLISHED_STRUCTURAL`
- `PROMISING_BUT_UNPROVEN`
- `NO_INCREMENTAL_EVIDENCE`
- `FAILING_OR_MISSPECIFIED`
- `REMOVE_OR_ARCHIVE`

At minimum inspect:
- goal attack strength
- goal defense strength
- intercept
- home advantage
- Dixon-Coles rho
- half-life / decay ensemble
- model probability
- aggregate calibration error
- research_score
- injury availability
- suspension availability
- rest / short turnaround
- travel
- venue / altitude / surface
- manager / tactical change
- recent form
- comparable H2H
- press / analyst commentary
- X / Reddit / forum signals
- corner attack
- corner defense
- corner home advantage
- corner dispersion k
- corner half-life ensemble

Do not infer usefulness from one winning or losing ticket.

## Required ablation plan

Design temporally clean tests comparing:
A. goal model only
B. goal model + preregistered context veto layer
C. expanded score-matrix market mappings
D. separate corner model

For each specify:
- training/discovery window
- untouched evaluation window
- sample requirement
- metric
- promotion threshold
- kill threshold
- whether odds are required

Use Brier/log loss/calibration for probability quality. Use CLV/EV/ROI only where contemporaneous, semantically matched odds exist.

## Known documentation/infrastructure risks to verify

- Legacy and newer operating rules coexist in long append-only Drive documents; precedence may be clear to the author but opaque to a new agent.
- The historical EXP-003 title still says Parlay-3 even though a separate expanded two-leg shadow portfolio now exists.
- The canonical Drive hierarchy includes dedicated Errors/Postmortems and Results/Learnings areas that may not reflect current GitHub-rich activity.
- Computational state is fresher in GitHub than narrative state in Drive unless explicitly synchronized.
- Timezone consistency across all ledgers/manifests must be checked.
- Cerebro Portátil identifier uniqueness must be checked.

## Auditor output

Return:
1. Executive verdict: HEALTHY / HEALTHY_WITH_MATERIAL_FIXES / UNSAFE_TO_CONTINUE / REBUILD_REQUIRED
2. Top 10 findings by severity
3. What is actually working
4. What is assumed to work but unproven
5. Contradictions and dead weight
6. Missing components
7. Variable/feature classification table
8. Data/leakage/calibration audit
9. GitHub/CI/reproducibility audit
10. Cerebro Portátil ↔ GitHub architecture recommendation
11. Exact action plan, maximum 12 items, each KEEP/REVISE/REMOVE/ADD/TEST
12. What must NOT change yet to prevent overfitting
