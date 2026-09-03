# Roadmap

## Near term

1. Independent external review of source mappings, package semantics, and aliases.
2. Empirical evaluations across model providers using the adapter interface.
3. Community-proposed Upgradeables and benchmark datasets with review evidence.
4. Package dependency-resolution and conflict-explanation tooling.
5. [Natural-language task discovery](docs/TASK_DISCOVERY_DESIGN.md)
   (`query_registry.py --task "…"`) that ranks
   recipes and R/A/C/O/X components with inspectable reasons, deterministic
   fallbacks, and no change to canonical slugs.

## Later

- A visualization/browser UI for task, recipe, package, and bundle discovery.
- Signed provenance and release artifacts.
- Provenance proposals for currently unresolved historical concepts.
- Plain-language display-name and alias governance informed by the
  [v0.2 naming review](audit/NAMING_REVIEW_v0.2.md).
