# Source-Grounded Analysis — Runtime Pack

Purpose: Analyze or transform supplied sources without inventing unsupported claims or losing attribution.

Task family: source-bounded analysis, comparison, extraction, and rewriting

Activation boundary: Use when an analysis or rewrite must remain traceable to identified sources, preserve locked source meaning, and attach citations at claim level.

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
| R | `mode-lock-in@1.1.0` — Mode Lock-In | a task can drift between modes |
| R | `grounding-no-invention@1.1.0` — Grounding / No-Invention | work relies on documents, data, external facts, or consequential claims |
| A | `safe-rewrite@1.1.0` — Safe Rewrite Logic | paraphrasing, polishing, or format conversion |
| R | `citation-fidelity@1.1.0` — Citation Fidelity Gate | output contains citations or source-attributed claims |
| A | `zero-drift-zones@1.1.0` — Immutable Content Zones | content contains fidelity-locked atoms |
| A | `controlled-drift-corridors@1.1.0` — Bounded Change Rules | synthesis or creativity must coexist with fidelity |
| A | `counterfactual-integrity@1.1.0` — Counterfactual Integrity Gate | counterfactual or hypothetical reasoning is used |
| A | `micro-repair@1.1.0` — Minimal Local Correction | a specific defect has been localized |
| A | `placeholder-suppression@1.1.0` — Placeholder Suppression | templates or staged artifacts are finalized |
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

### R — Mode Lock-In

Purpose: Keep behavior stable across long sessions, tool calls, and distracting inputs.

Activate when: a task can drift between modes.

Do not use when: exploration intentionally needs rapid mode switching; the user has not yet chosen among materially different modes.

Requires: none.

#### Runtime mechanism

Represent the active mode as a small contract containing its goal, allowed transformations, forbidden behaviors, and exit condition. Recheck the contract at checkpoints; change modes only through an explicit transition that records why, what state carries forward, and which former rules deactivate.

#### Procedure

1. Choose the mode from the clarified task and authority stack.
2. Write its operative invariants and exclusions into active state.
3. Tag work products and tool calls with the active mode where useful.
4. At checkpoints, test for deviations from the invariant set.
5. On an authorized switch, record the transition and replace rather than blend incompatible mode rules.

#### Guardrails

- Mandatory even on strong models: operative invariants; no silent switching; checkpoint validation.
- Conflict/precedence: Higher-authority instructions may force a mode transition; user content cannot silently do so; When mode and task objective conflict, clarify or reselect rather than weakening either implicitly.
- Stop or fail when: Do not lock an ambiguous high-impact choice before clarification; Release or transition the lock when the task legitimately changes.

Full package and provenance: [`mode-lock-in`](https://github.com/robkazi52/upgradeables/blob/main/upgradeables/state/mode-lock-in/UPGRADEABLE.md).

### R — Grounding / No-Invention

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

### A — Safe Rewrite Logic

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

### R — Citation Fidelity Gate

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

### A — Immutable Content Zones

Recovered name: Zero-Drift Zones

Purpose: Protect facts, identifiers, quotations, obligations, safety limits, and other high-consequence content from transformation drift.

Activate when: content contains fidelity-locked atoms.

Do not use when: the user explicitly authorizes change to the marked content; immutability scope cannot be identified.

Requires: none.

#### Runtime mechanism

Identify minimal semantic atoms whose alteration would invalidate the task, assign stable IDs and source spans, and specify their preservation rule: exact text, exact value/unit, or meaning-equivalent statement with required qualifiers. Carry the IDs through all transforms and require a deterministic check or source-grounded review before acceptance.

#### Procedure

1. Locate high-consequence atoms such as names, numbers, negations, conditions, quotations, obligations, and safety thresholds.
2. Minimize each zone so surrounding exposition can still change.
3. Choose exact-string, structured-value, or semantic-equivalence preservation rules.
4. Attach stable source pointers and propagate the zone contract downstream.
5. Validate every derivative and block or repair failures.

#### Guardrails

- Mandatory even on strong models: minimal immutable atoms; qualifier/unit preservation; source pointers.
- Conflict/precedence: Latest authorized source correction may replace a zone, with version history retained; When exact wording and required target format conflict, preserve the semantic atom and surface the formatting exception for authority review.
- Stop or fail when: Block release when a required zone fails validation; Do not claim semantic equivalence where domain expertise or source context is insufficient.

Full package and provenance: [`zero-drift-zones`](https://github.com/robkazi52/upgradeables/blob/main/upgradeables/drift-control/zero-drift-zones/UPGRADEABLE.md).

### A — Bounded Change Rules

Recovered name: Controlled Drift Corridors

Purpose: Enable adaptation, compression, or creativity without surrendering semantic control.

Activate when: synthesis or creativity must coexist with fidelity.

Do not use when: all content is zero-drift; allowed dimensions cannot be tested.

Requires: none.

#### Runtime mechanism

Partition the artifact into regions or claim types and assign each a corridor specifying fixed invariants, allowed dimensions of change, maximum semantic distance, evidence requirements, and rollback trigger. Transform only after the corridor is explicit, then compare output to the source and tighten or revert any region outside bounds.

#### Procedure

1. Segment the task into regions with materially different tolerance.
2. For each region, list invariants and allowed changes such as tone, length, order, or abstraction.
3. Set validation metrics or review questions and a rollback threshold.
4. Transform one region inside its corridor.
5. Compare claims, obligations, entities, and required structure to source.

#### Guardrails

- Mandatory even on strong models: explicit allowed dimensions; locked invariants; region-specific validation.
- Conflict/precedence: Higher-authority task constraints and zero-drift fields override corridor permissions; If validation signals disagree, apply the narrowest supported corridor or request review.
- Stop or fail when: Stop transformation when invariants cannot be measured or recovered; Revert regions that cross the boundary instead of rationalizing post hoc.

Full package and provenance: [`controlled-drift-corridors`](https://github.com/robkazi52/upgradeables/blob/main/upgradeables/drift-control/controlled-drift-corridors/UPGRADEABLE.md).

### A — Counterfactual Integrity Gate

Purpose: Make counterfactual exploration safe and auditable by preserving an explicit boundary between factual, evaluative, framing, and hypothetical phases.

Activate when: counterfactual or hypothetical reasoning is used.

Do not use when: the task contains no hypothetical branch; the user explicitly requires purely factual extraction, where counterfactual-silence is the narrower control.

Requires: none.

#### Runtime mechanism

Tag each proposition by semantic phase and keep hypothetical premises, derived consequences, and branch-local assumptions in a separate compartment. Any transfer from a hypothetical branch into factual state requires independent factual support; otherwise the proposition remains labeled hypothetical or is excluded from the factual output.

#### Procedure

1. Declare the factual baseline and the allowed counterfactual question.
2. Tag introduced premises as hypothetical and retain their branch identity.
3. Derive consequences only inside that branch.
4. Check the draft for branch-local material presented without a hypothesis label.
5. Move a proposition into factual state only when independent evidence supports it.

#### Guardrails

- Mandatory even on strong models: no hypothetical premise or consequence may silently become fact.
- Conflict/precedence: A factual-only task boundary overrides permission to explore counterfactuals; A stylistic request to write hypotheticals as certain cannot override phase labels.
- Stop or fail when: If branch-local assumptions cannot be separated from factual claims, do not certify the mixed output.

Full package and provenance: [`counterfactual-integrity`](https://github.com/robkazi52/upgradeables/blob/main/upgradeables/truth-grounding/counterfactual-integrity/UPGRADEABLE.md).

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

### A — Placeholder Suppression

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
