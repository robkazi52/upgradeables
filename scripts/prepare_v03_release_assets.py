"""Stage and checksum the reviewed v0.3.0 GitHub release assets."""
from __future__ import annotations

import argparse
import hashlib
import sys
import tomllib
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CANONICAL_ASSETS = (
    ROOT / "dist/ALL_IN_ONE_UPGRADEABLE_SKILL_KIT.md",
    ROOT / "registry/registry.json",
    ROOT / "registry/registry.yaml",
    ROOT / "registry/upgradeable_task_priors.json",
    ROOT / "audit/SELECTION_ONTOLOGY_REVIEW_v0.3.md",
)


def project_version() -> str:
    with (ROOT / "pyproject.toml").open("rb") as handle:
        return tomllib.load(handle)["project"]["version"]


def source_assets(version: str, package_dir: Path) -> tuple[Path, ...]:
    package_assets = (
        package_dir / f"upgradeables_registry-{version}-py3-none-any.whl",
        package_dir / f"upgradeables_registry-{version}.tar.gz",
    )
    return (*package_assets, *CANONICAL_ASSETS)


def checksum_text(paths: tuple[Path, ...]) -> str:
    lines = [f"{hashlib.sha256(path.read_bytes()).hexdigest()}  {path.name}" for path in paths]
    return "\n".join(lines) + "\n"


def expected_outputs(version: str, package_dir: Path, output_dir: Path) -> dict[Path, bytes]:
    sources = source_assets(version, package_dir)
    missing = [path for path in sources if not path.is_file()]
    if missing:
        raise FileNotFoundError(", ".join(str(path.relative_to(ROOT)) for path in missing))
    copied = tuple(output_dir / path.name for path in sources)
    outputs = {target: source.read_bytes() for source, target in zip(sources, copied, strict=True)}
    outputs[output_dir / f"SHA256SUMS_v{version}.txt"] = checksum_text(sources).encode("utf-8")
    return outputs


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--package-dir", type=Path, default=ROOT / "build/artifacts")
    parser.add_argument("--output-dir", type=Path)
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()

    version = project_version()
    if version != "0.3.0":
        print(f"release preparation refused: expected project version 0.3.0, found {version}", file=sys.stderr)
        return 1
    package_dir = args.package_dir.resolve()
    output_dir = (args.output_dir or ROOT / f"build/release-v{version}").resolve()
    try:
        outputs = expected_outputs(version, package_dir, output_dir)
    except FileNotFoundError as error:
        print(f"release preparation failed; missing asset(s): {error}", file=sys.stderr)
        return 1

    if args.check:
        stale = [path for path, content in outputs.items() if not path.is_file() or path.read_bytes() != content]
        if stale:
            print("release assets are missing or stale: " + ", ".join(path.name for path in stale), file=sys.stderr)
            return 1
        print(f"v{version} release asset check: OK ({len(outputs)} files)")
        return 0

    output_dir.mkdir(parents=True, exist_ok=True)
    for path, content in outputs.items():
        path.write_bytes(content)
    print(f"staged v{version} release assets in {output_dir} ({len(outputs)} files)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
