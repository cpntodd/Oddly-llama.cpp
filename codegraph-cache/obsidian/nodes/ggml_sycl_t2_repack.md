---
name: "ggml_sycl_t2_repack"
type: "function"
file: "ggml/src/ggml-sycl/ptq1-t2.cpp"
community: "ggml"
---

# ggml_sycl_t2_repack

**Type:** `function`  **File:** `ggml/src/ggml-sycl/ptq1-t2.cpp`

**Community:** [[communities/ggml]]

## Depends On

- [[nodes/parallel_for]] _calls_
- [[nodes/store]] _calls_
- [[nodes/getenv]] _calls_
- [[nodes/t2_s32]] _calls_

## Used By

- [[nodes/main]] _calls_
- [[nodes/ggml_sycl_t2_tensor]] _calls_
