---
name: "ggml_wrap_around"
type: "function"
file: "ggml/src/ggml-cpu/ops.cpp"
community: "ggml"
---

# ggml_wrap_around

**Type:** `function`  **File:** `ggml/src/ggml-cpu/ops.cpp`

**Community:** [[communities/ggml]]

## Depends On

- [[nodes/ggml_is_contiguous]] _calls_
- [[nodes/all]] _calls_
- [[nodes/ggml_get_type_traits]] _calls_
- [[nodes/ggml_barrier]] _calls_
- [[nodes/ggml_type_size]] _calls_
- [[nodes/ggml_nbytes]] _calls_
- [[nodes/ggml_get_op_params_i32]] _calls_
- [[nodes/ggml_vec_dot_f16]] _calls_
- [[nodes/ggml_vec_dot_f32]] _calls_

## Used By

- [[nodes/ggml_conv_2d_dw_knl_f32]] _calls_
