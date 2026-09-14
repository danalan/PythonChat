#!/usr/bin/env python3
"""EXP-003 Clausura 2025 J15 model-only replay.

Temporal contract
-----------------
- Target slate: Clausura 2025 Jornada 15, 10-13 April 2025.
- Global model freeze: 2025-04-10 00:00. No J15 result is eligible.
- J1-J14 are historical and may enter training.
- External price/context snapshot cutoff: 2025-04-10 20:04 America/Mexico_City, immediately before the first J15 kickoff.
- Context is excluded from mechanical selection because researcher outcome exposure occurred during schedule discovery.
"""
from __future__ import annotations
import json
from datetime import datetime
import numpy as np
import parlay_replay_dc as base

MODEL_CUTOFF = datetime(2025, 4, 10, 0, 0, 0)
CONTEXT_CUTOFF = "2025-04-10T20:04:00-06:00"
EXPECTED_TRAINING_ROWS = 973

FIXTURES = [
    ("J15-01", "2025-04-10", "Club Tijuana", "Atlético San Luis"),
    ("J15-02", "2025-04-11", "Club Necaxa", "CF Pachuca"),
    ("J15-03", "2025-04-11", "Mazatlán FC", "Deportivo Guadalajara"),
    ("J15-04", "2025-04-12", "Pumas UNAM", "FC Juárez"),
    ("J15-05", "2025-04-12", "Club León", "Puebla FC"),
    ("J15-06", "2025-04-12", "Atlas Guadalajara", "Deportivo Toluca"),
    ("J15-07", "2025-04-12", "UANL Tigres", "CF Monterrey"),
    ("J15-08", "2025-04-12", "CF América", "Cruz Azul"),
    ("J15-09", "2025-04-13", "Santos Laguna", "Gallos Blancos"),
]

KNOWN_ABS_ERROR = {
    "DC_12": 0.0011004523947688,
    "HOME_TG_O0.5": 0.0046173990890806,
    "HOME_TG_U2.5": 0.013866299032083,
    "TOTAL_O1.5": 0.0321663976272116,
    "DC_1X": 0.0499629373171155,
    "DC_X2": 0.0510633897118843,
    "1X2_HOME": 0.0510633897118843,
    "1X2_AWAY": 0.0499629373171155,
}
CANONICAL = {"DC_12", "HOME_TG_O0.5", "HOME_TG_U2.5"}


def market_probs(M):
    n = M.shape[0]
    h = float(np.tril(M, -1).sum())
    d = float(np.trace(M))
    a = float(np.triu(M, 1).sum())
    z = {
        "1X2_HOME": h, "1X2_DRAW": d, "1X2_AWAY": a,
        "DC_1X": h + d, "DC_12": h + a, "DC_X2": d + a,
        "BTTS_YES": float(M[1:, 1:].sum()),
        "BTTS_NO": float(M[0, :].sum() + M[1:, 0].sum()),
    }
    for line in (1.5, 2.5, 3.5, 4.5):
        k = int(line)
        u = float(sum(M[i, j] for i in range(n) for j in range(n) if i + j <= k))
        z[f"TOTAL_U{line}"] = u
        z[f"TOTAL_O{line}"] = 1 - u
    for side, marg in (("HOME", M.sum(axis=1)), ("AWAY", M.sum(axis=0))):
        for line in (0.5, 1.5, 2.5):
            k = int(line)
            u = float(marg[:k + 1].sum())
            z[f"{side}_TG_U{line}"] = u
            z[f"{side}_TG_O{line}"] = 1 - u
    return z


def risk_band(market, p):
    if p >= 0.78:
        return "CONSERVATIVE_CANDIDATE"
    if 0.55 <= p < 0.70 and (
        market.startswith("1X2_") or market in {"BTTS_YES", "BTTS_NO", "TOTAL_O2.5", "TOTAL_U2.5"}
    ):
        return "AGGRESSIVE_CANDIDATE"
    return "STANDARD"


def main():
    allm = base.load_all()
    tr = [m for m in allm if m.date < MODEL_CUTOFF]
    if len(tr) != EXPECTED_TRAINING_ROWS:
        raise SystemExit(f"J15 chronology drift: expected {EXPECTED_TRAINING_ROWS}, got {len(tr)}")
    mods = base.ensemble(tr, MODEL_CUTOFF)
    legacy_pool = base.make_candidates(mods, FIXTURES)
    legacy_selected = base.select_three(legacy_pool)

    expanded = []
    for fid, date, home, away in FIXTURES:
        M, meta = base.avg_matrix(mods, home, away)
        for market, p in market_probs(M).items():
            err = KNOWN_ABS_ERROR.get(market)
            expanded.append({
                "fixture_id": fid, "date": date, "home": home, "away": away,
                "market": market, "p_model": float(p),
                "known_abs_error": err,
                "research_score": None if err is None else float(p - err),
                "canonical_v01r": market in CANONICAL,
                "signal_status": "CANONICAL_ELIGIBILITY_TEST" if market in CANONICAL else "EXPERIMENTAL_SIGNAL",
                "risk_band": risk_band(market, float(p)),
                "ensemble_meta": meta,
            })
    expanded_ranked = sorted(expanded, key=lambda r: (-r["p_model"], r["fixture_id"], r["market"]))
    out = {
        "track": "HISTORICAL_J15_MODEL_ONLY_PRE_CONTEXT",
        "model": "V0.1R_RECOVERED",
        "model_cutoff": MODEL_CUTOFF.isoformat(),
        "context_cutoff_max": CONTEXT_CUTOFF,
        "training_count": len(tr),
        "fixtures": [{"fixture_id": f[0], "date": f[1], "home": f[2], "away": f[3]} for f in FIXTURES],
        "legacy_selected": [{k: r[k] for k in ("fixture_id", "date", "home", "away", "contract", "probability", "aggregate_error", "research_score")} for r in legacy_selected],
        "legacy_joint_probability": float(np.prod([r["probability"] for r in legacy_selected])),
        "expanded_top60": expanded_ranked[:60],
        "warning": "MODEL_ONLY pre-context. Human researcher is outcome-exposed for J15; selection must remain deterministic model+price only."
    }
    print("J15_MODEL_ONLY_OUTPUT", json.dumps(out, ensure_ascii=False, sort_keys=True), flush=True)

if __name__ == "__main__":
    main()
