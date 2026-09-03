# Authoring — Runtime Pack

Purpose: Draft or rewrite a controlled deliverable for a defined message, audience, style, and source boundary.

Task family: controlled drafting, rewriting, and publication preparation

Activation boundary: Use when drafting or rewriting a controlled deliverable with an explicit message, audience, style, source, or placeholder contract.

Use this generated pack for execution. Do not also load the source recipe,
resolved recipe, catalog record, or full packages unless a material ambiguity
requires deeper inspection.

`R` owns a required guarantee but may remain dormant until its pipeline phase.
`A`, `C`, and `O` still require active triggers. `X` remains excluded without
a task-specific reason.

## Composition

Frame and lock the task, establish explicit state, load evidence and behavior
components, perform the task, then run applicable validators. Increase depth
with risk; remove scaffolding that has no active trigger.

## Output contract

Return the requested artifact, evidence, limitations, and unresolved inputs.

## Component routing

| Role | Component | Activate when |
|:---:|---|---|
| R | `task-set-lock-in@1.1.0` — Task-Set Lock-In | multi-step work begins or scope changes |
| C | `grounding-no-invention@1.1.0` — Grounding / No-Invention | work relies on documents, data, external facts, or consequential claims |
| A | `style-alignment@1.1.0` — Style-Alignment Module | a style or voice is specified |
| C | `pedagogical-alignment@1.1.0` — Pedagogical Alignment Constraint | an audience or teaching level is known |
| R | `safe-rewrite@1.1.0` — Safe Rewrite Logic | paraphrasing, polishing, or format conversion |
| C | `citation-fidelity@1.1.0` — Citation Fidelity Gate | output contains citations or source-attributed claims |
| R | `placeholder-suppression@1.1.0` — Placeholder Suppression | templates or staged artifacts are finalized |
| A | `micro-repair@1.1.0` — Minimal Local Correction | a specific defect has been localized |
| A | `parallel-qms@1.1.0` — Parallel Validation System | a composed workflow needs structured quality evaluation |

## Runtime component cards

### R — Task-Set Lock-In

Purpose: Prevent scope substitution and goal drift during execution.

Activate when: multi-step work begins or scope changes.

Do not use when: the task is still materially ambiguous; open-ended ideation intentionally has no fixed deliverable.

Requires: none.

#### Runtime mechanism

Convert the clarified request into a compact task-set contract: primary objective, required outputs, quality gates, constraints, non-goals, dependencies, and change authority. Check each planned action and final artifact against it; update only through an explicit, versioned scope-change decision.

#### Procedure

1. Extract the objective, required artifacts, constraints, success tests, and exclusions.
2. Resolve material ambiguity before locking.
3. Record the task set as locked fields with a version and change authority.
4. Gate planned actions and newly proposed work against the set.
5. For legitimate changes, record the requester, rationale, and new version.

#### Guardrails

- Mandatory even on strong models: objective; required deliverables; constraints and non-goals.
- Conflict/precedence: System and latest explicit authorized user scope changes override older task-set versions; When a new request conflicts with locked acceptance criteria, pause for a scope-change decision.
- Stop or fail when: Do not claim completion when a required artifact or quality gate lacks evidence; Unlock and clarify when task identity changes materially.

Full package and provenance: [`task-set-lock-in`](https://github.com/robkazi52/upgradeables/blob/main/upgradeables/state/task-set-lock-in/UPGRADEABLE.md).

### C — Grounding / No-Invention

Purpose: Prevent fabricated facts, citations, measurements, policies, records, and gap-filling in source-grounded work.

Activate when: work relies on documents, data, external facts, or consequential claims.

Do not use when: pure creative generation has no asserted factual source boundary; the task explicitly asks for labeled brainstorming rather than factual claims.

Requires: none.

#### Runtime mechanism

Maintain a boundary between source-supported atoms and model-generated interpretation. Each material factual claim must resolve to supplied data or verified external evidence; missing fields remain missing, and permissible inference is labeled instead of being written back as source fact.

#### Procedure

1. Declare the allowed evidence boundary.
2. Extract material source-supported facts without filling absent fields.
3. Separate facts from interpretations and hypotheses.
4. For each candidate factual claim, locate supporting evidence inside the boundary.
5. Label, narrow, omit, or fail closed on unsupported claims.

#### Guardrails

- Mandatory even on strong models: every asserted material fact must remain within the authorized evidence boundary.
- Conflict/precedence: Verified evidence outranks fluent completion and stylistic requests; An explicit hypothetical mode may generate possibilities, but they remain outside factual state.
- Stop or fail when: When an essential material claim lacks support inside the authorized evidence boundary, omit it or fail closed.

Full package and provenance: [`grounding-no-invention`](https://github.com/robkazi52/upgradeables/blob/main/upgradeables/truth-grounding/grounding-no-invention/UPGRADEABLE.md).

### A — Style-Alignment Module

Purpose: Make artifacts consistent with audience, publication, or organizational style while keeping truth and requirements dominant.

Activate when: a style or voice is specified.

Do not use when: the requested style impersonates a living person or conflicts with policy; exact quoted language must remain untouched.

Requires: none.

#### Runtime mechanism

Translate the authorized style request into an observable style vector—tone, formality, sentence rhythm, vocabulary level, structure, formatting, and disallowed tendencies—while extracting a separate semantic invariant ledger. Transform surface choices toward the style vector, protect quoted and zero-drift zones, then score both conformance and semantic preservation; truth, task, and citation constraints veto any stylistic gain.

#### Procedure

1. Extract the authorized style source and convert it into observable positive and negative constraints.
2. Lock facts, reasoning relations, requirements, citations, uncertainty, and exact-text zones.
3. Revise diction, rhythm, organization, and formatting only where the style contract permits.
4. Compare the result against the style vector using representative passages rather than vague resemblance.
5. Run a semantic and citation diff; revert any stylistic change that alters truth, logic, or attribution.

#### Guardrails

- Mandatory even on strong models: explicit target dimensions; truth and task veto; semantic and citation back-check.
- Conflict/precedence: Truth, safety, citation fidelity, and explicit task constraints outrank the style guide; Exact quotations and legally controlled text are excluded from stylistic transformation.
- Stop or fail when: fact drift for tone; vague imitation.

Full package and provenance: [`style-alignment`](https://github.com/robkazi52/upgradeables/blob/main/upgradeables/output/style-alignment/UPGRADEABLE.md).

### C — Pedagogical Alignment Constraint

Purpose: Make correct content learnable and usable for a specified audience without diluting claims or inventing simplifications.

Activate when: an audience or teaching level is known.

Do not use when: the audience and purpose cannot be inferred and the choice materially changes content; exact legal or technical wording must remain verbatim.

Requires: none.

#### Runtime mechanism

Build a compact audience model—known prerequisites, target capability, jargon tolerance, and action context—then choose the smallest conceptual steps that bridge from that model to the target. Define or replace jargon at first use, order prerequisite before dependent ideas, add an example only where it resolves a likely misconception, and run an accuracy-backcheck against the unsimplified claim.

#### Procedure

1. Identify the reader's likely starting knowledge and the capability they need after reading.
2. List prerequisites and terms that the explanation currently assumes.
3. Sequence content from familiar anchor through the minimum conceptual bridge to the target.
4. Define necessary jargon or replace it with accurate plain language; add a representative example where abstraction alone is likely to fail.
5. Back-check every simplification, analogy, and example against the original technical claim and retain important limitations.

#### Guardrails

- Mandatory even on strong models: internal prerequisite model; accuracy back-check; boundary-preserving simplification.
- Conflict/precedence: Accuracy, scope, and uncertainty outrank ease of explanation; Exact source language is preserved in quoted or zero-drift zones and explained around rather than rewritten.
- Stop or fail when: oversimplification; undefined jargon.

Full package and provenance: [`pedagogical-alignment`](https://github.com/robkazi52/upgradeables/blob/main/upgradeables/output/pedagogical-alignment/UPGRADEABLE.md).

### R — Safe Rewrite Logic

Purpose: Make paraphrase, polish, tone, or formatting safe by treating content atoms as invariants rather than suggestions.

Activate when: paraphrasing, polishing, or format conversion.

Do not use when: the user asks to change substantive meaning; the source is internally contradictory and needs adjudication.

Requires: none.

#### Runtime mechanism

Extract a before-state ledger of factual and constraint atoms, mark the dimensions authorized to change, perform the rewrite only along those dimensions, then compare names, numbers, dates, quotes, citations, modality, requirements, and causal claims. Any atom difference not explicitly authorized is reverted or surfaced for approval.

#### Procedure

1. Identify authorized change dimensions such as tone, length, format, or reading level.
2. Extract locked atoms: claims, entities, numbers, dates, quotations, citations, requirements, negations, and uncertainty markers.
3. Rewrite without adding evidence or changing the locked atoms.
4. Diff the rewritten artifact against the atom ledger and inspect citation-to-claim fit.
5. Restore unauthorized changes and report any requested transformation that cannot preserve meaning.

#### Guardrails

- Mandatory even on strong models: internal atom extraction; authorized-dimension discipline; post-rewrite names/numbers/dates/quotes/citations check.
- Conflict/precedence: Truth and locked constraints outrank requested style; If shortening would remove a required qualification, keep the qualification or report the conflict.
- Stop or fail when: semantic drift; citation drift.

Full package and provenance: [`safe-rewrite`](https://github.com/robkazi52/upgradeables/blob/main/upgradeables/editing-repair/safe-rewrite/UPGRADEABLE.md).

### C — Citation Fidelity Gate

Purpose: Ensure citations prove the precise nearby claim instead of functioning as decorative evidence.

Activate when: output contains citations or source-attributed claims.

Do not use when: the output contains no externally attributed factual claims; the task explicitly requests unsupported fiction.

Requires: none.

#### Runtime mechanism

For every citation-bearing claim, open the exact cited artifact and pass five independent tests: the artifact exists and is the represented edition; the cited passage entails the full claim including qualifiers; quoted text matches exactly; paraphrase retains scope, modality, polarity, and attribution; and evidence belongs to this claim rather than being borrowed from an adjacent citation, nearby sentence, or different source. A failure at any layer blocks the claim, even if the source is authoritative.

#### Procedure

1. Atomize each externally checkable claim and bind each citation to a specific atom.
2. Resolve the cited artifact, version, locator, and authorship.
3. Inspect the cited passage rather than relying on search snippets or secondary descriptions.
4. Test entailment of subject, predicate, scope, date, quantity, and modal strength.
5. For quotes, compare exact words and mark every omission or alteration.

#### Guardrails

- Mandatory even on strong models: direct passage inspection; claim-level entailment; quote exactness.
- Conflict/precedence: The source passage outranks a draft's intended meaning; A precise unsupported subclaim must be removed even when the broader sentence is supported.
- Stop or fail when: Block any material claim whose cited artifact cannot be opened, whose passage does not entail it, or whose quote/paraphrase changes meaning.

Full package and provenance: [`citation-fidelity`](https://github.com/robkazi52/upgradeables/blob/main/upgradeables/validation/citation-fidelity/UPGRADEABLE.md).

### R — Placeholder Suppression

Purpose: Prevent scaffolding artifacts from escaping as if they were complete content.

Activate when: templates or staged artifacts are finalized.

Do not use when: the deliverable is explicitly a template whose placeholders are the product; an example intentionally teaches placeholder syntax.

Requires: none.

#### Runtime mechanism

Run a two-layer completion scan: a lexical detector for markers such as TODO, TBD, FIXME, bracket prompts, dummy domains, sample IDs, and unresolved interpolation syntax; then a schema detector for empty required sections, null required fields, and uninstantiated variables. Classify every hit using a narrow allowlist for intentional template, example, or redaction contexts; all other hits must be filled from authority, removed with requirement revalidation, or explicitly labeled unresolved before release.

#### Procedure

1. Load the artifact's required sections, fields, and variable schema.
2. Scan text and code for known marker tokens, dummy values, bracketed instructions, and unresolved interpolation forms.
3. Scan structure for empty or default-valued required elements.
4. Classify hits as accidental, intentionally illustrative, approved redaction, or genuinely unresolved using context and an explicit allowlist.
5. Resolve accidental hits from authoritative inputs, omit only when the requirement permits, and label genuine gaps with impact and owner.

#### Guardrails

- Mandatory even on strong models: lexical plus schema scan; context-specific classification; post-fix rescan.
- Conflict/precedence: Never fabricate content to satisfy completion; Approved template and example placeholders remain only when clearly scoped and non-executable.
- Stop or fail when: false completion; fabricated replacements.

Full package and provenance: [`placeholder-suppression`](https://github.com/robkazi52/upgradeables/blob/main/upgradeables/output/placeholder-suppression/UPGRADEABLE.md).

### A — Minimal Local Correction

Recovered name: Micro-Repair

Purpose: Restore local correctness or completeness with the minimum semantic blast radius.

Activate when: a specific defect has been localized.

Do not use when: the artifact architecture is globally wrong; the same defect repeats systemically.

Requires: none.

#### Runtime mechanism

Define a repair window around the smallest unit that fails an explicit criterion, freeze the surrounding accepted region, patch only that unit and any directly required connective token, then compare the window before and after. Widen once only when a direct dependency proves the first window insufficient; recurring or architecture-level failure escalates instead of allowing scope creep.

#### Procedure

1. Identify the exact failed criterion and the smallest text, field, rule, or code unit causing it.
2. Mark the surrounding accepted content and locked facts as frozen.
3. Draft the smallest replacement that satisfies the criterion.
4. Check boundary coherence with the immediately preceding and following units.
5. Verify the target defect is gone and no frozen atom changed.

#### Guardrails

- Mandatory even on strong models: smallest-fault localization; changed-atom comparison; systemic-failure escalation.
- Conflict/precedence: Do not preserve a frozen neighbor if it is proven part of the defect; explicitly widen the window instead; A locked invariant outranks local fluency.
- Stop or fail when: scope creep; cosmetic rewriting around a defect.

Full package and provenance: [`micro-repair`](https://github.com/robkazi52/upgradeables/blob/main/upgradeables/editing-repair/micro-repair/UPGRADEABLE.md).

### A — Parallel Validation System

Recovered name: Parallel Quality Management System

Purpose: Match validation topology to failure risk instead of treating QMS as one generic critic or a majority vote.

Activate when: a composed workflow needs structured quality evaluation.

Do not use when: one low-risk deterministic check is sufficient; the caller cannot define a decision criterion or bounded exit.

Requires: none.

#### Runtime mechanism

Select modes by distinct failure hypotheses, run them with separated evidence where independence matters, preserve typed outputs, and collapse only after resolving material disagreement and honoring vetoes. Mirror QMS compares two independently derived answers; Risk-Tier-Split allocates shallow, medium, or deep checks by consequence; Cross-Phase separately inspects factual, evaluative, framing, and hypothetical phases; Redundancy QMS seeks logical, structural, narrative, and safety corroboration; ExIt-Integrated couples scores to bounded repair and convergence; Hierarchical validates atom, paragraph/component, section/subsystem, and global levels; Transversal cuts across temporal, causal, modal, and logical dimensions; Heterogeneous assigns coherence, evidence, relevance, and safety to different validator lenses; Monte QMS perturbs assumptions, wording, or structure without claiming…

#### Procedure

1. State the decision, critical truths, risk tier, and stop conditions.
2. Choose only modes tied to plausible distinct failures: QMS-M for independent-answer agreement; QMS-RTS for consequence-scaled depth; QMS-XP for factual/evaluative/framing/hypothetical separation; QMS-R for logical/structural/narrative/safety redundancy; QMS-EI for bounded repair convergence; HQMS for atom-to-global hierarchy; T-QMS for temporal/causal/modal/logical cuts; hQMS for…
3. Define inputs, independence boundaries, and typed pass/fail output for each selected mode.
4. Run independent modes without sharing draft conclusions when contamination would defeat the purpose.
5. Collect disagreements without averaging them away.

#### Guardrails

- Mandatory even on strong models: mode distinction; critical-truth agreement; conflict preservation.
- Conflict/precedence: Crucial factual conflict must be resolved or surfaced before collapse; Safety and ethical vetoes cannot be outvoted.
- Stop or fail when: Do not certify while a crucial truth is disputed, a safety/ethical veto is active, validator independence is falsely claimed, or bounded repair fails to converge.

Full package and provenance: [`parallel-qms`](https://github.com/robkazi52/upgradeables/blob/main/upgradeables/validation/parallel-qms/UPGRADEABLE.md).
