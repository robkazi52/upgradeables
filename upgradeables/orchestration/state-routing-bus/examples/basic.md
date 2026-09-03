# Basic composition example

**Situation:** multiple components exchange state.

**Composition:** establish a task lock, activate `state-routing-bus`, preserve
explicit state and evidence boundaries, then pass the result through the
workflow's applicable validator.

**Expected:** the component performs only its documented purpose and reports
uncertainty or failure instead of manufacturing missing support.
