# Cross-Module Coordination (`resonance@1.1.0`)

Recovered name: Resonance

Purpose: Coordinate active modules that should reinforce one another while suppressing irrelevant effects and preserving authority boundaries.

Activate when: several active modules must align.

Do not use when: only one module is active; the proposed reinforcement would amplify repetition, exaggeration, or an authority conflict.

Requires: none.

## Runtime mechanism

Identify the specific outputs or constraints through which selected modules should reinforce one another, declare the direction and limit of that coupling, and suppress unrelated effects. Check hierarchy before amplification so a lower-authority module cannot become stronger through repetition. Amplification means clearer coordination and usable handoff, not duplicated content.

## Procedure

1. List active modules and the exact relationship that should be reinforced.
2. Verify their authority, source, and state boundaries are compatible.
3. Define the bounded handoff or mutual constraint that creates the useful coupling.
4. Suppress duplicate, irrelevant, or conflicting module effects.
5. Check the coordinated result and dissolve the coupling when its trigger ends.

## Guardrails

- Mandatory even on strong models: explicit relationship, bounded effect, noise suppression, and authority preservation.
- Conflict/precedence: Host, system, domain, and explicit user authority take precedence over this component; If the modules have incompatible authority or source boundaries, stop or escalate rather than forcing a nominal success.
- Stop or fail when: the modules have incompatible authority or source boundaries; the coupling produces repetition or exaggeration instead of clearer coordination.

Full package and provenance: [`resonance`](../../upgradeables/orchestration/resonance/UPGRADEABLE.md).
