# Tool Use and Action Workflows

Research track: E — tool use, browser/computer use, APIs, files, shell, databases,
actions, retries, approval, and recovery.

Date accessed: 2026-09-03

## Scope and evidence labels

This note identifies workflow controls that can inform deterministic Upgradeables
selection. It does not define a provider policy or claim that any Upgradeable has
been empirically shown to improve a task.

- **Evidence** means the linked primary source explicitly supports the stated
  pattern.
- **Synthesis** means the pattern is a proposed normalization for this repository,
  derived from one or more sources and intended to be tested in the v0.3 resolver.
- **Selection prior** means an Upgradeable should enter consideration; its trigger,
  non-trigger, dependencies, conflicts, and current task still determine whether it
  activates.

Sources were limited to provider documentation, platform documentation, protocol
specifications, and an IETF standard. Product-specific mechanisms are used as
examples of a broader control pattern, not treated as universal requirements.

## Source-supported findings

| Finding | Label | Source support |
|---|---|---|
| Prefer simple, composable workflows and add autonomous agent loops only when task uncertainty warrants them. | Evidence | Anthropic reports that successful implementations commonly use simple composable patterns and distinguishes predefined workflows from autonomous agents. [Building Effective AI Agents](https://www.anthropic.com/engineering/building-effective-agents) |
| An agent loop needs observations from the environment, stopping conditions, and a path to human feedback or blockers. | Evidence | Anthropic describes plan-act-observe loops grounded by tool results or code execution, plus checkpoints and maximum-iteration stopping conditions. [Building Effective AI Agents](https://www.anthropic.com/engineering/building-effective-agents) |
| Tool descriptions and interfaces are part of reliability, not incidental documentation. | Evidence | Anthropic explicitly calls clear, thoughtful toolset design and documentation crucial to agent execution. [Building Effective AI Agents](https://www.anthropic.com/engineering/building-effective-agents) |
| Permissions can be action-specific rather than globally on or off. | Evidence | Anthropic describes per-action states such as always allow, needs approval, and block; it also describes plan review as an alternative to approval fatigue for many-step work. [Trustworthy agents in practice](https://www.anthropic.com/research/trustworthy-agents) |
| Tool risk should distinguish read-only/write, reversibility, account permission, and impact; high-risk actions warrant human oversight and retry thresholds warrant handoff. | Evidence | OpenAI's agent guide names these factors for tool safeguards and recommends human intervention for exceeded failure thresholds and sensitive, irreversible, or high-stakes actions. [A practical guide to building agents](https://openai.com/business/guides-and-resources/a-practical-guide-to-building-ai-agents/) |
| Approval must be bound to the concrete tool call and arguments and execution must be resumable after approval or rejection. | Evidence | The OpenAI Agents SDK documents per-call approval IDs, argument-aware approval rules, fail-closed handling for malformed arguments, interruption, serialized state, and resume. [Human-in-the-loop](https://openai.github.io/openai-agents-python/human_in_the_loop/) |
| Tool metadata can expose read-only, destructive, idempotent, and open-world properties, but untrusted metadata is only a hint. | Evidence | The MCP schema defines these four annotations and warns clients not to base decisions on annotations from untrusted servers. [MCP schema reference](https://modelcontextprotocol.io/specification/2025-11-25/schema) |
| Authentication and authorization do not themselves establish task authority. | Synthesis | MCP authorization binds clients and resource servers through OAuth-oriented controls, scopes, audience validation, and protected-resource discovery. This note separately models whether a particular user intent authorizes a particular side effect. [MCP authorization](https://modelcontextprotocol.io/specification/2025-11-25/basic/authorization) |
| Read-only defaults, declared write surfaces, credential isolation, bounded branches, and human merge review are practical defense layers. | Evidence | GitHub Agentic Workflows use read-only defaults and declared safe outputs; Copilot cloud agent limits branches/credentials, requires human review before merge, restricts workflow execution, and preserves audit attribution. [Agentic Workflows](https://docs.github.com/en/copilot/concepts/agents/about-github-agentic-workflows), [Copilot risks and mitigations](https://docs.github.com/en/copilot/concepts/agents/cloud-agent/risks-and-mitigations) |
| Automatic retry is safe only when the operation is known to be idempotent or the system can establish that the first attempt was not applied. | Evidence | HTTP semantics permits automatic retry of idempotent requests after communication failure and warns against automatically retrying non-idempotent requests without application knowledge; it also advises against repeatedly retrying a failed automatic retry. [RFC 9110 §9.2.2](https://www.rfc-editor.org/rfc/rfc9110.html#section-9.2.2) |

## Proposed normalized task archetypes

These are synthesis categories for task discovery, not claims about frequency.

| Archetype | Description | Representative requests | Default complexity |
|---|---|---|---|
| `tool-assisted-observation` | Use a tool to retrieve, inspect, calculate, search, or test without intentionally changing external state. | “Search these docs,” “run the focused test,” “query this table.” | L1; raise to L2 for many sources or resumable state |
| `bounded-local-mutation` | Modify local, versioned, or readily recoverable state inside a declared scope. | “Patch this file,” “rename this symbol,” “update this branch.” | L1–L2 |
| `external-state-mutation` | Create or change a record outside the immediate workspace. | “Open an issue,” “update the CRM record,” “post a comment.” | L2–L4 depending on reversibility and reach |
| `consequential-action` | Execute a sensitive, irreversible, costly, or rights-affecting side effect. | “Send the message,” “deploy,” “delete production data,” “make a payment.” | L3–L4, with explicit approval/authority |
| `iterative-tool-loop` | Repeatedly act and observe because the next step depends on environmental feedback. | “Diagnose and repair until the focused tests pass.” | L2–L4 with stopping and retry budgets |
| `cross-system-workflow` | Coordinate tools across trust, identity, or transaction boundaries. | “Read a ticket, patch the repo, then notify the customer.” | L3–L5; orchestration only if responsibilities genuinely separate |
| `long-running-action-workflow` | Pause, persist explicit state, wait for approval or external completion, and resume. | “Prepare deployment, wait for approval, then continue.” | L4; L5 only for multiple workers/handoffs |

Tool use is an environment modifier as well as an archetype. A research task that
uses web search remains a research task; a simple edit that uses a file tool remains
a transformation/edit task. The resolver should not replace the user's primary task
archetype with the generic label `tool-use` merely because a tool is available.

## Proposed action-control model

The following seven-stage model is **Synthesis**, grounded in the source patterns
above.

1. **Classify the operation.** Identify whether it is observational or mutating,
   local or external, additive or destructive, reversible or irreversible,
   idempotent or non-idempotent, and closed-world or open-world.
2. **Resolve authority and capability separately.** Confirm that the host can call
   the tool, the credential has the needed scope, and the current user instruction
   authorizes the exact target and effect. Possessing a credential is not consent.
3. **Minimize reach.** Choose the narrowest tool, target set, permissions, and data
   exposure that can complete the job. Prefer read-only inspection before mutation.
4. **Preflight consequential calls.** Surface the tool, exact arguments/targets,
   expected effect, reversibility, validation plan, and material uncertainty. Obtain
   approval where the risk policy or user instruction requires it.
5. **Execute once and capture identity.** Preserve a call/request ID, target version,
   or other correlation key so an ambiguous result can be reconciled.
6. **Observe and reconcile.** Treat the tool result and resulting external state as
   evidence. Check postconditions rather than interpreting “call returned” as proof
   of success.
7. **Recover within bounds.** Retry only when retry safety is known. Otherwise query
   state, compensate/revert when authorized, or escalate. Stop at a declared attempt,
   action, time, or cost boundary.

### Tool selection record

A deterministic resolver or Skill brief should be able to represent:

```text
task_requirement
candidate_tool
capability_available
read_only
mutates_external_state
destructive
reversible
idempotent
open_world
credential_scope
authorized_target
approval_required
preconditions
postconditions
retry_policy
compensation_or_recovery
stop_condition
```

Unknown values should remain `unknown`; absence of metadata must not be interpreted
as safety.

## Permission and action tiers

This is a **Synthesis** vocabulary suitable for environment modifiers and complexity
ceilings.

| Tier | Operation | Default workflow control | Ceiling effect |
|---|---|---|---|
| T0 | No tool; reasoning or transformation over supplied content | No tool controls | No increase |
| T1 | Read-only, scoped, closed-world observation | Declare source/target; validate tool result when material | Usually L0–L1 |
| T2 | Reversible local mutation in a bounded/versioned workspace | Inspect first, preserve scope, diff/postcondition check | Usually L1–L2 |
| T3 | External or shared-state mutation, even if reversible | Explicit target/effect, scoped credentials, audit ID, postcondition check; approval according to policy | At least L2; often L3 |
| T4 | Destructive, irreversible, financial, privacy-sensitive, deployment, or rights-affecting action | Mandatory explicit authorization, preflight, independent/deterministic validation where useful, durable record, fail-closed on ambiguity | L3–L4; L5 only for real coordination needs |

Approval is not validation: approval answers “may this action occur?” while
validation answers “is this the correct action with correct arguments?” Both may be
needed.

## Retry and recovery rules

The rules below are **Synthesis** from RFC 9110, provider agent loops, and durable
approval patterns.

- Retry reads and other known-idempotent calls only for plausibly transient failure,
  using a bounded attempt/time budget.
- For a mutation with an ambiguous outcome, inspect the target state or query by the
  request/idempotency key before deciding whether to call again.
- Never infer “not applied” from a lost response.
- Do not automatically retry a non-idempotent or destructive operation without a
  reliable deduplication or reconciliation mechanism.
- Separate tool-call failure from task failure. A different tool or a human handoff
  may complete the task without repeating the side effect.
- Preserve partial-success state explicitly. A multi-step workflow should know which
  postconditions hold before compensation or resume.
- A rollback is itself an action requiring authority and validation; it is not always
  safe or complete.
- Stop after the configured failure threshold and report observed state, attempted
  actions, unresolved effects, and the safest next step.

## Environment modifiers and resolver effects

All mappings in this table are **Synthesis**.

| Modifier | Promote | Demote/exclude | Complexity effect / hard restriction |
|---|---|---|---|
| `shell_available` | Tool-assisted observation; focused testing; bounded local mutation | Claims that shell was used when unavailable | No automatic increase; dangerous commands remain separately classified |
| `web_available` | Current-source retrieval when task permits it | Implied browsing when disallowed | Open-world output requires source/injection scrutiny |
| `tools_required` | Tool selection and postcondition controls | Answer-only completion when evidence/action requires a tool | Raise one level if an iterative loop is necessary |
| `file_write_allowed` | Bounded local mutation | Editing when review-only or write denied | Does not authorize files outside declared scope |
| `review_only` | Read-only inspection and reporting | All editing/mutation modules | Hard exclusion on side effects |
| `editing_requested` | Local mutation and diff validation | Review-only completion if it would leave task undone | Usually L1; raise for broad/structural change |
| `irreversible_action` | Preflight, explicit approval, fail-closed handling, audit record | Automatic execution/retry | Minimum L3; no action on ambiguous authority |
| `human_approval_available` | Pause/resume workflow for T3/T4 | Treating silence as approval | Approval must be call/target specific |
| `human_approval_unavailable` | Draft/preview/plan output | T4 execution and policy-required T3 calls | Stop before action; return approval packet |
| `persistent_work` | Explicit state, request IDs, checkpoints, resume | Hidden-memory claims | Raise to L2/L4 according to duration and actions |
| `open_world_tool` | Injection/data-boundary checks and output validation | Trusting retrieved instructions as authority | May raise one level when combined with write tools |
| `tool_metadata_untrusted` | Conservative classification and independent capability policy | Auto-approval from tool annotations | Treat missing/claimed-safe properties as unknown |
| `multi_agent_available` | Delegation only for separable work with explicit handoffs | Orchestration for a single serial tool loop | Raise to L5 only when parallelism/specialization adds value |

## Observable failures

| Failure signal | Proposed normalized failure mode | Response prior |
|---|---|---|
| A tool is selected because it is available, not because its contract fits the task. | `tool-misselection` | Reclassify task requirement and compare narrower candidates. |
| The model claims a tool, permission, state, or result it did not observe. | `capability-hallucination` | Fail closed on the dependent claim; request access or report limitation. |
| Read-only review produces edits or external side effects. | `action-permission-violation` | Stop, preserve state, disclose effect, and seek recovery authority. |
| A credential's scope is treated as user authorization. | `authority-scope-conflation` | Re-resolve explicit task authority and target before action. |
| A destructive target is represented by an unresolved variable, broad path, or stale identifier. | `unsafe-target-resolution` | Resolve and preview exact targets; do not execute while ambiguous. |
| A timed-out mutation is immediately repeated without checking whether it applied. | `unsafe-retry` | Reconcile external state or request ID first. |
| The agent repeats a failed strategy until cost/turn exhaustion. | `unbounded-tool-loop` | Apply retry/turn budget and hand off with accumulated evidence. |
| A multi-step workflow reports success after only the call, without testing postconditions. | `unverified-side-effect` | Inspect resulting state and compare with the output contract. |
| A partial workflow is resumed from prose memory with no durable action ledger. | `partial-state-loss` | Reconstruct explicit completed/pending/unknown state before continuing. |
| Retrieved open-world content changes action authority or expands targets. | `untrusted-content-control-flow` | Restore authority boundary; treat retrieved instructions as data. |
| Approval is requested so often that the target/effect is no longer meaningfully reviewed. | `approval-fatigue` | Batch a bounded plan where appropriate while retaining per-risk checkpoints. |
| A rollback is assumed to restore all external consequences. | `false-reversibility` | Verify compensating effects and disclose residual consequences. |

## Candidate Upgradeable priors

These mappings are **repository synthesis only**. They do not establish empirical
effectiveness and must be reconciled with canonical metadata.

| Workflow need | Primary candidates | Secondary/counterbalance candidates | Normally unnecessary |
|---|---|---|---|
| Lock target, scope, requested effect, and review/edit mode | `task-set-lock-in`, `authority-anchor-enforcement` | `clarification-gateway` when authority or target is missing | Large state machinery for one clear read |
| Select only relevant tools/components | `scoped-loader` | `activation-budget-funnel` for large tool catalogs | Orchestration for one known call |
| Prevent invented capabilities/results | `grounding-no-invention` | `epistemic-status-gating` | Citation machinery for a purely local observable result |
| Preflight costly or irreversible action | `forethought-checkpoints` | `risk-tier-scaling`, `critical-atomic-verification` | Alternative-universe reasoning when deterministic checks settle the call |
| Persist explicit action state | `stateblock`, `state-snapshot` | `sequential-memory-state-engine` for genuinely long workflows | Durable state for a single synchronous read |
| Bound retries and loops | `bounded-exit` | `reasoning-scale-controller` | Repeated QMS when the tool has a direct postcondition |
| Perform the smallest authorized local edit | `micro-repair` | `invariance-stress-scaffold`, `bidirectional-consistency` | Architectural repair for a localized defect |
| Fail safely when authorization/evidence is missing | `fail-closed-abstention` | `clarification-gateway` | Generic refusal when a preview or partial result is safe |
| External persistence/automation | `external-state-automation` only when a real store/tool and explicit authorization exist | `state-snapshot`, `forethought-checkpoints` | Any claim of hidden durable memory |

## Complexity implications

- L0 should not gain tool scaffolding merely because tools exist.
- L1 fits one or a few read-only calls or a reversible local edit with a direct
  validator.
- L2 is justified by explicit state, several dependent calls, partial success, or a
  shared external mutation.
- L3 adds stronger preflight/validation and human review for material consequences.
- L4 fits autonomous act-observe-recover loops with tools, explicit state, action
  budgets, and approval boundaries.
- L5 requires genuinely separable workers, distinct permissions, or handoffs. Multiple
  tool calls by one agent are not sufficient.

The action tier can raise the minimum control level, but should not automatically
activate every high-cost component. A deterministic postcondition can be stronger and
cheaper than parallel model review.

## Resolver implications

The v0.3 resolver should:

1. preserve the primary task archetype and add tool/action modifiers;
2. distinguish capability, authentication, authorization, approval, and validation;
3. classify missing tool safety properties as unknown rather than safe;
4. hard-exclude mutations for review-only tasks;
5. promote reconciliation before retry after an ambiguous mutation;
6. require exact targets before destructive operations;
7. expose `needs-agent-evaluation` when reversibility, authority, or retry semantics
   cannot be determined from explicit state;
8. suppress orchestration and long-context controls for short deterministic calls;
9. prefer previews or plans when approval is unavailable;
10. report what was attempted, observed, and left unresolved.

## Source list

- Anthropic, [Building Effective AI Agents](https://www.anthropic.com/engineering/building-effective-agents).
- Anthropic, [Trustworthy agents in practice](https://www.anthropic.com/research/trustworthy-agents).
- OpenAI, [A practical guide to building agents](https://openai.com/business/guides-and-resources/a-practical-guide-to-building-ai-agents/).
- OpenAI Agents SDK, [Human-in-the-loop](https://openai.github.io/openai-agents-python/human_in_the_loop/).
- Model Context Protocol, [Schema reference — ToolAnnotations](https://modelcontextprotocol.io/specification/2025-11-25/schema#toolannotations).
- Model Context Protocol, [Authorization](https://modelcontextprotocol.io/specification/2025-11-25/basic/authorization).
- GitHub, [About GitHub Agentic Workflows](https://docs.github.com/en/copilot/concepts/agents/about-github-agentic-workflows).
- GitHub, [Risks and mitigations for GitHub Copilot cloud agent](https://docs.github.com/en/copilot/concepts/agents/cloud-agent/risks-and-mitigations).
- IETF, [RFC 9110 §9.2.2 — Idempotent Methods](https://www.rfc-editor.org/rfc/rfc9110.html#section-9.2.2).
