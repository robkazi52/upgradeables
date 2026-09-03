# Build a Skill Prompt

Copy the block below when you want an LLM to turn a task into a reusable Skill.

```text
Use https://github.com/robkazi52/upgradeables to build a complete, reusable [GENERIC OR PROVIDER-NAME] Skill for this job:

[DESCRIBE THE JOB, USERS, INPUTS, AND DESIRED OUTPUT]

First read START_HERE.md and MODEL_CONSUMPTION_GUIDE.md. Then:
1. Check implementations/community for an existing task Skill to reuse or adapt.
2. If none fits, query the task and open one compact runtime recipe pack. Inspect a full Upgradeable package only when deeper implementation detail is necessary.
3. Apply recipe roles correctly: R is structurally required but can remain dormant until its phase trigger; A/C/O require active triggers; X needs explicit justification.
4. Resolve requires, counterbalances, conflicts, and redundancy. Prefer the smallest sufficient composition.
5. Return a concise table listing component, version, keep/drop decision, trigger, and reason.
6. Produce a complete SKILL.md using templates/SKILL_IMPLEMENTATION_TEMPLATE.md. Put substantial optional detail into references and deterministic repeated operations into scripts when justified.
7. Include target-host compatibility, authority, state, failure behavior, provenance, output contract, and positive/negative/authority/failure/composition tests.

Deliver the finished Skill package, not merely a plan. If you cannot access the repository, ask me for dist/OFFLINE_START.md and the matching dist/recipe-packs file.
```
