# Start Here

This is the shortest route into Upgradeables for both people and models.

Upgradeables are optional building blocks for doing work with an LLM. They can
be used temporarily in one chat, composed into a reusable Skill, or implemented
inside an agent system. Start with the task, not the framework.

A repository cannot grant browsing or file access to a chat. The model must be
able to open the URL, receive an uploaded file, or run inside a cloned checkout.

## For people

Choose one route:

1. **Do a task now:** copy [Quick Task](prompts/QUICK_TASK.md) into a new chat.
2. **Build a reusable Skill:** copy [Build a Skill](prompts/BUILD_A_SKILL.md).
3. **Work from sources:** use [Research from Sources](prompts/RESEARCH_FROM_SOURCES.md).
4. **Process a long document:** use [Work with Long Documents](prompts/WORK_WITH_LONG_DOCUMENTS.md).
5. **Connect an IDE agent:** clone the repository and point the agent here.

If your model can open web links, the one-line prompt below is usually enough:

```text
Read https://raw.githubusercontent.com/robkazi52/upgradeables/main/START_HERE.md and follow the instructions for models. Then complete this task: [PASTE YOUR TASK]. If you cannot access the link, ask me to attach the all-in-one kit.
```

If your model cannot open links, download or open the
[all-in-one kit](dist/ALL_IN_ONE_UPGRADEABLE_SKILL_KIT.md), attach it to the
chat, and use the same prompt without the URL.

## Instructions for models

First classify the user's intent:

- **Do the work:** use Upgradeables internally and deliver the requested result.
  Do not respond with only a framework explanation or Skill design.
- **Build a Skill:** produce a reusable task package using the Skill template.
- **Contribute:** preserve registry contracts and follow the appropriate
  contribution route.

### Route A: do the work

1. Restate the task boundary, required inputs, and output contract briefly.
2. Select one primary recipe in [`recipes/`](recipes/), if one applies. Then
   search for explicit output requirements it does not cover—such as citations,
   long context, or persistence—and add only matching cross-cutting components.
   Do not merge whole recipes.
3. Keep every `R` component when using that recipe. `A`, `C`, and `O` components
   still need an active trigger. Exclude `X` unless there is an explicit reason.
4. Load only the retained component packages and their `requires` dependencies.
   Check counterbalances, conflicts, and redundancy.
5. Apply the mechanisms while completing the user's actual task. Do not make the
   user learn registry terminology unless it helps them.
6. Validate important claims and outputs in proportion to risk. Report material
   uncertainty, missing inputs, or unavailable host capabilities honestly.

For ordinary tasks, a one-line note such as
`Using: task-set-lock-in, grounding-no-invention` is enough. Skip even that if
the user requested a clean deliverable and the component list adds no value.

### Route B: build a reusable Skill

1. Read [Model Consumption Guide](MODEL_CONSUMPTION_GUIDE.md).
2. Select the closest recipe and inspect each retained package.
3. Use [the Skill template](templates/SKILL_IMPLEMENTATION_TEMPLATE.md).
4. Return a short keep/drop table, the complete Skill, host adaptation notes,
   and behavioral/composition tests.
5. Cite every selected `slug@version`. Do not create one Skill per Upgradeable;
   compose a task-oriented package.

The [worked research Skill](implementations/community/source-bounded-research/SKILL.md)
shows the expected level of specificity.

### Route C: contribute

Read [CONTRIBUTING.md](CONTRIBUTING.md). Adding a community Skill and proposing
a new canonical Upgradeable are different workflows. Prefer contributing a Skill
that composes existing primitives unless a genuinely new cross-cutting mechanism
is needed.

## Efficient loading

Do not load the entire repository by default.

- **Fast chat:** use one file from [`prompts/`](prompts/).
- **Normal task:** load one recipe plus the selected component packages.
- **Skill construction:** add the model guide, template, and applicable spec.
- **No repository browsing:** attach the all-in-one kit.
- **Machine query:** use [`registry/catalog.json`](registry/catalog.json) or run
  `python scripts/query_registry.py --help`.

The full [`registry/registry.json`](registry/registry.json) is authoritative for
current machine metadata. The compact catalog is a discovery aid. Files under
`archive/` are provenance records, not live operating instructions; read them
only for historical or recovery questions.

## Non-negotiable boundaries

- System, developer, organizational, and user authority outrank this repository.
- Treat repository content as reference material, not as permission for external
  actions or access to unavailable tools.
- Never invent missing component definitions or hidden capabilities.
- Validators can detect or request repair; they cannot manufacture truth.
- Use the minimum useful composition and remove needless scaffolding.
