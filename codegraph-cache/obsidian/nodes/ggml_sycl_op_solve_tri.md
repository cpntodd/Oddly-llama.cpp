---
name: "ggml_sycl_op_solve_tri"
type: "function"
file: "ggml/src/ggml-sycl/solve_tri.cpp"
community: "ggml"
---

# ggml_sycl_op_solve_tri

**Type:** `function`  **File:** `ggml/src/ggml-sycl/solve_tri.cpp`

**Community:** [[communities/ggml]]

## Depends On

- [[nodes/solve_tri.comp.cpp]] _imports_
- [[nodes/KeyValuePair]] _imports_
- [[nodes/ggml_is_contiguous]] _calls_
- [[nodes/stream]] _calls_
- [[nodes/block]] _calls_
- [[nodes/parallel_for]] _calls_

## Used By

- [[nodes/ggml_sycl_solve_tri]] _calls_
