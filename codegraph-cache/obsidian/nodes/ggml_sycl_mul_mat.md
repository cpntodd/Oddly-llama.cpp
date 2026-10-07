---
name: "ggml_sycl_mul_mat"
type: "function"
file: "ggml/src/ggml-sycl/ggml-sycl.cpp"
community: "ggml"
---

# ggml_sycl_mul_mat

**Type:** `function`  **File:** `ggml/src/ggml-sycl/ggml-sycl.cpp`

**Community:** [[communities/ggml]]

## Depends On

- [[nodes/ggml_sycl_t2_restore_tensor]] _calls_
- [[nodes/ggml_get_op_params_i32]] _calls_
- [[nodes/ggml_sycl_op_fwht]] _calls_
- [[nodes/ggml_backend_buffer_is_sycl_split]] _calls_
- [[nodes/can_use_dequantize_mul_mat_vec]] _calls_
- [[nodes/can_use_mul_mat_vec_q]] _calls_
- [[nodes/ggml_sycl_supports_mmq]] _calls_
- [[nodes/should_reorder_tensor]] _calls_
- [[nodes/ggml_sycl_supports_reorder_mmvq]] _calls_
- [[nodes/ggml_sycl_supports_reorder_esimd]] _calls_
- [[nodes/ggml_is_permuted]] _calls_
- [[nodes/ggml_is_contiguous]] _calls_
- [[nodes/ggml_is_transposed]] _calls_

## Used By

- [[nodes/ggml_sycl_mul_mat_glu_mmvq_fused]] _calls_
- [[nodes/ggml_sycl_argmax]] _calls_
- [[nodes/check_graph_compatibility]] _calls_
