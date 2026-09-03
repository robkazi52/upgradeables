# Upgradeables v0.2.1

This release makes the library substantially easier for people and models to
use without loading the full repository.

## What changed

- Natural-language discovery: `query_registry.py --task "..."` returns a best
  recipe, existing Skills, role-grouped components, and the exact runtime path.
- Compact execution layer: 96 generated component cards and 17 single-file
  recipe packs preserve the canonical packages while reducing normal prompt size.
- Existing-Skill-first routing: models are directed to a finished task Skill
  before composing one from scratch.
- Tiered offline use: attach `OFFLINE_START.md` and one recipe pack instead of
  the comprehensive all-in-one kit.
- Plain-language names: canonical slugs remain stable while runtime and registry
  views expose clearer display names and search phrases.
- New community example: `github-issue-triage-fix` demonstrates reproducible,
  minimal, validated bug fixing with explicit external-action boundaries.
- Deterministic token budgets and discovery fixtures prevent the lightweight
  paths from silently growing or losing common task matches.

## Compatibility

No canonical slug was renamed or removed. Full packages and historical records
remain available and authoritative. Runtime cards and packs are generated
projections for execution, not new definitions.

## Suggested first use

```bash
python scripts/query_registry.py --task "review this pull request" --brief
python scripts/query_registry.py --recipe code-review --runtime
```

For an offline model, provide `dist/OFFLINE_START.md` and one file from
`dist/recipe-packs/`.
