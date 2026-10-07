---
name: "ggml_backend_sycl_graph_compute_impl"
type: "function"
file: "ggml/src/ggml-sycl/ggml-sycl.cpp"
community: "ggml"
---

# ggml_backend_sycl_graph_compute_impl

**Type:** `function`  **File:** `ggml/src/ggml-sycl/ggml-sycl.cpp`

**Community:** [[communities/ggml]]

## Depends On

- [[nodes/ggml_sycl_is_view_or_noop]] _calls_
- [[nodes/ggml_sycl_fuse]] _calls_
- [[nodes/ggml_backend_sycl_buffer_type]] _calls_
- [[nodes/ggml_sycl_ssm_conv_fused]] _calls_
- [[nodes/ggml_sycl_op_rms_norm_fused]] _calls_
- [[nodes/ggml_get_unary_op]] _calls_
- [[nodes/ggml_sycl_op_unary_mul_fused]] _calls_
- [[nodes/ggml_sycl_mul_mat_glu_mmvq_fused]] _calls_
- [[nodes/ggml_op_name]] _calls_

## Used By

- [[nodes/ggml_backend_sycl_graph_compute]] _calls_
