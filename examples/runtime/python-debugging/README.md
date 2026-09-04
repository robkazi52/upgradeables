# Python debugging runtime example

This deterministic example shows the complete boundary from a raw task through
v0.3 selection and v0.4 compilation. `baseline-request.json` has the ordinary
user task only. `adaptive-request.json` preserves the same task and base
instruction while adding the compiled managed block.

`mock-result.json` is explicitly illustrative and is not experimental evidence.
Regenerate or verify the checked-in artifacts with:

```bash
python scripts/build_runtime_example.py
python scripts/build_runtime_example.py --check
```
