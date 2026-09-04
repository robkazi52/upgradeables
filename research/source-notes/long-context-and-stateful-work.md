# Long-Context and Stateful Work

**Research track:** D — Long-context / corpus / stateful project work
**Access date:** 2026-09-03
**Status:** source notes for ontology synthesis; not an empirical claim that any Upgradeable improves task performance

## Scope and evidence boundary

This track covers long documents, multi-document corpora, repositories, tool-heavy sessions, multi-session continuation, explicit project state, retrieval, context budgeting, compaction, provenance, and handoff. A large advertised context window is not treated as proof that all included material will be used reliably.

Sections labeled **Evidence** report cited findings or documented engineering observations. Sections labeled **Synthesis** propose v0.3 ontology and selection rules. The latter are design inferences and should be tested against the other tracks and project fixtures.

## Evidence findings

| Evidence | Supported observation | Resolver implication |
|---|---|---|
| [Lost in the Middle](https://arxiv.org/abs/2307.03172) | On multi-document QA and key-value retrieval, changing where relevant information appeared caused significant performance variation; relevant material in the middle was often used less reliably than material at the beginning or end. | Do not equate “fits in the window” with “reliably accessible.” Promote targeted retrieval and evidence localization when relevant material is dispersed. |
| [LongBench](https://aclanthology.org/2024.acl-long.172/) | Long-context work spans materially different tasks: single- and multi-document QA, summarization, few-shot learning, synthetic retrieval, and code completion. Evaluated models still struggled as context grew. | `long_context` is an environment modifier, not one task archetype or one recipe. Route first by task, then apply context controls. |
| [RULER](https://arxiv.org/abs/2404.06654) | Claimed window size exceeded measured effective performance in the tested models. Increasing distractors, hops, chains, or aggregation demands caused degradation, incomplete retrieval, cross-chain mistakes, and more reliance on parametric knowledge. | Include distractor density, multi-hop dependence, and completeness requirements in complexity/risk signals. Simple needle retrieval is not a sufficient validation model. |
| [ALCE](https://aclanthology.org/2023.emnlp-main.398/) | More retrieved passages did not automatically improve correctness or citation quality in the reported experiments. Summaries/snippets improve capacity but are lossy, motivating the ability to revisit full passages. | Progressive loading should retain retrieval pointers and permit source rehydration; compression artifacts must not become the sole authority. |
| [Anthropic, *Effective context engineering for AI agents*](https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents) | Anthropic describes context as finite and recommends the smallest high-signal set, just-in-time retrieval, and compaction for long-horizon work. | Treat context as a budget. Prefer staged access over broad ingestion and compile transient work into explicit state. |
| [Anthropic, *Effective harnesses for long-running agents*](https://www.anthropic.com/engineering/effective-harnesses-for-long-running-agents) | Anthropic reports that compaction alone did not prevent half-finished work, state reconstruction, or premature completion. Its harness used explicit requirements, incremental work, progress artifacts, git history, and clean session boundaries. | Stateful work needs durable acceptance state and handoff artifacts in addition to compressed conversation. Prefer bounded increments with verification. |
| [OpenAI, *From model to agent: Equipping the Responses API with a computer environment*](https://openai.com/index/equip-responses-api-computer-environment/) | OpenAI documents bounded tool output, native compaction, and staging resources in a filesystem so agents can retrieve targeted inputs instead of packing everything into the prompt. | Tool output and corpus access should be bounded; project files can be durable state, while prompt context remains a disposable working set. |
| [MemGPT](https://arxiv.org/abs/2310.08560) | The paper evaluates explicit memory tiers and movement of information between limited active context and external storage for long documents and multi-session conversation. | Distinguish durable state, retrieval storage, and active context. Do not claim hidden memory: every retained item needs an explicit storage and retrieval path. |
| [RepoBench](https://openreview.net/forum?id=pPjZIOuQuF) | Repository-level completion was decomposed into cross-file retrieval, completion, and an integrated pipeline. | Repository understanding needs a retrieval stage; a repository profile must not cause indiscriminate code ingestion. |
| [SWE-bench](https://arxiv.org/abs/2310.06770) | Real issue resolution can require coordinating edits across functions, classes, files, tests, and execution environments over very large project context. | Codebase work can raise complexity, but only the current issue determines the working set and active recipe. |
| [Anthropic, multi-agent research engineering](https://www.anthropic.com/engineering/multi-agent-research-system) | The provider reports that agent state errors can compound, and uses explicit saved plans, retries, checkpoints, and resumable execution. It also reports that multi-agent systems are a poor fit for tightly coupled shared-context work. | Handoff and orchestration must preserve authoritative state and ownership. Parallel agents should not be selected solely because the corpus is large. |

## Proposed task archetypes — synthesis

Long context should usually modify one of these tasks rather than replace its task identity.

| Proposed slug | Plain name | Boundary and representative phrases | Default complexity |
|---|---|---|---|
| `long-document-qa` | Answer across one long document | “Find all places this report discusses…”, “Answer from this 200-page PDF.” | L1–L3 |
| `long-document-transformation` | Transform a long source with fidelity | Long rewrite, translation, restructuring, or extraction where literals/relationships must survive. | L1–L3 |
| `multi-document-corpus-analysis` | Analyze a bounded corpus | Questions, comparisons, or synthesis over many named documents. | L2–L4 |
| `repository-understanding` | Understand a codebase | Locate architecture, definitions, call paths, tests, or cross-file dependencies without necessarily editing. | L1–L3 |
| `long-horizon-project-execution` | Execute a project over many steps | Implementation/migration/research that cannot fit in one working session and requires incremental verified progress. | L3–L4 |
| `multi-session-continuation` | Resume prior work | “Continue from the last session”, explicit handoff, checkpoint, or fresh-agent continuation. | L2–L4 |
| `stateful-tool-workflow` | Maintain state across tool loops | Repeated file/API/database/browser operations with durable intermediate results and recovery needs. | L3–L4 |
| `cross-agent-handoff` | Transfer work between agents | Explicit delegation, supervisor/worker synthesis, or ownership transition. | L4–L5 |

A possible `dynamic-corpus-maintenance` archetype should be added only if other tracks show enough recurring tasks where sources change during execution. Otherwise model corpus mutability as an environment modifier.

## Explicit state model — synthesis

The harness should distinguish these state classes:

| State class | Meaning | Authority rule |
|---|---|---|
| `source_of_truth` | User-owned requirements, canonical documents, repository state, tests, or locked decisions | Never silently replaced by a summary. |
| `protected_state` | Goals, constraints, identifiers, safety conditions, acceptance tests | Kept continuously salient or reloaded before decisions. |
| `working_set` | Small task-relevant excerpts, files, tool results, and hypotheses | Disposable and refreshable. |
| `derived_summary` | Compression of prior work or source material | Must be labeled derived and retain provenance/retrieval pointers. |
| `progress_state` | Completed/incomplete items, validations, blockers, next step | Updated atomically at session boundaries. |
| `retrieval_index` | Stable locator from concepts/claims to sources | Pointer, not evidence by itself. |
| `handoff_packet` | Scope, authoritative state, changes, checks, unresolved decisions | Must separate verified facts from hypotheses and proposed next actions. |

This model forbids claims of hidden memory. If state is not in the active context or an explicit project artifact, the harness should treat it as unavailable.

## Observable failure modes — synthesis

| Failure-mode candidate | Observable signals | Primary controls to consider | Counterbalance / stopping condition |
|---|---|---|---|
| `context-overload` | Broad scans, giant prompt dumps, repeated irrelevant files, tool logs crowding out task facts. | `scoped-loader`, `activation-budget-funnel`, bounded tool output | Do not build retrieval machinery for a short source. |
| `middle-information-loss` | Relevant evidence exists but is ignored when buried among many documents or long sections. | `scoped-loader`, `critical-atomic-verification`, source indexing | Position heuristics are not proof; verify the actual critical atom. |
| `distractor-contamination` | Values or claims from nearby irrelevant passages/branches appear in the result. | `attention-compression-scaffold`, `grounding-no-invention`, `non-authoritative-branch-suppression` | Retain credible alternatives until authority/relevance is established. |
| `retrieval-miss` | Needed file/passage is absent from the working set; reasoning proceeds from memory. | `activation-budget-funnel`, `scoped-loader` | Stop when the bounded authoritative source resolves the question. |
| `lossy-compaction` | A summary drops constraints, provenance, exceptions, or unfinished work. | `stable-long-context`, `working-memory-lock-in`, retrieval pointers | Avoid duplicating the entire transcript; retain source-of-truth artifacts. |
| `provenance-loss` | Derived notes cannot be traced to exact files/passages/commands. | `citation-fidelity`, indexed state, `activation-budget-funnel` | Use lightweight pointers when full citation output is unnecessary. |
| `lost-state` | A resumed session repeats work, guesses prior actions, or forgets decisions. | `stable-long-context`, `working-memory-lock-in`, explicit progress/handoff state | Short single-session tasks do not need durable state machinery. |
| `stale-state` | Progress map or summary conflicts with current files, tests, or source versions. | `critical-atomic-verification`, `meta-stability` when widespread | Refresh from authoritative state before adding another summary layer. |
| `constraint-displacement` | New context causes goals, protected literals, or review-only limits to disappear. | `task-set-lock-in`, `working-memory-lock-in`, `zero-drift-zones` | Allow only explicit authorized constraint changes. |
| `branch-contamination` | Obsolete plans or speculative branches override a locked decision. | `non-authoritative-branch-suppression`, `controlled-drift-corridors` | Keep unresolved alternatives visible when authority is genuinely unsettled. |
| `partial-session-handoff` | Session ends mid-change with no status, validation, or recovery path. | `stable-long-context`, explicit handoff packet, incremental checkpoints | Do not force checkpoints around atomic work that fits comfortably in one session. |
| `premature-completion` | Agent sees progress and declares the project done despite failing acceptance items. | explicit acceptance state, `cross-checking-chains` | Stop promptly when all defined acceptance criteria are actually met. |
| `continuation-thrash` | Each new session re-reads the corpus and reconstructs the same plan. | `attention-compression-scaffold`, progress state, retrieval index | Refresh only state that may have changed. |
| `stateful-overengineering` | A one-step task creates memory stores, supervisors, or elaborate checkpoints. | complexity ceiling, `activation-budget-funnel` | L0/L1 tasks should remain direct. |

## Environment modifiers — synthesis

| Modifier | Selection effect |
|---|---|
| `long_context` | Promote context budgeting and targeted retrieval consideration; never activate a heavy stack by itself. |
| `multi_document` | Promote source identity, indexed retrieval, and provenance. |
| `corpus_mutable` | Require freshness/version checks before using prior summaries. This should be considered as a new modifier. |
| `requires_exact_fidelity` | Promote source rehydration and validation against originals after compression or transformation. |
| `contains_protected_literals` | Promote `zero-drift-zones` for numbers, quotations, identifiers, obligations, and interfaces. |
| `persistent_work` | Promote explicit progress state, checkpoints, and versioned artifacts. |
| `handoff_expected` | Require a handoff packet with authority, completion, validation, blockers, and next action. |
| `context_window_pressure` | Promote compression and staged retrieval. This is more precise than source length alone and should be considered as a derived modifier. |
| `shell_available` / `file_write_allowed` | Permit project-file state and targeted file access; do not infer permission to modify user content. |
| `tools_required` | Raise need for bounded outputs, retries, and explicit observation state. |
| `multi_agent_available` | Makes orchestration possible, not justified. Promote only when branches are independent and synthesis cost is acceptable. |
| `review_only` | Exclude editing even when repository context is present. |
| `structured_output_required` | Favor machine-checkable progress and handoff records. |
| `time_sensitive` | Prior state and cached retrieval require freshness checks. |

## Complexity implications — synthesis

- **L0 — Direct:** a short source or local fact fits comfortably; no persistent state or compression.
- **L1 — Controlled:** one long document or repository lookup with targeted retrieval and a small working set.
- **L2 — Stateful:** multi-document or continuation work needs explicit protected state, retrieval pointers, and progress records.
- **L3 — Evaluated:** dispersed evidence, exact-fidelity transformation, or long-running implementation adds checkpoint and source-of-truth validation.
- **L4 — Agentic:** repeated tool loops, mutable state, retries, resumability, and safe session boundaries.
- **L5 — Orchestrated:** multiple workers with explicit ownership, independent branches, durable handoffs, and supervisor synthesis.

Raise the ceiling for cross-session work, mutable corpora, multi-hop dependencies, protected literals, irreversible actions, many tool steps, or explicit handoffs. Lower it when the relevant source is short, the task is a local lookup/edit, the corpus is static and bounded, or one session can complete and verify the work.

## Candidate composition priors — synthesis

These are selection priors, not automatic activation.

| Task/risk | Promote for consideration | Normally suppress unless separately triggered |
|---|---|---|
| Long-document QA | `scoped-loader`, `activation-budget-funnel`, `grounding-no-invention`; `critical-atomic-verification` for decisive facts | persistent state, meta-supervision, multi-agent orchestration |
| Fidelity-preserving long transformation | `task-set-lock-in`, `zero-drift-zones`, `controlled-drift-corridors`, `bidirectional-consistency` | broad alternative search if the transformation contract is fixed |
| Multi-document corpus analysis | `activation-budget-funnel`, `attention-compression-scaffold`, `scoped-loader`, `citation-fidelity` when attribution is required | loading the entire registry or corpus into every turn |
| Repository understanding | `scoped-loader`, `activation-budget-funnel`, `working-memory-lock-in` for critical interfaces | editing components when the task is inspect/review only |
| Multi-session continuation | `stable-long-context`, `working-memory-lock-in`, `task-set-lock-in`, explicit progress and handoff state | `meta-stability` unless actual coherence degradation is observed |
| Stateful tool workflow | `stable-long-context`, `cross-checking-chains`, checkpoints, bounded outputs | orchestration when steps are tightly coupled |
| Stale or conflicting project state | `critical-atomic-verification`, `non-authoritative-branch-suppression`; `meta-stability` for systemic degradation | treating the newest summary as automatically authoritative |
| Cross-agent handoff | `task-set-lock-in`, `working-memory-lock-in`, explicit ownership/provenance; `multi-truth-gating` only for fragile consequential synthesis | shared full-context duplication across all workers |

## Recommendations to the synthesis agent

1. Keep `long_context` as an environment modifier; route by the underlying task archetype first.
2. Add `corpus_mutable` and consider a derived `context_window_pressure` modifier.
3. Make explicit state classes part of the harness contract: source of truth, protected state, working set, derived summary, progress, retrieval index, and handoff.
4. Require summaries to retain provenance and retrieval pointers; never let compaction silently replace authoritative sources.
5. Model advertised window size and effective usable context separately. The resolver should not use provider token limits as evidence of task reliability.
6. Promote `stable-long-context` only for actual continuation/long-running work, not every large file.
7. Select `meta-stability` only after observed systemic coherence degradation; it is too costly for ordinary retrieval misses.
8. Penalize multi-agent selection when branches share substantial context or have dense dependencies.
9. Add explicit fixture cases for stale summaries, resumption after partial work, protected literals, review-only repositories, and trivial tasks inside large projects.
10. Preserve the principle that a large project increases priors but the current task defines the active working set.

## Source list

- Liu et al. [Lost in the Middle: How Language Models Use Long Contexts](https://arxiv.org/abs/2307.03172), TACL 2024.
- Bai et al. [LongBench: A Bilingual, Multitask Benchmark for Long Context Understanding](https://aclanthology.org/2024.acl-long.172/), ACL 2024.
- Hsieh et al. [RULER: What’s the Real Context Size of Your Long-Context Language Models?](https://arxiv.org/abs/2404.06654), 2024.
- Gao et al. [Enabling Large Language Models to Generate Text with Citations](https://aclanthology.org/2023.emnlp-main.398/), EMNLP 2023.
- Anthropic. [Effective context engineering for AI agents](https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents), 2025.
- Anthropic. [Effective harnesses for long-running agents](https://www.anthropic.com/engineering/effective-harnesses-for-long-running-agents), 2025.
- OpenAI. [From model to agent: Equipping the Responses API with a computer environment](https://openai.com/index/equip-responses-api-computer-environment/), 2026.
- Packer et al. [MemGPT: Towards LLMs as Operating Systems](https://arxiv.org/abs/2310.08560), 2023.
- Liu, Xu, and McAuley. [RepoBench: Benchmarking Repository-Level Code Auto-Completion Systems](https://openreview.net/forum?id=pPjZIOuQuF), ICLR 2024.
- Jimenez et al. [SWE-bench: Can Language Models Resolve Real-World GitHub Issues?](https://arxiv.org/abs/2310.06770), ICLR 2024.
- Anthropic. [How we built our multi-agent research system](https://www.anthropic.com/engineering/multi-agent-research-system), 2025.
