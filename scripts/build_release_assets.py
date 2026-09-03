"""Build deterministic SHA-256 checksums for public v0.2 release assets."""
from __future__ import annotations

import argparse
import hashlib
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
TARGET = ROOT / "dist/SHA256SUMS.txt"
ASSETS = (
    "dist/ALL_IN_ONE_UPGRADEABLE_SKILL_KIT.md",
    "registry/registry.json",
    "registry/registry.yaml",
    "audit/OPERATIONAL_PACKAGE_REVIEW_v0.2.md",
)


def render():
    lines = []
    for relative in ASSETS:
        path = ROOT / relative
        if not path.is_file():
            raise FileNotFoundError(relative)
        digest = hashlib.sha256(path.read_bytes()).hexdigest()
        lines.append(f"{digest}  {relative}")
    return "\n".join(lines) + "\n"


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()
    try:
        expected = render()
    except FileNotFoundError as error:
        print(f"missing release asset: {error}", file=sys.stderr)
        return 1
    if args.check:
        if not TARGET.exists() or TARGET.read_text(encoding="utf-8") != expected:
            print("release checksums are stale", file=sys.stderr)
            return 1
        print(f"release asset check: OK ({len(ASSETS)} assets)")
        return 0
    TARGET.write_text(expected, encoding="utf-8", newline="\n")
    print(f"built {TARGET.relative_to(ROOT)} ({len(ASSETS)} assets)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
