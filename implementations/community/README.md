# Community Skill Implementations

Add a model-agnostic Skill at `implementations/community/<skill-slug>/SKILL.md`.
Use [the Skill template](../../templates/SKILL_IMPLEMENTATION_TEMPLATE.md) and
review the [source-bounded research example](source-bounded-research/SKILL.md)
or the contrasting [ARC perception solver](arc-perception-solver/SKILL.md).

A contribution must identify its target compatibility, activation and failure
boundaries, selected `slug@version` components, provenance, output contract, and
behavioral tests. Supporting `references/`, `scripts/`, and `assets/` are optional.

Validate it before opening a pull request:

```bash
python scripts/validate_skill.py implementations/community/<skill-slug>
```

Provider-specific packages belong under `implementations/<provider>/`. Adapters
may change packaging but cannot redefine canonical Upgradeables.
