# Skills, agent packaging, and recurring workflows

Research track H for the v0.3 selection ontology. Sources were reviewed on
2026-09-03.

## Scope and evidence labels

This note asks when work should remain a one-off task, become a reusable prompt,
move into project-local instructions, become a Skill, use a deterministic
script/tool, or justify a specialized agent or multi-agent workflow.

- **Evidence** means a finding from a linked open specification or official
  provider/platform document.
- **Synthesis** means a proposed Upgradeables packaging rule. It is not a claim
  that packaging alone improves outcomes.
- Product-specific locations and optional fields vary. Canonical Upgradeables
  identity should remain platform-neutral even when adapters are generated.

## Source-grounded findings

### Skills are discoverable, task-activated packages

**Evidence.** The Agent Skills specification defines a Skill as a directory
with a required `SKILL.md` containing name and description metadata plus
instructions. Optional `scripts/`, `references/`, and `assets/` directories
carry executable helpers, detailed knowledge, and static resources. [H1]

**Evidence.** The specification uses progressive disclosure: clients initially
load compact metadata, load the full `SKILL.md` after activation, and load
supporting resources only when needed. It recommends keeping core instructions
focused and moving detail into directly referenced files. [H1] [H2]

**Synthesis.** A Skill is appropriate when a recognizable task family needs a
repeatable procedure, boundaries, resources, or output contract that should not
be in every session. It is not merely a long prompt or a wrapper around one
component.

### Always-on instructions and Skills solve different problems

**Evidence.** GitHub describes custom instructions as always-on repository or
scope guidance and Skills as task-relevant instructions loaded when needed. It
recommends simple standards that apply broadly as custom instructions and more
detailed conditional workflows as Skills. [H3] [H4]

**Synthesis.** Project-wide facts such as build commands, repository etiquette,
and universal safety boundaries belong in a concise project adapter. A release,
review, migration, or evidence workflow belongs in a Skill if it is conditional
and stable. Duplicating the same guidance in both creates precedence and drift
problems.

### Prompt, resource, tool, and Skill are distinct package types

**Evidence.** MCP distinguishes user-controlled prompt templates,
application-controlled resources, and model-controlled tools. Tools can retrieve
information or cause actions and therefore require visible capability and
consent controls. [H5]

**Evidence.** GitHub's customization guide separately identifies custom
instructions, reusable prompt files, custom agents, runtime subagents, Skills,
hooks, and MCP servers. [H4]

**Synthesis.** Package according to the missing capability:

- reusable wording or input slots -> prompt template;
- stable read-only context -> reference/resource;
- deterministic computation or mutation -> script/tool;
- conditional procedure using context/tools -> Skill;
- persistent specialist role with scoped tools -> custom agent;
- independent delegated work within a run -> subagent.

A Skill may compose these pieces but should not pretend prose creates a tool or
permission that the host lacks.

### Project and personal scopes have different portability

**Evidence.** GitHub supports project Skills in repository paths and personal
Skills in user-level paths. It describes project Skills as shared repository
assets and personal Skills as available across projects. [H3]

**Evidence.** Agent Skills metadata can declare compatibility requirements,
while scripts and references remain part of the portable folder. [H1]

**Synthesis.** Use project scope when the workflow depends on repository paths,
commands, policies, schemas, or organization-specific references. Use a global
or community Skill only when its task boundary and procedure remain useful
without private project assumptions. A project Skill may cite global
`slug@version` components while adding local instructions.

### Specialized agents and subagents add isolation and coordination cost

**Evidence.** GitHub describes custom agents as named configurations with their
own prompts, tools, and optional MCP servers, and subagents as isolated delegated
executions whose results return to a parent session. [H6]

**Evidence.** OpenAI recommends a single agent with tools when possible because
multiple agents add complexity and overhead. It identifies manager and handoff
patterns when specialization, conditional logic, or overlapping tools require
separation. [H7]

**Evidence.** Anthropic advises using subagents for independent workstreams,
parallel work, or isolated context, and avoiding them for simple operations,
sequential work, or steps that require tightly shared context. [H8]

**Synthesis.** A Skill should remain a Skill unless execution needs durable
specialist identity, isolated context, distinct tool permissions, or adaptive
delegation. Repetition alone is not a reason to create an agent.

### Skill activation depends on precise metadata and bounded content

**Evidence.** The Agent Skills specification requires the description to say
what the Skill does and when to use it; compatible clients use metadata for
discovery before loading instructions. [H1] [H2]

**Evidence.** Agent Skills best practices warn that overly broad or exhaustive
Skills can distract the agent and recommend concise steps, focused references,
examples, and explicit conditions for loading support files. [H9]

**Synthesis.** Activation quality is part of Skill correctness. Every Skill
needs positive triggers, negative boundaries, required inputs, capability
requirements, an output contract, and a validation strategy. “Helpful for X” is
not enough to distinguish it from adjacent Skills.

## Packaging decision model

The table below is **synthesis**.

| Packaging form | Use when | Required stability | Do not use when |
|---|---|---|---|
| One-off task | Goal is immediate and procedure need not recur | Clear goal and current inputs | The user must repeatedly restate a stable workflow |
| Reusable prompt | Wording/input slots recur but procedure is shallow | Stable request shape | Scripts, references, or conditional steps are needed |
| Project instructions | Guidance applies to most work in a repository/scope | Stable project fact or universal rule | Guidance is relevant only to one workflow |
| Skill | A conditional task needs a repeatable procedure, resources, or output contract | Stable activation boundary and core workflow | Task is unique, trivial, or too unsettled to standardize |
| Script/hook | A step is deterministic and mechanically executable | Defined inputs, outputs, errors | Judgment is the primary work |
| Resource/reference | Agents need authoritative context on demand | Maintained source and clear load condition | The data must be mutated or computed dynamically |
| MCP/tool package | New external data or executable capability is required | Stable interface, permission model, error behavior | Instructions alone are sufficient |
| Custom agent | A recurring specialist needs its own prompt, context, and tool boundary | Stable role and handoff contract | A Skill on the current agent is sufficient |
| Runtime subagent | A current task has independent delegated work | Bounded objective and return contract | Work is tiny, sequential, or depends on shared evolving state |
| Orchestrated workflow | Multiple roles/workstreams need routing and synthesis | Stable coordination graph and failure handling | A single agent or deterministic workflow can do the job |

### Task-to-Skill threshold

**Synthesis.** Recommend a Skill only when all essential conditions hold:

1. The task has recurred or is deliberately being standardized for future use.
2. Its activation boundary can be described more specifically than a broad
   domain label.
3. Required inputs and unavailable-input behavior are known.
4. The core procedure is stable enough to encode without inventing project
   semantics.
5. A recognizable output contract or completion check exists.
6. The workflow benefits from instructions or resources that should load only
   for this task.
7. There is an owner or source of truth for project-specific knowledge.

Repetition is evidence for consideration, not automatic creation. A repeated
badly specified task should first be clarified or redesigned.

### Skill-to-agent threshold

**Synthesis.** Keep a workflow as a Skill unless at least one material need
exists:

- isolated context prevents unrelated state from contaminating the work;
- the role needs a distinct tool or permission boundary;
- routing among several specialists is itself part of the workflow;
- the work must run adaptively for many steps with explicit stop/retry logic;
- a parent must delegate a bounded result and synthesize it with other work.

Even then, first test whether one agent activating the Skill and tools is
sufficient.

## Proposed normalized packaging archetypes

All entries are **synthesis**.

| Archetype | Goal | Typical artifact |
|---|---|---|
| `one-off-assistance` | Complete a current bounded request | response or task result |
| `prompt-reuse` | Reuse an input/output frame | parameterized prompt |
| `project-guidance` | Share universal project facts and rules | concise `AGENTS.md`/provider adapter block |
| `procedural-skill` | Standardize a conditional multi-step task | `SKILL.md` plus optional resources |
| `reference-packaging` | Make maintained knowledge available on demand | focused reference files/resources |
| `deterministic-automation` | Execute repeatable mechanical logic | script, hook, test, or CLI command |
| `external-capability-integration` | Connect agents to systems or data | MCP server/tool package |
| `specialist-agent-configuration` | Give a stable role distinct context/tools | custom-agent definition |
| `delegated-subtask` | Isolate bounded work during a larger run | subagent objective and result contract |
| `multi-agent-orchestration` | Coordinate several independent specialists | manager/handoff graph and synthesis contract |
| `skill-validation-distribution` | Verify and share a reusable package | tests, compatibility metadata, versioned release |

These packaging archetypes should complement, not replace, the task archetype.
For example, `code-review` can be one-off assistance, a project Skill, or a
specialist agent depending on recurrence and environment.

## Recurring failure patterns

The following are **synthesis categories** informed by the specifications and
provider guidance above.

| Failure-mode candidate | Observable signal | Selection implication |
|---|---|---|
| `activation-ambiguity` | Description matches unrelated or adjacent tasks | Add concrete positive and negative activation phrases |
| `overbroad-skill` | One Skill covers a whole profession/domain | Split by stable user job and output contract |
| `wrapper-per-component` | Package adds no task procedure beyond naming a mechanism | Compose components inside job-performing Skills |
| `always-on-context-bloat` | Detailed conditional workflow loads every session | Move it from project instructions into a Skill/reference |
| `progressive-disclosure-failure` | Full manuals load before relevance is known | Keep metadata compact and references conditional |
| `deep-reference-chain` | Agent must traverse nested files to find required steps | Keep core procedure in `SKILL.md` and references shallow |
| `duplicate-guidance` | Same rule differs across instructions, Skill, and prompt | Define one owner and precedence |
| `stale-project-context` | Skill encodes obsolete paths, commands, or policies | Version/validate local references and report drift |
| `hidden-precondition` | Skill fails because a tool, file, permission, or network is absent | Declare inputs and compatibility/capability requirements |
| `capability-by-prose` | Instructions claim access to a tool or memory the host lacks | Check host capabilities and degrade explicitly |
| `permission-leak` | Skill activation silently expands write/action authority | Keep permissions outside activation and require task consent |
| `nondeterministic-mechanical-step` | Model improvises a check a script could perform reliably | Package stable computation as script/tool |
| `agent-proliferation` | Many roles exist without distinct context/tool boundaries | Collapse to a single agent with Skills |
| `delegation-overhead` | Subagent setup/synthesis costs exceed task work | Apply complexity ceiling before delegation |
| `context-fragmentation` | Subagents lack state needed for coherent decisions | Keep tightly coupled work in one context or define handoff state |
| `version-drift` | Skill references latest/unpinned components or incompatible tools | Pin canonical versions and declare compatibility |
| `validation-theater` | Package checks schema but not behavioral output | Add representative activation and behavior tests |
| `auto-packaging-noise` | Repetition threshold creates low-value Skills automatically | Suggest; require user/agent review before creation |

## Environment modifiers

These are **synthesis recommendations**.

| Modifier | Packaging effect |
|---|---|
| `recurrence_count` | Raises Skill candidacy only with workflow similarity |
| `stable_task_boundary` | Required for reliable Skill activation |
| `stable_inputs_and_output` | Supports prompt/Skill reuse and behavioral tests |
| `stable_procedure` | Supports Skill or deterministic workflow packaging |
| `applies_to_most_project_tasks` | Promotes concise project instructions |
| `project_specific_context` | Promotes project-local Skill/reference rather than global package |
| `cross_project_portability` | Promotes community/global Skill with compatibility metadata |
| `large_reference_material` | Promotes progressive disclosure and focused references |
| `deterministic_step_available` | Promotes script/hook instead of prose improvisation |
| `external_system_required` | Promotes MCP/tool package with explicit permissions |
| `distinct_tool_boundary` | May promote a specialist agent |
| `isolated_context_beneficial` | May promote subagent execution |
| `parallel_independent_work` | May promote multiple subagents and synthesis |
| `tightly_shared_state` | Demotes subagents and decentralized handoffs |
| `network_required` | Must be declared; absence requires offline fallback or refusal |
| `sensitive_data` | Constrain references/tools and distribution scope |
| `write_or_action_required` | Keep authorization separate from Skill activation |
| `host_support_unknown` | Require portable fallback and avoid platform-specific claims |
| `maintenance_owner_present` | Supports durable project/community packaging |
| `compatibility_constraints` | Require explicit host, tool, package, or runtime requirements |

## Complexity implications

This table is **synthesis**.

| Workflow shape | Default packaging/ceiling | Raise complexity when | Normally excessive |
|---|---|---|---|
| Unique simple request | One-off task, L0-L1 | Consequence or validation demands it | Skill or custom agent |
| Repeated shallow wording | Prompt template, L0-L1 | Conditional procedure emerges | Agent orchestration |
| Universal repository rules | Project instructions, L1 | Path-specific variants are necessary | Loading full registry/docs always |
| Repeated conditional procedure | Skill, L1-L2 | Tools, references, or stateful checks are needed | Separate agent without a role boundary |
| Mechanical repeatable operation | Script/hook, L1-L2 | External system or recovery loop is needed | Model-only execution |
| Context-rich project workflow | Project Skill, L2-L3 | Long state, high stakes, multiple tools | Global Skill containing private assumptions |
| External integration | Skill plus MCP/tool, L2-L4 | Side effects, retries, or approvals exist | Claiming capability in prose alone |
| Independent delegated analysis | Subagent, L2-L4 | Parallel breadth or context isolation matters | Delegation for a tiny lookup/edit |
| Stable specialist role | Custom agent, L3-L4 | Distinct permissions/context persist across tasks | Agent per narrow Skill |
| Multi-role adaptive workflow | Orchestration, L4-L5 | Roles are separable and synthesis is explicit | Multi-agent solely for prestige or availability |

## Project-local instruction recommendations

All items are **synthesis**.

Keep the always-loaded project adapter short and limited to:

- project identity and root;
- canonical build, test, format, and validation commands;
- repository-wide safety and mutation boundaries;
- where the harness, task map, lock, and project Skills live;
- instruction precedence and how to resolve a task;
- universal handoff or reporting requirements.

Do not place these in the always-loaded adapter:

- all component definitions;
- every recipe;
- long domain references;
- workflow-specific edge cases;
- provider-specific capability claims;
- instructions that only apply after one Skill activates.

Project Skills should refer to stable project references by path, state when to
load them, and avoid copying large source documents into `SKILL.md`.

## Skill package recommendations

These are **synthesis** requirements for the v0.3 Skill factory.

Every scaffold should expose:

1. Canonical Skill slug and plain display name.
2. Positive activation examples and explicit non-triggers.
3. Required inputs and missing-input behavior.
4. Host/tool/permission compatibility requirements.
5. Primary recipe and pinned `slug@version` composition.
6. Procedure with deterministic scripts preferred for mechanical steps.
7. Conditions for loading each reference or asset.
8. Output contract, stopping rule, and failure/escalation behavior.
9. Draft versus validated status.
10. Activation, non-activation, behavior, and failure-path tests.

The package should remain portable by isolating provider adapters from the core
Skill and by avoiding undocumented memory, tool, or permission assumptions.

## Subagent and orchestration recommendations

All items are **synthesis**.

- Spawn a subagent only with a bounded objective, relevant context, permitted
  tools, output format, and stop condition.
- Use isolated context for independent exploration or validation; keep tightly
  coupled sequential edits with the primary agent.
- Prefer a manager pattern when one agent must retain user context and synthesize
  results.
- Prefer handoff only when control should genuinely transfer to another stable
  specialist.
- Do not confuse a Skill used by an agent with a new agent identity.
- Include delegation cost in the complexity ceiling.
- Validate coverage and conflicts at synthesis; do not concatenate worker
  outputs.

## Ontology recommendations for synthesis

1. Record both `task_archetype` and `packaging_form`; neither can substitute for
   the other.
2. Model the progression as task -> recurring stable workflow -> Skill -> agent
   only when each threshold adds a necessary capability.
3. Keep project instructions always-on and minimal; load Skills and references
   just in time.
4. Score Skill candidacy from recurrence, boundary stability, procedure
   stability, and testability—not recurrence count alone.
5. Make Skill suggestion advisory and based only on explicit local task events.
6. Separate procedural knowledge from deterministic execution and external
   capability. Use scripts/tools for the latter.
7. Separate Skill activation from authority to read, write, send, deploy, or
   transact.
8. Use canonical `slug@version` identities inside locks while allowing portable
   plain-language discovery metadata.
9. Require a capability/compatibility manifest and an explicit fallback for
   hosts that lack optional features.
10. Treat activation precision, token footprint, version drift, and behavior
    tests as first-class package quality dimensions.

## Sources

- **[H1]** Agent Skills, [Specification](https://agentskills.io/specification), accessed 2026-09-03.
- **[H2]** Agent Skills, [How to add Skills support to an agent](https://agentskills.io/client-implementation/adding-skills-support), accessed 2026-09-03.
- **[H3]** GitHub Docs, [About agent skills](https://docs.github.com/en/copilot/concepts/agents/about-agent-skills), accessed 2026-09-03.
- **[H4]** GitHub Docs, [Copilot customization cheat sheet](https://docs.github.com/en/copilot/reference/customization-cheat-sheet), accessed 2026-09-03.
- **[H5]** Model Context Protocol, [Server primitives overview](https://modelcontextprotocol.io/specification/2025-06-18/server/index), protocol revision 2025-06-18.
- **[H6]** GitHub Docs, [Custom agents and sub-agent orchestration](https://docs.github.com/en/copilot/how-tos/copilot-sdk/features/custom-agents), accessed 2026-09-03.
- **[H7]** OpenAI, [A practical guide to building agents](https://openai.com/business/guides-and-resources/a-practical-guide-to-building-ai-agents/), accessed 2026-09-03.
- **[H8]** Anthropic, [Prompting best practices: subagents and context](https://docs.anthropic.com/en/docs/build-with-claude/prompt-engineering/prompt-templates-and-variables), accessed 2026-09-03.
- **[H9]** Agent Skills, [Best practices for Skill creators](https://agentskills.io/skill-creation/best-practices), accessed 2026-09-03.
- **[H10]** Anthropic, [Equipping agents for the real world with Agent Skills](https://www.anthropic.com/engineering/equipping-agents-for-the-real-world-with-agent-skills), 2025.
