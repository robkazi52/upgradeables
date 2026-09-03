# Model Consumption Guide

[START_HERE.md](START_HERE.md) is the universal router. Use this guide when
building a reusable Skill, adapting the library, or resolving a difficult
composition decision.

## Load the least context that can do the job

| Need | Load |
|---|---|
| Discover a route | [`runtime/router.json`](runtime/router.json) or `query_registry.py --task` |
| Execute a known task family | One [`runtime/recipes/`](runtime/recipes/) pack |
| Add one missing behavior | One [`runtime/components/`](runtime/components/) card |
| Use a finished workflow | One [`implementations/community/`](implementations/community/) Skill |
| Inspect or contribute | Full package, specs, and registry records as needed |
| Work offline | [`dist/OFFLINE_START.md`](dist/OFFLINE_START.md) plus one recipe pack |

Do not load parallel representations of the same selection. The source recipe,
resolved recipe, runtime recipe, registry, and all-in-one kit overlap. The
all-in-one kit is a comprehensive archive-style fallback, not the normal prompt.
Never load `archive/` for routine execution.

Useful commands:

```bash
python scripts/query_registry.py --task "review this pull request" --brief
python scripts/query_registry.py --task "fix this reported bug" --paths-only
python scripts/query_registry.py --search "long context" --brief --limit 5
python scripts/query_registry.py --recipe research-skill --runtime
```

## Deterministic selection

1. Identify the task, output, source boundary, risk, and available capabilities.
2. Prefer an existing task Skill. Otherwise choose one primary recipe.
3. Keep every `R` component after selecting the recipe. `R` means structurally
   required, not continuously active: a phase-specific component can remain
   dormant until its trigger occurs. Reject the recipe if that trigger cannot
   occur in this workflow.
4. Keep `A`, `C`, or `O` only when its observable trigger applies. Normally drop
   `X`. Add individual cross-cutting components only for explicit uncovered
   requirements; never merge whole recipes.
5. Resolve `requires`, precedence, counterbalances, conflicts, and redundancy.
   Remove every non-required component without an active trigger.
6. Apply the retained mechanisms and run risk-appropriate checks. Do not claim
   hidden memory, private reasoning, unavailable tools, or simulated agents.

## Skill-building contract

Use [the Skill template](templates/SKILL_IMPLEMENTATION_TEMPLATE.md). Return:

1. a compact table with component, version, keep/drop decision, trigger, and reason;
2. a complete task-oriented `SKILL.md`, not one wrapper per Upgradeable;
3. only necessary references, deterministic scripts, or assets;
4. target-host limits, authority, state, failure states, provenance, and output;
5. positive, negative, authority, failure, and composition tests.

See [source-bounded research](implementations/community/source-bounded-research/SKILL.md),
[ARC perception](implementations/community/arc-perception-solver/SKILL.md), and
[GitHub issue triage and fix](implementations/community/github-issue-triage-fix/SKILL.md).

## Selection cautions

Confirm actual purpose, trigger, exclusion, OS placement, and task fit instead of
matching only a name. `modern-interpretation` and `provisional` mechanisms must
not be presented as recovered historical definitions. Validators can detect or
request repair; they cannot manufacture evidence. Host policy and user authority
always win.

Preliminary author-reported experiments in [`evidence/`](evidence/) are design
signals, not independent proof. Prefer the shortest control that targets an
observed failure while preserving its invariant.
