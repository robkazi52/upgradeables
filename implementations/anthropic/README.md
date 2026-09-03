# Anthropic Adapter

Map a task Skill to instruction, context, and tool surfaces actually enabled in
the selected Anthropic host. Canonical behavior remains in `upgradeables/`.

## Mapping

| Concern | Mapping |
|---|---|
| Task Skill / behavior | Place the full workflow in the verified instruction surface; preserve triggers and exclusions. |
| Core loading | Attach or retrieve only references required by the active stage. |
| State | Serialize explicit StateBlock fields and declare their real lifetime. |
| Validators | Use configured tools for deterministic checks; otherwise retain cases as unevaluated specifications. |
| Orchestration | Map delegation only to verified primitives and validate returned results. |
| Persistence / parallelism | Name the backing mechanism; role-labeled prompting is insufficient. |

## Capability matrix

- **Supported:** provider-neutral instruction composition, explicit text/JSON
  state, bounded references, and local repository validators.
- **Unsupported by specification alone:** durable memory, isolated subagents,
  external tools, and unattended execution.
- **Unknown / version-dependent:** packaging, context limits, retrieval, tool
  interfaces, persistence, and parallel execution. Verify and date these claims.

Apply [the shared contract](../ADAPTER_CONTRACT.md); host/system policy retains precedence.
