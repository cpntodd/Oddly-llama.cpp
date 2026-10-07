---
name: "ggml_sycl_op_fill"
type: "function"
file: "ggml/src/ggml-sycl/fill.cpp"
community: "ggml"
---

# ggml_sycl_op_fill

**Type:** `function`  **File:** `ggml/src/ggml-sycl/fill.cpp`

**Community:** [[communities/ggml]]

## Depends On

- [[nodes/fill.comp.cpp]] _imports_
- [[nodes/KeyValuePair]] _imports_
- [[nodes/ggml_is_contiguous]] _calls_
- [[nodes/stream]] _calls_
- [[nodes/ggml_nelements]] _calls_
- [[nodes/parallel_for]] _calls_

## Used By

- [[nodes/ggml_sycl_fill]] _calls_
