# Recipe Review v0.2

All 16 recipes were reviewed against v0.2 package semantics.

| Recipe | Required | High cost | Review |
|---|---|---|:---:|
| `research-skill` | `task-set-lock-in`, `scoped-loader`, `stateblock`, `grounding-no-invention` | `multi-truth-gating`, `critical-atomic-verification` | PASS |

**Boundary:** Use for seed composition for research skill workflows when its required controls have active triggers.

**Required rationale:** `task-set-lock-in` — Prevent scope substitution and goal drift during execution. `scoped-loader` — Keep modular OS or Skill execution relevant, ordered, and within context limits instead of loading the full library at session start. `stateblock` — Give tools, agents, validators, and handoffs a shared source of current task truth. `grounding-no-invention` — Prevent fabricated facts, citations, measurements, policies, records, and gap-filling in source-grounded work.

**Important exclusion:** Omit durable or parallel machinery unless corpus size or real host execution triggers it.

| `source-grounded-analysis` | `task-set-lock-in`, `mode-lock-in`, `grounding-no-invention`, `citation-fidelity` | None | PASS |

**Boundary:** Use for seed composition for source-grounded analysis workflows when its required controls have active triggers.

**Required rationale:** `task-set-lock-in` — Prevent scope substitution and goal drift during execution. `mode-lock-in` — Keep behavior stable across long sessions, tool calls, and distracting inputs. `grounding-no-invention` — Prevent fabricated facts, citations, measurements, policies, records, and gap-filling in source-grounded work. `citation-fidelity` — Ensure citations prove the precise nearby claim instead of functioning as decorative evidence.

**Important exclusion:** Omit branching and creative expansion unless competing interpretations are an explicit deliverable.

| `high-stakes-reasoning` | `grounding-no-invention`, `epistemic-status-gating`, `risk-tier-scaling`, `critical-atomic-verification`, `multi-truth-gating`, `truth-priority-hierarchy`, `domain-mode-isolation`, `fail-closed-abstention`, `parallel-qms` | `critical-atomic-verification`, `multi-truth-gating`, `truth-redundancy`, `fail-closed-abstention`, `fermionic-veto` | PASS |

**Boundary:** Use for seed composition for high-stakes reasoning workflows when its required controls have active triggers.

**Required rationale:** `grounding-no-invention` — Prevent fabricated facts, citations, measurements, policies, records, and gap-filling in source-grounded work. `epistemic-status-gating` — Keep mixed-certainty reasoning auditable and stop conclusions from laundering inference or hypothesis into fact. `risk-tier-scaling` — Apply proportionate rigor so low-risk tasks remain efficient and high-risk claims or actions receive stronger evidence and fail-closed handling. `critical-atomic-verification` — Concentrate verification on the smallest facts whose failure would invalidate the output. `multi-truth-gating` — Reduce dependence on one fragile source, inference chain, or evaluator before a consequential conclusion is committed. `truth-priority-hierarchy` — Resolve conflicting signals without letting fluency, optimization, or an undifferentiated vote override stronger evidence or safety authority. `domain-mode-isolation` — Prevent cross-domain contamination while permitting explicit, reviewed transfers of shared facts. `fail-closed-abstention` — Ensure that missing essential support produces an explicit bounded result rather than fabricated closure. `parallel-qms` — Match validation topology to failure risk instead of treating QMS as one generic critic or a majority vote.

**Important exclusion:** Omit style and ideation modules; do not add simulated distributed evaluators.

| `medical-evidence` | `task-set-lock-in`, `grounding-no-invention`, `risk-tier-scaling`, `critical-atomic-verification`, `truth-priority-hierarchy`, `fail-closed-abstention`, `domain-mode-isolation`, `parallel-qms` | `critical-atomic-verification`, `fail-closed-abstention` | PASS |

**Boundary:** Use for seed composition for medical evidence workflows when its required controls have active triggers.

**Required rationale:** `task-set-lock-in` — Prevent scope substitution and goal drift during execution. `grounding-no-invention` — Prevent fabricated facts, citations, measurements, policies, records, and gap-filling in source-grounded work. `risk-tier-scaling` — Apply proportionate rigor so low-risk tasks remain efficient and high-risk claims or actions receive stronger evidence and fail-closed handling. `critical-atomic-verification` — Concentrate verification on the smallest facts whose failure would invalidate the output. `truth-priority-hierarchy` — Resolve conflicting signals without letting fluency, optimization, or an undifferentiated vote override stronger evidence or safety authority. `fail-closed-abstention` — Ensure that missing essential support produces an explicit bounded result rather than fabricated closure. `domain-mode-isolation` — Prevent cross-domain contamination while permitting explicit, reviewed transfers of shared facts. `parallel-qms` — Match validation topology to failure risk instead of treating QMS as one generic critic or a majority vote.

**Important exclusion:** Omit unconstrained generation and any validator whose evidence boundary cannot be supplied.

| `legal-evidence` | `task-set-lock-in`, `grounding-no-invention`, `risk-tier-scaling`, `critical-atomic-verification`, `truth-priority-hierarchy`, `citation-fidelity`, `fail-closed-abstention`, `parallel-qms` | `critical-atomic-verification`, `fail-closed-abstention` | PASS |

**Boundary:** Use for seed composition for legal evidence workflows when its required controls have active triggers.

**Required rationale:** `task-set-lock-in` — Prevent scope substitution and goal drift during execution. `grounding-no-invention` — Prevent fabricated facts, citations, measurements, policies, records, and gap-filling in source-grounded work. `risk-tier-scaling` — Apply proportionate rigor so low-risk tasks remain efficient and high-risk claims or actions receive stronger evidence and fail-closed handling. `critical-atomic-verification` — Concentrate verification on the smallest facts whose failure would invalidate the output. `truth-priority-hierarchy` — Resolve conflicting signals without letting fluency, optimization, or an undifferentiated vote override stronger evidence or safety authority. `citation-fidelity` — Ensure citations prove the precise nearby claim instead of functioning as decorative evidence. `fail-closed-abstention` — Ensure that missing essential support produces an explicit bounded result rather than fabricated closure. `parallel-qms` — Match validation topology to failure risk instead of treating QMS as one generic critic or a majority vote.

**Important exclusion:** Omit creative rewriting and preserve jurisdiction, date, authority, and quotation boundaries.

| `coding-debugging` | `task-set-lock-in`, `invariance-stress-scaffold`, `micro-repair` | `surgery-edit` | PASS |

**Boundary:** Use for seed composition for coding / debugging workflows when its required controls have active triggers.

**Required rationale:** `task-set-lock-in` — Prevent scope substitution and goal drift during execution. `invariance-stress-scaffold` — Operationalize the recovered name without pretending the original January 2026 mechanics were recovered. `micro-repair` — Restore local correctness or completeness with the minimum semantic blast radius.

**Important exclusion:** Omit Surgery Edit while the defect remains local; omit citation controls without external sources.

| `code-review` | `task-set-lock-in`, `scoped-loader`, `grounding-no-invention`, `invariance-stress-scaffold` | `critical-atomic-verification`, `fail-closed-abstention` | PASS |

**Boundary:** Use for seed composition for review-only code and pull request analysis when its required controls have active triggers.

**Required rationale:** `task-set-lock-in` — Prevent scope substitution and goal drift during execution. `scoped-loader` — Keep modular OS or Skill execution relevant, ordered, and within context limits instead of loading the full library at session start. `grounding-no-invention` — Prevent fabricated facts, citations, measurements, policies, records, and gap-filling in source-grounded work. `invariance-stress-scaffold` — Operationalize the recovered name without pretending the original January 2026 mechanics were recovered.

**Important exclusion:** Omit rewrite modules unless remediation is requested; review evidence must precede edits.

| `long-context-corpus` | `stateblock`, `sequential-memory-state-engine`, `stable-long-context`, `activation-budget-funnel`, `drift-suppression` | None | PASS |

**Boundary:** Use for seed composition for long-context / corpus workflows when its required controls have active triggers.

**Required rationale:** `stateblock` — Give tools, agents, validators, and handoffs a shared source of current task truth. `sequential-memory-state-engine` — Preserve sequence, provenance, relevance, and current truth across long-running work. `stable-long-context` — Extend usable context duration without treating the entire transcript as equally current or important. `activation-budget-funnel` — Protect limited active context by progressively disclosing sources and transferring verified evidence into compact indexed state before higher-level decisions. `drift-suppression` — Keep execution aligned after distracting context, repeated transformation, or model error.

**Important exclusion:** Omit full-corpus reloads and alternative-branch generation unless explicitly triggered.

| `authoring` | `task-set-lock-in`, `safe-rewrite`, `placeholder-suppression` | None | PASS |

**Boundary:** Use for seed composition for authoring workflows when its required controls have active triggers.

**Required rationale:** `task-set-lock-in` — Prevent scope substitution and goal drift during execution. `safe-rewrite` — Make paraphrase, polish, tone, or formatting safe by treating content atoms as invariants rather than suggestions. `placeholder-suppression` — Prevent scaffolding artifacts from escaping as if they were complete content.

**Important exclusion:** Omit citation fidelity for source-free drafting and omit structural surgery for tonal edits.

| `creative-ideation` | `task-set-lock-in`, `controlled-drift-corridors` | `multiverse-reasoning` | PASS |

**Boundary:** Use for seed composition for creative ideation workflows when its required controls have active triggers.

**Required rationale:** `task-set-lock-in` — Prevent scope substitution and goal drift during execution. `controlled-drift-corridors` — Enable adaptation, compression, or creativity without surrendering semantic control.

**Important exclusion:** Omit high-stakes evidence gates unless factual claims enter the deliverable.

| `education-explanation` | `pedagogical-alignment`, `task-set-lock-in` | None | PASS |

**Boundary:** Use for seed composition for education / explanation workflows when its required controls have active triggers.

**Required rationale:** `pedagogical-alignment` — Make correct content learnable and usable for a specified audience without diluting claims or inventing simplifications. `task-set-lock-in` — Prevent scope substitution and goal drift during execution.

**Important exclusion:** Omit deep validation stacks for low-risk exposition; retain accuracy checks that the domain requires.

| `decision-support` | `task-set-lock-in`, `decision-first-scaffold`, `grounding-no-invention` | None | PASS |

**Boundary:** Use for seed composition for decision support workflows when its required controls have active triggers.

**Required rationale:** `task-set-lock-in` — Prevent scope substitution and goal drift during execution. `decision-first-scaffold` — Keep analysis shaped around a decision, options, and decision criteria rather than accumulating directionless detail. `grounding-no-invention` — Prevent fabricated facts, citations, measurements, policies, records, and gap-filling in source-grounded work.

**Important exclusion:** Omit Multiverse when options are already fixed; never turn candidate generation into fake evidence.

| `architecture-skill-building` | `architect-orchestrator`, `scoped-loader`, `stateblock`, `parallel-qms` | `architect-orchestrator`, `power-mode`, `hybrid-mode`, `multiverse-reasoning`, `behavior-gene-builder`, `domain-core-builder`, `meta-supervisor`, `adapter-first-experimentation`, `surgery-edit`, `future-proof-mode-selector` | PASS |

**Boundary:** Use for seed composition for architecture / skill building workflows when its required controls have active triggers.

**Required rationale:** `architect-orchestrator` — Plan and coordinate modular system design from goal discovery through critique, localized repair, synthesis, and continuation state. `scoped-loader` — Keep modular OS or Skill execution relevant, ordered, and within context limits instead of loading the full library at session start. `stateblock` — Give tools, agents, validators, and handoffs a shared source of current task truth. `parallel-qms` — Match validation topology to failure risk instead of treating QMS as one generic critic or a majority vote.

**Important exclusion:** Omit suite-level supervision for a single small Skill and omit surgery for additive changes.

| `multi-agent-orchestration` | `architect-orchestrator`, `scoped-loader`, `state-routing-bus`, `stateblock`, `state-snapshot`, `domain-mode-isolation` | `architect-orchestrator`, `state-routing-bus` | PASS |

**Boundary:** Use for seed composition for multi-agent / orchestration workflows when its required controls have active triggers.

**Required rationale:** `architect-orchestrator` — Plan and coordinate modular system design from goal discovery through critique, localized repair, synthesis, and continuation state. `scoped-loader` — Keep modular OS or Skill execution relevant, ordered, and within context limits instead of loading the full library at session start. `state-routing-bus` — Pass explicit task state, decisions, evidence pointers, and module outputs through real host-supported handoffs. `stateblock` — Give tools, agents, validators, and handoffs a shared source of current task truth. `state-snapshot` — Create a stable checkpoint that can be resumed or audited after interruption. `domain-mode-isolation` — Prevent cross-domain contamination while permitting explicit, reviewed transfers of shared facts.

**Important exclusion:** Omit distributed claims when the host cannot provide isolated workers or result collection.

| `deterministic-intake-routing` | `task-set-lock-in`, `grounding-no-invention`, `scoped-loader`, `domain-mode-isolation`, `stateblock`, `authenticity-anti-evasion` | None | PASS |

**Boundary:** Use for seed composition for deterministic intake / routing workflows when its required controls have active triggers.

**Required rationale:** `task-set-lock-in` — Prevent scope substitution and goal drift during execution. `grounding-no-invention` — Prevent fabricated facts, citations, measurements, policies, records, and gap-filling in source-grounded work. `scoped-loader` — Keep modular OS or Skill execution relevant, ordered, and within context limits instead of loading the full library at session start. `domain-mode-isolation` — Prevent cross-domain contamination while permitting explicit, reviewed transfers of shared facts. `stateblock` — Give tools, agents, validators, and handoffs a shared source of current task truth. `authenticity-anti-evasion` — Keep process-status and completion claims auditable, especially when the host lacks a requested source, tool, persistent state, or execution capability.

**Important exclusion:** Omit model-judged routing when deterministic predicates fully decide the route.

| `long-context-source-fidelity` | `working-memory-lock-in`, `sequential-memory-state-engine`, `stateblock`, `stable-long-context`, `zero-drift-zones`, `drift-suppression`, `fail-closed-abstention` | `fail-closed-abstention`, `truth-redundancy` | PASS |

**Boundary:** Use for seed composition for long-context source fidelity workflows when its required controls have active triggers.

**Required rationale:** `working-memory-lock-in` — Prevent critical goals, constraints, identifiers, or safety conditions from being displaced by incoming context. `sequential-memory-state-engine` — Preserve sequence, provenance, relevance, and current truth across long-running work. `stateblock` — Give tools, agents, validators, and handoffs a shared source of current task truth. `stable-long-context` — Extend usable context duration without treating the entire transcript as equally current or important. `zero-drift-zones` — Protect facts, identifiers, quotations, obligations, safety limits, and other high-consequence content from transformation drift. `drift-suppression` — Keep execution aligned after distracting context, repeated transformation, or model error. `fail-closed-abstention` — Ensure that missing essential support produces an explicit bounded result rather than fabricated closure.

**Important exclusion:** Omit persistence when one context suffices and omit citation certification for inaccessible sources.

