# Semantic Profile Sources

The JSON files in this directory are hand-reviewed v0.2 semantic source data.
They are split only to keep the 96-package audit reviewable. The deterministic
`scripts/build_semantic_packages.py` renderer uses them to update package
metadata, documentation, examples, behavioral cases, source notes, and audit
reports.

Each profile must remain concept-specific and must label modern operational
interpretation separately from recovered historical mechanism.
