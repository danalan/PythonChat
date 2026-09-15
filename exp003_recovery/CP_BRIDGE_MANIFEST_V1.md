# Cerebro Portátil ↔ GitHub Bridge Manifest V1

Status: ACTIVE
Updated: 2026-09-14
Repository scope: `exp003_recovery/`

## Purpose

GitHub is the canonical computational record for the 1000→100000 betting laboratory. Cerebro Portátil / Google Drive remains the canonical human-readable governance and decision layer. The Master Bet Ledger remains the canonical REAL execution ledger.

This manifest defines aliases only. The repository is public, so no private Drive IDs, private URLs, account information, or personal data belong here.

## Logical aliases

- `ARCHITECTURE_CANON` → current canonical architecture/governance document in Cerebro Portátil.
- `OPERATIVE_PROMPT_CANON` → current ChatGPT operating rules in Cerebro Portátil.
- `FISCAL_PROMPT_CANON` → current Claude fiscal/audit prompt in Cerebro Portátil.
- `MASTER_BET_LEDGER_CANON` → current append-only REAL execution ledger.
- `AP25_REPLAY_NARRATIVE_CANON` → human-readable Apertura 2025 replay state in Cerebro Portátil.
- `EXP003_COMPUTE_ROOT` → `exp003_recovery/`.

## Source-of-truth split

| Layer | Canonical system | What belongs there |
|---|---|---|
| Governance | Cerebro Portátil / Drive | architecture, rules, audit decisions, explanations, source notes |
| Computation | GitHub | code, tests, manifests, freezes, settlements, model artifacts, workflows |
| REAL execution | Master Bet Ledger | Bet Key, execution confirmation, actual odds/stake/timestamp, P&L |
| Historical research | GitHub + AP25 replay narrative | research freezes, price snapshots, selection freezes, settlement, calibration, postmortems |

## Traceability contract

1. Every material computational freeze or settlement must have a Git commit SHA.
2. Cerebro Portátil records the corresponding computational checkpoint in narrative form.
3. A governance change that changes calculation must result in a versioned code/config change in GitHub before prospective use.
4. Historical files are never silently rewritten to make new rules look old.
5. If Drive and GitHub disagree about a numerical result, inspect the frozen GitHub artifact and commit first; log the discrepancy rather than patching from memory.
6. If Ledger and GitHub disagree about whether money was actually executed, the Ledger plus user-confirmed execution evidence governs REAL; GitHub governs model/research state.

## Historical replay research ownership — ACTIVE FROM J14 PREPARATION

External historical research is now performed directly by ChatGPT instead of delegated to Perplexity/Gemini.

Mandatory order:

`INTERNAL LEDGER → MODEL FREEZE → EXTERNAL RESEARCH → PRICE SNAPSHOT → SELECTOR → SELECTION FREEZE → RESULT LOOKUP → SETTLEMENT`

Rules:
- Internal canonical ledger owns standings, form, home/away splits, prior results, GF/GA and training chronology.
- External research is limited to fixture metadata, injuries, suspensions, roster/coach/institutional news, probable lineups, contemporary press/community context and historical pre-kickoff prices.
- External context never rewrites `p_model` and cannot veto a selection without a preregistered rule.
- If a result or other post-cutoff Jn fact becomes visible before selection freeze, that jornada is permanently `NO-PROMOTION`, even if the leaked information is not used in model, price or selection calculations.
- Mechanical replay may continue after contamination, but contaminated evidence cannot justify architecture promotion.
- Historical price rows must be complete same-book 1X2 rows. Never mix books, infer missing prices or backsolve prices.
- Same-day sources without a trustworthy pre-kickoff timestamp are rejected unless stronger provenance exists.
- A page with a pre-kickoff original publication timestamp but later modification is usable only with an explicit provenance caveat; it is weaker than a captured/archived pre-kickoff quote.

## Active canonical historical architecture

`V2.1_WINDOWED_100`

- Canonical probability source: raw `V0.1R` Dixon-Coles ensemble.
- Half-lives: 180 / 365 / 730 / 1460 days.
- Candidate must have positive model EV.
- One candidate per fixture: highest full-Kelly fraction.
- Admission gate: full Kelly >= 0.05.
- Fixed single stakes:
  - Kelly >= 0.15 → MXN20
  - Kelly >= 0.08 → MXN15
  - Kelly >= 0.05 → MXN10
- Secondary parlay: MXN5 two-leg parlay within an execution window only when >=2 primary singles qualify in that window; top two by Kelly.
- Risk ceiling: MXN100 per jornada/windowed week. Ceiling, not allocation target.
- Do not recycle early-window returns within the same jornada risk budget.

Calibration shadow remains `CAL_SHRINK_GLOBAL_V0_1`, k=0.5620833333.

`V2.2_FRACTIONAL_KELLY_SHADOW` remains shadow-only at FK15/FK20/FK25 and does not control canonical selection.

## Current checkpoint — after Apertura 2025 J13

- J13 model training count: 1124.
- J13 model was frozen before external J13 research.
- External research later exposed a J13 result before selection freeze, so J13 is permanently `NO-PROMOTION`.
- J13 complete accepted historical price coverage: nine same-book Bet365 1X2 rows recovered from contemporaneous SportyTrader prediction pages, with provenance caveat that pages may have later modification dates.
- J13 canonical selections:
  - Tijuana ML @3.05, MXN20.
  - Pachuca ML @2.75, MXN10.
  - Guadalajara–Mazatlán DRAW @5.25, MXN10.
  - Pachuca ML + Guadalajara–Mazatlán DRAW parlay @14.4375, MXN5.
- J13 canonical risk: MXN45.
- J13 canonical P&L: -MXN45.
- Canonical closing bankroll after J13: MXN392.3012159211471.
- Shadow closing bankrolls after J13:
  - FK15: MXN443.0890 approximately.
  - FK20: MXN429.6736 approximately.
  - FK25: MXN416.2316 approximately.
- J1–J13 selected-single calibration: n=39.
  - raw Brier ≈ 0.18489 vs shrink ≈ 0.20591.
  - raw log loss ≈ 0.55596 vs shrink ≈ 0.60335.
  - raw V0.1R remains ahead cumulatively, but historical contamination means this does not by itself authorize promotion.
- Pre-J14 Apertura completed matches: 117.
- Expected J14 training count: 1133.

Key GitHub checkpoints:
- J13 external research audit: `9759f638ff345ee1e5038d3d987c304c70bbe1ea`.
- J13 price snapshot: `bbd070faaf18c70dac6fbaaf5704afecd8f7525e`.
- J13 selector implementation: `3067f44404819013ca40aad33c5e52827b551113`.
- J13 authoritative selection freeze: `5d60247b05236a7cd338900e280f9f2d1cb8ada2`.
- J13 settlement: `2cc573601014055d98e2aa17d8302d049d6c7b21`.
- Pre-J14 internal snapshot: `5bfeca121d143194f61b90e7f7af91caa6b1ad25`.

## Known active audit questions

1. Is SportyTrader original-publication provenance strong enough for canonical historical price use when pages were later modified?
2. Are the V2.1 Kelly gate and fixed stake buckets justified independently, or merely inherited heuristics?
3. Does the window-based secondary parlay create unnecessary correlated portfolio risk or selection noise?
4. Is the cumulative raw-vs-shrink calibration comparison interpretable given repeated `NO-PROMOTION` jornadas and selected-bet conditioning?
5. Are fixture reschedules/time corrections represented safely enough that historical cutoffs cannot silently drift?
6. Can external-search leakage be technically reduced further, or should all replay jornadas sourced through modern web search automatically remain research-only?
7. Is the current `NO-PROMOTION` concept sufficient, or should contamination severity be split into model-contaminated / selection-contaminated / observer-exposed classes?

## Privacy rule

Never add private Drive identifiers, private links, personal notes, betting-account data, credentials, screenshots containing private account information, or non-public Cerebro Portátil content to this public repository. Use logical aliases and public commit references only.
