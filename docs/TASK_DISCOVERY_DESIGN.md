# Natural-Language Task Discovery Design

## Goal

Support a future command such as:

```bash
python scripts/query_registry.py --task "review this pull request for bugs and regressions"
```

and return one best-fit recipe plus required, likely, conditional, optional, and
excluded components with inspectable reasons. This is a discovery aid; the model
or user still confirms triggers and exclusion conditions before activation.

## Proposed output

```text
Best recipe: code-review
Why: matched pull request, bugs, regressions

Required: task-set-lock-in, scoped-loader, grounding-no-invention, invariance-stress-scaffold
Likely: anti-tunnel-vision, bidirectional-consistency, forethought-checkpoints
Conditional: critical-atomic-verification, fail-closed-abstention
Excluded: rewrite modules unless remediation was requested
```

JSON output should include the score, matched registry fields, recipe role,
trigger evidence, exclusion evidence, and package version for every result.

## Deterministic first implementation

1. Normalize task text and public display-name aliases without changing canonical slugs.
2. Score recipes using `display_name`, `purpose`, `task_family`, and curated task
   phrases. Prefer one coherent primary recipe over merged recipe stacks.
3. Resolve the recipe's R/A/C/O/X classifications.
4. Score package `best_fit_tasks`, triggers, purpose, OS role, keywords, and
   aliases. Penalize matches to `avoid_when` and explicit user negations.
5. Keep every R component for the selected recipe. Present A/C/O as candidates,
   not activated facts. Keep X excluded unless a positive trigger is explained.
6. Return deterministic tie-breaking and human-readable match reasons.

No API, embedding model, or network access should be required for the default
path. A later semantic adapter may rerank candidates, but it must preserve the
deterministic result, disclose the provider/model, and never silently override
hard exclusions or authority rules.

## Naming and alias contract

Canonical slugs remain stable identifiers. Plain-language display names and
search aliases improve recall but do not create new packages. Aliases need
collision tests, provenance, and a redirect/migration policy before any slug
change. Search results should always emit canonical `slug@version` values.

## Evaluation before release

Create a versioned set of realistic task queries with expected primary recipes,
required inclusions, important exclusions, and acceptable ties. Measure recipe
top-1/top-3 recall, package precision, exclusion violations, and explanation
coverage. Include simple tasks that should recommend no recipe so the feature
does not become an over-scaffolding engine.

## Delivery stages

1. Curate task phrases and an evaluation fixture.
2. Add deterministic scoring and `--task`, `--json`, and `--explain` behavior.
3. Test aliases, negation, ties, no-match, and stable ordering.
4. Trial optional semantic reranking only after the deterministic baseline is measured.
