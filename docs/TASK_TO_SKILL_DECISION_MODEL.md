# Task-to-Skill decision model

Status: v0.3 research synthesis. This is a deterministic packaging model for the
project harness and future `upgradeables skill suggest`; it is not evidence that
packaging a workflow as a Skill improves its outcomes.

## Purpose

The harness must distinguish the work a user wants from the way that work is
packaged. A `code-review` task can be completed once, invoked through a reusable
prompt, standardized as a project Skill, or delegated to a specialist agent.
Those are different decisions.

The model uses only explicit task descriptions, project configuration, Skill
metadata, and opt-in project task-event records. It does not infer hidden memory,
private chain-of-thought, or latent learning.

## Packaging vocabulary

| Form | What it supplies | Appropriate when | Not sufficient when |
|---|---|---|---|
| One-off task | Current goal and inputs | Work is unique, simple, or not yet stable | The same procedure must be rediscovered repeatedly |
| Reusable prompt | Repeatable wording and input slots | Request shape repeats but execution is shallow | Conditional procedure, references, or tools matter |
| Project instructions | Small always-on set of repository facts and universal rules | Guidance applies to nearly every task in its scope | Guidance belongs to one occasional workflow |
| Skill | Discoverable, conditional procedure with optional references, scripts, assets, and tests | A recognizable task recurs with stable boundaries and completion checks | New executable capability or durable specialist isolation is required |
| Script or hook | Deterministic transformation, check, or trigger | Inputs, outputs, and failure behavior are mechanically defined | The main work requires judgment |
| Tool or MCP package | External data or executable capability | The agent must query or act on another system | Instructions alone can complete the task |
| Custom agent | Persistent specialist prompt, context, and tool boundary | A stable role needs separation beyond conditional instructions | A general agent activating a Skill is sufficient |
| Runtime subagent | Isolated delegated work inside a larger task | Work is bounded and independent or benefits from isolated context | Steps are tiny, sequential, or share rapidly changing state |
| Orchestration | Routing, handoffs, and synthesis across roles | Several genuinely separable responsibilities must coordinate | A single agent, Skill, or deterministic workflow is adequate |

Prompts, resources, tools, Skills, and agents may be composed, but they are not
synonyms. Prose cannot create a tool, permission, external memory, or durable
state that the host does not provide.

## Decision sequence

Apply these questions in order:

1. **Is this only the current task?** Keep it one-off unless an explicit
   standardization request or eligible recurring pattern exists.
2. **Does only the wording/input frame repeat?** Use a prompt template.
3. **Does the guidance apply to nearly every project task?** Put the smallest
   stable version in project instructions.
4. **Is there a conditional, recognizable job with a stable procedure and output
   contract?** Consider a Skill.
5. **Can a step be made deterministic?** Package that step as a script, hook, or
   validator and let the Skill call it when useful.
6. **Is external context or action capability missing?** Add a resource or
   tool/MCP package with explicit compatibility and permissions.
7. **Does the work need a durable specialist context or distinct tool boundary?**
   Consider a custom agent.
8. **Does this run contain bounded independent work?** Consider a subagent.
9. **Are several roles, handoffs, and synthesis genuinely required?** Only then
   consider orchestration.

Choose the least complex form that supplies the missing capability.

## Skill eligibility gate

`skill suggest` may emit a candidate only when every hard condition is met:

- Task-event recording was explicitly enabled.
- The configured recurrence threshold is met; the default is three comparable
  events.
- The events describe the same user job, not merely the same broad domain.
- A positive activation boundary and at least one useful non-trigger can be
  stated.
- Required inputs and missing-input behavior are known.
- The central procedure is stable enough to encode without inventing project
  semantics.
- A meaningful output contract or completion check exists.
- No existing validated project/community Skill already covers the job with a
  compatible boundary.

Meeting the recurrence threshold begins evaluation; it does not by itself make
the workflow eligible.

## Explicit evidence used by `skill suggest`

The suggestion engine may use these project-local facts:

```text
event_id
timestamp
normalized_task
task_archetype
selected_recipe
environment_modifiers
explicit project constraints
requested output shape
skill_used
user/agent override
outcome, only when explicitly supplied
```

It must not record or analyze private reasoning. Raw task text should remain
local and may be omitted from summaries when the normalized task is sufficient.

## Recurrence grouping

Group events with transparent, deterministic keys:

```text
primary task archetype
+ selected recipe or direct path
+ stable project constraint signature
+ requested output-contract signature
+ authority mode (review / edit / external action)
```

Broad lexical overlap is not enough. For example, “review this API change” and
“implement this API change” have different authority modes. “Research the five
named papers” and “survey the open web” have different source boundaries.

For each group report exact counts, date range, representative event IDs,
variation in modifiers, existing Skills considered, and failed eligibility
conditions. Do not generate a probabilistic confidence score.

## Positive suggestion signals

These signals are ordinal and explainable:

- repeated task boundary;
- repeated primary recipe or stable direct path;
- stable required inputs;
- stable project references or commands;
- repeated output schema or handoff format;
- repeated validators or acceptance checks;
- repeated tool/capability needs;
- repeated exclusions, such as review-only or closed-source;
- repeated user corrections that can become an explicit boundary;
- clear maintenance owner or source of truth.

## Suppression signals

Do not suggest a Skill when any material condition applies:

- occurrences share only a broad topic;
- requirements or procedure are still changing substantially;
- the task is trivial and a prompt or command is enough;
- guidance belongs in universal project instructions;
- the repeated step is deterministic and should be a script;
- the workflow primarily needs a missing external tool;
- a validated compatible Skill already exists;
- packaging would embed secrets, private data, or unstable generated state;
- activation cannot be distinguished from adjacent tasks;
- success cannot be evaluated even at a basic behavioral level;
- the proposed Skill would merely wrap one Upgradeable without performing a
  recognizable job.

## Choosing project, personal, or community scope

| Scope | Choose when | Required boundary |
|---|---|---|
| Project | Paths, commands, policies, schemas, or references are repository-specific | Keep local assumptions explicit and versioned |
| Personal | The workflow reflects one user's stable cross-project preference | Do not present personal conventions as project authority |
| Community/global | The task contract remains useful without private project context | Declare compatibility and provide portable fallbacks |

A project Skill may select global Upgradeables by canonical `slug@version` while
keeping local references and commands in the project package.

## When a Skill should contain another package

- Put a stable algorithmic check in `scripts/` rather than re-describing it in
  prose on every run.
- Put detailed or domain-specific material in focused `references/` files and
  state exactly when each should be loaded.
- Put templates and fixed resources in `assets/`.
- Connect an MCP/tool only when external data or execution is genuinely needed.
- Keep host-specific adapters outside the portable core where practical.
- Keep `SKILL.md` focused on activation, procedure, authority, failure handling,
  and output. Avoid deep reference chains.

Skill activation never grants additional read, write, send, deploy, or transact
authority. Those permissions come from the current task and host.

## Skill-to-agent and orchestration gate

Keep a workflow as a Skill unless a custom agent adds at least one necessary
property:

- distinct context isolation;
- distinct tool or permission boundary;
- stable specialist role across multiple related Skills;
- adaptive multi-step control with explicit stop/retry behavior;
- a real handoff contract to or from another actor.

Use a runtime subagent only for a bounded objective with provided context,
allowed tools, expected output, and a stop condition. Use orchestration only
when workstreams are genuinely separable and synthesis is specified. Agent or
subagent availability alone is never a promotion signal.

## Suggestion output contract

Human output should resemble:

```text
Candidate Skill: api-safe-dependency-review
Scope: project
Observed comparable events: 4
Date range: 2026-07-10 to 2026-08-28
Primary job: review dependency updates for API compatibility
Primary recipe: code-review
Stable modifiers: review_only, public_api_or_schema
Stable inputs: dependency diff, API contract, relevant tests
Output contract: prioritized findings with evidence; no edits
Existing Skills checked: code-review (boundary too general)
Why a Skill: conditional recurring procedure with project references
Why not instructions: not relevant to most project tasks
Why not an agent: no distinct context or tool boundary required
Next: upgradeables skill scaffold api-safe-dependency-review --task "..."
```

Stable JSON should include:

```json
{
  "status": "candidate",
  "packaging_form": "project-skill",
  "slug": "api-safe-dependency-review",
  "event_ids": ["evt-12", "evt-18", "evt-23", "evt-31"],
  "occurrence_count": 4,
  "task_archetype": "code-review",
  "recipe": "code-review",
  "stable_modifiers": ["review_only", "public_api_or_schema"],
  "eligibility_checks": {
    "recurrence": "pass",
    "activation_boundary": "pass",
    "stable_inputs": "pass",
    "stable_procedure": "pass",
    "output_contract": "pass",
    "existing_skill_gap": "pass"
  },
  "alternatives_rejected": [
    {"form": "project-instructions", "reason": "conditional workflow"},
    {"form": "custom-agent", "reason": "no distinct role or tool boundary"}
  ]
}
```

Other valid statuses are `not-enough-history`, `unstable-workflow`,
`existing-skill`, `prefer-prompt`, `prefer-project-instructions`,
`prefer-script`, `prefer-tool`, and `needs-user-definition`.

## Validation before candidate status

A scaffold remains `draft` until it passes:

1. frontmatter/schema validation;
2. positive activation examples;
3. nearby non-activation examples;
4. missing-input and unavailable-capability behavior;
5. representative procedure/output test;
6. authority test proving review-only does not mutate;
7. component and recipe reference validation;
8. compatibility and path validation;
9. token/progressive-disclosure budget checks;
10. duplicate/overlap review against existing Skills.

Schema success alone is not behavioral validation.

## Interaction with task resolution

Skill selection happens after the current task is classified and before loading
a full recipe pack:

```text
current task
-> task archetype + modifiers + complexity ceiling
-> matching validated project/community Skill?
-> yes: load Skill and its pinned composition
-> no: resolve one primary recipe and minimum component candidates
```

An applicable validated Skill can refine the recipe and project references, but
it cannot override explicit task authority, hard environment restrictions, or
the component lock.

## Evidence basis and synthesis boundary

This decision model synthesizes all eight v0.3 research tracks. Its packaging
distinctions are directly informed by the Agent Skills specification, GitHub's
customization categories, MCP primitive boundaries, and provider guidance to
start with the simplest adequate agent architecture. Thresholds, event grouping,
status names, and the eligibility gate are repository design decisions to be
tested; they are not external empirical claims.

See:

- [General task taxonomy](../research/source-notes/general-agent-task-taxonomy.md)
- [Software agent tasks](../research/source-notes/software-agent-tasks.md)
- [Research and knowledge tasks](../research/source-notes/research-and-knowledge-tasks.md)
- [Long-context and stateful work](../research/source-notes/long-context-and-stateful-work.md)
- [Tool use and actions](../research/source-notes/tool-use-and-action-workflows.md)
- [Planning, decisions, and reasoning](../research/source-notes/planning-decision-and-reasoning.md)
- [High-stakes validation](../research/source-notes/high-stakes-and-validation.md)
- [Skills and recurring workflows](../research/source-notes/skills-and-recurring-workflows.md)
