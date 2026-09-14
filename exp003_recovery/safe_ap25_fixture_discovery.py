#!/usr/bin/env python3
"""Safe Apertura 2025 fixture discovery from openfootball 2025-26 data.

The upstream file contains scores, but this utility never serializes or prints them.
Only date/home/away are emitted, to protect researcher outcome blindness while
reconstructing historical jornada schedules.
"""
from __future__ import annotations
import argparse, json
from datetime import datetime
import parlay_replay_dc as base

SOURCE="2025-26_mx1.txt"

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("--start", required=True)
    ap.add_argument("--end", required=True)
    ap.add_argument("--expected", type=int, default=None)
    args=ap.parse_args()
    start=datetime.fromisoformat(args.start); end=datetime.fromisoformat(args.end)
    text=base.fetch_text(SOURCE)
    all_rows=base.parse_openfootball(text,SOURCE)
    matches=[m for m in all_rows if start <= m.date < end]
    rows=sorted([{"date":m.date.strftime("%Y-%m-%d"),"home":m.home,"away":m.away} for m in matches], key=lambda r:(r["date"],r["home"],r["away"]))
    if args.expected is not None and len(rows)!=args.expected:
        raise SystemExit(f"fixture discovery count mismatch: expected {args.expected}, got {len(rows)}")
    print("SAFE_AP25_FIXTURES",json.dumps({"source":SOURCE,"start":args.start,"end":args.end,"count":len(rows),"fixtures":rows},ensure_ascii=False,sort_keys=True))

if __name__=="__main__": main()
