---
name: "ggml_sycl_mul_mat_glu_mmvq_fused"
type: "function"
file: "ggml/src/ggml-sycl/ggml-sycl.cpp"
community: "ggml"
---

# ggml_sycl_mul_mat_glu_mmvq_fused

**Type:** `function`  **File:** `ggml/src/ggml-sycl/ggml-sycl.cpp`

**Community:** [[communities/ggml]]

## Depends On

- [[nodes/ggml_sycl_t2_tensor]] _calls_
- [[nodes/ggml_backend_buffer_is_sycl_split]] _calls_
- [[nodes/pool]] _calls_
- [[nodes/get]] _calls_
- [[nodes/ggml_get_glu_op]] _calls_
- [[nodes/ggml_is_contiguous]] _calls_
- [[nodes/opt_for_reorder_id]] _calls_
- [[nodes/assign]] _calls_
- [[nodes/ggml_nbytes]] _calls_
- [[nodes/ggml_sycl_mul_mat]] _calls_
- [[nodes/min]] _calls_
- [[nodes/parallel_for]] _calls_

## Used By

- [[nodes/ggml_backend_sycl_graph_compute_impl]] _calls_
