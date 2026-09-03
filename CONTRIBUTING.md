# Contributing

Community members, research groups, and companies are welcome to contribute.
There are two distinct routes.

## Add a Skill implementation

Choose this route when you have a task-oriented workflow composed from existing
Upgradeables.

1. Search [`registry/catalog.json`](registry/catalog.json) and select the closest
   [recipe](recipes/).
2. Copy [the Skill template](templates/SKILL_IMPLEMENTATION_TEMPLATE.md).
3. Put a model-agnostic implementation in
   `implementations/community/<skill-slug>/`, or a host-specific implementation
   in `implementations/<provider>/<skill-slug>/`.
4. Include `SKILL.md`. Add `references/`, `scripts/`, or `assets/` only when the
   Skill actually needs them.
5. List target-host compatibility, selected `slug@version` components,
   activation and failure boundaries, provenance, and behavioral tests.
6. Run the validation commands in [README.md](README.md), then open a pull
   request. Validate the Skill directly with
   `python scripts/validate_skill.py implementations/community/<skill-slug>`.
   You may start with the
   [new Skill issue form](https://github.com/robkazi52/upgradeables/issues/new?template=new_skill.yml).

See the [worked research Skill](implementations/community/source-bounded-research/SKILL.md).
Adding a Skill does not require changing canonical registry metadata.

## Contribute empirical evidence

Evidence may motivate a recipe or test but does not redefine historical package
semantics. Put study reports under [`evidence/`](evidence/) and include the task
manifest, prompts or hashes, model/build identifiers, inference parameters, raw
outputs, grader source, per-run results, dates, and an aggregation command where
licensing permits. Label retrospective, exploratory, confirmatory, and independently
reproduced evidence distinctly. Reconcile aggregate totals before making comparative
claims, cite external baselines, and disclose missing artifacts explicitly.

## Propose a new Upgradeable

Choose this route only for a reusable cross-cutting mechanism that cannot be
represented by composing current primitives.

1. Search the full [`registry/registry.json`](registry/registry.json) for prior
   art, aliases, conflicts, and historical records.
2. Open the [new Upgradeable issue form](https://github.com/robkazi52/upgradeables/issues/new?template=new_upgradeable.yml)
   or copy [the proposal template](templates/UPGRADEABLE_PROPOSAL_TEMPLATE.md).
3. Explain the identifiable trigger, bounded behavior, interface, predictable
   result, failure boundary, tests, and reason it is not a recipe or setting.
4. Let maintainers coordinate the canonical ID and registry generation during
   review; do not reuse historical IDs.
5. Add package metadata, documentation, tests, and generated registry changes as
   agreed in the proposal.

## General rules

Preserve canonical IDs and slugs when improving terminology. Propose clearer
display names and aliases using the principles in the
[v0.2 naming review](audit/NAMING_REVIEW_v0.2.md); path changes require an
explicit versioned migration and redirect plan.

Fork and branch from `main`, keep pull requests focused, and use the pull request
checklist. Do not invent missing history, collapse acronym collisions, claim host
capabilities that are not present, or let a validator add unsupported facts.
Do not turn an exploratory benchmark into a universal superiority claim.

By contributing, you agree that your contribution is licensed under Apache-2.0.
