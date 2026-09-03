# Upgradeables

Reusable, model-agnostic building blocks for AI work. Use them directly in a
chat, combine them into a reusable Skill, or adapt them to an agent system.

You do not need to understand the whole registry before using it.

Want to experiment first? Open [Try These Five Things](TRY_IT.md).

## Start in 30 seconds

### Use it in a chat

Paste this into a model that can open web links:

```text
Read https://raw.githubusercontent.com/robkazi52/upgradeables/main/START_HERE.md and follow the model route. Then complete this task: [PASTE YOUR TASK].
```

If the model cannot open links, copy [Quick Task](prompts/QUICK_TASK.md), or
upload [Offline Start](dist/OFFLINE_START.md) plus the one matching compact
file from [`dist/recipe-packs/`](dist/recipe-packs/). The
[all-in-one kit](dist/ALL_IN_ONE_UPGRADEABLE_SKILL_KIT.md) remains available for
deep offline inspection, but is intentionally much larger.

### Build a reusable Skill

Copy [Build a Skill](prompts/BUILD_A_SKILL.md) into a new chat. It asks the
model to select components, explain keep/drop decisions, produce a complete
`SKILL.md`, and define behavioral tests.

### Use it from an IDE or agent

Clone the repository. Agents should discover [AGENTS.md](AGENTS.md), while
GitHub Copilot receives [repository instructions](.github/copilot-instructions.md).
The universal model entrypoint is [START_HERE.md](START_HERE.md).

```bash
git clone https://github.com/robkazi52/upgradeables.git
cd upgradeables
python scripts/query_registry.py --task "review this pull request" --brief
python scripts/query_registry.py --recipe code-review --runtime
```

## What is an Upgradeable?

An Upgradeable is an optional capability with a defined trigger, inputs,
outputs, procedure, compatibility rules, failure boundary, and tests. Examples
include task locking, source grounding, citation checking, drift control,
structured state, and bounded repair.

Skills perform jobs. Upgradeables are building blocks used inside those Skills.

| Layer | What it does |
|---|---|
| Skill | Performs a task for a user |
| Upgradeable | Adds one reusable capability or control |
| Behavior Gene | Sets a recurring behavior or reasoning style |
| Core | Supplies domain reasoning and reference knowledge |
| Validator | Checks, scores, vetoes, or requests repair |
| Recipe | Suggests a minimal starting composition for a task family |
| OS / bundle | Coordinates a larger operating environment |

## How to choose Upgradeables

Use one of three short discovery paths:

- **Task → Recipe → Upgradeables:** start in [`recipes/`](recipes/) for a
  reviewed task-family composition, then retain only components with active triggers.
- **Upgradeable → Purpose / OS Fit / Tasks / Interactions:** search the compact
  catalog, inspect a package's placement and exclusions, then follow explained links.
- **Bundle → Curated multi-Upgradeable composition:** start in [`bundles/`](bundles/)
  when the task genuinely needs a coordinated subsystem rather than one capability.

## Find the right building blocks

- Human/model router: [START_HERE.md](START_HERE.md)
- Tiny machine router: [`runtime/router.json`](runtime/router.json)
- Compact runtime cards and recipe packs: [`runtime/`](runtime/)
- Compact machine catalog: [`registry/catalog.json`](registry/catalog.json)
- Full machine registry: [`registry/registry.json`](registry/registry.json)
- Task-family starting points: [`recipes/`](recipes/)
- Individual packages: [`upgradeables/`](upgradeables/)
- Plain-language name recommendations: [v0.2 naming review](audit/NAMING_REVIEW_v0.2.md)
- Copy-ready chat prompts: [`prompts/`](prompts/)
- Low-context offline start: [Offline Start](dist/OFFLINE_START.md)
- Comprehensive offline reference: [all-in-one kit](dist/ALL_IN_ONE_UPGRADEABLE_SKILL_KIT.md)
- Deeper model instructions: [Model Consumption Guide](MODEL_CONSUMPTION_GUIDE.md)

The query helper has no third-party dependencies:

```bash
python scripts/query_registry.py --slug grounding-no-invention
python scripts/query_registry.py --class validation
python scripts/query_registry.py --search long-context
python scripts/query_registry.py --recipe coding-debugging
python scripts/query_registry.py --task "triage and fix this GitHub issue" --brief
python scripts/query_registry.py --search "long context" --brief --limit 5
```

Or query the compact catalog directly:

```python
import json
from pathlib import Path

registry = json.loads(
    Path("registry/registry.json").read_text(encoding="utf-8")
)

research = next(
    recipe["classifications"]
    for recipe in registry["recipes"]
    if recipe["slug"] == "research-skill"
)
```

## Evidence

The repository now preserves preliminary, author-reported experiments that
motivated several composition choices. The ARC report describes one-shot grid
reasoning runs and a small within-session comparison in which focused directives
matched or exceeded a more elaborate prompt on three of five ARC-AGI-2 tasks.

These reports are not independently reproduced: raw runs and grader artifacts
are not yet archived, and the supplied ARC-AGI-1 totals contain discrepancies.
Read the [evidence status and methodology limits](evidence/) before citing any
number. See [Design Principles](DESIGN_PRINCIPLES.md) for the deliberately narrow
hypotheses the results motivate.

## Build and contribute Skills

Use the [Skill implementation template](templates/SKILL_IMPLEMENTATION_TEMPLATE.md)
and the [worked community examples](implementations/community/), covering research,
coding/debugging, GitHub issue fixing, long-context analysis, creative ideation,
high-stakes evidence, Skill architecture, and ARC-style perception reasoning.
Community members and companies can contribute complete Skills without changing
the canonical Upgradeable registry. See [CONTRIBUTING.md](CONTRIBUTING.md) for the
separate Skill and Upgradeable contribution paths.

```bash
python scripts/validate_skill.py implementations/community/source-bounded-research
```

Before proposing a new primitive, search the registry and explain why composing
existing building blocks is insufficient. Historical names and unresolved ideas
are preserved rather than guessed or silently rewritten.

## Validate locally

Requires Python 3.11+ and no runtime dependencies:

```bash
python scripts/build_semantic_packages.py --check
python scripts/build_ecosystem_reviews.py --check
python scripts/build_registry.py --check
python scripts/build_runtime.py --check
python scripts/validate_registry.py
python scripts/validate_behavior_cases.py
python scripts/run_deterministic_package_checks.py
python scripts/audit_semantic_specificity.py
python scripts/validate_skill.py
python -m unittest discover -s tests -v
python scripts/build_all_in_one.py --check
python scripts/build_release_assets.py --check
python scripts/check_links.py
```

## Give this repo to an LLM

Point the model to [Start Here](START_HERE.md). It will use the tiny router, an
existing Skill, or one compact runtime recipe. For offline use, attach
[Offline Start](dist/OFFLINE_START.md) and one recipe pack. Use the full registry
and all-in-one kit only for deep inspection or contribution work.

## Authority and safety

Host and system policy always win. Upgradeables cannot provide hidden memory,
private chain-of-thought access, unavailable tools, or safety bypasses. Models
must disclose unavailable capabilities and must not invent unresolved history.

Licensed under [Apache-2.0](LICENSE).
