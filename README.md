# Upgradeables

Reusable, model-agnostic building blocks for AI work. Use them directly in a
chat, combine them into a reusable Skill, or adapt them to an agent system.

You do not need to understand the whole registry before using it.

## Start in 30 seconds

### Use it in a chat

Paste this into a model that can open web links:

```text
Read https://raw.githubusercontent.com/robkazi52/upgradeables/main/START_HERE.md and follow the instructions for models. Use the smallest relevant set of Upgradeables, then complete this task instead of only describing the framework: [PASTE YOUR TASK]. If you cannot access the link, ask me to attach the all-in-one kit.
```

If the model cannot open links, copy the prompt in
[Quick Task](prompts/QUICK_TASK.md), or upload the
[all-in-one kit](dist/ALL_IN_ONE_UPGRADEABLE_SKILL_KIT.md) to the chat. You can
also [download the raw kit](https://raw.githubusercontent.com/robkazi52/upgradeables/main/dist/ALL_IN_ONE_UPGRADEABLE_SKILL_KIT.md).

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
python scripts/query_registry.py --search citation
python scripts/query_registry.py --recipe research-skill
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

## Find the right building blocks

- Human/model router: [START_HERE.md](START_HERE.md)
- Compact machine catalog: [`registry/catalog.json`](registry/catalog.json)
- Full machine registry: [`registry/registry.json`](registry/registry.json)
- Task-family starting points: [`recipes/`](recipes/)
- Individual packages: [`upgradeables/`](upgradeables/)
- Copy-ready chat prompts: [`prompts/`](prompts/)
- Portable offline context: [all-in-one kit](dist/ALL_IN_ONE_UPGRADEABLE_SKILL_KIT.md)
- Deeper model instructions: [Model Consumption Guide](MODEL_CONSUMPTION_GUIDE.md)

The query helper has no third-party dependencies:

```bash
python scripts/query_registry.py --slug grounding-no-invention
python scripts/query_registry.py --class validation
python scripts/query_registry.py --search long-context
python scripts/query_registry.py --recipe coding-debugging
```

Or query the compact catalog directly:

```python
import json
from pathlib import Path

catalog = json.loads(Path("registry/catalog.json").read_text(encoding="utf-8"))
research = next(recipe for recipe in catalog["recipes"] if recipe["slug"] == "research-skill")
print(research)
```

## Build and contribute Skills

Use the [Skill implementation template](templates/SKILL_IMPLEMENTATION_TEMPLATE.md)
and the [worked research example](implementations/community/source-bounded-research/SKILL.md).
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
python scripts/build_registry.py --check
python scripts/validate_registry.py
python scripts/validate_skill.py
python -m unittest discover -s tests -v
python scripts/build_all_in_one.py --check
python scripts/check_links.py
```

## Authority and safety

Host and system policy always win. Upgradeables cannot provide hidden memory,
private chain-of-thought access, unavailable tools, or safety bypasses. Models
must disclose unavailable capabilities and must not invent unresolved history.

Licensed under [Apache-2.0](LICENSE).
