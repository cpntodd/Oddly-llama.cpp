---
name: "ggml_compute_forward_tri"
type: "function"
file: "ggml/src/ggml-cpu/ops.cpp"
community: "ggml"
---

# ggml_compute_forward_tri

**Type:** `function`  **File:** `ggml/src/ggml-cpu/ops.cpp`

**Community:** [[communities/ggml]]

## Depends On

- [[nodes/ggml_compute_forward_tri_f32]] _calls_
- [[nodes/ggml_is_contiguous_rows]] _calls_
- [[nodes/ggml_are_same_shape]] _calls_
- [[nodes/ggml_nrows]] _calls_
- [[nodes/ggml_vec_gelu_erf_f32]] _calls_
- [[nodes/ggml_vec_gelu_erf_f16]] _calls_
- [[nodes/ggml_vec_gelu_quick_f32]] _calls_
- [[nodes/ggml_vec_gelu_quick_f16]] _calls_
- [[nodes/ggml_vec_silu_f32]] _calls_
- [[nodes/ggml_vec_silu_f16]] _calls_
- [[nodes/ggml_is_contiguous_1]] _calls_
- [[nodes/ggml_vec_leaky_relu_f32]] _calls_
- [[nodes/ggml_vec_leaky_relu_f16]] _calls_
- [[nodes/ggml_vec_silu_backward_f32]] _calls_
- [[nodes/ggml_vec_silu_backward_f16]] _calls_
- [[nodes/ggml_get_op_params_i32]] _calls_
- [[nodes/ggml_vec_reglu_f32]] _calls_
- [[nodes/ggml_vec_reglu_f16]] _calls_
- [[nodes/ggml_vec_geglu_f32]] _calls_
- [[nodes/ggml_vec_geglu_f16]] _calls_
- [[nodes/ggml_vec_swiglu_f32]] _calls_
- [[nodes/ggml_vec_swiglu_f16]] _calls_
- [[nodes/ggml_get_op_params_f32]] _calls_
- [[nodes/ggml_vec_geglu_erf_f32]] _calls_
- [[nodes/ggml_vec_geglu_erf_f16]] _calls_
- [[nodes/ggml_vec_geglu_quick_f32]] _calls_
- [[nodes/ggml_vec_geglu_quick_f16]] _calls_
- [[nodes/ggml_vec_sum_f32]] _calls_
- [[nodes/ggml_vec_cvar_f32]] _calls_
- [[nodes/ggml_vec_scale_f32]] _calls_

## Used By

- [[nodes/ggml_compute_forward]] _calls_
