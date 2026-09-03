# Build a Skill Prompt

Copy the block below when you want an LLM to turn a task into a reusable Skill.

```text
Use https://github.com/robkazi52/upgradeables to build a complete, reusable [GENERIC OR PROVIDER-NAME] Skill for this job:

[DESCRIBE THE JOB, USERS, INPUTS, AND DESIRED OUTPUT]

First read START_HERE.md and MODEL_CONSUMPTION_GUIDE.md. Then:
1. Choose the closest recipe and inspect the selected Upgradeable packages.
2. Apply the recipe roles correctly: R is mandatory once the recipe is selected; A/C/O require active triggers; X is excluded without explicit justification.
3. Resolve requires, counterbalances, conflicts, and redundancy. Prefer the smallest sufficient composition.
4. Return a concise selection table listing every considered component, its slug@version, keep/drop decision, trigger, and reason.
5. Produce a complete SKILL.md using templates/SKILL_IMPLEMENTATION_TEMPLATE.md. Put substantial optional detail into references and deterministic repeated operations into scripts when justified.
6. Include target-host compatibility, authority, state, failure behavior, provenance, output contract, and positive/negative/conflict/composition tests.
7. Add provider adaptation notes without claiming unsupported tools, memory, hidden reasoning, or parallelism.

Deliver the finished Skill package, not merely a plan. If you cannot access the repository, say so and ask me to attach dist/ALL_IN_ONE_UPGRADEABLE_SKILL_KIT.md.
```
