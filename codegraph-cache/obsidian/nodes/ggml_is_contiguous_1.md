---
name: "ggml_is_contiguous_1"
type: "function"
file: "ggml/src/ggml.c"
community: "ggml"
---

# ggml_is_contiguous_1

**Type:** `function`  **File:** `ggml/src/ggml.c`

**Community:** [[communities/ggml]]

## Depends On

- [[nodes/ggml_is_contiguous_m_n]] _calls_

## Used By

- [[nodes/ggml_get_tensor]] _calls_
- [[nodes/apply_unary_op_functor]] _calls_
- [[nodes/ggml_compute_forward_tri]] _calls_
- [[nodes/dispatch_ggml_sycl_op_fused_glu]] _calls_
- [[nodes/ggml_sycl_op_unary_mul_fused]] _calls_
- [[nodes/ggml_sycl_op_swiglu_oai]] _calls_
- [[nodes/ggml_metal_library_get_pipeline_glu]] _calls_
- [[nodes/ggml_metal_library_get_pipeline_argmax]] _calls_
- [[nodes/ggml_backend_et_device_supports_op]] _calls_
- [[nodes/ggml_hexagon_supported_activations]] _calls_
- [[nodes/do_ggml_backend_sycl_device_supports_op]] _calls_
