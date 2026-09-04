# General LLM and agent task taxonomy

Research track A for the v0.3 selection ontology. Sources were reviewed on
2026-09-03.

## Scope and evidence labels

This note asks what people give general-purpose LLMs and agents to do, which
execution forms those tasks require, and which recurrent failures should alter
selection priors.

- **Evidence** means a finding stated or directly supported by a linked primary
  provider document or benchmark paper.
- **Synthesis** means a proposed normalization for Upgradeables. It is a design
  inference, not a claim that an Upgradeable has been empirically shown to
  improve the task.
- Benchmark inclusion demonstrates that a capability can be evaluated; it does
  not establish how common that task is in real use.

## Source-grounded findings

### Agentic form is not the task taxonomy

**Evidence.** Anthropic distinguishes workflows, whose paths are predefined in
code, from agents, which dynamically choose their process and tool use. It
recommends beginning with the simplest adequate solution because agentic systems
trade latency and cost for flexibility and performance. Its documented workflow
patterns are prompt chaining, routing, parallelization, orchestrator-workers,
and evaluator-optimizer loops. [A1]

**Evidence.** OpenAI similarly defines an agent by model-controlled workflow
execution and dynamic tool choice. It treats tools as either context/data tools
or action tools and recommends agents for workflows involving complex decisions,
unstructured data, or brittle rule systems; otherwise deterministic software
may suffice. [A2]

**Synthesis.** `direct`, `workflow`, `agentic`, and `orchestrated` should be
execution forms or complexity levels, not peer task archetypes. For example,
research can be direct, a fixed workflow, or an orchestrated agent task without
changing its underlying task archetype.

### Real assistant tasks compose multiple capabilities

**Evidence.** GAIA evaluates questions that combine reasoning, web browsing,
multimodal handling, and tool use. The tasks are designed around a single
verifiable answer but become harder as the number and kind of required steps
increase. [A3]

**Evidence.** AgentBench evaluates multi-turn behavior across operating-system,
database, knowledge-graph, web browsing, web shopping, household, game, and
lateral-reasoning environments. Its reported obstacles include weak long-term
reasoning, decision-making, and instruction following. [A4]

**Synthesis.** A resolver should classify the user's goal separately from the
capabilities needed to reach it. `web_available`, `tools_required`,
`multimodal_input`, and `multi_step` are environment/task modifiers, not reasons
to replace the goal with a generic `agent` category.

### Parallelism is conditional, not a default upgrade

**Evidence.** Anthropic recommends parallelization when subtasks are independent
or when diverse attempts increase confidence. Its production research system
uses an orchestrator-worker design for breadth-heavy searches, but reports that
vague delegation causes duplicate work, scope overlap, and coverage gaps. It
uses explicit objectives, boundaries, source guidance, and output formats for
workers. [A1] [A5]

**Synthesis.** `multi_agent_available` should only promote orchestration when
the task is decomposable, breadth or independent validation matters, and the
coordination cost stays below the benefit. It should not raise a simple task's
complexity ceiling by itself.

### Actions need stronger controls than information work

**Evidence.** OpenAI recommends risk-rating tools using properties such as
read-only versus write access, reversibility, permissions, and financial impact.
It identifies repeated failure and high-risk action as triggers for human
intervention. [A2]

**Evidence.** Anthropic's trustworthy-agent principles emphasize human control,
transparent operation, privacy, and secured interactions. It describes the
agent loop as plan, act, observe, adjust, and either finish or check with a
human. [A6]

**Synthesis.** Retrieval and action must be distinct modifiers. `web_available`
or `shell_available` does not imply permission to use them, and tool availability
does not imply permission to mutate state. Irreversible or consequential actions
should raise validation and approval requirements without necessarily changing
the primary task archetype.

### Stopping, validation, and handoff are first-class

**Evidence.** OpenAI describes explicit loop exit conditions such as a final
output, no further tool calls, errors, or maximum turns, and recommends layered
guardrails plus human escalation when failure thresholds are exceeded. [A2]

**Evidence.** Anthropic's multi-agent research report identifies continuing
after sufficient results, poor tool choice, overly narrow searches, duplicate
work, and missing coverage as operational failures. [A5]

**Synthesis.** A task map should include expected completion evidence and stop
conditions. `weak_stopping_rule`, `under_verification`, `over_verification`, and
`poor_handoff` are cross-task failure modes rather than standalone task types.

## Proposed normalized task archetypes

The following is a **synthesis** intended for deterministic discovery. The
names are deliberately broad; narrower intent belongs in subtypes and phrases.

| Archetype | User goal | Common subtypes | Normally excluded interpretation |
|---|---|---|---|
| `knowledge-explanation` | Obtain an answer or understanding | answer, explain, teach, troubleshoot conceptually | Does not imply external research |
| `content-understanding` | Derive meaning from supplied material | summarize, extract, classify, compare, synthesize | Does not imply changing source material |
| `content-transformation` | Change representation while preserving stated meaning or constraints | rewrite, translate, restructure, format, convert | Does not imply factual expansion |
| `content-authoring` | Produce new communicative material | report, documentation, proposal, outline, presentation plan | Does not imply source-grounded research unless requested |
| `research-grounding` | Locate and reconcile external or supplied evidence | search, fact-check, literature review, multi-source synthesis | Does not imply action on external systems |
| `quantitative-analysis` | Compute or interpret numeric/structured data | calculation, table analysis, statistics, data exploration | Does not imply open-ended ideation |
| `constraint-reasoning` | Find or verify a solution under explicit rules | logic, relational, spatial, scheduling, consistency | Does not imply exhaustive branching |
| `planning-design` | Define a future course or structure | project plan, decomposition, architecture, system or workflow design | Does not authorize implementation |
| `decision-support` | Compare choices against criteria | trade-off analysis, recommendation, prioritization | Does not make the decision or action by default |
| `creative-exploration` | Generate and develop alternatives | brainstorm, concepts, hypotheses, alternative designs | Does not require convergence unless requested |
| `software-engineering` | Understand, change, test, or review software | delegated to the coding taxonomy in track B | Does not authorize repository writes unless stated |
| `tool-mediated-retrieval` | Obtain state through a tool | files, search, APIs, databases | Read access only unless action is explicit |
| `action-execution` | Change external or durable state | write, send, deploy, transact, update records | Must not be inferred from analysis/recommendation |
| `workflow-automation` | Repeatedly run a stable trigger-to-output process | routing, extraction pipelines, scheduled processing | Not every repeated prompt warrants a Skill |
| `stateful-project-work` | Continue work while preserving explicit decisions and constraints | resume, maintain state, cross-session handoff | No hidden memory claim |
| `skill-agent-creation` | Package recurring instructions, references, tools, and validation | create Skill, configure agent, reusable workflow | Does not imply autonomous execution |
| `evaluation-audit` | Judge an artifact or process against criteria | review, validate, grade, red-team, quality audit | Review-only unless remediation is requested |

### Archetype boundaries

**Synthesis.** Several terms should be represented as orthogonal fields:

- `review` can specialize `evaluation-audit` with a domain such as code,
  evidence, policy, or quality.
- `generation`, `retrieval`, `transformation`, and `action` describe different
  relationships to state and therefore should not be collapsed into “create.”
- `planning-design` must remain separate from `action-execution`; a request for
  a plan does not authorize implementation.
- `workflow-automation`, `stateful-project-work`, and `skill-agent-creation`
  describe packaging or continuity as well as the work's domain. Preserve a
  secondary `domain_archetype` when useful.
- High-stakes status is a modifier, not an archetype. The same research,
  decision, or action task can become high-stakes.

## Recurring failure patterns

These are **synthesis categories** informed by the sources above.

| Failure-mode candidate | Observable signals | Commonly affected work | Selection implication |
|---|---|---|---|
| `task-drift` | Output stops serving the stated goal | long, multi-step, delegated tasks | Preserve task contract and checkpoints |
| `scope-or-mode-drift` | Analysis becomes editing, review becomes remediation | review, planning, tool work | Enforce explicit mode and authority |
| `ambiguous-intent` | Multiple plausible goals or missing success criteria | all, especially action and coding | Ask or return bounded alternatives |
| `unsupported-claim` | Claims lack supplied evidence or provenance | research, explanation, reports | Ground claims and retain citations |
| `constraint-loss` | Required literals, format, or rules disappear | transformation, reasoning, action | Lock and verify invariants |
| `premature-commitment` | First plausible route is accepted without checking | decisions, planning, diagnosis | Promote alternatives only when stakes/ambiguity justify them |
| `over-branching` | Search or reasoning expands past useful bounds | creative, research, planning | Apply complexity ceiling and stopping rule |
| `context-overload-or-loss` | Relevant evidence is omitted, stale, or displaced | corpora, long tasks, stateful work | Scope retrieval and externalize explicit state |
| `tool-selection-error` | Wrong tool, unsupported capability, or malformed use | tool and agent tasks | Check capability and tool contract |
| `action-authority-violation` | Mutation occurs without permission or before validation | action execution | Separate read/write and require approval as risk rises |
| `duplicate-or-gapped-delegation` | Workers overlap while another question is uncovered | orchestration | Partition objectives and synthesize coverage |
| `under-verification` | Completion asserted without suitable evidence | quantitative, action, code, high-stakes | Require risk-scaled validation |
| `over-verification` | Checks cost more than the bounded task warrants | trivial/direct tasks | Cap controls at task complexity |
| `weak-stopping-rule` | Agent loops after sufficient evidence or retries repeatedly | research and tool loops | Define success, retry, and escalation limits |
| `poor-handoff` | Result omits state, uncertainty, or next action | stateful and delegated work | Use explicit handoff contract |

## Environment modifiers

These are **synthesis recommendations**, not prevalence claims.

| Modifier | Effect on selection |
|---|---|
| `has_supplied_sources` | Promote source-bounded extraction and provenance; demote unnecessary web retrieval |
| `requires_citations` | Require claim-to-source alignment and citation validation |
| `external_research_allowed` | Permit web/search tools; absence or false value is a hard retrieval boundary |
| `multimodal_input` | Promote modality-aware extraction; do not treat absent OCR/vision as available |
| `long_context` / `multi_document` | Promote scoped retrieval, state, and coverage tracking; raise ceiling only when needed |
| `requires_exact_fidelity` / `protected_literals` | Promote invariance checks for transformation |
| `review_only` | Exclude editing and action components |
| `editing_requested` | Permit bounded mutation but retain scope and validation controls |
| `tools_required` | Require capability checks, tool contract, and observable results |
| `read_only_tooling` | Hard-exclude external mutation even when action tools exist |
| `irreversible_action` | Raise validation, approval, and fail-closed behavior |
| `human_approval_available` | Add a handoff point for consequential or uncertain actions |
| `persistent_work` / `handoff_expected` | Promote explicit state and concise continuation artifacts |
| `multi_agent_available` | Enables but does not require delegation; promote only for separable breadth |
| `structured_output_required` | Make schema conformance part of completion evidence |
| `high_stakes` | Raise evidence and validation requirements; lower tolerance for unsupported precision |
| `latency_or_cost_constrained` | Demote branching, repeated judges, and orchestration unless essential |

## Complexity implications

The following is **synthesis**, aligned with provider advice to begin simply:

| Level | Appropriate form | Raise to this level when | Do not raise merely because |
|---|---|---|---|
| L0 Direct | One response or deterministic operation | Goal and inputs are clear, impact is low | A powerful model is available |
| L1 Controlled | Small local composition with explicit constraints/check | Fidelity, scope, or a bounded validation matters | The task contains several nouns |
| L2 Stateful | Retrieval, checkpoints, or explicit state | Context is large, multi-document, resumable, or multi-step | The project itself is large but current task is trivial |
| L3 Evaluated | Alternatives or independent/risk-scaled validators | Ambiguity, high stakes, or hard-to-observe correctness warrants it | “Quality” appears in the prompt |
| L4 Agentic | Tool loop with bounded retries and exits | The model must adaptively gather state or act | A fixed workflow can solve the task |
| L5 Orchestrated | Multiple bounded workers plus synthesis | Work is separable, breadth is material, and coordination is justified | Parallel agents happen to be available |

Default ceiling recommendations:

- Knowledge explanation, simple extraction, and formatting: L0-L1.
- Multi-source research, consequential decisions, or long-corpus synthesis:
  L2-L3; L4 only when adaptive tools are actually required.
- External state-changing workflows: at least L1 controls, often L4 execution;
  risk determines approval and validation, not agent count.
- Orchestration: L5 only after a decomposition check.

## Ontology recommendations for synthesis

1. Store `task_archetype`, `execution_form`, `domain`, `failure_modes`,
   `environment_modifiers`, and `complexity_ceiling` separately.
2. Let explicit task wording outrank project-profile priors and tool
   availability.
3. Treat mutation authority as a hard constraint, not a ranking hint.
4. Prefer one primary archetype; attach secondary archetypes only for genuinely
   composite outputs.
5. Distinguish task success from process form: a report is `content-authoring`
   even if produced by a research workflow.
6. Keep validation risk-scaled. Under-verification and over-verification are
   dual failure modes.
7. Require an explicit decomposition justification before multi-agent priors.
8. Use benchmarks to identify capability bundles and failure surfaces, not to
   infer task prevalence or Upgradeable efficacy.
9. Keep the candidate-prior layer inspectable: each promotion or exclusion
   should cite task text, a modifier, or an observable failure risk.
10. A recurring task becomes a Skill candidate only when its inputs, procedure,
    boundaries, and output contract are stable. This is a synthesis criterion
    to be tested in research track H.

## Sources

- **[A1]** Anthropic, [Building effective agents](https://www.anthropic.com/engineering/building-effective-agents), 2024.
- **[A2]** OpenAI, [A practical guide to building agents](https://openai.com/business/guides-and-resources/a-practical-guide-to-building-ai-agents/), accessed 2026-09-03.
- **[A3]** Mialon et al., [GAIA: a benchmark for General AI Assistants](https://arxiv.org/abs/2311.12983), ICLR 2024.
- **[A4]** Liu et al., [AgentBench: Evaluating LLMs as Agents](https://arxiv.org/abs/2308.03688), ICLR 2024; arXiv revision 2025.
- **[A5]** Anthropic, [How we built our multi-agent research system](https://www.anthropic.com/engineering/multi-agent-research-system), 2025.
- **[A6]** Anthropic, [Trustworthy agents in practice](https://www.anthropic.com/research/trustworthy-agents), accessed 2026-09-03.
