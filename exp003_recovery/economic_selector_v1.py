#!/usr/bin/env python3
"""Deterministic 3x3 economic selector for EXP-003.

This selector is deliberately mechanical. It cannot consume outcomes or narrative
context. It combines a frozen MODEL_ONLY probability surface with a frozen
pre-cutoff 1X2 price snapshot and MARKET_PROXY_V1.

Rule V1
-------
1. One leg per fixture, exactly nine fixtures.
2. Candidate market must be supported by MARKET_PROXY_V1.
3. p_model must be inside the recovered V0.1R support interval [0.60, 0.8224852071].
4. For each fixture choose the eligible leg with maximum model EV at proxy price.
   Forced-track selection still chooses the least-bad leg if all eligible EVs are <=0.
5. Rank the nine chosen fixture-legs by EV descending; tie-break higher p_model,
   fixture_id, market.
6. P1 (80 MXN) gets ranks 1,3,5; P2 (80) ranks 2,4,6; P3 (40) ranks 7,8,9.
7. No fixture can repeat across tickets. No replacement after freeze.

The user-requested FORCED_200_TRACK uses all three tickets. A separate diagnostic
EV-disciplined view may hold cash on ticket-level EV <= 0.
"""
from __future__ import annotations

import argparse
import importlib
import json
from pathlib import Path
import numpy as np

import parlay_replay_dc as base
from economic_proxy_v1 import price_market

SUPPORT_LOW = 0.60
SUPPORT_HIGH = 0.8224852071005917

MARKET_MAP = {
    "DC_12": "DOUBLE_CHANCE_12",
    "DC_1X": "DOUBLE_CHANCE_1X",
    "DC_X2": "DOUBLE_CHANCE_X2",
    "HOME_TG_O0.5": "HOME_TEAM_OVER_0.5",
    "AWAY_TG_O0.5": "AWAY_TEAM_OVER_0.5",
    "HOME_TG_U2.5": "HOME_TEAM_UNDER_2.5",
    "AWAY_TG_U2.5": "AWAY_TEAM_UNDER_2.5",
    "TOTAL_O1.5": "TOTAL_OVER_1.5",
    "TOTAL_U3.5": "TOTAL_UNDER_3.5",
    "TOTAL_U4.5": "TOTAL_UNDER_4.5",
}


def candidate_rows(replay, prices):
    allm = base.load_all()
    tr = [m for m in allm if m.date < replay.MODEL_CUTOFF]
    expected = getattr(replay, "EXPECTED_TRAINING_ROWS", None)
    if expected is not None and len(tr) != expected:
        raise SystemExit(f"chronology drift: expected {expected}, got {len(tr)}")
    mods = base.ensemble(tr, replay.MODEL_CUTOFF)

    rows = []
    for fid, date, home, away in replay.FIXTURES:
        odds = prices["fixtures"][fid]["decimal_1x2"]
        M, _ = base.avg_matrix(mods, home, away)
        probs = replay.market_probs(M)
        for internal_market, proxy_market in MARKET_MAP.items():
            p = float(probs[internal_market])
            if not (SUPPORT_LOW <= p <= SUPPORT_HIGH):
                continue
            px = price_market(proxy_market, odds)
            ev = p * px.proxy_decimal - 1.0
            rows.append({
                "fixture_id": fid,
                "date": date,
                "home": home,
                "away": away,
                "market": internal_market,
                "proxy_market": proxy_market,
                "p_model": p,
                "market_fair_probability": px.fair_probability,
                "market_disagreement": p - px.fair_probability,
                "source_overround": px.source_overround,
                "proxy_decimal": px.proxy_decimal,
                "break_even_proxy": 1.0 / px.proxy_decimal,
                "model_ev_at_proxy": ev,
                "lambda_home_market_proxy": px.lambda_home,
                "lambda_away_market_proxy": px.lambda_away,
                "price_temporal_confidence": prices["fixtures"][fid].get("temporal_confidence"),
                "price_source": prices["fixtures"][fid].get("source"),
            })
    return rows, len(tr)


def select(rows):
    per_fixture = {}
    for r in rows:
        per_fixture.setdefault(r["fixture_id"], []).append(r)
    if len(per_fixture) != 9:
        missing = sorted(set(f"J12-{i:02d}" for i in range(1, 10)) - set(per_fixture))
        raise SystemExit(f"not all fixtures have eligible proxy markets: {missing}")

    chosen = []
    for fid, pool in sorted(per_fixture.items()):
        best = sorted(pool, key=lambda r: (-r["model_ev_at_proxy"], -r["p_model"], r["market"]))[0]
        chosen.append(best)

    ranked = sorted(chosen, key=lambda r: (-r["model_ev_at_proxy"], -r["p_model"], r["fixture_id"], r["market"]))
    assignments = {
        "P1": [ranked[i] for i in (0, 2, 4)],
        "P2": [ranked[i] for i in (1, 3, 5)],
        "P3": [ranked[i] for i in (6, 7, 8)],
    }
    stakes = {"P1": 80.0, "P2": 80.0, "P3": 40.0}
    tickets = {}
    for label, legs in assignments.items():
        p_joint = float(np.prod([x["p_model"] for x in legs]))
        px_joint = float(np.prod([x["proxy_decimal"] for x in legs]))
        tickets[label] = {
            "stake_mxn": stakes[label],
            "legs": legs,
            "p_model_joint_independence_approx": p_joint,
            "proxy_decimal": px_joint,
            "break_even_proxy": 1.0 / px_joint,
            "model_ev_at_proxy": p_joint * px_joint - 1.0,
            "ev_disciplined_eligible": bool(p_joint * px_joint > 1.0),
        }
    return ranked, tickets


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--replay-module", required=True)
    ap.add_argument("--price-snapshot", required=True)
    args = ap.parse_args()

    replay = importlib.import_module(args.replay_module)
    prices = json.loads(Path(args.price_snapshot).read_text())
    rows, training_count = candidate_rows(replay, prices)
    ranked, tickets = select(rows)
    out = {
        "selector": "ECONOMIC_SELECTOR_V1",
        "replay_module": args.replay_module,
        "price_snapshot": args.price_snapshot,
        "training_count": training_count,
        "model_cutoff": replay.MODEL_CUTOFF.isoformat(),
        "context_cutoff": replay.CONTEXT_CUTOFF,
        "support_interval": [SUPPORT_LOW, SUPPORT_HIGH],
        "fixture_winners_ranked_by_ev": ranked,
        "tickets": tickets,
        "integrity": {
            "selection_mode": "MECHANICAL_MODEL_PLUS_PRE_CUTOFF_PRICE",
            "context_used": False,
            "outcomes_used": False,
            "no_fixture_repeat": len({x["fixture_id"] for t in tickets.values() for x in t["legs"]}) == 9,
            "note": "If the human researcher was outcome-exposed, this mechanical selector prevents discretionary leakage into selection."
        }
    }
    print("ECONOMIC_SELECTOR_OUTPUT", json.dumps(out, ensure_ascii=False, sort_keys=True), flush=True)


if __name__ == "__main__":
    main()
