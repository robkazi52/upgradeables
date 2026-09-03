# Selection Ontology Review v0.3

**Review type:** independent research-gate audit
**Handoff:** `UPGRADEABLES_V0.3_PROJECT_HARNESS_HANDOFF_v1.1_RESEARCH_FIRST.md`
**Review date:** 2026-09-03
**Baseline:** registry v0.2.1 with 96 operational Upgradeables

## Scope and method

This review evaluates the ten synthesis-gate questions in Section 0.12 of the
authoritative v1.1 handoff. It covers all eight research notes, the synthesis
map, the task-to-Skill decision model, the five machine-readable ontology
registries, the evidence matrix, all three reviewed selection-prior shards, and
the generated JSON/CSV/Markdown task-prior audit.

The review treats task/component mappings as selection priors. It does not treat
them as activation rules or empirical proof that an Upgradeable improves a task.

Read-only checks established:

- research tracks: 8/8 present, each with external primary, official, standards,
  or research sources and explicit evidence/synthesis boundaries;
- evidence matrix: 73 populated rows across A-H, representing 61 distinct source
  URLs, with all nine required columns;
- task ontology: 15 primary archetypes, 92 subtype placements, 102 unique common
  user phrases, and 63 unique representative tasks;
- failure ontology: 36 failure modes and 108 observable signals (three per mode);
- environment ontology: 37 signals -- 14 task modifiers, 8 host capabilities,
  5 permissions, and 10 derived signals;
- complexity ontology: 6 ordered levels and bounds for all 15 archetypes;
- composition priors: 17 inherited, rule-like mappings with valid condition and
  canonical recipe/component references;
- Upgradeable task priors: 96 records, 96 unique canonical slugs, 0 missing,
  0 extra, 0 duplicates, and 0 unreviewed;
- generated parity: the JSON is identical to the three reviewed shards, and all
  96 CSV rows reproduce the JSON fields exactly.

## Gate questions

### 1. Are task archetypes mutually understandable and reasonably non-overlapping?

**Yes.** The ontology uses 15 broad primary outcomes and separates them from
domain, subtype, execution form, environment, failure signals, and complexity.
Each archetype has a plain display name, boundary-bearing description, at least
six user phrases, representative tasks, input/output patterns, and explicit
normally excluded recipes.

There are 92 subtype placements and 88 unique subtype names. The four repeated
names are intentional domain/goal intersections: `code-review`,
`architecture-design`, `plan-validation`, and `concept-selection`. The synthesis
map explicitly explains how primary outcome and domain disambiguate these cases.
They therefore represent controlled intersections rather than duplicate top-level
archetypes.

### 2. Can ordinary user requests map into them deterministically?

**Yes.** The 15 records provide 102 unique exact common phrases, 63 unique
representative tasks, 45 input-pattern descriptions, subtypes, compatible
execution forms, and candidate/excluded recipes. The synthesis specifies a
deterministic order: explicit wording and negation, one primary archetype,
optional subtype, separate project prior, hard boundaries, failure signals,
complexity, then recipe/component ranking. It also permits ambiguity and no-match
instead of forcing a category.

The four subtype intersections above require the primary archetype/domain axis,
which is already part of the declared input model. No exact common phrase or
representative-task string is duplicated across archetypes.

### 3. Are failure modes observable enough to help selection?

**Yes.** All 36 normalized failure modes include a description, three observable
signals, common task archetypes, primary and secondary canonical controls,
counterbalances, an escalation path, normally unnecessary controls, and source
references. All referenced archetypes and components resolve. The signals are
behavioral or artifact-level observations -- for example a missing source,
changed authority mode, unverified side effect, stale state, or unrelated edit --
rather than hidden-model-state claims.

The registry labels all 36 families as synthesis. That is appropriate: research
supports the recurring failure surfaces, while the normalization and control
mapping remain repository design decisions.

### 4. Do environment modifiers materially change decisions?

**Yes.** All 37 environment records define recipe-ranking effects, component
promotions/demotions/exclusions, a complexity effect, hard restrictions, and
false/unknown behavior. Thirty-three promote at least one recipe, 36 promote at
least one component, and all 37 contain a hard restriction and explicit
complexity treatment.

Material boundaries are encoded rather than implied. `review_only` excludes five
editing/state-mutation components and demotes editing recipes; `irreversible_action`
sets at least L3 and requires exact authority/target/retry handling;
`multi_agent_available` explicitly does not raise complexity by itself; and
`long_context` promotes scoped retrieval while forbidding indiscriminate corpus
ingestion. Capability, permission, and task intent are separate namespaces.

### 5. Does the complexity ceiling stop over-scaffolding?

**Yes.** `task_complexity_levels.json` defines L0-L5 in exact order, supplies
raise/lower conditions for every one of the 15 archetypes, and applies lowering
conditions before raising conditions. L0 suppresses branch search, persistent
state, agent loops, orchestration, and full QMS; L1 suppresses durable memory for
one turn, unbounded alternatives, and orchestration.

The operational composition rule `simple-exact-edit-suppression` caps a bounded
low/moderate-risk edit at L1, forces no recipe, promotes only `micro-repair`, and
hard-excludes `multiverse-reasoning`, `parallel-qms`, `meta-supervisor`,
`sequential-memory-state-engine`, and `surgery-edit`. The `no-match` rule likewise
caps at L1 and prevents a fabricated stack.

### 6. Do all 96 Upgradeables have a defensible prior map?

**Yes.** `registry/upgradeable_task_priors.json` contains each of the 96 canonical
operational slugs exactly once. Every record has all 20 required audit fields,
at least one primary and secondary archetype, at least one primary and secondary
failure mode, a canonical pipeline, environment promoters, complexity bounds,
project priors, exclusions, source support, a PASS review status, and a bounded
selection note. All archetype, failure, environment, profile, complexity,
escalation, counterbalance, recipe, and component references resolve.

Canonical identity fields -- slug, version, plain name, pipeline stages, and
source-support classification -- match `registry/registry.json`. The source
support distribution is 69 `sufficiently-recovered`, 14 `strongly-derivable`,
12 `source-gap`, and 1 `modern-operationalization`; those labels describe
mechanism provenance, not task-level effectiveness. The generated CSV has 96
rows and exact field parity with the JSON, while the Markdown summary reports
96/96, missing 0, and unreviewed 0.

### 7. Are task archetypes distinguished from project profiles?

**Yes.** The ontology defines the primary archetype as the user's requested
outcome and domain/project context as a separate prior that cannot replace or
override that goal. The 15 archetypes refer to ten likely project profiles --
`general`, `software-development`, `research`, `long-context`, `authoring`,
`data-analysis`, `medical-evidence`, `legal-evidence`, `agent-development`, and
`documentation` -- without treating any profile as permanent activation.

The synthesis also distinguishes eight content domains and explains that
`authoring` and `long-context` are useful project profiles but not content-domain
or task-identity substitutes. Explicit task wording, authority, and source
boundaries outrank profile priors throughout the composition rules.

### 8. Are task archetypes distinguished from Skills?

**Yes.** `docs/TASK_TO_SKILL_DECISION_MODEL.md` separates a current task from ten
packaging forms: one-off task, reusable prompt, project instructions, Skill,
script/hook, resource/reference, tool/MCP package, custom agent, runtime subagent,
and orchestration. It directs the harness to choose the least complex form that
adds the missing capability.

Skill suggestion has eight hard eligibility conditions, including opt-in task
history, a stable job and procedure, positive and negative activation boundaries,
known missing-input behavior, an output/completion contract, and an existing-Skill
check. Recurrence starts evaluation; it does not auto-create a Skill, and a Skill
does not grant tools, memory, or action authority.

### 9. Are empirical/support claims properly separated from design inference?

**Yes.** Every research note defines evidence and synthesis labels and warns that
benchmark inclusion does not establish task prevalence or Upgradeable efficacy.
The 73-row evidence matrix records source type, access date, domain, bounded
claim/pattern, proposed ontology support, and notes limiting generalization.
Sources span benchmarks and papers, provider/platform documentation, open
specifications and protocols, an Internet standard, and government frameworks.

The synthesis map, task-to-Skill model, five registries, composition rules, and
96-component prior file each repeat the selection-prior boundary. Failure-family,
threshold, taxonomy, and component-selection decisions are labeled synthesis.
Canonical mechanism provenance is preserved separately, including 12 explicit
source gaps, rather than being converted into an efficacy claim.

### 10. Are high-cost/meta Upgradeables naturally suppressed on simple work?

**Yes.** The canonical registry identifies 22 high-cost Upgradeables. In the
reviewed prior map, none has an L0 minimum, 21/22 require at least L2, and 19/22
require at least L3. The sole L1 exception is
`critical-atomic-verification`, whose scope is a bounded decision-critical atom
rather than general meta-orchestration. `ultimate-suite-supervisor` is L5-L5,
`meta-supervisor` is L4-L5, and broad alternatives/QMS are L3 or higher.

The base composition rule demotes expensive branching, QMS, supervision, durable
state, and external automation absent positive evidence. The simple-edit and
no-match rules hard-exclude the major heavy controls, while orchestration requires
independent branches, an explicit synthesis need, and actual multi-agent
capability. Tightly shared state or a simple exact edit activates the separate
orchestration-suppression rule.

## Gate result

All ten gate questions are satisfied by the current research and machine-readable
ontology. The layer is suitable to compile into a deterministic harness while
retaining task-time trigger/non-trigger evaluation and minimum-composition rules.

RESEARCH_GATE = PASS

## Completion checkpoint

```text
Research tracks completed: 8/8
Sources reviewed: 73 evidence rows / 61 distinct source URLs
Task archetypes: 15
Failure modes: 36
Environment modifiers/capabilities/permissions/derived signals: 37
Complexity levels: 6
Composition-prior rules: 17
Operational Upgradeables reviewed: 96/96
Missing Upgradeable mappings: 0
Unreviewed Upgradeables: 0
Selection ontology review: PASS
```
