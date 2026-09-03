"""Check local Markdown links without network access."""
from __future__ import annotations
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
LINK = re.compile(r"(?<!!)\[[^\]]*\]\(([^)]+)\)")

def main():
    broken = []
    checked = 0
    for document in ROOT.rglob("*.md"):
        if ".git" in document.parts:
            continue
        # Build handoffs are byte-preserved input artifacts. Their prospective
        # example links are not repository navigation and cannot be rewritten.
        if document.is_relative_to(ROOT / "archive/build-spec"):
            continue
        text = document.read_text(encoding="utf-8")
        for raw in LINK.findall(text):
            target = raw.strip().split()[0].strip("<>")
            if target.startswith(("http://", "https://", "mailto:", "#")):
                continue
            path_part = target.split("#", 1)[0]
            if not path_part:
                continue
            checked += 1
            resolved = (document.parent / path_part).resolve()
            try:
                resolved.relative_to(ROOT.resolve())
            except ValueError:
                broken.append(f"{document.relative_to(ROOT)} -> {target} (escapes repository)")
                continue
            if not resolved.exists():
                broken.append(f"{document.relative_to(ROOT)} -> {target}")
    if broken:
        print("broken internal links:")
        for item in broken:
            print("- " + item)
        return 1
    print(f"internal link check: OK ({checked} links)")
    return 0
if __name__ == "__main__":
    raise SystemExit(main())
