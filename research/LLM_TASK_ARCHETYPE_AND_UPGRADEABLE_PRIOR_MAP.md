# LLM Task Archetype and Upgradeable Prior Map

**Milestone:** Upgradeables v0.3 research-first selection ontology  
**Baseline registry:** v0.2.1, 96 operational Upgradeables  
**Synthesis date:** 2026-09-03  
**Status:** normalized design synthesis from eight research tracks

## Selection-prior disclaimer

This map is a deterministic discovery layer, not an activation table and not empirical proof that an Upgradeable improves a task. A match means “consider this recipe or component.” Task-time evaluation must still apply explicit task wording, permissions, complexity ceiling, recipe roles, triggers, non-triggers, dependencies, conflicts, counterbalances, and available capabilities.

The synthesis deliberately does not infer:

```text
software project -> coding stack permanently active
long file -> all long-context controls active
high stakes -> maximal validation or many agents
tool available -> tool use or mutation authorized
repeated task -> Skill automatically created
```

## Research basis

The synthesis uses all eight source notes:

| Track | Source note | Main contribution |
|---|---|---|
| A | [General LLM and agent task taxonomy](source-notes/general-agent-task-taxonomy.md) | Broad user goals, execution forms, tool/action distinction, stopping and handoff |
| B | [Software engineering and coding-agent tasks](source-notes/software-agent-tasks.md) | Repository, diagnosis, repair, review, testing, migration, and authority boundaries |
| C | [Research and knowledge tasks](source-notes/research-and-knowledge-tasks.md) | Retrieval, verification, evidence synthesis, citation quality, and research breadth |
| D | [Long-context and stateful work](source-notes/long-context-and-stateful-work.md) | Context limits, explicit state, retrieval, compaction, continuation, and handoff |
| E | [Tool use and action workflows](source-notes/tool-use-and-action-workflows.md) | Capability, permission, action tiers, preflight, retry, postconditions, and recovery |
| F | [Planning, decision, and reasoning](source-notes/planning-decision-and-reasoning.md) | Planning, constraints, branching, falsification, creative phases, and missing premises |
| G | [High-stakes and validation](source-notes/high-stakes-and-validation.md) | Risk-scaled evidence, uncertainty, approval, validation, abstention, and escalation |
| H | [Skills and recurring workflows](source-notes/skills-and-recurring-workflows.md) | Task-to-Skill thresholds, progressive disclosure, packaging, and agent boundaries |

Source quality is predominantly original benchmark/paper literature, standards, or official provider/platform documentation. Provider engineering reports are treated as current implementation observations, not independent universal evaluations. Benchmark findings identify task structures and failure surfaces; they do not establish real-world prevalence or Upgradeable efficacy.

Representative evidence behind the synthesis includes [GAIA](https://arxiv.org/abs/2311.12983) for mixed tool/reasoning tasks, [SWE-bench](https://arxiv.org/abs/2310.06770) and [RepoBench](https://arxiv.org/abs/2306.03091) for repository workflows, [FEVER](https://arxiv.org/abs/1803.05355) and [ALCE](https://aclanthology.org/2023.emnlp-main.398/) for evidence and citation distinctions, [Lost in the Middle](https://arxiv.org/abs/2307.03172) and [RULER](https://arxiv.org/abs/2404.06654) for long-context failure surfaces, [TravelPlanner](https://arxiv.org/abs/2402.01622) and [ConstraintBench](https://arxiv.org/abs/2602.22465) for plan/constraint structure, NIST’s [AI RMF Core](https://airc.nist.gov/airmf-resources/airmf/5-sec-core/) for proportional risk controls, and the [Agent Skills specification](https://agentskills.io/specification) for Skill packaging.

## Normalized selection model

The central normalization is to keep the user’s goal separate from where and how the work happens.

```text
PRIMARY TASK ARCHETYPE
What outcome did the user request?

        + DOMAIN / PROJECT PROFILE
What subject and project context apply?

        + SUBTYPE
What narrower form of that goal is present?

        + EXECUTION FORM
Direct, fixed workflow, tool-assisted, stateful, agentic, or orchestrated?

        + OBSERVABLE FAILURE / RISK SIGNALS
What can plausibly go wrong in this task?

        + ENVIRONMENT MODIFIERS
Sources, tools, permissions, fidelity, persistence, action, stakes, output?

        + COMPLEXITY FLOOR / CEILING
What is the smallest justified control level and what is too expensive?

        -> CANDIDATE RECIPE + COMPONENT PRIORS
        -> RECIPE ROLE AND TRIGGER/NON-TRIGGER EVALUATION
        -> MINIMUM SUFFICIENT ACTIVE COMPOSITION
```

Use one primary archetype whenever possible. Composite work may have secondary archetypes, but the resolver must explain why each materially affects the output. Explicit task wording outranks project profile priors.

## Primary task archetypes

The machine-readable source is [`registry/task_archetypes.json`](../registry/task_archetypes.json).

| Primary archetype | Normalized subtypes | Default bounds | Candidate recipe priors |
|---|---|---|---|
| `knowledge-explanation` | direct answer, explanation, teaching, conceptual troubleshooting | L0–L1 | `education-explanation` |
| `content-understanding` | summarize, extract, classify, source-bounded QA, document analysis, bounded comparison | L0–L3 | `source-grounded-analysis`, `long-context-source-fidelity`, `long-context-corpus` |
| `content-transformation` | rewrite, translate, restructure, format/convert, long fidelity transformation | L0–L3 | `authoring`, `long-context-source-fidelity` |
| `content-authoring` | report, documentation, proposal, outline, citation-bearing authoring | L1–L3 | `authoring`, `research-skill`, `source-grounded-analysis` |
| `research-grounding` | fact retrieval, claim verification, source comparison, synthesis, systematic review, open investigation | L1–L4 | `research-skill`, `source-grounded-analysis`, domain evidence recipes |
| `quantitative-analysis` | calculation, table/statistical analysis, exploration, quantitative comparison | L1–L3 | `source-grounded-analysis`, `high-stakes-reasoning` when consequence warrants |
| `constraint-reasoning` | logical/spatial reasoning, feasibility, optimization, counterfactual, argument evaluation | L1–L3 | `perception-reasoning`, `high-stakes-reasoning` conditionally |
| `planning-design` | plan generation/validation, replanning, decomposition, architecture, workflow design | L1–L3 | `architecture-skill-building`, `decision-support`; orchestration only conditionally |
| `decision-support` | tradeoffs, comparison, recommendation, concept selection | L1–L3 | `decision-support`, domain/high-stakes recipes when applicable |
| `creative-exploration` | ideation, concept development/selection, hypothesis generation, alternatives | L1–L2 | `creative-ideation`, then `decision-support` for convergence |
| `software-engineering` | repository understanding, diagnosis, repair, implementation, tests, review, refactor, migration, dependency, release | L1–L4 | `coding-debugging`, `code-review`, `architecture-skill-building`, source-fidelity routes |
| `evaluation-audit` | code/factual/evidence/quality review, plan validation, high-impact audit | L1–L3 | `code-review`, `source-grounded-analysis`, appropriate evidence/high-stakes recipe |
| `action-execution` | local mutation, external mutation, communication, deployment, deletion, transaction | L1–L4 | task-domain recipe plus action controls; no generic action recipe is forced |
| `workflow-automation` | deterministic automation, tool loop, routing, cross-system or long-running workflow | L1–L4 | `deterministic-intake-routing`, `architecture-skill-building`, orchestration conditionally |
| `skill-agent-creation` | prompt reuse, project guidance, Skill, references, tool integration, specialist agent | L1–L4 | `architecture-skill-building`; `multi-agent-orchestration` only after the agent threshold |

### Boundary decisions

- `tool-mediated-retrieval` is an execution form, not a primary goal. Web research remains research; a repository lookup remains software/content understanding.
- `stateful-project-work` is a continuity form. The underlying task may be research, coding, authoring, or action.
- `long-document-qa` is `content-understanding` with `source-bounded-qa + long_context`, not a competing top-level archetype.
- `issue-to-patch` is a composite software workflow across inspect, localize, diagnose, edit, verify, and handoff. It is not the default for every code request.
- `breadth-first-research` is an orchestrated execution form, not a research goal.
- `code-review` specializes `evaluation-audit` in the software domain and defaults to `review_only=true`.
- `architecture-design` is planning/design in a software or agent domain; it does not authorize implementation.
- `documentation-maintenance` normally uses authoring/transformation as the goal and software/documentation as the domain.
- High stakes changes controls and evidence requirements; it never replaces the primary archetype.

## Domains and project profiles

Normalized domains align with the planned built-in profiles:

```text
general
software-development
research-and-knowledge
documentation
data-analysis
medical-evidence
legal-evidence
agent-development
```

`authoring` and `long-context` remain useful project profiles but are not content domains: authoring describes a dominant task family, and long-context describes a persistent project condition. A profile may raise recipe priors but never override explicit task wording, review/edit mode, source boundaries, or component non-triggers.

## Execution forms

| Execution form | Meaning | Typical complexity |
|---|---|---|
| `direct-response` | One bounded response or deterministic operation | L0–L1 |
| `fixed-workflow` | Predefined sequence with known checks and exits | L1–L3 |
| `tool-assisted` | Tools retrieve, calculate, inspect, or validate while the primary goal remains unchanged | L1–L3 |
| `stateful-continuation` | Explicit state persists across context windows, sessions, approvals, or waits | L2–L4 |
| `agentic-loop` | Next step depends on observed tool/environment results under bounded retries | L3–L4 |
| `orchestrated-workers` | Separable workers have bounded scopes and explicit synthesis/handoffs | L5 |

Multi-agent availability only establishes feasibility. L5 requires separable work, a coordination contract, and value exceeding delegation and synthesis cost.

## Packaging is a separate decision

Task classification must not predetermine packaging.

```text
one-off task
reusable prompt
project guidance
procedural Skill
deterministic script or hook
reference/resource
external tool integration
specialist agent
runtime subagent
orchestrated workflow
```

A Skill candidate requires a stable activation boundary, inputs, procedure, output contract, missing-input behavior, and maintenance owner—not recurrence alone. A Skill should remain a Skill unless isolated context, distinct permissions/tools, adaptive specialist behavior, or routing among roles adds a necessary capability.

## Normalized failure-mode families

These names are synthesis candidates for `registry/failure_modes.json`. Domain-specific observable signals should attach to one normalized family instead of creating synonyms.

| Family | Normalized failure modes |
|---|---|
| Task and authority | `task-misinterpretation`, `task-drift`, `scope-creep`, `mode-or-authority-violation`, `ambiguous-intent` |
| Evidence | `unsupported-claim`, `unsupported-precision`, `citation-source-mismatch`, `source-authority-mismatch`, `applicability-overreach`, `stale-evidence`, `correlated-evidence-inflation`, `contradiction-flattening`, `poor-uncertainty-handling` |
| Context and state | `retrieval-miss`, `relevant-context-omission`, `distractor-contamination`, `context-overload`, `lossy-compaction`, `provenance-loss`, `state-loss`, `stale-state`, `branch-contamination` |
| Reasoning and search | `constraint-or-invariant-loss`, `premature-commitment`, `tunnel-vision`, `over-branching`, `unsupported-scoring`, `missing-premise-guessing`, `self-validation-loop`, `early-convergence`, `endless-ideation` |
| Software change | `context-mislocalization`, `premature-edit`, `surface-repair`, `incomplete-change-coverage`, `over-editing`, `under-editing`, `test-overfitting`, `test-oracle-mismatch` |
| Tools and actions | `tool-misselection`, `capability-hallucination`, `unsafe-target-resolution`, `unsafe-retry`, `unbounded-tool-loop`, `unverified-side-effect`, `untrusted-content-control-flow`, `false-reversibility`, `approval-validation-conflation` |
| Validation and exit | `under-verification`, `over-verification`, `evaluation-overclaim`, `premature-closure`, `weak-stopping-rule`, `failure-to-abstain`, `over-abstention`, `poor-handoff` |
| Packaging and delegation | `activation-ambiguity`, `overbroad-skill`, `always-on-context-bloat`, `progressive-disclosure-failure`, `capability-by-prose`, `permission-leak`, `agent-proliferation`, `delegation-partition-failure`, `version-drift`, `auto-packaging-noise`, `over-scaffolding` |

Normalization examples:

- “question drift” maps to `task-drift`; an initially misunderstood request maps to `task-misinterpretation`.
- Research selection omission and code-review false negatives map to `relevant-context-omission` with different domain signals.
- Weak verification maps to `under-verification`; repeated unnecessary checks remain `over-verification`.
- Research overreach and stateful overengineering map to `over-scaffolding`.
- Partial-session handoff maps to `poor-handoff`.

## Environment modifiers

Modifiers should be explicit booleans/enums or deterministic derived signals. Availability, permission, and task intent remain separate.

### Sources, evidence, and fidelity

```text
has_supplied_sources
source_boundary_closed
external_research_allowed
requires_citations
multimodal_input
long_context
multi_document
corpus_mutable
requires_exact_fidelity
contains_protected_literals
time_sensitive
evidence_conflicting
```

An explicit “no citations” sets `requires_citations=false`; it does not disable grounding or internal provenance. `source_boundary_closed` forbids external evidence even when web capability exists.

### Task mode, risk, and output

```text
review_only
editing_requested
action_requested
irreversible_action
human_approval_available
high_stakes
persistent_work
handoff_expected
structured_output_required
latency_or_cost_constrained
```

`review_only` is a hard no-edit boundary. Approval answers whether an action may occur; validation answers whether the proposed action is correct.

### Host capabilities and permissions

```text
shell_available
web_available
network_available
tools_required
file_write_allowed
branch_write_allowed
push_requested
merge_requested
deploy_requested
read_only_tooling
multi_agent_available
durable_state_available
```

Tool presence does not authorize tool use, credentials do not establish user intent, and Skill activation does not expand permissions.

### Project and workflow signals

```text
tests_available
acceptance_criteria_present
repository_instructions_present
multi_file_contract
public_api_or_schema
security_sensitive
production_critical
ci_available
cross_repository
large_repository
stable_task_boundary
stable_inputs_and_output
stable_procedure
project_specific_context
parallel_independent_work
tightly_shared_state
```

Useful derived signals include `context_window_pressure`, `task_underspecified`, `test_oracle_uncertain`, and `parallelizable_breadth`. Derived values must retain their observed reasons and must not be described as probabilities.

## Complexity ceiling

The machine-readable levels and per-archetype bounds are in [`registry/task_complexity_levels.json`](../registry/task_complexity_levels.json).

| Level | Name | Selection rule |
|---|---|---|
| L0 | Direct | One step, minimal controls, no persistent state |
| L1 | Controlled | Small bounded composition with one suitable check |
| L2 | Stateful | Explicit state, retrieval, or checkpoints are necessary |
| L3 | Evaluated | Material ambiguity/consequence justifies stronger or independent validation |
| L4 | Agentic | Adaptive tool loop with state, retries, action boundaries, and recovery |
| L5 | Orchestrated | Multiple separable workers with ownership, handoffs, budgets, and synthesis |

Apply lowering conditions before raising conditions. A project can be huge while the current task remains L0. A high-stakes task can remain L1 when one direct authoritative source and deterministic check settle the critical atom. Multiple tool calls do not imply L5.

## Upgradeable selection-prior map

The following maps recurring task/failure needs to candidate mechanisms. It does not replace the required 96-row component prior audit.

| Need | Candidate priors | Counterbalance or normal exclusion |
|---|---|---|
| Lock goal, scope, authority, or review/edit mode | `task-set-lock-in`, `authority-anchor-enforcement`; `clarification-gateway` when required state is missing | Do not lock an unresolved interpretation |
| Load only relevant components, sources, files, or tools | `scoped-loader`; `activation-budget-funnel` when many items compete | Avoid retrieval machinery for a short fixed input |
| Prevent invented source claims, capabilities, or observations | `grounding-no-invention`, `epistemic-status-gating` | Creative work may speculate when clearly labeled |
| Verify critical facts or transformations | `critical-atomic-verification`, `bidirectional-consistency` | Focus on outcome-changing atoms; do not validate everything equally |
| Keep citations aligned to nearby claims | `citation-fidelity` | Do not activate for outputs without attributed claims |
| Preserve literals, obligations, interfaces, and invariants | `zero-drift-zones`, `invariance-stress-scaffold`; `controlled-drift-corridors` when bounded change is allowed | Do not freeze material the user explicitly authorized changing |
| Avoid fixation and test alternatives | `anti-tunnel-vision`; `multiverse-reasoning` only within a justified branch budget | Direct authoritative answers and L0/L1 work suppress broad branching |
| Preserve long-running state and context | `stable-long-context`, `working-memory-lock-in`, `attention-compression-scaffold` | Derived summaries retain provenance; `meta-stability` waits for observed systemic degradation |
| Make the smallest authorized repair | `micro-repair`, with `invariance-stress-scaffold` when protected behavior exists | Exclude mutation in review-only mode and avoid architectural redesign |
| Plan before consequential action | `forethought-checkpoints`, `risk-tier-scaling` | A direct reversible action may need only one local check |
| Bound loops, retries, and failed strategies | `bounded-exit`, `reasoning-scale-controller` | Stop/reconcile before retrying ambiguous mutation |
| Handle conflicting or fragile evidence | `multi-truth-gating`, `truth-priority-hierarchy`; `parallel-qms` only for genuinely independent evidence | Correlated agreement is not independent confirmation |
| Fail safely on missing critical evidence or authority | `fail-closed-abstention`, `clarification-gateway` | Prefer a safe supported subset over whole-task refusal |
| Persist explicit workflow state | `stateblock`, `state-snapshot`; `sequential-memory-state-engine` for genuinely long workflows | No durable machinery for a one-turn direct task |
| Use external persistence or automation | `external-state-automation` only with a real store/tool and explicit authorization | Never claim hidden memory or implied action permission |

### Archetype-level recipe and component tendencies

- **Knowledge/explanation:** start direct; add grounding for external facts and education structure when teaching is requested.
- **Content understanding:** start with grounding and scoped loading; add citation or long-context controls only from explicit source/output conditions.
- **Transformation:** protect declared literals and invariants; use bounded change corridors rather than creative expansion.
- **Authoring:** use task lock and revision controls; evidence components enter only when factual/source-bearing output requires them.
- **Research:** grounding and provenance are central; anti-tunnel vision, multiple evidence gates, or orchestration depend on breadth, stakes, and independence.
- **Quantitative/constraint work:** represent state and constraints explicitly; prefer deterministic verification over repeated model self-review.
- **Planning/decision:** separate feasibility, alternatives, recommendation, authority, and action. Branch only when forks matter and can be evaluated.
- **Creative work:** protect the divergence/convergence phase boundary. Heavy validation during early ideation is normally counterproductive.
- **Software:** choose subtype and pipeline stage first. Review is read-only, repair is minimal, refactor protects behavior, and issue-to-patch is composite.
- **Audit:** require grounded findings and risk-scaled coverage; neither fluent criticism nor silence proves correctness.
- **Action:** capability, authentication, authorization, approval, target resolution, validation, and recovery are distinct gates.
- **Workflow/Skill:** prefer deterministic scripts for mechanical steps, progressive disclosure for context, and a single agent until separation adds a real capability.

## Deterministic resolution order

1. Normalize explicit task text and detect negation.
2. Identify one primary archetype and an optional subtype.
3. Record domain/project-profile priors separately.
4. Extract hard boundaries: review/edit/action authority, source scope, citation request, fidelity, approvals, and unavailable capabilities.
5. Detect observable failure signals and derived environment signals.
6. Apply the archetype’s default floor/ceiling, lowering before raising.
7. Rank candidate recipes using exact IDs, task phrases, aliases, purpose, subtype, and profile priors.
8. Prefer one primary recipe; allow no match or uncertainty.
9. Map required-by-recipe, trigger-likely, conditional, optional, excluded, and needs-agent-evaluation roles.
10. Enforce dependencies, conflicts, counterbalances, version locks, and the complexity ceiling.
11. Explain every material promotion/exclusion from task text, an observed signal, or a profile prior.

## Legitimate bounded outcomes

The resolver and connected agent must support:

```text
no confident recipe
missing required information
supported
qualified
conflicting
insufficient evidence
required capability unavailable
review complete without edits
action awaiting approval
partial success with reconciled state
no feasible option
all hypotheses unresolved
```

These states are preferable to invented closure or an unjustified maximal stack.

## Synthesis conclusions

1. Fifteen broad primary archetypes are enough for deterministic discovery when subtypes, domains, and execution forms remain separate.
2. Long context, tool use, high stakes, statefulness, orchestration, and Skill packaging are modifiers or execution decisions—not user goals by default.
3. Failure-targeted priors are more defensible than activating components from project type or keyword alone.
4. Complexity must suppress as well as promote. The first resolver question after classification is what is unnecessary.
5. Authority boundaries are hard restrictions, not soft scores.
6. Sources, citations, and external-research permission are independent fields.
7. Explicit project state is authoritative only according to its state class; compressed summaries cannot silently replace source-of-truth artifacts.
8. Independent validation means new information or a different failure surface, not repeated agreement.
9. Repetition makes a Skill eligible for consideration only after workflow stability is established.
10. The next ontology stages should align `failure_modes.json`, `environment_modifiers.json`, `composition_priors.json`, and the 96-component audit to the canonical names in this synthesis.
