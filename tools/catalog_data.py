"""Seed data transcribed from the three canonical recovery documents.

This module deliberately separates current operational entries from historical-only
and unresolved records. It is build input, not a replacement for archived sources.
"""

FUNCTIONAL_CLASSES = [
    "framing-intake", "state", "context-retrieval", "planning-reasoning",
    "truth-grounding", "validation", "drift-control", "editing-repair",
    "output", "orchestration", "meta-control", "persistence",
]

def e(identifier, slug, name, category, classes, activation, forms, purpose,
      tier, triggers=None, companions=None, aliases=None, lifecycle="stable",
      recovery="exact_recovery", requires=None, counterbalances=None,
      redundant=None, skill_types=None, notes=""):
    return {
        "id": identifier, "slug": slug, "display_name": name,
        "category": category, "functional_classes": classes,
        "activation_class": activation, "implementation_forms": forms,
        "purpose": purpose, "tiers": [tier], "triggers": triggers or [],
        "recommended_with": companions or [], "historical_aliases": aliases or [],
        "lifecycle_status": lifecycle, "recovery_status": recovery,
        "requires": requires or [], "counterbalances": counterbalances or [],
        "potentially_redundant_with": redundant or [],
        "recommended_skill_types": skill_types or ["general-agent-workflow"],
        "notes": notes,
    }

ENTRIES = [
    # Tier 1: core reliability.
    e("T1-01", "micro-scaffolding", "Micro-Scaffolding", "foundation", ["planning-reasoning", "state"], "U0-foundational", ["skill-component", "parent-skill-mode"], "Create only the smallest temporary checkpoints needed to preserve goals, constraints, evidence boundaries, and the next step.", "T1", ["multi-step or high-constraint work"], ["task-set-lock-in", "drift-suppression"], ["Micro-Scaffolding (Planning Before Writing)"]),
    e("T1-02", "drift-suppression", "Drift Suppression", "drift-control", ["drift-control", "validation"], "U0-foundational", ["validator", "skill-component"], "Detect and correct gradual movement away from the active goal, constraints, terminology, or evidence boundary.", "T1", ["long, branching, or iterative work"], ["task-set-lock-in", "stateblock"]),
    e("T1-03", "clarification-gateway", "Clarification Gateway", "foundation", ["framing-intake", "orchestration"], "U1-common-conditional", ["orchestrator", "guard"], "Distinguish ambiguity that can be resolved safely from ambiguity that materially blocks correct execution.", "T1", ["required variables are missing or instructions conflict"], ["task-set-lock-in"], ["Clarification-First", "Clarification-First Behavior"]),
    e("T1-04", "grounding-no-invention", "Grounding / No-Invention", "truth-grounding", ["truth-grounding", "validation"], "U0-foundational", ["validator", "guard"], "Keep factual output within supplied or verified evidence and label or omit unsupported material.", "T1", ["work relies on documents, data, external facts, or consequential claims"], ["citation-fidelity", "fail-closed-abstention"]),
    e("T1-05", "mode-lock-in", "Mode Lock-In", "state", ["state", "drift-control"], "U0-foundational", ["state-schema", "guard"], "Preserve the selected factual, hypothetical, design, execution, critique, or drafting mode until an authorized transition occurs.", "T1", ["a task can drift between modes"], ["task-set-lock-in", "domain-mode-isolation"]),
    e("T1-06", "task-set-lock-in", "Task-Set Lock-In", "state", ["framing-intake", "state"], "U0-foundational", ["state-schema", "state-manager"], "Lock the goal, deliverable, constraints, terminology, source boundaries, current subtask, and completion criteria.", "T1", ["multi-step work begins or scope changes"], ["stateblock", "drift-suppression"]),
    e("T1-07", "scoped-loader", "Scoped Loader / Loader Sequencing", "context-retrieval", ["context-retrieval", "orchestration"], "U0-foundational", ["orchestrator", "skill-component"], "Discover and load only the task-relevant Genes, Cores, Upgradeables, references, tools, and validators in authority order.", "T1", ["a modular workflow has multiple available components"], ["activation-budget-funnel", "task-set-lock-in"], ["Loader Sequencing", "Loader"]),
    e("T1-08", "placeholder-suppression", "Placeholder Suppression", "output", ["output", "validation"], "U1-common-conditional", ["validator", "deterministic-script"], "Prevent TODOs, dummy values, empty required sections, and unresolved markers from leaking into final artifacts.", "T1", ["templates or staged artifacts are finalized"], ["safe-rewrite"]),
    e("T1-09", "working-memory-cues", "Working-Memory Cues", "state", ["state"], "U0-foundational", ["state-schema", "skill-component"], "Maintain compact reminders of the current objective and constraints without repeatedly loading the full instruction set.", "T1", ["many constraints must remain active"], ["stateblock", "working-memory-lock-in"]),
    e("T1-10", "safe-rewrite", "Safe Rewrite Logic", "editing-repair", ["editing-repair", "truth-grounding"], "U0-foundational", ["guard", "skill-component"], "Rewrite authorized dimensions while preserving locked facts, meaning, citations, numbers, names, and constraints.", "T1", ["paraphrasing, polishing, or format conversion"], ["micro-repair", "citation-fidelity"]),

    # Consolidated Tier 2.
    e("T2-01", "bounded-exit", "Bounded ExIt", "reasoning", ["planning-reasoning", "validation"], "U1-common-conditional", ["parent-skill-mode", "orchestrator"], "Run evaluate-repair cycles with an explicit quality threshold and iteration budget.", "T2", ["a draft needs iterative improvement"], ["micro-repair", "parallel-qms"]),
    e("T2-02", "structured-refinement", "Structured Refinement Cycles", "editing-repair", ["editing-repair", "validation"], "U1-common-conditional", ["skill-component"], "Separate factual, structural, style, and final-validation revision passes while preserving accepted decisions.", "T2", ["revision has multiple defect classes"], ["safe-rewrite", "bounded-exit"]),
    e("T2-03", "regenerative-rewrite", "Regenerative Rewrite", "editing-repair", ["editing-repair"], "U2-specialized", ["skill-component"], "Rebuild an output when local repair cannot restore global structure or coherence, while preserving locked truths.", "T2", ["architecture or source mapping is globally broken"], ["task-set-lock-in", "surgery-edit"], counterbalances=["micro-repair"]),
    e("T2-04", "micro-repair", "Micro-Repair", "editing-repair", ["editing-repair"], "U0-foundational", ["skill-component", "deterministic-script"], "Correct the smallest faulty unit while preserving correct surrounding material.", "T2", ["a defect is localized"], ["safe-rewrite", "invariance-stress-scaffold"], counterbalances=["regenerative-rewrite"]),
    e("T2-05", "multi-layer-consistency", "Multi-Layer Consistency", "validation", ["validation", "orchestration"], "U1-common-conditional", ["validator"], "Check that system, project, task, Gene, Core, evidence, and output layers do not contradict one another.", "T2", ["multiple authority layers are composed"], ["domain-mode-isolation", "parallel-qms"]),
    e("T2-06", "progressive-mode-shaping", "Progressive Mode Shaping", "orchestration", ["orchestration", "planning-reasoning"], "U1-common-conditional", ["orchestrator", "parent-skill-mode"], "Narrow exploration through comparison and selection into precise execution as decisions become locked.", "T2", ["work moves from design to execution"], ["mode-lock-in", "hybrid-mode"]),
    e("T2-07", "stable-long-context", "Stable Long-Context", "state", ["state", "drift-control"], "U1-common-conditional", ["state-manager", "guard"], "Preserve decisions, terminology, constraints, and source meaning across large contexts while retiring obsolete branches.", "T2", ["large corpus or long-running workflow"], ["stateblock", "coherence-heartbeat"], ["Long-Context Coherence"]),
    e("T2-08", "working-memory-lock-in", "Working-Memory Lock-In", "state", ["state"], "U1-common-conditional", ["state-manager"], "Keep the most task-critical information in compact active state, verbatim where fidelity requires it.", "T2", ["critical state competes with large context"], ["working-memory-cues", "activation-budget-funnel"], ["WM Lock-In"]),
    e("T2-09", "stateblock", "StateBlock", "state", ["state"], "U0-foundational", ["state-schema"], "Represent goal, phase, constraints, decisions, uncertainties, active modules, completed work, and next step explicitly.", "T2", ["work spans multiple steps or components"], ["sequential-memory-state-engine", "state-snapshot"]),
    e("STATE-2025-12-03-T3", "cot-structured-state-block", "CoT-Structured State Block", "state", ["state"], "U1-common-conditional", ["state-schema"], "Represent task and reasoning state explicitly without claiming access to hidden or private chain-of-thought.", "historical-2025-12", ["structured intermediate task state must survive across steps"], ["stateblock", "sequential-memory-state-engine"], lifecycle="candidate", notes="Exact recovered name and role; modern implementations expose task state only."),
    e("T2-10", "sequential-memory-state-engine", "Sequential Memory State Engine (SMSE)", "state", ["state", "persistence"], "U1-common-conditional", ["state-manager"], "Update StateBlock incrementally while preserving source chunk boundaries, provenance, and locked state.", "T2", ["state changes across steps or source chunks"], ["stateblock", "stable-long-context"], ["SMSE"]),
    e("T2-11", "selfblock-auto-update", "SelfBlock Auto-Update", "state", ["state"], "U2-specialized", ["state-manager"], "Maintain task working state automatically without creating an identity narrative or unsupported memory.", "T2", ["the host can update explicit state after steps"], ["stateblock", "external-state-automation"]),
    e("T2-12", "reflectos", "Work Reflection Loop OS / ReflectOS", "validation", ["validation", "editing-repair"], "U1-common-conditional", ["validator", "parent-skill-mode"], "Run a bounded goal-anchored reflect, test, revise loop that corrects process errors without inventing facts.", "T2", ["output needs a deliberate quality pass"], ["stateblock", "bounded-exit"], ["WRL", "ReflectOS"]),
    e("T2-14A", "image-text-fidelity-capture", "Image Text Fidelity Capture", "truth-grounding", ["context-retrieval", "truth-grounding"], "U2-specialized", ["skill-component", "validator"], "Extract text and visible structure from images without inferring missing content.", "T2", ["an image contains source text to transcribe"], ["grounding-no-invention", "zero-drift-zones"], ["ITFC"], notes="Distinct from the unresolved Intent/Task Framing Controller use of ITFC."),
    e("T2-16", "activation-budget-funnel", "Activation-Budget Funnel", "context-retrieval", ["context-retrieval", "state"], "U1-common-conditional", ["orchestrator", "state-manager"], "Stage retrieve, capture, index, transform, write, and verify so raw retrieval does not compete with synthesis; keep roughly no more than five to seven active pulls in the live workspace.", "T2", ["many sources or modules compete for attention"], ["scoped-loader", "neuro-focus"], ["ABF"]),
    e("T2-17", "forethought-checkpoints", "Forethought / Checkpoints", "reasoning", ["planning-reasoning", "validation"], "U1-common-conditional", ["guard", "skill-component"], "Before irreversible or costly actions, predict likely downstream failures and verify prerequisites.", "T2", ["an action is costly, irreversible, or dependency-sensitive"], ["risk-tier-scaling"]),
    e("T2-18", "bidirectional-consistency", "Bidirectional Consistency", "validation", ["validation", "planning-reasoning"], "U1-common-conditional", ["validator"], "Check reasoning forward from evidence to conclusion and backward from conclusion to required evidence.", "T2", ["causal, logical, quantitative, or evidence claims are central"], ["critical-atomic-verification", "inversion-qms"]),
    e("T2-19", "anti-tunnel-vision", "Anti-Tunnel Vision", "reasoning", ["planning-reasoning", "validation"], "U1-common-conditional", ["guard", "skill-component"], "Test a favored interpretation against a small plausible alternative set before committing.", "T2", ["premature fixation is plausible"], ["multiverse-reasoning", "neuro-focus"], counterbalances=["neuro-focus"]),
    e("T2-20", "external-state-automation", "External State Automation", "persistence", ["state", "persistence"], "U2-specialized", ["state-manager", "deterministic-script"], "Serialize task state to real files, memory, databases, or project documents only when the host provides persistence.", "T2", ["continuation requires real external state"], ["state-snapshot", "stateblock"]),
    e("T2-21", "adapter-first-experimentation", "Adapter-First Experimentation", "meta-control", ["meta-control", "orchestration"], "U4-meta-architecture", ["orchestrator", "plugin-bundle-component"], "Prototype new capability as a detachable adapter and promote it only after evaluation.", "T2", ["a new capability may destabilize a base workflow"], ["architect-orchestrator"]),

    e("RS-00", "reasoning-scale-controller", "Reasoning-Scale Controller", "reasoning", ["planning-reasoning", "meta-control"], "U1-common-conditional", ["parent-skill-mode", "orchestrator"], "Select Subatomic, Atomic, Nano, Micro, QMS, or Cosmic decomposition and verification granularity without exposing private reasoning.", "RS", ["task complexity or risk requires depth selection"], ["cognitive-governor", "dynamic-depth-allocation"], notes="Nano is retained as a lightweight intermediate mode; its historical detailed specification is unresolved."),

    # Tier 3 truth, safety, and alignment.
    e("T3-01", "multi-truth-gating", "Multi-Truth Gating", "truth-grounding", ["truth-grounding", "validation"], "U3-high-risk-expensive", ["validator"], "Require compatible independent anchors or checks for important conclusions; resolve disagreement or abstain.", "T3", ["an important conclusion rests on fragile evidence"], ["truth-redundancy", "parallel-qms"]),
    e("T3-02", "controlled-drift-corridors", "Controlled Drift Corridors", "drift-control", ["drift-control", "truth-grounding"], "U1-common-conditional", ["guard", "parent-skill-mode"], "Declare zero, micro, or bounded exploratory transformation width according to task and risk.", "T3", ["synthesis or creativity must coexist with fidelity"], ["grounding-no-invention", "counterfactual-integrity"]),
    e("T3-03", "truth-redundancy", "Truth Redundancy", "truth-grounding", ["truth-grounding", "validation"], "U3-high-risk-expensive", ["validator"], "Use two independent truth anchors so one failure is less likely to corrupt the result.", "T3", ["a consequential claim can be independently checked"], ["multi-truth-gating"], ["Dual-Lepton Truth Redundancy"]),
    e("T3-04", "critical-atomic-verification", "Critical Atomic Verification", "validation", ["validation", "truth-grounding"], "U3-high-risk-expensive", ["validator"], "Identify and verify the smallest claims critical to the final decision before synthesis.", "T3", ["small factual errors could change the outcome"], ["citation-fidelity", "risk-tier-scaling"]),
    e("T3-05", "risk-tier-scaling", "Risk-Tier Scaling", "meta-control", ["meta-control", "validation"], "U1-common-conditional", ["orchestrator", "guard"], "Increase reasoning depth, verification, and veto strength as consequence, uncertainty, or irreversibility rises.", "T3", ["task risk varies or must be classified"], ["dynamic-depth-allocation", "fail-closed-abstention"]),
    e("T3-06", "truth-priority-hierarchy", "Truth Priority Hierarchy", "truth-grounding", ["truth-grounding", "orchestration"], "U1-common-conditional", ["orchestrator", "validator"], "Resolve evidence conflicts with an explicit domain hierarchy in which verified evidence outranks fluency.", "T3", ["evidence classes or authorities conflict"], ["conflict-resolution-qms"]),
    e("T3-07", "cross-checking-chains", "Cross-Checking Chains", "validation", ["validation"], "U2-specialized", ["validator"], "Validate linked dependencies where one failure could cascade into a larger conclusion.", "T3", ["a conclusion relies on a dependency chain"], ["critical-atomic-verification"]),
    e("T3-08", "two-truths-and-corridor", "Two Truths + Corridor", "truth-grounding", ["truth-grounding", "drift-control"], "U2-specialized", ["plugin-bundle-component", "guard"], "Combine two independent anchors with an explicitly permitted synthesis corridor.", "T3", ["source-grounded synthesis permits bounded interpretation"], ["truth-redundancy", "controlled-drift-corridors"]),
    e("T3-09", "fermionic-veto", "Fermionic Veto Strengthening", "validation", ["validation", "meta-control"], "U3-high-risk-expensive", ["validator", "guard"], "Block commitment when a critical contradiction, safety condition, or integrity failure is detected.", "T3", ["a defined critical condition must have veto authority"], ["fail-closed-abstention"]),
    e("T3-10", "domain-mode-isolation", "Domain / Mode Isolation", "state", ["state", "drift-control", "orchestration"], "U0-foundational", ["guard", "state-schema"], "Prevent assumptions, evidence standards, or hypothetical content from contaminating another domain or mode.", "T3", ["multiple domains or semantic modes coexist"], ["mode-lock-in", "resonance"]),
    e("T3-11", "fail-closed-abstention", "Fail-Closed Abstention", "truth-grounding", ["truth-grounding", "validation", "output"], "U3-high-risk-expensive", ["guard", "validator"], "Narrow or stop a conclusion when required evidence or integrity gates fail, returning only supported content.", "T3", ["required evidence cannot be verified"], ["grounding-no-invention", "fermionic-veto"], ["Fail-Closed Tier-3 Abstention"]),
    e("T3-12", "counterfactual-integrity", "Counterfactual Integrity Gate", "truth-grounding", ["truth-grounding", "drift-control"], "U1-common-conditional", ["guard", "validator"], "Keep hypothetical and counterfactual reasoning explicitly separated from factual claims.", "T3", ["counterfactual or hypothetical reasoning is used"], ["domain-mode-isolation", "controlled-drift-corridors"]),
    e("T3-13", "citation-fidelity", "Citation Fidelity Gate", "validation", ["validation", "truth-grounding"], "U1-common-conditional", ["validator", "deterministic-script"], "Verify that each citation exists and actually supports its attached claim without adjacent-source borrowing or meaning drift.", "T3", ["output contains citations or source-attributed claims"], ["grounding-no-invention", "critical-atomic-verification"]),
    e("T3-14", "zero-drift-zones", "Zero-Drift Zones", "drift-control", ["drift-control", "truth-grounding"], "U1-common-conditional", ["guard", "state-schema"], "Mark quotes, definitions, citation metadata, numbers, and exact policy language that may not be creatively transformed.", "T3", ["content contains fidelity-locked atoms"], ["safe-rewrite", "controlled-drift-corridors"], ["Zero-Drift Citation / Quote / Definition Zones"]),
    e("T3-15", "style-alignment", "Style-Alignment Module", "output", ["output"], "U1-common-conditional", ["skill-component"], "Match an authorized style without changing facts, evidence relationships, or reasoning integrity.", "T3", ["a style or voice is specified"], ["safe-rewrite", "citation-fidelity"]),
    e("T3-16", "pedagogical-alignment", "Pedagogical Alignment Constraint", "output", ["output", "framing-intake"], "U1-common-conditional", ["skill-component"], "Match explanation complexity and examples to the reader while preserving technical accuracy.", "T3", ["an audience or teaching level is known"], ["explanation-minimality-scaffold", "style-alignment"]),
    e("T3-17", "cognitive-governor", "Reasoning Budget / Cognitive Governor", "meta-control", ["meta-control", "planning-reasoning"], "U1-common-conditional", ["orchestrator"], "Allocate reasoning effort by complexity, risk, and expected value so trivial work is not overprocessed and high-risk work is not underchecked.", "T3", ["effort allocation materially affects cost or quality"], ["reasoning-scale-controller", "risk-tier-scaling"]),
    e("T3-18", "authenticity-anti-evasion", "Authenticity & Anti-Evasion Principle", "truth-grounding", ["truth-grounding", "output"], "U0-foundational", ["guard", "validator"], "Expose uncertainty and actual work status instead of pretending work occurred or substituting vague language for unsupported claims.", "T3", ["claims about evidence, actions, or completion are emitted"], ["grounding-no-invention"]),

    e("PQ-00", "parallel-qms", "Parallel Quality Management System", "validation", ["validation", "orchestration"], "U1-common-conditional", ["validator", "parent-skill-mode"], "Run one or more independent validation modes, compare results, and approve, reject, request repair, or abstain without adding facts.", "PQ", ["a composed workflow needs structured quality evaluation"], ["bounded-exit", "multi-layer-consistency"], aliases=["Parallel-QMS"]),

    # Advanced architecture.
    e("A-01", "multiverse-reasoning", "Multiverse Engine", "reasoning", ["planning-reasoning"], "U3-high-risk-expensive", ["orchestrator", "parent-skill-mode"], "Generate two or three materially distinct candidate paths, evaluate them, and collapse to one bounded result.", "A", ["competing hypotheses or designs would add value"], ["parallel-qms", "anti-tunnel-vision"]),
    e("A-02", "state-routing-bus", "State Routing Bus", "orchestration", ["state", "orchestration"], "U4-meta-architecture", ["state-manager", "orchestrator"], "Pass explicit task state, decisions, evidence pointers, and module outputs through host-supported handoffs.", "A", ["multiple components exchange state"], ["stateblock", "state-snapshot"], ["Teleport Bus"]),
    e("A-04", "coherence-heartbeat", "Global Coherence Heartbeat", "validation", ["validation", "state"], "U1-common-conditional", ["validator"], "Periodically verify that active plan, state, modules, and output remain globally coherent during long workflows.", "A", ["a workflow is long or multi-stage"], ["stable-long-context", "state-snapshot"]),
    e("A-05", "resonance", "Resonance", "orchestration", ["orchestration", "drift-control"], "U2-specialized", ["orchestrator", "guard"], "Coordinate mutually reinforcing modules, suppress irrelevant effects, and preserve authority boundaries.", "A", ["several active modules must align"], ["domain-mode-isolation", "multi-layer-consistency"], ["Resonance Locks"]),
    e("A-06", "resonance-gene-builder", "Resonance Gene Builder", "meta-control", ["meta-control", "orchestration"], "U4-meta-architecture", ["orchestrator", "reference-module"], "Encode recurring cross-module coupling rules as compact Behavior Genes with explicit authority boundaries.", "A", ["the same module relationship recurs"], ["behavior-gene-builder", "resonance"], ["Resonance Genes"]),
    e("A-07", "crispr-edit", "CRISPR Editing", "editing-repair", ["editing-repair"], "U2-specialized", ["skill-component", "deterministic-script"], "Apply a localized, invariant-preserving patch to a document, Skill, prompt, or architecture.", "A", ["a change is small and local"], ["invariance-stress-scaffold", "micro-repair"], counterbalances=["surgery-edit"]),
    e("A-08", "surgery-edit", "Surgery Editing", "editing-repair", ["editing-repair", "orchestration"], "U3-high-risk-expensive", ["skill-component", "orchestrator"], "Perform controlled structural replacement when a local patch cannot address an architecture-level change.", "A", ["layers, Cores, or workflows require major replacement"], ["regenerative-rewrite", "task-set-lock-in"], counterbalances=["crispr-edit"]),
    e("A-09", "neuro-focus", "Neuro-Focus", "context-retrieval", ["context-retrieval", "planning-reasoning"], "U1-common-conditional", ["orchestrator", "skill-component"], "Concentrate processing on the highest-value active region while suppressing irrelevant context.", "A", ["large sources or a narrow debug region demand concentration"], ["activation-budget-funnel", "anti-tunnel-vision"], counterbalances=["anti-tunnel-vision"]),
    e("A-11", "coherence-loops", "Coherence Loops", "validation", ["validation", "editing-repair"], "U2-specialized", ["validator", "parent-skill-mode"], "Boundedly compare local output with global goals and structure until coherence is sufficient.", "A", ["local edits risk global inconsistency"], ["bounded-exit", "coherence-heartbeat"]),

    e("BG-00", "behavior-gene-builder", "Behavior Gene Builder", "meta-control", ["meta-control", "orchestration"], "U4-meta-architecture", ["orchestrator", "reference-module"], "Create and validate reusable behavior and reasoning patterns without embedding domain knowledge dumps.", "BG", ["a recurring task family needs reusable behavior"], ["domain-core-builder", "architect-orchestrator"], ["Behavior Gene OS"]),
    e("C-00", "domain-core-builder", "Domain Core Builder", "meta-control", ["meta-control", "context-retrieval"], "U4-meta-architecture", ["orchestrator", "reference-module"], "Create high-density domain reasoning and evidence references that remain distinct from behavior instructions.", "C", ["a recurring domain needs structured knowledge and decision logic"], ["behavior-gene-builder", "citation-fidelity"]),
    e("O-01", "architect-orchestrator", "Architect Orchestrator", "orchestration", ["orchestration", "meta-control", "planning-reasoning"], "U4-meta-architecture", ["orchestrator"], "Plan modular systems, select components, resolve conflicts, coordinate execution and critique, then emit a compact state snapshot.", "O", ["designing or refactoring a Skill, OS, framework, or workflow"], ["scoped-loader", "parallel-qms", "state-snapshot"]),
    e("O-03", "state-snapshot", "State Snapshot", "state", ["state", "persistence"], "U1-common-conditional", ["state-schema", "state-manager"], "Capture the smallest sufficient goal, architecture, locked decisions, active modules, open issues, and next step for continuation.", "O", ["a workflow pauses, hands off, or persists"], ["stateblock", "external-state-automation"]),

    # Tier 4 and supervisor modes.
    e("T4-01", "meta-supervisor", "Meta-Supervisor Bundle", "meta-control", ["meta-control", "orchestration", "validation"], "U4-meta-architecture", ["orchestrator", "plugin-bundle-component"], "Monitor process health, active modes, state, loops, contradictions, and module interactions.", "T4", ["complex scaffolding itself needs supervision"], ["meta-awareness", "stuck-pattern-reset", "contradiction-micro-repair"]),
    e("T4-02", "meta-awareness", "Meta-Awareness Pack", "meta-control", ["meta-control", "validation"], "U4-meta-architecture", ["validator"], "Monitor task-process health and active module interactions without making identity or consciousness claims.", "T4", ["process failure signals must be observed"], ["meta-supervisor"]),
    e("T4-03", "stuck-pattern-reset", "Stuck-Pattern Reset Pack", "meta-control", ["meta-control", "editing-repair"], "U2-specialized", ["guard", "skill-component"], "Detect repeated failed approaches and reset only the failed path while preserving locked facts and constraints.", "T4", ["reasoning loops or stale approaches repeat"], ["bounded-exit", "stateblock"]),
    e("T4-04", "contradiction-micro-repair", "Contradiction Micro-Repair Pack", "editing-repair", ["editing-repair", "validation"], "U1-common-conditional", ["validator", "skill-component"], "Detect a contradiction and repair only the implicated region when a local fix is sufficient.", "T4", ["a localized contradiction is detected"], ["micro-repair", "bidirectional-consistency"]),
    e("T4-05", "ultimate-suite-supervisor", "Ultimate Suite Supervisor", "meta-control", ["meta-control", "orchestration", "validation"], "U4-meta-architecture", ["orchestrator"], "Declare modes, enforce the core stack, select local versus global editing, resolve pack conflicts, and run post-output health checks.", "T4", ["a large suite needs top-level coordination"], ["meta-supervisor", "hybrid-mode"]),
    e("T4-06", "safe-mode", "SAFE Mode", "meta-control", ["meta-control", "truth-grounding"], "U3-high-risk-expensive", ["parent-skill-mode"], "Use narrow drift, strong grounding, atomic verification, and conservative output during consequential execution.", "T4", ["execution is factual, consequential, or uncertain"], ["critical-atomic-verification", "grounding-no-invention"]),
    e("T4-07", "power-mode", "POWER Mode", "meta-control", ["meta-control", "planning-reasoning"], "U4-meta-architecture", ["parent-skill-mode"], "Use broad bounded exploration, deeper planning, candidate comparison, and system-level architecture reasoning.", "T4", ["architecture or design benefits from broad exploration"], ["multiverse-reasoning", "parallel-qms"]),
    e("T4-08", "hybrid-mode", "HYBRID Mode", "meta-control", ["meta-control", "orchestration"], "U4-meta-architecture", ["parent-skill-mode", "orchestrator"], "Use POWER for planning and SAFE for execution with explicit supervisor-controlled transitions.", "T4", ["work includes both broad design and grounded execution"], ["power-mode", "safe-mode"]),
    e("T4-09", "drift-spectra-scaling", "Drift-Spectra Scaling", "drift-control", ["drift-control", "meta-control"], "U2-specialized", ["orchestrator", "guard"], "Scale permitted transformation drift according to task type, evidence sensitivity, and risk.", "T4", ["different task regions need different drift widths"], ["controlled-drift-corridors", "risk-tier-scaling"], ["DS-Scale"]),
    e("T4-10", "compute-adaptive-drift", "Compute-Adaptive Drift Constraining", "drift-control", ["drift-control", "meta-control"], "U2-specialized", ["guard"], "Adjust drift constraints as reasoning depth or compute allocation changes.", "T4", ["compute/depth varies across a task"], ["dynamic-depth-allocation", "drift-spectra-scaling"], ["CADC"]),
    e("T4-11", "domain-normalized-drift", "Domain-Normalized Drift Field", "drift-control", ["drift-control"], "U2-specialized", ["guard", "reference-module"], "Set acceptable drift according to domain rather than applying one creativity width universally.", "T4", ["domains have materially different fidelity needs"], ["domain-mode-isolation", "controlled-drift-corridors"], ["DNDF"]),
    e("T4-12", "dynamic-depth-allocation", "Dynamic Depth Allocation", "meta-control", ["meta-control", "planning-reasoning"], "U1-common-conditional", ["orchestrator"], "Spend more reasoning depth on difficult, uncertain, or consequential regions and less on trivial ones.", "T4", ["task regions vary in difficulty or risk"], ["risk-tier-scaling", "cognitive-governor"], ["DDA"]),
    e("T4-13", "reasoning-throughput-governor", "Reasoning Throughput Governor", "meta-control", ["meta-control", "planning-reasoning"], "U2-specialized", ["orchestrator"], "Balance speed, breadth, and validation to avoid both underprocessing and wasteful overprocessing.", "T4", ["latency, breadth, and validation compete"], ["cognitive-governor", "dynamic-depth-allocation"], ["RTG"]),
    e("T4-14", "drift-immunity-propagation", "Drift Immunity Propagation", "drift-control", ["drift-control", "state"], "U2-specialized", ["state-manager", "guard"], "Carry locked constraints and invariants through downstream modules so resolved drift does not reappear.", "T4", ["many downstream modules consume locked decisions"], ["stateblock", "domain-mode-isolation"], ["DIP"]),
    e("T4-15", "meta-stability", "Meta-Stability Mode", "meta-control", ["meta-control", "state"], "U2-specialized", ["parent-skill-mode", "guard"], "Enter a stability-preserving mode when repeated changes, long context, or module conflicts threaten coherence.", "T4", ["coherence degrades under repeated change"], ["coherence-heartbeat", "drift-suppression"], ["MSM"]),
    e("T4-16", "cross-universe-consistency", "Cross-Universe Consistency Mode", "validation", ["validation", "planning-reasoning"], "U3-high-risk-expensive", ["validator", "parent-skill-mode"], "Compare candidate branches and reject a selection that depends on an unacknowledged contradiction.", "T4", ["parallel candidate paths are compared"], ["multiverse-reasoning", "parallel-qms"], ["CUCM"]),
    e("T4-17", "future-proof-mode-selector", "Future-Proof Mode Selector", "meta-control", ["meta-control", "orchestration"], "U4-meta-architecture", ["orchestrator"], "Select lighter or heavier scaffolding from host capability, environment support, and task risk.", "T4", ["an implementation targets models with different capabilities"], ["model-size-drift-scaling", "risk-tier-scaling"], ["FPMS"]),
    e("T4-18", "model-size-drift-scaling", "Drift-Stability Scaling with Model Size", "meta-control", ["meta-control", "drift-control"], "U4-meta-architecture", ["guard", "reference-module"], "Reduce unnecessary scaffolding as base-model reliability grows while preserving required truth, safety, and state controls.", "T4", ["adapting a workflow across model capability levels"], ["future-proof-mode-selector"], ["DSS-MS"]),

    # January 2026 exact-name training/scaffolding snapshot. Mechanisms are conservative operational interpretations.
    e("JAN26-01", "phase-locked-reasoning-scaffold", "Phase-Locked Reasoning Scaffold", "reasoning", ["planning-reasoning", "state"], "U2-specialized", ["state-schema", "guard"], "Keep factual, evaluative, framing, and hypothetical work in declared phases with explicit transitions.", "historical-2026-01", ["semantic phase leakage is a risk"], ["domain-mode-isolation"], lifecycle="candidate"),
    e("JAN26-02", "attention-compression-scaffold", "Attention Compression Scaffold", "context-retrieval", ["context-retrieval", "state"], "U1-common-conditional", ["state-manager"], "Compress verified, task-relevant context into a smaller indexed representation without changing meaning.", "historical-2026-01", ["source volume exceeds the active workspace"], ["activation-budget-funnel"], lifecycle="candidate"),
    e("JAN26-03", "dominant-driver-isolation-scaffold", "Dominant-Driver Isolation Scaffold", "reasoning", ["planning-reasoning"], "U1-common-conditional", ["skill-component"], "Identify the factor most responsible for an observed failure or decision before choosing an intervention.", "historical-2026-01", ["many possible causes compete"], ["anti-tunnel-vision"], lifecycle="candidate"),
    e("JAN26-04", "decision-first-scaffold", "Decision-First Scaffold", "reasoning", ["planning-reasoning", "output"], "U1-common-conditional", ["skill-component"], "State the decision target and criteria before collecting supporting analysis.", "historical-2026-01", ["analysis risks becoming directionless"], ["task-set-lock-in"], lifecycle="candidate"),
    e("JAN26-05", "epistemic-status-gating", "Epistemic Status Gating", "truth-grounding", ["truth-grounding", "validation"], "U1-common-conditional", ["guard", "validator"], "Label and gate statements as fact, inference, framing, or hypothesis before they influence conclusions.", "historical-2026-01", ["claims of mixed certainty are present"], ["grounding-no-invention"], lifecycle="candidate"),
    e("JAN26-06", "counterfactual-silence-scaffold", "Counterfactual Silence Scaffold", "truth-grounding", ["truth-grounding", "output"], "U2-specialized", ["guard"], "Suppress counterfactual additions when the task does not authorize hypothetical reasoning.", "historical-2026-01", ["factual output could be contaminated by hypothetical content"], ["counterfactual-integrity"], lifecycle="candidate"),
    e("JAN26-07", "temporal-anchor-scaffold", "Temporal Anchor Scaffold", "state", ["state", "truth-grounding"], "U1-common-conditional", ["state-schema", "validator"], "Preserve dates, sequence, effective periods, and temporal reference points during reasoning.", "historical-2026-01", ["time or chronology affects correctness"], ["stateblock"], lifecycle="candidate"),
    e("JAN26-08", "explanation-minimality-scaffold", "Explanation Minimality Scaffold", "output", ["output"], "U1-common-conditional", ["skill-component"], "Use the shortest explanation that remains accurate, sufficient, and appropriate for the audience.", "historical-2026-01", ["verbosity can obscure the answer"], ["pedagogical-alignment"], lifecycle="candidate"),
    e("JAN26-09", "invariance-stress-scaffold", "Invariance Stress Scaffold", "validation", ["validation", "editing-repair"], "U1-common-conditional", ["validator", "deterministic-script"], "Test whether protected behavior and facts outside a change remain unchanged.", "historical-2026-01", ["a patch or rewrite must preserve invariants"], ["crispr-edit", "safe-rewrite"], lifecycle="candidate"),
    e("JAN26-10", "drift-sink-scaffold", "Drift Sink Scaffold", "drift-control", ["drift-control", "state"], "U2-specialized", ["guard"], "Capture and retire irrelevant branches so they no longer compete with active task state.", "historical-2026-01", ["discarded branches keep resurfacing"], ["drift-suppression"], lifecycle="candidate", notes="Distinct exact-name snapshot entry; do not infer the unresolved ECL expansion."),
    e("JAN26-11", "cross-context-resonance-lock", "Cross-Context Resonance Lock", "orchestration", ["orchestration", "state"], "U2-specialized", ["guard", "state-manager"], "Preserve an explicit alignment relationship between related source contexts while respecting their boundaries.", "historical-2026-01", ["related contexts must stay aligned across a long task"], ["resonance", "domain-mode-isolation"], ["Resonance Upgradeable"], lifecycle="candidate"),
    e("JAN26-12", "authority-anchor-enforcement", "Authority Anchor Enforcement", "orchestration", ["orchestration", "validation"], "U1-common-conditional", ["guard", "validator"], "Bind decisions to the governing authority layer and prevent lower-priority modules from overriding it.", "historical-2026-01", ["multiple instruction authorities coexist"], ["multi-layer-consistency"], lifecycle="candidate"),
    e("JAN26-13", "structured-state-projection", "Structured State Projection", "state", ["state", "output"], "U2-specialized", ["state-schema", "state-manager"], "Project selected explicit state fields into a downstream component without exposing unrelated context.", "historical-2026-01", ["a component needs a bounded state view"], ["stateblock", "state-routing-bus"], lifecycle="candidate"),
    e("JAN26-14", "non-authoritative-branch-suppression", "Non-Authoritative Branch Suppression", "drift-control", ["drift-control", "orchestration"], "U2-specialized", ["guard"], "Prevent superseded or lower-authority branches from re-entering active decisions.", "historical-2026-01", ["obsolete alternatives conflict with locked decisions"], ["authority-anchor-enforcement", "drift-sink-scaffold"], lifecycle="candidate"),
    e("JAN26-15", "specificity-penalty-gate", "Specificity Penalty Gate", "validation", ["validation", "truth-grounding"], "U2-specialized", ["validator"], "Reject detail whose specificity exceeds the available evidence.", "historical-2026-01", ["precise details may be plausible but unsupported"], ["grounding-no-invention", "epistemic-status-gating"], lifecycle="candidate"),
]

QMS_MODES = [
    ("PQ-01", "mirror", "Mirror QMS", "Run mirrored independent checks and compare results."),
    ("PQ-02", "risk-tier-split", "Risk-Tier-Split QMS", "Apply evaluative depth and criteria by risk tier."),
    ("PQ-03", "cross-phase", "Cross-Phase QMS", "Check separation across factual, evaluative, framing, and hypothetical phases."),
    ("PQ-04", "redundancy", "Redundancy-QMS", "Use independent validation passes with veto or abstention capability."),
    ("PQ-05", "exit-integrated", "ExIt-Integrated QMS", "Combine scoring with bounded refinement and convergence."),
    ("PQ-06", "hierarchical", "Hierarchical QMS", "Check atomic, section, and global consistency."),
    ("PQ-07", "transversal", "Transversal QMS", "Check temporal, causal, logical, and modal dimensions."),
    ("PQ-08", "heterogeneous", "Heterogeneous QMS", "Apply different evaluator perspectives to the same candidate."),
    ("PQ-09", "monte", "Monte QMS", "Perturb assumptions and test stability; this is not formal Monte Carlo unless sampling is implemented."),
    ("PQ-10", "inversion", "Inversion QMS", "Test whether a conclusion's implied evidence is actually present."),
    ("PQ-11", "conflict-resolution", "Conflict-Resolution QMS", "Resolve evaluator or evidence conflicts with explicit priority rules."),
    ("PQ-12", "distributed", "Distributed QMS", "Use real isolated evaluators when available, otherwise label independent sequential passes honestly."),
    ("PQ-13", "meta", "Meta-QMS", "Evaluate the quality and agreement of other QMS evaluations."),
    ("PQ-14", "semantic-glass-box", "Semantic Glass-Box QMS", "Emit an auditable semantic pass/fail map instead of only a score."),
    ("PQ-15", "ethical", "Ethical QMS", "Apply an ethical or safety evaluator with explicit veto authority where applicable."),
]

GENES = [
    ("BG-01", "ipmn", "IPMN Gene", "Inpatient medical-necessity appeal reasoning and writing behavior."),
    ("BG-02", "ipta", "IPTA Gene", "Inpatient technical or administrative appeal routing behavior."),
    ("BG-03", "opmn", "OPMN Gene", "Outpatient medical-necessity reasoning behavior."),
    ("BG-04", "opta", "OPTA Gene", "Outpatient administrative or authorization reasoning behavior."),
    ("BG-05", "readmission", "Readmission Gene", "Compare episodes, discharge conditions, deterioration, barriers, and preventability."),
    ("BG-06", "gmn", "GMN Gene", "Fallback behavior for mixed or cross-setting medical-necessity work."),
    ("BG-07", "tone", "Tone Genes", "Apply authorized tone without changing truth, evidence, or structure."),
    ("BG-08", "risk-emphasis", "Risk-Emphasis Genes", "Adjust risk emphasis according to task and evidence."),
    ("BG-09", "deep-summary", "Deep Summary Gene", "Produce source-faithful deep summaries."),
    ("BG-10", "compare-contrast", "Compare-Contrast Gene", "Compare sources, options, or frameworks systematically."),
    ("BG-11", "alignment", "Alignment Gene", "Map agreement among sources, requirements, or plans."),
    ("BG-12", "conflict-handling", "Conflict-Handling Gene", "Surface and reconcile contradictory source claims or requirements."),
    ("BG-13", "synthesis", "Synthesis Gene", "Combine supported findings into a coherent higher-level model."),
    ("BG-14", "memory", "Memory Gene", "Preserve established decisions and cross-source consistency without inventing memory."),
]

CORES = [
    ("C-01", "ipmn", "IPMN Core", "Inpatient medical-necessity domain reasoning and evidence reference."),
    ("C-02", "ipta", "IPTA Core", "Inpatient technical or administrative appeal reference."),
    ("C-03", "opmn", "OPMN Core", "Outpatient medical-necessity domain reference."),
    ("C-04", "opta", "OPTA Core", "Outpatient technical or authorization reference."),
    ("C-05", "readmission", "Readmission Core", "Readmission evidence and comparison reference."),
    ("C-06", "gmn", "GMN Core", "General medical-necessity domain reference."),
    ("C-07", "policy", "Policy Core", "Versioned policy evidence and authority reference."),
    ("C-08", "chart-review", "Chart-Review Core", "Source-faithful chart review variables and evidence map."),
    ("C-09", "analysis", "Analysis Core", "Coordinates Deep Summary and Compare-Contrast behavior."),
    ("C-10", "synthesis", "Synthesis Core", "Coordinates Alignment and Synthesis behavior."),
    ("C-11", "meta-integrity", "Meta-Integrity Core", "Coordinates conflict handling, memory, fabrication checks, and speculation labels."),
]

DOMAIN_OS = [
    ("D-01", "architect-os", "Architect OS", "System architecture, modular decomposition, controlled editing, validation, and state snapshots."),
    ("D-02", "appeal-caf-os", "Appeal / CAF OS", "Routes inpatient, outpatient, technical, readmission, and general medical-necessity Gene/Core pairs."),
    ("D-03", "research-decision-os", "Research & Decision OS", "Corpus intake, evidence evaluation, conceptual mapping, decision criteria, synthesis, and planning."),
    ("D-04", "paper-author-os", "Paper-Author OS", "Source-grounded authoring with semantic phase separation, citation fidelity, and global validation."),
    ("D-05", "local-chat-analysis-author-os", "Local Chat-Analysis Author OS", "Source-faithful analysis and synthesis of pasted conversations."),
    ("D-06", "multi-os", "Multi-OS", "Coordinates domain operating systems while preserving domain and mode isolation."),
]

HISTORICAL_T1 = [
    "FACT_SCOPE_GATE_T1", "NO_INFERENCE_GATE_APPEALS_T1", "HALLUCINATION_NO_MANS_LAND_T1",
    "UNKNOWNS_PROTOCOL_T1", "UNCERTAINTY_CONTAINMENT_T1", "CLINICAL_PLAUSIBILITY_GATE_T1",
    "EVIDENCE_CHAIN_BINDING_T1", "PRIORITY_RETRIEVAL_LANES_T1", "GLOBAL_LOCAL_ANCHOR_SPLIT_T1",
    "ZERO_DRIFT_LOOP_T1", "SUPERVISOR_WORKER_PATTERN_T1", "UPGRADEABLE_ACTIVATION_TIERS_T1",
    "RULE_INDEX_OS_T1", "DRIFT_MONITOR_T1", "EXECUTION_LOG_OS_T1", "PA_AI_BROKER_PATTERN_T1",
    "PA_RULE_LOADER_FROM_INDEX_T1", "PA_QUEUE_BASED_AI_REQUESTS_T1",
]

HISTORICAL_T2 = [
    ("T2-008", "Novelty & Creativity Expansion"), ("T2-009", "Micro-Creative Mode"),
    ("T2-010", "Cognitive Flexibility"), ("T2-011", "Perspective Break"),
    ("T2-012", "Strange Loop Generator"), ("T2-013", "Balanced Exploration"),
    ("T2-014", "Dream-Mode Creative"), ("T2-015", "Hypnagogic Divergence"),
    ("T2-016", "Grounding & Reality Testing"), ("T2-017", "Drift Blocker (Inhibition)"),
    ("T2-018", "Chain-of-Thought Stabilizer"), ("T2-019", "Oscillation Regulator"),
    ("T2-020", "Deliberate Pacing"), ("T2-021", "Noise Suppression"),
    ("T2-022", "Reasoning Simplification"), ("T2-023", "Global Stabilizer (Macro)"),
    ("T2-031", "Reasoning Resection"), ("T2-032", "Cognitive Debridement"),
    ("T2-033", "Structural Reconstruction"), ("T2-034", "Reasoning Anastomosis"),
    ("T2-035", "Context Revascularization"), ("T2-036", "Cognitive Prosthetics"),
    ("T2-037", "Global Trauma Stabilizer"),
]

LEGACY_OS = [
    ("ELROS", "Ethical Reasoning OS", "ethical judgment"),
    ("SOROS", "Social Reasoning OS", "social reasoning"),
    ("PROOS", "Conflict-Resolution OS", "conflicting values and conflict resolution"),
    ("TIMOS", "Temporal OS", "time, commitments, and temporal reasoning"),
    ("GROOS", "Optimization Governor OS", "limits aggressive optimization"),
    ("ALMOS", "Learning & Adaptation OS", "safe learning and adaptation"),
    ("CROS", "Creativity Regulator OS", "keeps creativity bounded away from factual claims"),
]

PREFREEZE_T1 = [
    ("SEMANTIC_ANCHORING_PACK_T1", "Maintain recurring concepts and phrases across a workflow."),
    ("RECALL_TRIGGERS_T1", "Map phrases or conditions to explicit rule reactivation or retrieval."),
    ("HEARTBEAT_SNAPSHOTS_T1", "Capture current actions, locked decisions, goal, and next steps."),
    ("ANCHOR_TOKENS_SOFT_TAGS_T1", "Mark key rule blocks with explicit tags or priority labels."),
    ("RULE_VERSIONING_PIPELINE_T1", "Version modules with change tracking and audit history."),
    ("RULE_PROMOTION_DEV_TO_PROD_T1", "Promote modules only after testing and approval."),
    ("BEHAVIOR_PROFILE_SELECTOR_T1", "Select named behavior or configuration profiles."),
    ("RULE_STATUS_FLAGS_T1", "Attach explicit lifecycle/status flags to rules."),
    ("RULEPACK_COMPATIBILITY_MATRIX_T1", "Record compatibility, counterbalance, conflict, and redundancy."),
    ("CONFIG_OVERRIDE_GOVERNOR_T1", "Control override priority through explicit precedence."),
    ("SCENARIO_PACK_REGRESSION_T1", "Run known scenarios to detect behavior regressions."),
    ("EXPLAINABILITY_SNAPSHOT_T1", "Emit a compact auditable state/rule/result snapshot, not private reasoning."),
    ("HEALTH_SNAPSHOT_ENGINE_T1", "Summarize missing modules, drift, conflicts, stale state, and validation failures."),
]

RESONANCE_T2 = [
    ("T2-038", "High-Coherence State Induction", "Concentrate work around high-value constraints and anchors.", "neuro-focus"),
    ("T2-039", "Resonance Warm-Ups", "Restate task, load minimal anchors, lock constraints, and establish mode.", "micro-scaffolding"),
    ("T2-040", "Attention Corridor Narrowing", "Narrow attention to essential task elements with anti-fixation counterbalance.", "neuro-focus"),
    ("T2-041", "Anchor-Chain Reinforcement", "Reassert critical anchors at meaningful checkpoints.", "drift-immunity-propagation"),
    ("T2-042", "Resonance Plateau Detection", "Detect diminishing returns or excessive rigidity and relax/stop.", "bounded-exit"),
    ("T2-043", "Stability Guardrails", "Enforce reasoning boundaries and prevent drift.", "drift-suppression"),
]

SUPERVISOR_T2 = [
    ("T2-061", "Mode Declaration Engine"), ("T2-062", "Pack Routing Engine"),
    ("T2-063", "Pack Conflict Resolver"), ("T2-064", "Pack Health Check Engine"),
    ("T2-065", "Reasoning Pipeline Orchestrator"), ("T2-066", "Pack Activation/Deactivation Manager"),
    ("T2-067", "Mode Transition Stabilizer"),
]

UNRESOLVED = [
    ("ocg", "OCG", "Exact expansion and behavior were not recovered."),
    ("ecl-drift-sink", "ECL / Drift Sink", "ECL expansion and full original definition were not recovered."),
    ("lros", "LROS", "The acronym expansion was not recovered."),
    ("intent-task-framing-controller", "Intent/Task Framing Controller (ITFC)", "Name is recovered, but the full original specification is incomplete."),
    ("frozen-t1-missing-members", "Frozen T1-Core Bundle missing members", "Ten members of the 28-item bundle were not re-exposed."),
    ("frozen-t2-neuro-focus-members", "Frozen T2-001..007 Neuro-Focus members", "Seven individual names were not re-exposed."),
    ("frozen-t2-crispr-members", "Frozen T2-024..030 CRISPR members", "Seven individual names were not re-exposed."),
    ("frozen-t2-duration-members", "Frozen T2-044..046 Duration members", "Three individual names were not re-exposed."),
    ("frozen-t2-energy-members", "Frozen T2-047..049 Energy members", "Three individual names were not re-exposed."),
    ("frozen-t2-immune-members", "Frozen T2-050..052 Immune members", "Three individual names were not re-exposed."),
    ("frozen-t2-tone-members", "Frozen T2-053..056 Interpersonal/Tone members", "Four individual names were not re-exposed."),
    ("frozen-t2-consciousness-members", "Frozen T2-057..060 Consciousness Layer members", "Four individual names were not re-exposed; no consciousness mechanism is inferred."),
    ("reasoning-scale-nano-details", "Nano reasoning-scale details", "The mode name and position are recovered; its detailed historical specification is not."),
    ("bounded-exit-acronym", "Bounded ExIt acronym expansion", "The operational loop is recovered, but the historical acronym expansion was not."),
]
