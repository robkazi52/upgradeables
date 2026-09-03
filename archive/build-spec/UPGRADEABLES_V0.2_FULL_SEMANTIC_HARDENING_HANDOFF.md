# Upgradeables v0.2 — Full Semantic Hardening, Behavioral Evals, and Release Handoff

**Handoff version:** 1.0  
**Target project:** `robkazi52/upgradeables`  
**Baseline release:** `v0.1.0`  
**Target release:** `v0.2.0`  
**Execution environment:** Windows PowerShell + local Git clone + Codex/Fable + GitHub CLI when available

---

# 0. EXECUTION DIRECTIVE

You are the implementation agent.

This is **not** a request to review a subset of Upgradeables.

Audit, deepen, correct, and validate **EVERY operational Upgradeable package that exists at the start of this work**.

The v0.1.0 release reported 96 operational Upgradeable packages. Verify the actual count on the current branch before editing. The authoritative requirement is:

> **100% of the baseline operational packages must be individually reviewed.**

Do not stop after improving the top 20–30.
Do not sample.
Do not leave the remainder with generic boilerplate.
Do not report completion while any baseline operational package is still marked `unreviewed`, `generic`, `needs-source-review`, or equivalent.

This is a repository-wide semantic-hardening release.

The project already has strong architecture, provenance, registry generation, recipes, CI, source preservation, and contribution mechanics. The main v0.2 objective is to make the **content of every Upgradeable as strong and distinctive as the architecture around it**.

---

# 1. BASELINE REPOSITORY

Expected remote:

```text
https://github.com/robkazi52/upgradeables
```

Before changing anything:

```powershell
git status
git remote -v
git branch --show-current
git fetch --all --tags
git log -5 --oneline
```

Confirm that `origin` points to the expected repository.

If unrelated local changes exist, preserve them. Do not overwrite them.

Create a working branch:

```powershell
git switch main
git pull --ff-only
git switch -c v0.2-semantic-hardening
```

If the branch already exists, inspect it before reusing it.

---

# 2. REQUIRED SOURCE CORPUS

The repository should already preserve these source documents under `archive/source/`:

1. `OS_Upgradeable_to_Skills_Translation_Catalog_v2_Recovery_Merged.md`
2. `OS_Upgradeables_Historical_Recovery_Inventory.md`
3. `OS_Upgradeables_Deep_Context_Recovery_Addendum_2026-09-03.md`

Read all three before performing mass semantic rewrites.

They are the source basis for recovered purpose, historical identity, aliases, architecture, interactions, task use, recovery confidence, and known gaps.

Do not modify the archived source corpus except to repair a demonstrable file-corruption problem. It is archival evidence.

---

# 3. SOURCE / PROVENANCE AUTHORITY

For historical claims use this order:

1. Direct recovered user-authored specification.
2. Explicit user acceptance / frozen artifact.
3. Historical Recovery Inventory.
4. Current Translation Catalog.
5. Historical assistant-generated artifact.
6. Modern implementation recommendation.

When a modern implementation is inferred from a recovered purpose, label it as such.

Do not convert an inference into a historical fact.

Do not invent:

- unrecovered names;
- acronym expansions;
- historical dates;
- hidden model mechanisms;
- original procedures that were never recovered;
- private chain-of-thought access;
- persistence or parallelism unsupported by the host.

If the source is insufficient for a fully historical procedure, write:

```text
Modern operational interpretation
```

or an equivalent explicit label.

---

# 4. PRIMARY V0.2 PROBLEM TO FIX

The v0.1.0 repository successfully generated operational packages, but some package bodies contain semantic boilerplate that can describe many unrelated Upgradeables.

Examples of language that MUST trigger review include:

```text
Prevents the workflow failure implied by the trigger...
```

```text
Apply the named behavior as an explicit, bounded control...
```

```text
the declared trigger is absent or the control would add no material value
```

```text
bounded component result
```

```text
Select and sequence only available components...
```

when the Upgradeable is not actually a loader/orchestrator.

The issue is not merely repeated wording.

The issue is that a generic template can erase the **distinctive mechanism** of the Upgradeable.

Example:

`Multiverse Engine` should actually describe:

```text
Generate bounded materially distinct candidate paths
→ prevent premature convergence
→ evaluate candidates against locked criteria
→ select/synthesize
→ retire losing branches from active state
```

It should not primarily describe a generic component router.

Similarly, `Micro-Scaffolding` should describe how minimal temporary task-local scaffolds are created and retired, not merely say "apply the named behavior."

---

# 5. ABSOLUTE COMPLETENESS REQUIREMENT

Create:

```text
audit/OPERATIONAL_PACKAGE_REVIEW_v0.2.csv
```

and:

```text
audit/OPERATIONAL_PACKAGE_REVIEW_v0.2.md
```

The audit must contain one row for **every baseline operational Upgradeable package**.

Required columns:

```text
slug
id
display_name
baseline_version
new_version
functional_class
source_support
source_refs
summary_review
purpose_review
problem_review
mechanism_review
procedure_review
trigger_review
os_fit_review
task_mapping_review
interaction_review
example_review
test_review
metadata_review
provenance_review
semantic_specificity
final_status
notes
```

Allowed final statuses:

```text
PASS
BLOCKED_BY_SOURCE_GAP
```

`BLOCKED_BY_SOURCE_GAP` is not permission to leave generic invented content. It means the package was fully reviewed but source limitations prevent claiming a recovered mechanism. In that case the package must explicitly distinguish known historical content from modern interpretation.

Acceptance condition:

```text
baseline_package_count
==
PASS + BLOCKED_BY_SOURCE_GAP
```

and:

```text
unreviewed == 0
```

A source-gap package may remain operational only when a defensible modern mechanism can be explicitly labeled as an interpretation. Otherwise consider lifecycle downgrade or historical-only disposition.

Do not hide this decision.

---

# 6. PACKAGE-BY-PACKAGE SOURCE RECOVERY PROCEDURE

For EVERY operational package:

## Step 1 — Identify the package

Read:

```text
metadata.yaml
UPGRADEABLE.md
examples/*
tests/*
```

Record:

- canonical ID;
- slug;
- aliases;
- historical IDs;
- registry generation;
- provenance source;
- source kind;
- recovery confidence.

## Step 2 — Search all three source files

Search using:

- exact ID;
- canonical display name;
- historical aliases;
- acronym;
- related family heading;
- known neighboring modules;
- old registry generation.

Do not rely only on the current package text.

## Step 3 — Build a source note

For each package create a temporary or retained structured note containing:

```text
Recovered facts
Recovered purpose
Recovered mechanism
Recovered trigger/use cases
Recovered interactions
Recovered failure boundaries
Recovered OS placement
Recovered examples
Recovered variants
Unresolved details
Modern interpretation needed?
```

Prefer retaining this under:

```text
audit/source-notes/<slug>.md
```

This makes the semantic rewrite auditable.

## Step 4 — Rewrite only from support

Use recovered content when available.

Where support is sparse:

- keep recovered facts exact;
- clearly label modern implementation guidance;
- do not fabricate historical detail merely to make the file look complete.

## Step 5 — Cross-check package vs metadata

The Markdown and machine-readable metadata must describe the same mechanism.

---

# 7. REQUIRED SECTIONS FOR EVERY OPERATIONAL `UPGRADEABLE.md`

Every operational package must have meaningful, concept-specific content for:

```text
# <Name>

## Summary
## Purpose
## Problem Solved
## Where It Fits in the OS
## Best-Fit Activities / Tasks
## When Not to Use
## Scope
## Trigger Conditions
## Non-Triggers
## Inputs / Required State
## Outputs / Produced State
## Mechanism
## Procedure
## Always-Do Rules
## Never-Do / Avoid Rules
## Interaction Rules
## Compatible Upgradeables
## Counterbalancing Upgradeables
## Potential Redundancy
## Conflict / Precedence Rules
## Failure Boundary
## Strong-Model Scaling
## Recommended Skill Types
## Example Composition
## Tests
## Provenance / Historical Aliases
```

If a section is genuinely not applicable, say why.

Do not fill a section with generic text simply because the template requires it.

---

# 8. NEW CORE REQUIREMENT: “WHERE DOES THIS FIT?”

The original public-use goal is not merely to define Upgradeables.

A fresh frontier model should be able to answer:

> What kinds of tasks should use this Upgradeable?

and:

> Where in an OS/Skill workflow does this Upgradeable belong?

Therefore every operational package must explicitly answer both.

## 8.1 `Where It Fits in the OS`

Describe actual placement.

Examples of placement concepts:

```text
intake / framing
pre-retrieval
retrieval
evidence capture
state update
planning
candidate generation
execution
mid-process checkpoint
validation
repair
pre-output verification
output shaping
persistence
supervision / meta-control
```

An Upgradeable may occupy more than one stage.

Explain whether it acts:

- before;
- during;
- after;

the primary task.

## 8.2 `Best-Fit Activities / Tasks`

Give concrete task families.

Examples:

```text
source-grounded research
long-context analysis
high-stakes evidence synthesis
creative ideation
software debugging
architecture design
editing
decision support
routing
stateful agent workflows
citation-bearing authoring
policy analysis
document fidelity
multi-step planning
```

Do not blindly assign every Upgradeable to `general-agent-workflow`.

## 8.3 `When Not to Use`

Explain the cost or failure mode of unnecessary activation.

Examples:

- adds needless overhead;
- suppresses useful exploration;
- causes overvalidation;
- duplicates another active component;
- requires source evidence that the task does not use;
- only matters when state persists;
- inappropriate for zero-source creative work.

This section should help a model *exclude* Upgradeables.

---

# 9. MACHINE-READABLE OS-FIT METADATA

Extend `metadata.yaml` and schema so every operational package can expose its placement and task recommendations programmatically.

Add fields equivalent to:

```yaml
os_role:
  - validation

pipeline_stages:
  - post-synthesis
  - pre-output

best_fit_tasks:
  - source-grounded research
  - citation-bearing authoring

avoid_when:
  - no citations or source-attributed claims are emitted

mechanism_basis: recovered
```

Allowed `mechanism_basis` values should include at least:

```text
recovered
normalized-from-recovered
modern-interpretation
provisional
```

Optional but recommended:

```yaml
activation_cost:
  level: low | medium | high
  notes: ""
```

Do not present cost as a measured compute benchmark unless actually measured. It is an architectural burden classification.

Update:

- JSON schema;
- validation scripts;
- registry build;
- registry JSON/YAML;
- all-in-one generation;
- docs.

Bump schema/version numbers appropriately.

---

# 10. SEMANTIC SPECIFICITY STANDARD

Every package must pass a new semantic-specificity review.

A package is **not** semantically specific merely because the name appears several times.

A good package should answer:

1. What exact failure does this prevent or capability does it add?
2. What actually happens when it activates?
3. What inputs/state does it operate on?
4. What changes or status does it produce?
5. Where does it sit in a workflow?
6. What task types benefit?
7. When would it be harmful or wasteful?
8. What other Upgradeables naturally pair with it?
9. What component counterbalances it?
10. What failure causes it to stop, veto, abstain, or escalate?
11. What may a stronger model safely omit?
12. What invariant remains mandatory?

Generic restatement of the name is insufficient.

---

# 11. ADD A SEMANTIC AUDITOR

Create:

```text
scripts/audit_semantic_specificity.py
```

Use only standard-library dependencies unless there is a compelling reason otherwise.

The auditor should scan all operational packages and fail CI for obvious regression patterns.

At minimum detect:

## 11.1 Forbidden / suspicious generic boilerplate

Flag phrases such as:

```text
Prevents the workflow failure implied by the trigger
Apply the named behavior as an explicit, bounded control
the declared trigger is absent or the control would add no material value
bounded component result
```

Allow an explicit per-package suppression only with a documented reason.

## 11.2 Missing required semantic sections

Fail when any operational package lacks:

- Where It Fits in the OS
- Best-Fit Activities / Tasks
- When Not to Use
- Mechanism
- Procedure
- Failure Boundary
- Strong-Model Scaling
- Provenance

## 11.3 Duplicated mechanisms / procedures

Normalize text and compare Mechanism/Procedure sections across packages.

Flag:

- exact duplicates;
- near-identical boilerplate;
- suspiciously high similarity.

Do not use similarity as an automatic semantic verdict. Use it to force human/agent review.

## 11.4 Generic-only task mapping

Flag an Upgradeable whose only recommendation is:

```text
general-agent-workflow
```

unless metadata explicitly justifies why it is truly cross-domain.

## 11.5 Empty or trivial examples/tests

Require real concept-specific examples and cases.

## 11.6 Documentation / metadata mismatch

Where practical, verify that:

- slug;
- ID;
- version;
- activation;
- functional class;
- recommended task types;
- provenance;

do not contradict each other.

Add this auditor to CI.

---

# 12. FIX EVERY PACKAGE — NOT JUST DOC TEXT

For every operational package, audit and fix:

```text
UPGRADEABLE.md
metadata.yaml
examples/
tests/
```

If the concept has deterministic logic, consider a package-local `scripts/` directory.

Examples:

```text
placeholder suppression
exact quote verification
state schema validation
protected-token preservation
registry/rule compatibility
structured state serialization
```

Do not force deterministic scripts onto inherently semantic tasks.

---

# 13. CONCEPT-SPECIFIC EXAMPLES FOR ALL PACKAGES

Every operational package must have at least one useful example.

Preferred:

```text
examples/basic.md
```

But for complex components add more.

Each example should contain:

```text
Task context
Why this Upgradeable activates
Inputs/state
What the Upgradeable does
What it does NOT do
Result / state change
Interaction with companion components
```

For historically recovered use cases, label them as recovered.

For newly created examples, label them:

```text
Illustrative modern example
```

Do not pretend a new example came from historical chats.

---

# 14. STRUCTURED BEHAVIORAL TEST CASES FOR ALL PACKAGES

The current Markdown composition tests are useful but insufficient.

Create a machine-readable behavioral test format.

Recommended:

```text
evals/schema/behavior_case.schema.json
```

and per package:

```text
tests/cases.json
```

Every operational package should have at minimum:

1. `positive_activation`
2. `negative_activation`
3. `precedence_or_conflict`
4. `failure_boundary`
5. `strong_model_scaling`
6. `distinctive_mechanism`

The sixth case is critical.

It must test what makes this Upgradeable different from generic scaffolding.

Examples:

### Multiverse

Test that candidate paths must be materially distinct and bounded.

### Citation Fidelity

Test that a citation cannot pass when the cited source does not support the attached claim.

### Anti-Tunnel Vision

Test that at least one plausible competing interpretation is considered when fixation risk exists, without forcing alternatives after evidence has clearly collapsed the space.

### Micro-Repair

Test that a local defect is fixed without rewriting correct neighboring material.

### Surgery Editing

Test that local patching is rejected when the required change is architectural/global.

### StateBlock

Test that locked decisions survive unrelated new input.

### ABF

Test that retrieval/evidence capture is staged before synthesis rather than mixing uncontrolled source pulls with decision-making.

---

# 15. BUILD A GENERIC EVALUATION HARNESS

Create a provider-neutral framework under:

```text
evals/
├── README.md
├── schema/
├── fixtures/
├── adapters/
└── reports/
```

The framework must distinguish:

## Static/deterministic validation

Can run in CI without a model/API.

Examples:

- schema;
- activation metadata;
- source presence;
- exact string invariants;
- required sections;
- prohibited boilerplate;
- dependency graph;
- package consistency.

## Behavioral model evaluation

Requires an actual model adapter.

The base framework should define an interface but must not require API keys in CI.

Provide:

```text
evals/adapters/base.py
evals/adapters/mock.py
evals/adapters/command.py
```

`command.py` may allow a user to plug in a local CLI/model command.

Provider adapters may be added separately.

The repository must never claim behavioral test success against a model unless the model was actually run.

---

# 16. EXECUTABLE DETERMINISTIC FIXTURES WHERE FEASIBLE

For Upgradeables whose core contract can be partially checked without an LLM, add real executable tests.

Examples worth examining:

- Placeholder Suppression
- Citation Fidelity exact-quote/source-existence subset
- Safe Rewrite protected literal/number preservation
- StateBlock schema/invariant preservation
- State Snapshot required fields
- Rule/compatibility index logic
- ABF active-pull count/state staging
- External State Automation capability declaration
- Domain/Mode Isolation schema separation

Do not pretend a deterministic lexical check proves semantic correctness.

Document exactly what the test proves.

---

# 17. INTERACTION QUALITY — REPLACE SLUG LISTS WITH REASONS

Current packages often list compatible Upgradeables.

v0.2 should explain **why**.

Example:

Instead of:

```text
Compatible:
- parallel-qms
- anti-tunnel-vision
```

write:

```text
Parallel-QMS:
Use after Multiverse candidate generation to independently evaluate and collapse
the bounded candidates.

Anti-Tunnel Vision:
Use before or during candidate generation when the initial favored path risks
dominating the alternative set; it prevents Multiverse from generating merely
cosmetic variants of one idea.
```

Do this for all meaningful pairings.

For `None declared`, add a short rationale when useful.

---

# 18. COUNTERBALANCE MODEL

Every package must explicitly consider whether it has a natural counterbalance.

Examples already established in the architecture:

```text
Neuro-Focus ↔ Anti-Tunnel Vision
Controlled Drift ↔ Grounding
Multiverse ↔ QMS Collapse
CRISPR ↔ Invariance Stress
Risk-Tier Scaling ↔ Dynamic Depth Allocation
Resonance ↔ Domain/Mode Isolation
POWER/Cosmic Planning ↔ SAFE Execution
```

Do not fabricate a counterbalance just to populate the field.

But do not leave it empty without reviewing the question.

---

# 19. REDUNDANCY / OVERLAP REVIEW ACROSS ALL 96

Run a repository-wide semantic overlap review.

For every operational package identify:

- closest conceptual neighbors;
- whether it composes with them;
- whether it is a narrower mode;
- whether it duplicates another package;
- whether the distinction is historical only.

Do not delete or merge historical identities merely for elegance.

If two modern operational packages are materially redundant:

1. preserve historical provenance;
2. identify preferred canonical mechanism;
3. consider alias/mode/deprecation;
4. create migration notes;
5. do not silently collapse.

Create:

```text
audit/OVERLAP_AND_REDUNDANCY_REVIEW_v0.2.md
```

---

# 20. SOURCE SUPPORT / OPERATIONAL STATUS REVIEW

Some recovered historical names have sparse original definitions.

For each such operational package decide:

### Case A — sufficiently recovered

Use:

```yaml
mechanism_basis: recovered
```

### Case B — strongly derivable from recovered purpose/role

Use:

```yaml
mechanism_basis: normalized-from-recovered
```

Explain what was normalized.

### Case C — useful modern operationalization but not historically recovered

Use:

```yaml
mechanism_basis: modern-interpretation
```

Label the modern interpretation in `UPGRADEABLE.md`.

### Case D — too little evidence to defend operational behavior

Do **not** generate confident mechanics from the name.

Consider:

- lifecycle downgrade;
- provisional package;
- historical-only record;
- unresolved registry.

Record the decision in the audit.

---

# 21. PACKAGE VERSIONING

Target repository release:

```text
v0.2.0
```

For individual Upgradeables:

- documentation typo only → patch;
- compatible semantic specificity / richer procedure / added metadata → minor;
- corrected operational behavior that changes the package contract → evaluate whether a major package bump is warranted;
- identity change → normally preserve alias/migration rather than silently changing identity.

Because many v0.1 operational packages will receive substantive semantic hardening, a `1.1.0` package version will often be appropriate.

Do not blindly bump versions without recording why.

Update all package-version references in:

- recipes;
- example Skills;
- bundles;
- registry;
- generated all-in-one;
- docs.

---

# 22. FIX THE README PYTHON EXAMPLE

The v0.1 README currently renders a Python snippet with inappropriate top-level indentation around the registry example.

Fix it so this runs when copied:

```python
import json
from pathlib import Path

registry = json.loads(
    Path("registry/registry.json").read_text(encoding="utf-8")
)

research = next(
    recipe["classifications"]
    for recipe in registry["recipes"]
    if recipe["slug"] == "research-skill"
)
```

Add a CI/doc test that detects the basic example or executes it.

Do not allow a broken README code example in v0.2.

---

# 23. README V0.2 IMPROVEMENTS

Keep the current concise architecture.

Add a clear section:

```text
## How to choose Upgradeables
```

Explain three discovery paths:

```text
Task → Recipe → Upgradeables

Upgradeable → Purpose / OS Fit / Tasks / Interactions

Bundle → Curated multi-Upgradeable composition
```

Add:

```text
## Give this repo to an LLM
```

with a short instruction pointing to:

- `MODEL_CONSUMPTION_GUIDE.md`
- `registry/registry.json`
- `dist/ALL_IN_ONE_UPGRADEABLE_SKILL_KIT.md`

Do not turn README into the all-in-one document.

---

# 24. MODEL CONSUMPTION GUIDE V0.2

Update `MODEL_CONSUMPTION_GUIDE.md` so a frontier model must inspect:

```text
os_role
pipeline_stages
best_fit_tasks
avoid_when
mechanism_basis
counterbalances
potential redundancy
```

before activation.

Add a rule:

> Do not activate an Upgradeable solely because its name seems relevant. Confirm its trigger, OS placement, task-fit, and exclusion conditions.

Add a rule:

> When a package's mechanism basis is `modern-interpretation` or `provisional`, do not present that implementation as the recovered historical definition.

---

# 25. SKILL RECIPES — FULL REVIEW

Review **every recipe**, not only research/coding.

Ensure classifications reflect the improved package semantics.

For every recipe:

- validate R/A/C/O/X assignments;
- remove generic over-inclusion;
- explain why required components are required;
- explain important exclusions;
- identify expensive/high-risk components;
- ensure the recipe does not become an always-on maximal stack.

Add machine-readable recipe rationales where practical.

---

# 26. BUNDLES — FULL REVIEW

Review every curated bundle.

For each bundle answer:

- What problem does the bundle solve?
- What is the activation boundary?
- Which Upgradeables are required?
- Which are optional?
- What is the load order?
- Which interactions are critical?
- What would make the bundle excessive?

Do not define a bundle merely as a list of slugs.

---

# 27. PROVIDER ADAPTER HARDENING

The current provider adapter notes are intentionally skeletal.

For v0.2, expand **every existing adapter directory** into a useful mapping guide while preserving model-agnostic authority.

Create or improve:

```text
implementations/ADAPTER_CONTRACT.md
```

The adapter contract should describe how a platform maps:

```text
task Skill
behavior instructions
Core/reference loading
Upgradeable instructions
state representation
validators
scripts/tools
orchestration
capability declarations
persistence
parallelism
```

Every provider-specific adapter must explicitly distinguish:

- supported;
- unsupported;
- unknown / version-dependent.

Do not invent provider capabilities.

Do not hard-code claims likely to become stale unless verified and dated.

Model-specific adapters may change; the canonical Upgradeable specification must not depend on them.

---

# 28. EXAMPLE SKILLS

Review all existing example Skills.

At minimum keep a high-quality research example.

Add several additional worked examples that demonstrate distinct compositions, such as:

```text
source-grounded research
coding/debugging
long-context corpus analysis
creative ideation
high-stakes evidence analysis
architecture/Skill building
```

Each example should:

- cite Upgradeable slugs + versions;
- state why each was selected;
- state which tempting Upgradeables were excluded;
- show host capability assumptions;
- include tests.

Do not make all examples maximal stacks.

---

# 29. ALL-IN-ONE KIT IMPROVEMENT

The generated all-in-one artifact should remain generated.

Update `scripts/build_all_in_one.py` so the portable kit includes enough semantic content to be genuinely useful without cloning the repo.

For each operational Upgradeable include at least:

```text
display name
slug / ID / version
purpose
OS role
pipeline stage
best-fit task types
trigger
when not to use
mechanism summary
key companions/counterbalances
failure boundary
mechanism basis
package path
```

Do not dump every full `UPGRADEABLE.md` unless size remains practical.

The portable kit should remain a navigation/consumption artifact, not an unbounded repository mirror.

---

# 30. RELEASE ASSETS

The v0.1.0 release had no explicit attached assets.

For v0.2.0 attach at minimum:

```text
dist/ALL_IN_ONE_UPGRADEABLE_SKILL_KIT.md
registry/registry.json
registry/registry.yaml
dist/SHA256SUMS.txt
```

Optionally include:

```text
audit/OPERATIONAL_PACKAGE_REVIEW_v0.2.md
```

if useful to external reviewers.

Create a deterministic checksum build step.

Example:

```text
scripts/build_release_assets.py
```

Do not include secrets, local paths, or temporary files.

---

# 31. CI V0.2

Extend `.github/workflows/validate.yml`.

At minimum run:

```text
registry reproducibility
schema validation
unit tests
all-in-one reproducibility
link checking
semantic-specificity audit
behavior-case schema validation
README executable example test
release-asset/checksum reproducibility
```

If deterministic package-local scripts exist, test them.

CI should fail if:

- any baseline package is missing from the v0.2 audit;
- any operational package lacks required semantic sections;
- forbidden generic boilerplate returns;
- behavior cases are missing;
- generated artifacts are stale;
- unresolved records gain invented procedures.

---

# 32. NEW TESTS FOR COMPLETENESS

Add tests specifically for the “ALL packages” requirement.

Examples:

```text
test_every_operational_package_in_audit
test_every_operational_package_has_os_fit
test_every_operational_package_has_best_fit_tasks
test_every_operational_package_has_when_not_to_use
test_every_operational_package_has_behavior_cases
test_every_operational_package_has_nontrivial_example
test_no_baseline_package_unreviewed
test_no_forbidden_boilerplate
test_no_duplicate_generic_mechanisms
```

Do not hard-code `96` forever.

Capture the v0.1 baseline list in a versioned manifest such as:

```text
audit/v0.1.0-operational-baseline.json
```

Then test that each baseline slug has a v0.2 disposition.

---

# 33. BEHAVIORAL QUALITY — DO NOT GAME THE AUDITOR

Do not "fix" boilerplate detection by synonym substitution.

Bad:

```text
Apply this specific behavior in a bounded fashion...
```

if the following text still does not explain the mechanism.

The objective is semantic specificity, not passing a word filter.

A reviewer should be able to remove the Upgradeable name from the page and still infer which concept is being described from the mechanism/procedure alone.

Use that as a manual quality test.

---

# 34. EXAMPLE TARGET QUALITY — MULTIVERSE

The exact wording may differ, but the content should resemble:

```text
Mechanism:
Create a small number of materially different candidate solution paths before
commitment. Enforce distinctness so candidates are not cosmetic paraphrases.
Evaluate each against the same locked objective, constraints, evidence, and risk
criteria. Select one, synthesize supported elements when appropriate, then remove
losing branches from active state so discarded assumptions do not leak forward.

Procedure:
1. Confirm the task warrants branching.
2. Define the common evaluation criteria.
3. Generate 2–3 materially distinct candidate paths.
4. Reject/replace duplicate or cosmetic variants.
5. Evaluate candidates independently.
6. Compare results through the selected QMS/decision gate.
7. Select or synthesize.
8. Retire losing branches and update StateBlock.
```

This is qualitatively stronger than generic orchestrator text.

---

# 35. EXAMPLE TARGET QUALITY — MICRO-SCAFFOLDING

The exact wording may differ, but the content should resemble:

```text
Mechanism:
Create a temporary task-local scaffold containing only the constraints or
checkpoints most likely to be lost during the current subtask. Keep it smaller
than the parent StateBlock and retire it when the subtask is complete.

Example:
For a high-constraint rewrite, the scaffold may hold:
- preserve all numbers;
- preserve citation mapping;
- change tone only;
- do not alter conclusion.

It should not reload the entire OS or source corpus.
```

Again, do not copy this blindly. Ground the final package in the source corpus.

---

# 36. HIGH-FIDELITY VALIDATOR EXAMPLE — CITATION FIDELITY

Citation Fidelity is already more specific than several v0.1 packages.

Preserve and deepen the good behavior:

- bind claim ↔ source passage;
- verify source exists;
- verify exact quote;
- verify paraphrase preserves meaning;
- prevent adjacent-source borrowing;
- do not certify failed/unverifiable claims;
- do not rewrite evidence to make it pass.

Use it as one quality reference for other validators.

---

# 37. PACKAGE-SPECIFIC FAILURE BOUNDARIES

Replace generic failure boundaries where possible.

Examples:

### Multiverse

Failure:
Cannot generate materially distinct paths or lacks common evaluation criteria.

### Micro-Repair

Failure:
The defect is systemic enough that a local patch would create contradictions.

### Citation Fidelity

Failure:
Source support cannot be verified.

### StateBlock

Failure:
New state would overwrite locked facts without reconciliation.

### Anti-Tunnel Vision

Failure:
Alternative generation becomes unbounded or ignores decisive evidence.

### CRISPR Edit

Failure:
Requested change crosses protected invariants or requires structural refactor.

### Surgery Edit

Failure:
The architecture-level change cannot preserve required interfaces/locked truth.

Every package should have a failure boundary that helps an agent decide what to do next.

---

# 38. STRONG-MODEL SCALING — PACKAGE SPECIFICITY

Do not use the same scaling text everywhere.

For each package answer:

### What may a stronger model omit?

Examples:
- verbose checkpoints;
- redundant formatting scaffolds;
- repeated re-anchoring;
- expensive alternative generation on simple tasks.

### What invariant remains?

Examples:
- citation support;
- explicit authority;
- state consistency;
- zero-drift exact fields;
- veto conditions;
- source boundary;
- non-invention.

This field is part of the future-model philosophy and must remain meaningful.

---

# 39. DOCUMENT THE DISTINCTIVE MECHANISM OF ALL QMS MODES

Review the entire QMS family.

Do not let variants collapse into:

```text
evaluate output and score it
```

Make the distinction operational:

- Mirror — independent mirrored check.
- Risk-Tier-Split — depth based on risk.
- Cross-Phase — checks factual/evaluative/framing/hypothetical separation.
- Redundancy — multiple validation paths.
- ExIt-Integrated — bounded refine/re-evaluate.
- Hierarchical — atom/paragraph/section/global consistency.
- Transversal — temporal/causal/logical/modal cross-checking.
- Heterogeneous — different evaluator perspectives.
- Monte — perturb assumptions/conditions and test stability.
- Inversion — conclusion → required evidence reverse check.
- Conflict-Resolution — resolve validator/evidence disagreement by explicit priority.
- Distributed — truly isolated evaluators only when supported.
- Meta — evaluates QMS quality/agreement.
- Semantic Glass-Box — auditable semantic pass/fail map.
- Ethical — safety/ethical evaluator/veto.

Preserve the warning that simulated independent passes are not actual distributed execution.

---

# 40. HISTORICAL / PROVISIONAL CONTENT

Do not reduce provenance quality while deepening semantics.

Examples that require caution include:

- pre-freeze T1 library items;
- provisional T2-061–067 recovered historical-artifact mappings;
- unresolved acronym expansions;
- historical family-only recoveries.

The semantic-hardening pass must **increase clarity without rewriting history**.

---

# 41. OVER-SCAFFOLDING CONTROL

A major repository purpose is selective activation.

Review all packages for accidental “always-on” language.

Only true foundational controls should approach global candidacy.

Even a U0 package should still respect task simplicity and host capability.

Recipes and model guidance should explicitly remove modules without active triggers.

---

# 42. RELEASE VERSION / CHANGELOG

Update:

```text
CHANGELOG.md
```

Add a v0.2.0 section summarizing:

- all operational packages individually audited;
- semantic mechanisms deepened;
- OS-fit/task-fit metadata added;
- behavior-case schema added;
- semantic-specificity auditor added;
- provider adapters expanded;
- README runnable example fixed;
- release assets/checksums added;
- all-in-one kit enriched;
- provenance preserved;
- any lifecycle downgrades or merges/deprecations.

Add:

```text
MIGRATIONS/v0.1-to-v0.2.md
```

Explain schema changes and package-version implications.

---

# 43. ROADMAP UPDATE

Remove items that v0.2 completes.

Add next logical priorities such as:

- independent external review;
- empirical model-provider evaluations;
- community-proposed Upgradeables;
- benchmark datasets;
- visualization/browser UI;
- package dependency resolution tooling;
- signed provenance/release artifacts.

Do not claim empirical superiority until measured.

---

# 44. SOURCE-TO-REGISTRY MAP REVIEW

Re-run the source traceability review.

Every operational package should link back to one or more source anchors.

Prefer adding structured source references such as:

```yaml
source_refs:
  - document: OS_Upgradeable_to_Skills_Translation_Catalog_v2_Recovery_Merged.md
    heading: "T3-13. Citation Fidelity Gate"
    source_kind: current_consolidated_catalog
```

Where useful add:

```yaml
additional_context:
  - document: OS_Upgradeables_Deep_Context_Recovery_Addendum_2026-09-03.md
    heading: "PARALLEL-QMS — DEEP HISTORICAL OPERATING DETAILS"
```

Do not invent line numbers unless derived deterministically from the immutable archived file.

---

# 45. REGISTRY VERSION

Update:

```text
registry_version: 0.2.0
```

and schema version as warranted by field additions.

Regenerate both:

```text
registry/registry.yaml
registry/registry.json
```

They must remain deterministic.

---

# 46. PRE-RELEASE COMMANDS

Before commit/release run all repository validation plus new v0.2 checks.

At minimum:

```powershell
python scripts/build_registry.py
python scripts/build_all_in_one.py
python scripts/build_release_assets.py
python scripts/validate_registry.py
python scripts/audit_semantic_specificity.py
python -m unittest discover -s tests -v
python scripts/check_links.py
```

Then check generated files:

```powershell
python scripts/build_registry.py --check
python scripts/build_all_in_one.py --check
```

Add equivalent `--check` mode to release assets if appropriate.

Run:

```powershell
git diff --check
git status
```

Review the diff for accidental source/archive edits.

---

# 47. MANUAL COMPLETENESS CHECK

Before declaring success:

1. Determine baseline operational package list.
2. Count audit rows.
3. Count PASS.
4. Count BLOCKED_BY_SOURCE_GAP.
5. Count missing.
6. Count unreviewed.
7. Count packages containing forbidden boilerplate.
8. Count packages missing behavior cases.
9. Count packages missing examples.
10. Count docs/metadata mismatches.

Required:

```text
missing = 0
unreviewed = 0
forbidden_unresolved_boilerplate = 0
missing_behavior_cases = 0
missing_examples = 0
metadata_mismatch = 0
```

Report the exact numbers.

---

# 48. COMMIT STRATEGY

Prefer several coherent commits rather than one massive unreviewable commit.

Suggested:

```text
1. Add v0.2 semantic audit framework and metadata schema
2. Deepen foundation/state/context Upgradeables
3. Deepen reasoning/editing Upgradeables
4. Deepen truth/validation/QMS Upgradeables
5. Deepen orchestration/meta/persistence/output Upgradeables
6. Add behavior fixtures and evaluation harness
7. Harden recipes/bundles/adapters/examples
8. Update generated registry/all-in-one/release assets/docs
```

Exact grouping may change.

Do not split commits mechanically if it harms coherence.

---

# 49. PR / MERGE / RELEASE

After local validation:

```powershell
git push -u origin v0.2-semantic-hardening
```

If `gh` is authenticated:

1. Open a PR to `main`.
2. Include exact package audit counts.
3. Wait for / inspect CI.
4. Fix all failures.
5. Merge only after CI succeeds and the completeness audit is clean.

After merge:

```powershell
git switch main
git pull --ff-only
```

Confirm final CI.

Create tag/release:

```text
v0.2.0
```

Release title:

```text
Upgradeables v0.2.0 — Semantic Hardening and Behavioral Evaluation
```

Attach the required release assets.

Do not create the release if the package audit is incomplete.

---

# 50. RELEASE NOTES — REQUIRED METRICS

Release notes must report actual measured repository counts, for example:

```text
- N operational Upgradeables individually reviewed
- N packages semantically deepened
- N packages explicitly marked modern-interpretation
- N packages blocked/downgraded because source was insufficient
- N machine-readable behavioral cases
- N deterministic package-level checks
- N recipes reviewed
- N bundles reviewed
- N provider adapters expanded
- 0 baseline operational packages left unreviewed
```

Do not reuse placeholder numbers.

---

# 51. FINAL COMPLETION REPORT TO USER

At the end report:

## Repository

- branch;
- PR;
- merge commit;
- v0.2.0 URL;
- CI result.

## Operational package audit

- baseline count;
- PASS count;
- source-gap count;
- missing count;
- unreviewed count.

## Semantic hardening

- number of packages rewritten;
- number with mechanism-basis changes;
- number lifecycle-downgraded/deprecated/merged, if any.

## Behavioral testing

- structured cases;
- deterministic tests;
- model-dependent fixtures.

## Documentation

- README fixed;
- model guide updated;
- adapters updated;
- all-in-one rebuilt.

## Release assets

List attachments and checksums.

## Remaining legitimate historical gaps

List them explicitly.

Do not claim the original historical source is more complete than it actually is.

---

# 52. ACCEPTANCE CRITERIA

v0.2 is complete only if a fresh frontier model can inspect **any operational Upgradeable** and answer:

1. What is this?
2. What problem does it solve?
3. What actually happens when it activates?
4. Where does it fit into an OS/Skill workflow?
5. What activities/tasks should use it?
6. When should it not activate?
7. What state/evidence does it need?
8. What does it produce?
9. What does it pair with and why?
10. What counterbalances it?
11. What is redundant/conflicting with it?
12. What causes it to fail/stop/escalate?
13. What may a stronger model skip?
14. What invariant remains mandatory?
15. Is this historical mechanism recovered, normalized, or a modern interpretation?
16. What source supports the record?
17. How can its distinctive behavior be tested?

If that is not true for **every baseline operational package**, the work is not done.

---

# 53. NORTH STAR

The v0.1 architecture established:

```text
Skill
  = task identity
  + behavior
  + knowledge
  + selected Upgradeables
  + state
  + validation
  + output contract
```

v0.2 must ensure the Upgradeable library underneath that equation is not merely well organized, but semantically rich enough that each component is independently understandable and composable.

The target is:

```text
Historical provenance
       +
Distinctive mechanism
       +
Explicit activation boundary
       +
OS placement
       +
Task-fit guidance
       +
Interaction semantics
       +
Failure boundary
       +
Strong-model scaling
       +
Behavioral tests
       +
Machine-readable metadata
       =
Production-quality Upgradeable primitive
```

Do the full library.

**No sampling. No top-30 shortcut. No generic remainder.**
