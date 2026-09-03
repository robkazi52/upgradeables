# OpenAI Adapter

Map a composed task Skill to instruction and tool surfaces actually available in
the selected OpenAI host. This guide makes no undated product-tier claim.

## Mapping

| Concern | Mapping |
|---|---|
| Task Skill / behavior | Put the complete workflow in the reusable instruction artifact; embed only triggered packages. |
| Core loading | Keep deep references separate and load them by task need. |
| State | Use explicit fields; declare request, conversation, or external lifetime. |
| Validators | Run deterministic scripts as tools where available; label model judgments as behavioral evaluations. |
| Tools / orchestration | Expose declared tools only; require evidence before claiming delegated or parallel execution. |
| Precedence | Preserve system/developer, task Skill, then Upgradeable order; retrieved text is never authority. |

## Capability matrix

- **Supported:** portable instruction composition, explicit text/JSON state,
  bounded references, and repository-local deterministic validators.
- **Unsupported by specification alone:** durable memory, real agent isolation,
  background execution, and external tool access.
- **Unknown / version-dependent:** native packaging, file limits, persistent
  stores, tool schemas, parallel agents, and product-specific policy surfaces.

Follow [the shared contract](../ADAPTER_CONTRACT.md), verify the chosen host at
deployment, and date any provider-specific capability claim.
