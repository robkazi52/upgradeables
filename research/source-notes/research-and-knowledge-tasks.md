# Research and Knowledge Tasks

**Research track:** C — Research / knowledge / source-grounded work  
**Access date:** 2026-09-03  
**Status:** source notes for ontology synthesis; not an empirical claim that any Upgradeable improves task performance

## Scope and evidence boundary

This track covers finding information, answering from supplied material, checking claims, comparing evidence, and producing source-grounded syntheses. It does not treat every factual question as “deep research,” and it does not treat citation presence as proof of correctness.

Sections labeled **Evidence** summarize cited sources. Sections labeled **Synthesis** propose deterministic resolver categories and selection priors for Upgradeables v0.3. Those proposals are design inferences, not externally validated performance claims.

## Evidence findings

| Evidence | Supported observation | Resolver implication |
|---|---|---|
| [OpenAI, *Introducing deep research*](https://openai.com/index/introducing-deep-research/) | Open-ended research can require iterative search, source interpretation, synthesis, and changes of direction. The provider also reports remaining risks around hallucination, source authority, confidence calibration, and citation formatting. | Distinguish open-ended investigation from direct lookup; require source-quality and uncertainty controls when the work is consequential. |
| [Anthropic, *How we built our multi-agent research system*](https://www.anthropic.com/engineering/multi-agent-research-system) | Research paths can be dynamic and breadth-first. Anthropic reports gains for independently parallelizable searches, but much higher token use and a poor fit when workers must share tightly coupled context. It evaluates factual accuracy, citation accuracy, completeness, source quality, and tool efficiency separately. | Parallel research should be conditional on breadth, independence, value, and available budget—not the default for “research.” Separate answer quality, support, coverage, source quality, and cost. |
| [OpenAI, BrowseComp](https://openai.com/index/browsecomp/) | Hard-to-find factual retrieval may require searching many sites. BrowseComp deliberately uses short, stable, verifiable answers and warns that this does not establish performance on open-ended user work. | Add a hard-to-find retrieval archetype, but do not use a lookup benchmark as the ontology for synthesis or literature review. |
| [WebGPT](https://arxiv.org/abs/2112.09332) | Browser-assisted long-form QA collected references during browsing so factual accuracy could be evaluated more easily. | Preserve source pointers during retrieval rather than reconstructing citations after drafting. |
| [Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks](https://papers.neurips.cc/paper/2020/hash/6b493230205f780e1bc26945df7481e5-Abstract.html) | Retrieval can improve knowledge-intensive QA and generation relative to a parametric-only baseline in the studied settings. | `external_research_allowed`, corpus availability, and retrieval capability materially change the feasible workflow; model memory alone is not a source boundary. |
| [FEVER](https://arxiv.org/abs/1803.05355) | Textual claim verification naturally includes at least supported, refuted, and not-enough-information outcomes, with evidence attached to supported/refuted judgments. | A verifier must allow explicit insufficient-evidence outcomes and must not force binary closure. |
| [QASPER](https://aclanthology.org/2021.naacl-main.365/) | Full-paper QA can require evidence from multiple parts of a document; the benchmark records supporting evidence, and reported model performance remained well below humans. | Single-document does not imply simple. Evidence localization and answer generation should remain distinct checks. |
| [ALCE](https://aclanthology.org/2023.emnlp-main.398/) | Citation correctness, citation completeness, answer correctness, and fluency are separable. The study found substantial missing support and found that adding more passages did not automatically improve results. | Activate citation checking only when attribution is required, and check whether each nearby claim is actually entailed. More context is not automatically better evidence. |
| [PRISMA 2020](https://www.bmj.com/content/372/bmj.n71) | A systematic review uses explicit methods for search, selection, appraisal, and synthesis, with transparent reporting of included/excluded material. | Reserve “systematic evidence review” for tasks with an explicit protocol and audit trail; do not inflate an ordinary web search into this workflow. |
| [GAIA](https://arxiv.org/abs/2311.12983) | Realistic information-seeking tasks can combine reasoning, browsing, multimodal inputs, and tools even when the human-facing question looks simple. | Complexity depends on the evidence path and tools required, not only the apparent length of the requested answer. |

## Proposed task archetypes — synthesis

The following categories should be tested against the other research tracks and merged where that improves resolver clarity.

| Proposed slug | Plain name | Boundary and representative phrases | Default complexity |
|---|---|---|---|
| `source-bounded-qa` | Answer from supplied sources | “According to these files…”, “What does this paper say?”, “Find the clause in this document.” No external evidence unless authorized. | L0–L2 |
| `targeted-fact-retrieval` | Find a specific fact | “Find the date/number/name…”, “Look up who…”. Expected output is narrow and verifiable. | L0–L2; L3 when difficult or consequential |
| `claim-verification` | Verify or refute a claim | “Fact-check this”, “Is this claim supported?”, “Confirm from primary sources.” Must allow insufficient evidence. | L1–L3 |
| `single-document-analysis` | Analyze one substantial source | “Analyze this paper/report/PDF”, including evidence dispersed across sections. Distinct from summarization when a question or analytic frame governs selection. | L1–L3 |
| `multi-source-comparison` | Compare sources or options | “Compare these studies/policies/products”, preserving which source supports each difference. | L1–L3 |
| `evidence-synthesis` | Reconcile evidence into a conclusion | “Synthesize the evidence”, “What does the literature indicate?”, including agreement, conflict, and uncertainty. | L2–L4 |
| `systematic-evidence-review` | Protocol-driven literature review | Explicit search/selection/appraisal protocol, inclusion criteria, and audit trail. Do not select from the word “research” alone. | L3–L4 |
| `open-web-investigation` | Explore an open question | Multi-step discovery where relevant sources and subquestions are not known in advance. | L2–L4 |
| `breadth-first-research` | Research independent branches in parallel | Enumerative or broad coverage request with separable branches and enough value/budget. Multi-agent execution is optional. | L4–L5 |

`citation-bearing authoring` should remain an authoring/output modifier rather than a separate research archetype unless the synthesis group finds a deterministic routing benefit.

## Observable failure modes — synthesis

| Failure-mode candidate | Observable signals | Primary controls to consider | Counterbalance / stopping condition |
|---|---|---|---|
| `question-drift` | Search or answer addresses a nearby question; inclusion criteria change without notice. | `task-set-lock-in`, `working-memory-lock-in` | Permit an explicit scope revision when new evidence makes the original framing untenable. |
| `retrieval-miss` | Known relevant entity/section is absent; queries are narrow synonyms; evidence gaps remain. | `anti-tunnel-vision`, `scoped-loader` | Stop broadening when the answer is directly established or the search budget is exhausted. |
| `source-authority-mismatch` | Secondary summaries replace an available primary source; SEO rank is treated as authority. | `grounding-no-invention`, `critical-atomic-verification` | One direct authoritative source may be sufficient for a low-risk atom. |
| `unsupported-claim` | A factual statement has no supporting source or exceeds what sources say. | `grounding-no-invention`, `epistemic-status-gating`, `fail-closed-abstention` | Creative or explicitly speculative content should be labeled, not suppressed as if factual. |
| `unsupported-precision` | Exact number/date/causal claim is inferred from approximate or indirect evidence. | `critical-atomic-verification`, `epistemic-status-gating` | Concentrate verification on outcome-changing atoms. |
| `citation-source-mismatch` | Citation is nearby but does not entail the claim, or supports only part of it. | `citation-fidelity` | Do not activate when the output has no attributed claims. |
| `evidence-selection-omission` | Answer ignores relevant sections, sources, or counterevidence in the defined corpus. | `scoped-loader`, `activation-budget-funnel`, `cross-checking-chains` | Do not demand exhaustive search for a bounded low-risk lookup. |
| `contradiction-flattening` | Conflicting findings are averaged or reported as consensus without reconciliation. | `multi-truth-gating`, `epistemic-status-gating`, `bidirectional-consistency` | Do not manufacture disagreement when sources answer different questions. |
| `provenance-loss` | Notes or synthesis statements cannot be traced back to exact sources. | `citation-fidelity`, `activation-budget-funnel` | Preserve pointers, not necessarily full source text, in active context. |
| `stale-evidence` | Time-sensitive answer relies on undated or superseded material. | `critical-atomic-verification`, `fail-closed-abstention` | Apply only when recency can change the result. |
| `premature-search-closure` | First plausible answer ends search despite explicit breadth/verification requirements. | `anti-tunnel-vision`, `multi-truth-gating` | A stopping rule is mandatory; breadth without discrimination becomes waste. |
| `research-overreach` | A direct lookup expands into many agents, sources, or validation layers. | complexity ceiling, `activation-budget-funnel` | L0/L1 tasks should default to one authoritative lookup or the supplied source. |

## Environment modifiers — synthesis

| Modifier | Selection effect |
|---|---|
| `has_supplied_sources` | Promote source-bounded QA/analysis and `grounding-no-invention`; restrict claims to the supplied corpus unless broader research is explicitly allowed. |
| `closed_source_boundary` | Hard restriction against outside evidence. This useful modifier is not in the provisional list and should be considered for addition. |
| `external_research_allowed` | Permit retrieval/open-web archetypes; absence must not be interpreted as permission. |
| `requires_citations` | Promote `citation-fidelity` and provenance capture. Citation-free output should not activate citation machinery merely because sources were consulted. |
| `no_citations_requested` | Demote citation formatting, but not factual grounding or internal source tracking. |
| `multi_document` | Promote scoped loading, evidence indexing, and explicit source identity. |
| `long_context` | Raise retrieval/context-management consideration, not research depth by itself. |
| `requires_exact_fidelity` / `contains_protected_literals` | Promote `zero-drift-zones` and critical-atom verification for quotations, figures, names, and identifiers. |
| `time_sensitive` | Promote recency checks and source dates; stale support may require abstention. |
| `web_available` / `tools_required` | Make open retrieval executable. If absent, report the capability boundary rather than simulate browsing. |
| `high_stakes` | Raise evidence quality, uncertainty, and validation requirements without importing domain policy. |
| `structured_output_required` | Preserve evidence-to-field mapping and validate completeness separately from prose quality. |
| `review_only` | Exclude editing/action components; research outputs remain advisory. |

## Complexity implications — synthesis

- **L0 — Direct:** supplied-source extraction, simple summary, or one stable fact from an authoritative source. Usually no branching, ledger, or multi-agent work.
- **L1 — Controlled:** bounded QA, low-risk verification, or small comparison with grounding and only the validators the output requires.
- **L2 — Stateful:** multiple documents or iterative search require an explicit question, source index, evidence notes, and stopping rule.
- **L3 — Evaluated:** conflicting evidence, protocol-driven reviews, consequential claims, or citation-bearing synthesis justify claim-level validation and uncertainty handling.
- **L4 — Agentic:** open-web investigation requiring repeated search/tool loops, query revision, and checkpointed state.
- **L5 — Orchestrated:** only for valuable breadth-first questions with genuinely independent branches; tightly coupled questions should remain single-agent or carefully staged.

Lower the ceiling when the answer is a direct transformation, the corpus is short and closed, one authoritative source resolves the question, citations are not requested, or the user asks for a quick orientation. Raise it for dispersed evidence, contested claims, changing facts, many independent branches, explicit systematic-review methods, or consequential conclusions.

## Candidate composition priors — synthesis

These are consideration pools, not activation claims.

| Task/risk | Promote for consideration | Normally suppress unless separately triggered |
|---|---|---|
| Supplied-source QA | `task-set-lock-in`, `grounding-no-invention`; `scoped-loader` for a large source | `multiverse-reasoning`, `parallel-qms`, orchestration |
| Targeted fact retrieval | `grounding-no-invention`, `critical-atomic-verification`; `citation-fidelity` when citation requested | long-context/state machinery for one short lookup |
| Claim verification | `grounding-no-invention`, `epistemic-status-gating`, `critical-atomic-verification`, `fail-closed-abstention` | forced consensus or binary answer when evidence is insufficient |
| Multi-source comparison/synthesis | `task-set-lock-in`, `scoped-loader`, `citation-fidelity`, `cross-checking-chains`, `controlled-drift-corridors` | exhaustive branching without a coverage requirement |
| Systematic evidence review | `activation-budget-funnel`, `scoped-loader`, `grounding-no-invention`, `citation-fidelity`, `epistemic-status-gating`, explicit state/checkpoints | autonomous actions; maximal meta-controls before the protocol is fixed |
| Open investigation | `anti-tunnel-vision`, `grounding-no-invention`, `citation-fidelity`, `epistemic-status-gating`; `fail-closed-abstention` for unresolved essentials | multi-agent work when branches share most context or expected value is low |

## Recommendations to the synthesis agent

1. Preserve separate archetypes for retrieval, verification, and synthesis; lexical “research” is too broad to select a workflow.
2. Model citation requirement, source boundary, and external-research permission independently.
3. Add `closed_source_boundary` (or an equivalent restriction) to environment modifiers.
4. Make `SUPPORTED`, `REFUTED`, and `INSUFFICIENT_EVIDENCE` valid resolver/output states for verification.
5. Treat source authority, claim support, citation entailment, coverage, and freshness as distinct failure dimensions.
6. Use multi-agent research only as an L5 prior for independent breadth; apply a strong complexity/cost penalty otherwise.
7. Keep systematic reviews distinct from ordinary evidence synthesis through explicit protocol signals.
8. Ensure “no citations” demotes citation presentation without licensing unsupported claims.

## Source list

- OpenAI. [Introducing deep research](https://openai.com/index/introducing-deep-research/), 2025, updated through 2026.
- Anthropic. [How we built our multi-agent research system](https://www.anthropic.com/engineering/multi-agent-research-system), 2025.
- Wei et al. [BrowseComp: A Simple Yet Challenging Benchmark for Browsing Agents](https://arxiv.org/abs/2504.12516), 2025.
- Nakano et al. [WebGPT: Browser-assisted question-answering with human feedback](https://arxiv.org/abs/2112.09332), 2021.
- Lewis et al. [Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks](https://papers.neurips.cc/paper/2020/hash/6b493230205f780e1bc26945df7481e5-Abstract.html), NeurIPS 2020.
- Thorne et al. [FEVER: a large-scale dataset for Fact Extraction and VERification](https://aclanthology.org/N18-1074/), NAACL 2018.
- Dasigi et al. [A Dataset of Information-Seeking Questions and Answers Anchored in Research Papers](https://aclanthology.org/2021.naacl-main.365/), NAACL 2021.
- Gao et al. [Enabling Large Language Models to Generate Text with Citations](https://aclanthology.org/2023.emnlp-main.398/), EMNLP 2023.
- Page et al. [The PRISMA 2020 statement](https://www.bmj.com/content/372/bmj.n71), BMJ 2021.
- Mialon et al. [GAIA: a benchmark for General AI Assistants](https://arxiv.org/abs/2311.12983), ICLR 2024.
