# Skill Translation Specification

```text
Skill = Task Identity + Behavior + Knowledge/References
        + Selected Upgradeables + State Requirements
        + Validation + Output Contract
```

Not every Skill needs every term, and not every Upgradeable becomes a Skill.

1. Identify the Skill archetype.
2. Define task identity and activation boundary.
3. Determine risk tier and evidence sensitivity.
4. Determine state and context requirements.
5. Select a Behavior Gene and Core where applicable.
6. Load foundational, then task-specific Upgradeables.
7. Add risk-dependent validators.
8. Check compatibility, counterbalances, conflicts, and redundancy.
9. Remove unnecessary scaffolding.
10. Choose the implementation form for every component.
11. Generate target instructions and move deep material to references/resources.
12. Add deterministic scripts only when they materially help.
13. Add positive, negative, conflict, long-context, and composition tests.
14. Run QMS/validation against the complete Skill.

Keep descriptions activation-oriented: say what the Skill does and when it should
activate, including exclusions. Preserve authority and failure boundaries.
Stronger models should receive less unnecessary scaffolding, while truth, state,
safety, and integrity controls remain when the task still requires them.
