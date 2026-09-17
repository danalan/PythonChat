#!/usr/bin/env python3
"""Operational daily Track-F runner. Reads a frozen request and calls Vn unchanged."""
from __future__ import annotations
import json, sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
if str(HERE) not in sys.path:
    sys.path.insert(0, str(HERE))

import vn2026_forward as vn


def main():
    if len(sys.argv) != 2:
        raise SystemExit("usage: daily_forward_request.py REQUEST.json")
    req_path = Path(sys.argv[1])
    req = json.loads(req_path.read_text(encoding="utf-8"))
    cutoff = vn.parse_cutoff(req["cutoff_local"])
    targets = [tuple(x) for x in req["targets"]]
    out, rows = vn.run_forward(cutoff, targets=targets)
    out.update({
        "request_id": req["request_id"],
        "timezone": req.get("timezone", "America/Mexico_City"),
        "governance_version": "DUAL_TRACK_LAB_V1.1",
        "model_status": "SHADOW MODEL SIGNAL",
        "execution_default": "SHADOW",
        "real_authorized": False,
        "last_admitted_match_local": max(vn.canonical_local_naive(m.date) for m in rows).isoformat(),
        "request_path": str(req_path),
    })
    dest = HERE / "forward_freezes" / f"{req['request_id']}_vn_daily.json"
    dest.parent.mkdir(parents=True, exist_ok=True)
    dest.write_text(json.dumps(out, ensure_ascii=False, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print("DAILY_FORWARD_REQUEST", req["request_id"])
    print("VN_CUTOFF", out["cutoff"])
    print("TRAINING", out["training_count"])
    print("LAST_MATCH", out["last_admitted_match_local"])
    print("SNAPSHOT", out["training_snapshot_sha256"])
    print("OUTPUT", dest)
    for f in out["fixtures"]:
        print("FIXTURE", json.dumps(f, ensure_ascii=False, sort_keys=True))


if __name__ == "__main__":
    main()
