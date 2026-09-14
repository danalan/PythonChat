#!/usr/bin/env python3
"""Discover historical target fixtures without ever printing outcomes.

This utility intentionally exposes only date/home/away. Goal fields and any other
post-kickoff data are never serialized, reducing outcome leakage during historical
replay schedule discovery.
"""
from __future__ import annotations
import argparse
from datetime import datetime
import json
import parlay_replay_dc as base


def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("--start", required=True, help="YYYY-MM-DD inclusive")
    ap.add_argument("--end", required=True, help="YYYY-MM-DD exclusive")
    ap.add_argument("--expected", type=int, default=None)
    args=ap.parse_args()
    start=datetime.fromisoformat(args.start)
    end=datetime.fromisoformat(args.end)
    matches=[m for m in base.load_all() if start <= m.date < end]
    rows=[{"date":m.date.strftime("%Y-%m-%d"),"home":m.home,"away":m.away} for m in matches]
    rows=sorted(rows,key=lambda r:(r["date"],r["home"],r["away"]))
    if args.expected is not None and len(rows)!=args.expected:
        raise SystemExit(f"fixture discovery count mismatch: expected {args.expected}, got {len(rows)}")
    print("SAFE_FIXTURES",json.dumps({"start":args.start,"end":args.end,"count":len(rows),"fixtures":rows},ensure_ascii=False,sort_keys=True))

if __name__=="__main__": main()
