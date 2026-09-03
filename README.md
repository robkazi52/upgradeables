# Upgradeables

An open, model-agnostic registry of composable reasoning, state, validation,
retrieval, editing, orchestration, and behavioral primitives for building AI
Skills and agent workflows.

> Skills define jobs. Behavior Genes define how a system behaves for a class of
> tasks. Cores define domain reasoning and evidence knowledge. Upgradeables
> define reusable capabilities and controls. Validators enforce integrity.
> Orchestrators compose them. OS bundles create complete operating environments.

This is not a prompt library and does not claim guaranteed model improvement.
It is a specification, registry, and contribution system for turning reusable
architecture into explicit, auditable mechanisms.

## The short version

An **Upgradeable** is a reusable primitive with an activation boundary, inputs,
outputs, mechanism, failure boundary, compatibility rules, and tests. A **Skill**
is a task-oriented implementation package assembled from task identity, behavior,
knowledge, selected Upgradeables, state, validation, and an output contract.

```text
Host model / system policy
            |
       OS or Skill bundle
            |
         Task shell
     +------+------+------+
     |             |      |
Behavior Gene    Core  Upgradeables <-> Explicit state
     +-------------+------+
                   |
               Validators
                   |
                 Output
```

| Concept | Responsibility |
|---|---|
| OS | Compositional operating environment and authority layer |
| Skill | A task-oriented package that performs a job |
| Upgradeable | A reusable cross-cutting capability or control |
| Behavior Gene | A recurring behavior and reasoning pattern |
| Core | High-density domain reasoning, evidence, and reference material |
| Validator | Checks, scores, vetoes, or requests repair; never manufactures truth |
| Orchestrator | Selects, sequences, coordinates, and resolves module authority |

## Use the registry

- Browse [96 operational packages](upgradeables/) by functional area.
- Query [`registry/registry.json`](registry/registry.json) from any JSON-capable tool.
- Use [`registry/registry.yaml`](registry/registry.yaml) where YAML is preferred. It
  is emitted as a JSON-compatible YAML subset so builds require only Python.
- Start from a [Skill recipe](recipes/) or a curated [bundle](bundles/).
- Give a frontier model the repository URL plus [`MODEL_CONSUMPTION_GUIDE.md`](MODEL_CONSUMPTION_GUIDE.md),
  or ingest the generated [all-in-one kit](dist/ALL_IN_ONE_UPGRADEABLE_SKILL_KIT.md).

Example query:

```python
import json
from pathlib import Path

    registry = json.loads(Path("registry/registry.json").read_text(encoding="utf-8"))
    research = next(
        recipe["classifications"] for recipe in registry["recipes"]
        if recipe["slug"] == "research-skill"
    )
```

## Build a Skill

1. Choose the Skill archetype, task boundary, risk tier, evidence sensitivity, and
   state needs.
2. Select a Behavior Gene and Core only when the task needs them.
3. Load foundational and task-specific Upgradeables.
4. Add risk-appropriate validators and check dependencies, counterbalances,
   conflicts, and redundancy.
5. Remove unnecessary scaffolding, choose an implementation form for each
   component, and generate the target Skill package.
6. Add positive, negative, conflict, long-context, and composition tests.

The complete procedure is in [Skill Translation](spec/SKILL_TRANSLATION_SPEC.md).
Provider mappings are adapter layers under [`implementations/`](implementations/).

## Contribute

Community additions are welcome: new primitives, modes, recipes, bundles, tests,
and provider-specific Skill implementations. Before proposing a primitive, search
the registry and explain why existing composition is insufficient. Start with
[CONTRIBUTING.md](CONTRIBUTING.md) and the [proposal template](templates/UPGRADEABLE_PROPOSAL_TEMPLATE.md).

Historical names and IDs are never silently rewritten. The three canonical source
documents are preserved byte-for-byte in [`archive/source/`](archive/source/), and
the [source map](archive/SOURCE_TO_REGISTRY_MAP.md) records normalization decisions.
Unresolved concepts remain explicitly unresolved.

## Validate locally

Requires Python 3.11+ and no runtime dependencies:

```bash
python scripts/build_registry.py --check
python scripts/validate_registry.py
python -m unittest discover -s tests -v
python scripts/build_all_in_one.py --check
python scripts/check_links.py
```

To rebuild generated artifacts, omit `--check` from the build commands.

## Authority and safety

Upgradeables operate beneath host/system policy authority. They cannot provide
hidden memory, hidden channels, private chain-of-thought access, or safety bypasses.
Parallel and persistent behavior must correspond to real host capabilities.

Licensed under [Apache-2.0](LICENSE).
