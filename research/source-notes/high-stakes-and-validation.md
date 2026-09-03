# High-Stakes and Validation Workflow Patterns

Research track: G — evidence quality, uncertainty, escalation, abstention, human
oversight, and risk-scaled validation.

Date accessed: 2026-09-03

## Scope and evidence labels

This note concerns workflow and control patterns, not medical, legal, financial, or
other domain policy. It does not define which substantive answer is correct and does
not claim that an Upgradeable has demonstrated empirical benefit.

- **Evidence** means the linked primary source explicitly supports the pattern.
- **Synthesis** means this document proposes a normalized category or resolver rule
  from the sources.
- **Selection prior** means the mapped Upgradeable should be considered and then
  evaluated against its canonical trigger and non-trigger.

“High stakes” should normally be treated as an environment/risk modifier, not as a
single content domain. The operative question is whether an unsupported claim or
incorrect action could materially affect safety, health, rights, finances, access,
reputation, critical operations, or another consequential outcome.

## Source-supported findings

| Finding | Label | Source support |
|---|---|---|
| Risk controls should be selected in context and in proportion to risk tolerance rather than applied as one universal checklist. | Evidence | NIST's AI RMF ties needed risk-management activity to organizational risk tolerance and says Playbook users should select practices appropriate to their context. [AI RMF Core](https://airc.nist.gov/airmf-resources/airmf/5-sec-core/), [AI RMF Playbook](https://airc.nist.gov/airmf-resources/playbook/) |
| Intended use, knowledge limits, human oversight, likely impact, and error costs should be mapped before measurement and action. | Evidence | NIST MAP outcomes call for documented task scope, knowledge limits, human oversight, expected costs, and likelihood/magnitude of impact. [AI RMF Core](https://airc.nist.gov/airmf-resources/airmf/5-sec-core/) |
| Validation should use objective, repeatable, or scalable methods, document measurement uncertainty, and reflect deployment-like conditions. | Evidence | NIST MEASURE outcomes call for documented TEVV, uncertainty, appropriate benchmarks, repeatable methods, and demonstration under conditions similar to deployment. [AI RMF Core](https://airc.nist.gov/airmf-resources/airmf/5-sec-core/) |
| Independent review can improve testing and mitigate internal bias or conflicts, but each measurement should add meaningful information. | Evidence | NIST states both points directly; this supports independent validation where justified, not automatic duplication of every check. [AI RMF Core](https://airc.nist.gov/airmf-resources/airmf/5-sec-core/) |
| Systems should fail safely beyond their knowledge limits and residual risk should remain within the applicable tolerance. | Evidence | NIST MEASURE 2.6 explicitly includes safe failure beyond knowledge limits, monitoring, reliability, robustness, and response time. [AI RMF Core](https://airc.nist.gov/airmf-resources/airmf/5-sec-core/) |
| Claims of model capability should be empirically evaluated; narrow anecdotal results should not be extrapolated; sources and citations require review. | Evidence | NIST AI 600-1 actions MS-2.3-002, MS-2.5-001, and MS-2.5-003 address these practices. [Generative AI Profile](https://doi.org/10.6028/NIST.AI.600-1) |
| Monitoring should support override, incident response, recovery, change management, and prompt escalation; errors and near-misses should be tracked. | Evidence | NIST AI 600-1 MANAGE actions call for these mechanisms and for qualified actors to escalate reported issues. [Generative AI Profile](https://doi.org/10.6028/NIST.AI.600-1) |
| Governance, data quality, performance against objectives, and monitoring are complementary accountability controls. | Evidence | GAO's accountability framework organizes practices under those four principles and supplies audit questions and procedures. [GAO-21-519SP](https://www.gao.gov/products/gao-21-519sp) |
| Uncertainty disclosure should scale with both degree of uncertainty and impact of error; high-stakes situations warrant heightened caution. | Evidence | OpenAI's public Model Spec explicitly identifies these dimensions and distinguishes knowledge, recency, intent, inherent-world, and prediction uncertainty. [Model Spec — Express uncertainty](https://model-spec.openai.com/2025-02-12.html#express-uncertainty) |
| Sensitive, irreversible, or high-stakes actions and exceeded failure thresholds are triggers for human intervention. | Evidence | OpenAI's agent guide identifies both as primary human-intervention triggers. [A practical guide to building agents](https://openai.com/business/guides-and-resources/a-practical-guide-to-building-ai-agents/) |

## Proposed task and risk archetypes

The categories below are **Synthesis**. They may overlap with primary task archetypes;
the high-stakes marker modifies the controls rather than replacing “research,”
“decision support,” “review,” or “action execution.”

| Archetype | Description | Example | Typical complexity |
|---|---|---|---|
| `consequential-evidence-synthesis` | Assemble and qualify evidence that may inform a material decision. | Compare source-backed options affecting health, rights, money, or operations. | L2–L3 |
| `critical-claim-verification` | Verify one or a few facts whose error could change the outcome. | Check an eligibility date, threshold, identity, dosage quoted from a source, or contract term. | L1–L3 according to impact |
| `consequential-decision-support` | Compare choices while keeping evidence, assumptions, value judgments, and authority distinct. | Recommend among materially different operational options. | L2–L3 |
| `high-impact-review` | Review an artifact for failures with material downstream consequences. | Security-sensitive code review or pre-publication factual review. | L2–L3 |
| `high-impact-action` | Execute or authorize a consequential side effect. | Deploy, transact, delete, submit, notify, or modify a rights-affecting record. | L3–L4 |
| `incident-triage-and-escalation` | Detect, bound, preserve, and route an observed or suspected harmful failure. | Respond to a critical incorrect output or unsafe automation behavior. | L3–L5 depending on coordination |

## Proposed risk dimensions

This is a **Synthesis** model for task-time modifiers. A resolver should not produce
a fake numerical probability. It can instead record ordinal, explainable signals.

```text
impact_magnitude: low | moderate | high | critical | unknown
affected_scope: individual | group | organization | public | unknown
reversibility: easy | partial | difficult | irreversible | unknown
time_sensitivity: routine | time-sensitive | urgent | immediate | unknown
evidence_availability: sufficient | partial | conflicting | unavailable | unknown
source_authority: direct/authoritative | credible-secondary | weak | unknown
independent_check_available: yes | no | unknown
human_review_available: yes | no | unknown
action_requested: no | draft-only | reversible | consequential
```

Unknown risk-relevant values should promote clarification or conservative handling,
not be silently converted to low risk.

## Evidence quality model

The following dimensions are **Synthesis**, informed by NIST's emphasis on data
quality, provenance, deployment context, source/citation verification, uncertainty,
and documented TEVV.

| Dimension | Question | Observable weakness |
|---|---|---|
| Authority | Is the source entitled and competent to establish this claim in the relevant context? | Commentary is treated as controlling authority. |
| Directness | Does the source directly support the proposition, or only a nearby inference? | Citation exists but does not entail the claim. |
| Applicability | Do jurisdiction, population, version, date, conditions, and intended use match? | Valid evidence is generalized beyond its conditions. |
| Recency/version | Is the source current for a time-sensitive or version-sensitive claim? | Superseded material is presented as current. |
| Provenance | Can the claim be traced to a stable source, passage, dataset, or observed tool result? | Source identity or transformation lineage is missing. |
| Independence | Do corroborating sources/checks add genuinely independent information? | Several sources repeat one unverified origin. |
| Completeness/coverage | Were material contrary evidence and known source gaps included? | Convenient supporting evidence substitutes for the authorized corpus. |
| Measurement fitness | Does the validator actually test the requirement under relevant conditions? | A passing proxy metric is presented as proof of the real outcome. |

Evidence quality and quantity are not interchangeable. One directly controlling
source may outweigh many derivative sources; multiple checks that share the same
assumption do not create independent confirmation.

## Proposed claim states

This compact vocabulary is **Synthesis** and is intended to prevent unsupported
binary confidence claims.

| State | Meaning | Permitted output behavior |
|---|---|---|
| `supported` | Direct, applicable evidence supports the bounded claim. | State claim with source and scope. |
| `qualified` | Evidence supports only a narrower or conditional claim. | State the supported subset and qualification. |
| `conflicting` | Material credible sources or validators disagree. | Preserve disagreement, authority/date/context, and unresolved consequence. |
| `insufficient` | Available evidence cannot establish the requested precision or conclusion. | Abstain from that claim; identify missing evidence. |
| `unavailable` | Required source, tool, expert, or environment cannot be accessed. | Report capability boundary and safe next step. |
| `not-evaluated` | The claim was outside the authorized scope or validation budget. | Do not imply review; list it as unassessed when material. |

Natural-language uncertainty should identify its source and behavioral consequence.
Invented percentages or confidence scores are inappropriate unless a defined,
validated measurement method supplies them.

## Risk-scaled validation ladder

This ladder is **Synthesis**. It operationalizes proportionality and a complexity
ceiling; it is not a domain standard.

| Risk level | Minimum validation | Possible additions | Stop/escalate condition |
|---|---|---|---|
| Low | Basic consistency or direct output check | One source/tool check if central | Missing check can be disclosed without blocking when consequences are trivial |
| Moderate | Verify material claims/constraints and inspect source or postcondition | Focused counterexample, second method, or human review when ambiguity persists | Stop the unsupported portion if evidence remains partial |
| High | Claim-level provenance, applicability check, explicit uncertainty, focused independent/deterministic validator, and qualified human review where available | Adversarial/counterfactual check, broader coverage, specialist handoff | Fail closed on a decision-critical unsupported claim or unauthorized action |
| Critical | Predefined acceptance criteria, authoritative evidence, independent review, exact action preflight, durable audit record, recovery/incident path, explicit approval | Staged/sandbox execution, two-person control, simulation, rollback rehearsal where the real system supports them | Do not execute when authority, target, evidence, or safe-failure path is unresolved |

More validation is not automatically better. Add a check only when it addresses a
material failure mode or supplies independent information. Excessive redundant
checking can delay urgent work, obscure the decision-critical claim, and create false
confidence through correlated agreement.

## Proposed high-stakes workflow

This nine-stage process is **Synthesis**.

1. **Lock task and authority.** Record the decision/action being supported, intended
   user, scope, deadline, and whether the output is analysis, recommendation, draft,
   or execution authority.
2. **Map consequence and tolerance.** Identify impact magnitude, affected scope,
   reversibility, time sensitivity, and decision-critical claims.
3. **Set the evidence boundary.** Declare authorized sources, external research
   permission, applicable date/version/jurisdiction, and inaccessible material.
4. **Build a claim-evidence ledger.** Separate observed facts, source statements,
   calculations, assumptions, inferences, value judgments, and unresolved questions.
5. **Evaluate evidence fitness.** Check authority, directness, applicability, recency,
   provenance, independence, coverage, and measurement fitness.
6. **Apply proportionate validators.** Start with deterministic/direct checks; add an
   independent method, counterexample, or qualified reviewer only when it can reveal
   a material distinct failure.
7. **Resolve conflict without averaging it away.** Apply declared authority and
   applicability rules, preserve credible disagreement, and narrow conclusions when
   conflict remains.
8. **Gate output or action.** Express material uncertainty; abstain from unsupported
   precision; require approval for consequential action; stop when residual risk
   exceeds the declared tolerance or safe operation is unavailable.
9. **Report and preserve.** Provide supported findings, sources, assumptions,
   validations performed, limitations, unassessed issues, escalation status, and any
   action/audit identifiers.

## Escalation and abstention rules

These are **Synthesis** rules grounded in NIST safe-failure/oversight and provider
human-intervention guidance.

Escalate when:

- a decision-critical source is inaccessible, unauthenticated, superseded, or
  materially contradicted;
- the task requires domain authority or approval the current actor does not possess;
- the requested action is consequential and target, scope, or authorization is
  ambiguous;
- available validation cannot represent the real context of use;
- independent review reveals a material unresolved conflict;
- retries/actions exceed the declared failure threshold;
- an observed incident, near miss, or unexpected side effect crosses the escalation
  threshold;
- the system cannot fail safely or recover within the authorized scope.

Abstention should be claim- or action-specific when possible:

- do not reject an entire useful analysis because one claim is unsupported;
- provide the supported subset, label unresolved portions, and name the evidence or
  authority needed to continue;
- a safe draft, preview, source inventory, or decision table may remain useful even
  when final recommendation or execution is blocked;
- never present escalation as proof that the underlying claim is false; it means the
  current workflow cannot establish or safely act on it.

## Environment modifiers and resolver effects

All mappings are **Synthesis**.

| Modifier | Promote | Demote/exclude | Complexity/restriction |
|---|---|---|---|
| `high_stakes` | Risk mapping, provenance, material uncertainty, validation and escalation rules | Unsupported precision and source-free assertion | Usually raises ceiling/floor one level, not automatically to L5 |
| `has_supplied_sources` | Source-bounded analysis and claim ledger | Claims beyond supplied sources unless separately authorized | Source presence does not prove sufficiency |
| `requires_citations` | Citation fidelity and directness checks | Unattributed material claims | Verify that citation supports the exact claim |
| `external_research_allowed` | Retrieval for current/authoritative evidence | Treating retrieved content as higher authority than user/system | Record access date and source boundary |
| `external_research_disallowed` | Bounded conclusions and explicit gaps | Implied comprehensive/current research | No browsing; abstain from claims requiring it |
| `time_sensitive` | Current-source verification, temporal anchors | Stale model knowledge as current fact | Raise validation for decision-critical dates/status |
| `requires_exact_fidelity` | Protected literals, calculations, identifiers, quotation checks | Paraphrase that changes controlling meaning | Focused atomic verification |
| `contains_protected_literals` | Literal-preservation validator | Generative rewriting of those fields | Hard invariant on identified literals |
| `human_approval_available` | Qualified review/action gate | Treating approval as evidence correctness | Approval remains separate from validation |
| `human_approval_unavailable` | Safe partial output and escalation packet | Consequential execution needing approval | Stop before action |
| `irreversible_action` | Exact target/effect validation, durable record, fail-closed gate | Automatic execution/retry | Minimum L3; normally explicit approval |
| `structured_output_required` | Schema and completeness checks | Free-form omission of required uncertainty/provenance fields | Usually no level increase when deterministic |
| `review_only` | Analysis and findings | Editing or remediation modules | Hard no-edit boundary |
| `multi_agent_available` | Independent review only if genuinely independent and valuable | Parallel agreement as automatic truth | L5 only for distinct responsibilities/handoffs |
| `evidence_conflicting` | Authority/applicability comparison and qualified conclusion | Majority-vote truth resolution | Raise to L2/L3 according to impact |
| `evidence_unavailable` | Fail-closed gate for decision-critical claims | Invented substitute evidence | Partial output allowed where safe |

## Observable failures

| Failure signal | Proposed normalized failure mode | Response prior |
|---|---|---|
| A precise number, date, attribution, or threshold lacks direct support. | `unsupported-precision` | Verify atomically or narrow/remove precision. |
| Citations are present but do not entail the adjacent claims. | `citation-source-mismatch` | Re-open sources and repair claim-level mapping. |
| A valid result is generalized beyond population, version, jurisdiction, or operating conditions. | `applicability-overreach` | Narrow claim and state context boundary. |
| Multiple derivative sources are counted as independent confirmation. | `correlated-evidence-inflation` | Trace provenance and collapse shared origins. |
| The system gives a confident answer because uncertainty is inconvenient to express. | `poor-uncertainty-handling` | Identify uncertainty type and decision consequence. |
| Every possible validator is loaded regardless of impact. | `over-verification` | Apply risk/novel-information test and complexity ceiling. |
| A consequential claim or action receives only a superficial self-check. | `under-verification` | Add focused direct/independent validation tied to the failure mode. |
| Conflicting evidence is silently averaged or one source is selected without authority reasoning. | `conflict-suppression` | Preserve conflict and apply explicit authority/applicability rules. |
| Human approval is treated as proof that evidence is correct. | `approval-validation-conflation` | Validate correctness separately from authorization. |
| The model refuses everything instead of returning a supported bounded result. | `over-abstention` | Return safe supported subset plus escalation path. |
| The model proceeds despite missing decision-critical evidence or authority. | `failure-to-abstain` | Block that claim/action and identify the unblock condition. |
| Evaluation success is inferred from one anecdotal or narrow benchmark result. | `evaluation-overclaim` | Bound claim to tested conditions and document limits. |
| A monitor detects failure but no owner, threshold, or response path exists. | `orphaned-alert` | Route to named actor and preserve incident state. |

## Candidate Upgradeable priors

These are **repository synthesis only**, not effectiveness claims.

| Workflow need | Primary candidates | Secondary/counterbalance candidates | Normally unnecessary |
|---|---|---|---|
| Lock consequential question, decision, and authority | `task-set-lock-in`, `authority-anchor-enforcement` | `clarification-gateway` | Heavy orchestration for a clear single claim |
| Prevent claims beyond evidence | `grounding-no-invention` | `epistemic-status-gating`, `truth-priority-hierarchy` | Citation checks when no citations/source claims are present |
| Verify decision-critical atomic facts | `critical-atomic-verification` | `citation-fidelity`, `bidirectional-consistency` | Full parallel QMS for low-impact facts with direct deterministic checks |
| Preserve source meaning and protected values | `safe-rewrite`, `zero-drift-zones` | `counterfactual-integrity`, `invariance-stress-scaffold` | Regenerative/surgical editing absent structural failure |
| Scale controls to consequence | `risk-tier-scaling` | `reasoning-scale-controller` | Maximum-depth reasoning by default |
| Resolve conflicting claims/authorities | `multi-truth-gating`, `truth-priority-hierarchy` | `domain-mode-isolation`, `fermionic-veto` where a non-compensable rule truly exists | Majority vote or branch proliferation without authority criteria |
| Add independent validation | `parallel-qms` when an independent check has distinct information | `critical-atomic-verification`, `bidirectional-consistency` | Redundant validators sharing evidence and assumptions |
| Stop unsupported claim/action safely | `fail-closed-abstention` | `clarification-gateway`, `bounded-exit` | Whole-task refusal when a supported partial answer is safe |
| Preserve audit/continuation state | `stateblock`, `state-snapshot` | `sequential-memory-state-engine` for long incidents | Durable state for a one-turn low-impact answer |
| Search credible alternatives/counterexamples | `anti-tunnel-vision` | `multiverse-reasoning` only when alternatives materially affect the decision | Open-ended branching after the decision boundary is met |

## Complexity implications

- High stakes raises validation in proportion to plausible impact and uncertainty; it
  does not automatically require multi-agent orchestration.
- L1 can be sufficient for one critical fact with an authoritative direct source and
  deterministic check.
- L2 fits a bounded evidence synthesis with explicit claims, sources, conflicts, and
  uncertainty.
- L3 fits consequential decisions or reviews requiring stronger validators, human
  review, or an escalation gate.
- L4 fits consequential actions with explicit state, approval, postconditions,
  recovery, and monitoring.
- L5 is reserved for genuinely distinct expert/operational roles, incident handoffs,
  or parallel independent evaluations. It should not be triggered by the phrase
  “high stakes” alone.

The resolver should lower the ceiling when the requested deliverable is explanatory,
the source and answer are direct, the impact is low, or a deterministic validator
settles the issue. It should raise it when material consequences combine with weak,
conflicting, time-sensitive, inaccessible, or hard-to-validate evidence.

## Resolver implications

The v0.3 resolver should:

1. represent `high_stakes` as a modifier on a primary task archetype;
2. identify the small set of decision-critical claims/actions before adding controls;
3. distinguish evidence quality from evidence quantity;
4. promote claim-level provenance and source verification when citations matter;
5. preserve `unknown`, `conflicting`, and `unavailable` states;
6. avoid generated numeric confidence unless a defined method provides it;
7. select validators by failure mode and independence, not by count;
8. separate human approval, qualified review, and correctness validation;
9. support partial abstention and actionable escalation;
10. suppress high-cost meta-controls when a direct source or deterministic check is
    sufficient.

## Source list

- NIST, [AI Risk Management Framework Core](https://airc.nist.gov/airmf-resources/airmf/5-sec-core/).
- NIST, [AI RMF Playbook](https://airc.nist.gov/airmf-resources/playbook/).
- NIST, [Artificial Intelligence Risk Management Framework: Generative Artificial Intelligence Profile (NIST AI 600-1)](https://doi.org/10.6028/NIST.AI.600-1).
- U.S. Government Accountability Office, [Artificial Intelligence: An Accountability Framework for Federal Agencies and Other Entities (GAO-21-519SP)](https://www.gao.gov/products/gao-21-519sp).
- OpenAI, [Model Spec — Express uncertainty](https://model-spec.openai.com/2025-02-12.html#express-uncertainty).
- OpenAI, [A practical guide to building agents](https://openai.com/business/guides-and-resources/a-practical-guide-to-building-ai-agents/).

