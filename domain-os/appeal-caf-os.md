# Appeal / CAF OS

**Source ID:** `D-02`

Routes inpatient, outpatient, technical, readmission, and general medical-necessity Gene/Core pairs.

Recovered user architecture: `GLOBAL OS -> INTAKE / CLASSIFICATION OS -> FAMILY OS -> BLUEPRINT -> authorized policy/regulatory/evidence references -> output`. Intake classifies and emits an explicit routing object; it does not draft or override the Global OS. Recovered Intake Decision Object fields include `task_type`, `appeal_family`, `clinical_or_technical`, and `encounter_model`; the complete historical field set is not recovered and must not be invented. Missing required values are marked `Not documented`, and routing to a reference folder does not establish that its contents apply. Separate intake and drafting calls preserve scoped loading and retrieval/decision separation.

This is a model-agnostic composition example, not a single Upgradeable or an
always-on prompt. It selects task-specific Genes, authorized Cores, explicit
state, and risk-appropriate Upgradeables/validators. Domain and mode isolation
prevent rule leakage. Any absent policy or domain detail remains absent; this
public seed does not infer private organization content.
