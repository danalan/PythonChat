# Cerebro Portátil ↔ GitHub Bridge Manifest V1

Status: ACTIVE
Date: 2026-09-13
Repository scope: `exp003_recovery/`

## Purpose

GitHub is the canonical computational record for the 1000→100000 betting laboratory. Cerebro Portátil / Google Drive remains the canonical human-readable governance and decision layer. The Master Bet Ledger remains the canonical execution ledger.

This manifest defines aliases only. The repository is public, so no private Drive IDs, private URLs, account information, or personal data belong here.

## Logical aliases

- `ARCHITECTURE_CANON` → current canonical architecture/governance document in Cerebro Portátil.
- `OPERATIVE_PROMPT_CANON` → current ChatGPT operating prompt in Cerebro Portátil.
- `FISCAL_PROMPT_CANON` → current Claude fiscal prompt in Cerebro Portátil.
- `MASTER_BET_LEDGER_CANON` → current append-only execution ledger.
- `EXP003_NARRATIVE_LOG` → Clausura 2025 walk-forward narrative document.
- `EXP003_COMPUTE_ROOT` → `exp003_recovery/`.

## Source-of-truth split

| Layer | Canonical system | What belongs there |
|---|---|---|
| Governance | Cerebro Portátil / Drive | architecture, rules, audit decisions, explanations, source notes |
| Computation | GitHub | code, tests, manifests, freezes, settlements, model artifacts, workflows |
| Execution | Master Bet Ledger | Bet Key, REAL/SIM execution, odds, stake, timestamp, P&L |
| Historical research | GitHub + EXP003 narrative log | research-only freezes, settlement, Brier/calibration, postmortems |

## Traceability contract

1. Every material computational freeze or settlement must have a Git commit SHA.
2. Cerebro Portátil records that SHA in the corresponding narrative state.
3. A governance change that changes calculation must result in a versioned code/config change in GitHub before it is used prospectively.
4. Historical files are never silently rewritten to make new rules look old.
5. If Drive and GitHub disagree about a numerical result, the frozen GitHub artifact and its commit are inspected first; the discrepancy is logged rather than patched by memory.
6. If Ledger and GitHub disagree about whether money was actually executed, the Ledger plus user-confirmed execution evidence governs the REAL track. GitHub governs model/research state.

## Current checkpoint

- Recovered bridge: `V0.1R_RECOVERED` from J8 onward.
- Recovery uncertainty envelope: ±0.003.
- J9 freeze commit: `6fd736198597bbb673f7b7c15e90736ad5fd54c4`.
- J9 settlement commit: `3e6695f9f5c5f12b7636ca712382af7188ab6182`.
- J9 scoring/cumulative update: `b5b83519f88dee223890ff6646e0067f60434694`.
- Corner model: `C0.1-CORNERS-NB-ENSEMBLE`, SHADOW_ONLY.

## Privacy rule

Never add private Drive identifiers, private links, personal notes, betting-account data, credentials, screenshots containing private account information, or non-public Cerebro Portátil content to this public repository. Use logical aliases and public commit references only.
