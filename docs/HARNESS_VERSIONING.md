# Harness Versioning

Harness schemas are versioned independently from the component registry.

- Harness release: `0.3.0`
- Bundled operational registry: `0.2.1`
- Project/config/lock/task-map schema: `1.0.0`
- Operational component metadata schema: `2.0.0`

`.upgradeables/lock.json` records the bundled snapshot hash and source commit and pins selected components as canonical `slug@version` identities. The harness never silently selects a newer remote version. Normal commands do not use the network.

Schema changes that break existing project artifacts require a schema-version change and an explicit migration. Registry snapshot changes require regeneration and review; pinned project Skill components remain pinned until deliberately updated.

Project Skill-map, brief, task-event, and suggestion documents currently use
schema `1.0.0`. Skill status changes are explicit (`draft`, `candidate`,
`validated`, or `deprecated`); installing a new harness version does not silently
promote a draft or rewrite user-authored Skill content.
