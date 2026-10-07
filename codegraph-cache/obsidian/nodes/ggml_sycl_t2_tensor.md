---
name: "ggml_sycl_t2_tensor"
type: "function"
file: "ggml/src/ggml-sycl/ggml-sycl.cpp"
community: "ggml"
---

# ggml_sycl_t2_tensor

**Type:** `function`  **File:** `ggml/src/ggml-sycl/ggml-sycl.cpp`

**Community:** [[communities/ggml]]

## Depends On

- [[nodes/ggml_backend_buffer_is_sycl]] _calls_
- [[nodes/ggml_is_contiguous]] _calls_
- [[nodes/ggml_sycl_t2_wants]] _calls_
- [[nodes/ggml_sycl_t2_restore_tensor]] _calls_
- [[nodes/ggml_sycl_t2_repack]] _calls_
- [[nodes/getenv]] _calls_
- [[nodes/pool]] _calls_
- [[nodes/ggml_sycl_t2_scratch_bytes]] _calls_
- [[nodes/get]] _calls_

## Used By

- [[nodes/ggml_sycl_mul_mat_glu_mmvq_fused]] _calls_
