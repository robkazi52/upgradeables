# Generic Adapter

Use this provider-neutral mapping when a host has no maintained adapter.

## Mapping procedure

1. Write a complete task Skill with objective, authority, outputs, and failures.
2. Select Upgradeables by trigger, OS role, task fit, and exclusions.
3. Inline concise behavior instructions; load deep references only on demand.
4. Represent StateBlock data explicitly and state its real lifetime.
5. Bind validators and scripts only to real host execution mechanisms.
6. Map orchestration, persistence, and parallelism only after capability evidence.

## Capability matrix

- **Supported:** plain-text composition, explicit serialized state,
  file-path reference plans, and local static validators.
- **Unsupported by specification alone:** tools, durable persistence, isolated
  agents, true parallelism, and background execution.
- **Unknown / version-dependent:** all host-specific packaging, context,
  retrieval, tool, storage, permission, and concurrency features.

Complete [the shared contract](../ADAPTER_CONTRACT.md). If a required capability
remains unknown, omit or fail closed on the affected behavior.
