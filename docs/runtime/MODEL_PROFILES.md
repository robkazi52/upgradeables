# Model profiles

Runtime model profiles control instruction density. They are not intelligence
ratings, provider endorsements, or claims that one model can be transformed
into another.

The canonical data is [model_profiles.json](../../runtime/model_profiles.json).

| Profile | Initial level | Intended use |
| --- | --- | --- |
| `small` | `full` | More explicit procedure and concrete checkpoints |
| `medium` | `standard` | Ordinary model and agent use |
| `strong` | `micro` | Compressed scaffolding with mandatory invariants retained |
| `auto` | `standard` | Safe medium fallback until reliable adapter metadata is used |
| `custom` | `standard` | Placeholder fallback for caller-owned policy |

## What changes

Each runtime representation may provide three levels:

- `micro`: the shortest useful directive form;
- `standard`: ordinary procedural detail;
- `full`: expanded but still compact execution scaffolding.

Mandatory invariants remain independently represented and survive density
compression and semantic deduplication. A profile affects instruction detail;
it does not grant tools, state, context length, parallel workers, or knowledge.

## Other ceilings

A requested profile is only the starting point:

- v0.3 complexity `L0` forces `micro`;
- v0.3 complexity `L1` caps density at `standard`;
- a component's `maximum_default_verbosity` may impose a lower cap;
- the directive budget may lower levels further;
- a missing required host capability suppresses ordinary directives from that
  component and produces a warning.

The selected level for every active component is recorded in the plan.

## `auto` and `custom` today

The current compiler does not infer a tier from a model name or query provider
metadata. `auto` resolves to the same initial level as `medium`. `custom` also
uses `standard`; there is not yet a custom policy callback or profile document
in the core API.

Applications may choose a profile explicitly, but should record that choice as
configuration rather than empirical fact.

## Future evidence-backed profiles

Provider/model-specific profiles, if added, belong under a separate evidence
surface and should contain model identifier/snapshot, suite versions, sample
counts, observed failure modes, tested controls, effect estimates, limitations,
and date. Do not derive one from marketing names or a single run, and do not
silently change the generic profile meanings.

## CLI and Python

```bash
upgradeables runtime profiles --format json
upgradeables runtime compile "task" --model-profile strong
```

```python
plan = compile_task("task", model_profile="small")
```

Use [Evaluation](EVALUATION.md) to test profile choices on a frozen task suite.
