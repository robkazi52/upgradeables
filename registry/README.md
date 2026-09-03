# Registry Files

Use [`catalog.json`](catalog.json) for fast discovery. It contains compact
Upgradeable records and resolves every recipe component to its current version,
trigger summary, dependencies, and package path.

Use [`registry.json`](registry.json) when you need complete canonical metadata,
historical records, unresolved records, Genes, Cores, modes, or provenance.
`registry.yaml` contains the same data as a JSON-compatible YAML 1.2 subset.

```bash
python scripts/query_registry.py --slug grounding-no-invention
python scripts/query_registry.py --recipe research-skill
python scripts/query_registry.py --class validation
python scripts/query_registry.py --search citation
```

These files are generated. Edit package metadata or source data, then run
`python scripts/build_registry.py`; do not hand-edit generated registries.
