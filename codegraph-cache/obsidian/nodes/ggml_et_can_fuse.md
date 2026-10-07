---
name: "ggml_et_can_fuse"
type: "function"
file: "ggml/src/ggml-et/ggml-et.cpp"
community: "ggml"
---

# ggml_et_can_fuse

**Type:** `function`  **File:** `ggml/src/ggml-et/ggml-et.cpp`

**Community:** [[communities/ggml]]

## Depends On

- [[nodes/ggml_can_fuse]] _calls_
- [[nodes/ggml_is_contiguous]] _calls_
- [[nodes/ggml_is_contiguous_rows]] _calls_
- [[nodes/rows]] _calls_

## Used By

- [[nodes/ggml_backend_et_graph_compute]] _calls_
- [[nodes/ggml_et_op_glu]] _calls_
