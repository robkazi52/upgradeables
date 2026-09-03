# Domain-Calibrated Change Tolerance (`domain-normalized-drift@1.1.0`)

Recovered name: Domain-Normalized Drift Field

Purpose: Avoid applying casual creative tolerance to precision domains or unnecessary rigidity to expressive domains.

Activate when: domains have materially different fidelity needs.

Do not use when: domain is ambiguous and stakes are high; a task-specific explicit policy already controls every region.

Requires: none.

## Runtime mechanism

Classify the operative domain and consequence classes, load a versioned domain profile describing default treatment of facts, terminology, citations, uncertainty, formatting, and creative latitude, then override it with explicit task instructions and region-level evidence. The profile supplies defaults only; it never determines truth or authority.

## Procedure

1. Identify the operative domain and mixed-domain boundaries.
2. Assess consequences of factual, terminological, structural, and stylistic drift.
3. Select a versioned domain default profile.
4. Apply higher-authority task constraints and source-specific requirements.
5. Instantiate region-level corridors and validation checks.

## Guardrails

- Mandatory even on strong models: consequence assessment; task override precedence; mixed-domain boundary handling.
- Conflict/precedence: Explicit task/source authority outranks the domain profile; For mixed-domain content, apply the stricter relevant profile at shared boundaries unless an authorized rule says otherwise.
- Stop or fail when: Do not select a permissive profile when domain classification or consequence is uncertain; Escalate profile conflicts in regulated or safety-critical work.

Full package and provenance: [`domain-normalized-drift`](../../upgradeables/drift-control/domain-normalized-drift/UPGRADEABLE.md).
