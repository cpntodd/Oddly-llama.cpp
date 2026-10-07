---
name: "ggml_sycl_op_repeat_back"
type: "function"
file: "ggml/src/ggml-sycl/repeat_back.cpp"
community: "ggml"
---

# ggml_sycl_op_repeat_back

**Type:** `function`  **File:** `ggml/src/ggml-sycl/repeat_back.cpp`

**Community:** [[communities/ggml]]

## Depends On

- [[nodes/repeat_back.comp.cpp]] _imports_
- [[nodes/KeyValuePair]] _imports_
- [[nodes/stream]] _calls_
- [[nodes/parallel_for]] _calls_

## Used By

- [[nodes/ggml_sycl_repeat_back]] _calls_
