# Basic composition example

**Situation:** state changes across steps or source chunks.

**Composition:** establish a task lock, activate `sequential-memory-state-engine`, preserve
explicit state and evidence boundaries, then pass the result through the
workflow's applicable validator.

**Expected:** the component performs only its documented purpose and reports
uncertainty or failure instead of manufacturing missing support.
