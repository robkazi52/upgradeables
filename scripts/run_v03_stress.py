#!/usr/bin/env python3
"""Run the bounded v0.3 stress gate one or more times."""
from __future__ import annotations

import argparse
import sys
import time
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repeat", type=int, default=1, help="repeat the full gate (default: 1)")
    args = parser.parse_args()
    if args.repeat < 1:
        parser.error("--repeat must be at least 1")

    started = time.perf_counter()
    for iteration in range(1, args.repeat + 1):
        print(f"[RUN] v0.3 stress gate {iteration}/{args.repeat}")
        suite = unittest.defaultTestLoader.discover(
            str(ROOT / "tests"), pattern="test_v03_stress.py"
        )
        result = unittest.TextTestRunner(verbosity=2).run(suite)
        if not result.wasSuccessful():
            print("V0.3 STRESS GATE: FAIL", file=sys.stderr)
            return 1
    elapsed = time.perf_counter() - started
    print(f"V0.3 STRESS GATE: PASS ({args.repeat} run(s), {elapsed:.2f}s)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
