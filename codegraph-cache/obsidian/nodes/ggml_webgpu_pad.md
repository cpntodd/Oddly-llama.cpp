---
name: "ggml_webgpu_pad"
type: "function"
file: "ggml/src/ggml-webgpu/ggml-webgpu.cpp"
community: "ggml"
---

# ggml_webgpu_pad

**Type:** `function`  **File:** `ggml/src/ggml-webgpu/ggml-webgpu.cpp`

**Community:** [[communities/ggml]]

## Depends On

- [[nodes/get_pad_pipeline]] _calls_
- [[nodes/ggml_nelements]] _calls_
- [[nodes/ggml_webgpu_tensor_misalignment]] _calls_
- [[nodes/ggml_type_size]] _calls_
- [[nodes/ggml_get_op_params_i32]] _calls_
- [[nodes/get_solve_tri_pipeline]] _calls_
- [[nodes/get_conv2d_pipeline]] _calls_
- [[nodes/compute_2d_workgroups]] _calls_
- [[nodes/ggml_is_contiguous]] _calls_
- [[nodes/get_conv2d_dw_pipeline]] _calls_
- [[nodes/get_im2col_pipeline]] _calls_
- [[nodes/get_ssm_conv_pipeline]] _calls_
- [[nodes/ggml_webgpu_tensor_buf]] _calls_
- [[nodes/get_gated_delta_net_pipeline]] _calls_
- [[nodes/ggml_is_empty]] _calls_
- [[nodes/get_set_rows_pipeline]] _calls_
- [[nodes/ggml_is_quantized]] _calls_
- [[nodes/ggml_blck_size]] _calls_
- [[nodes/get_get_rows_pipeline]] _calls_
- [[nodes/get_quantize_q8_pipeline]] _calls_
- [[nodes/ggml_webgpu_tensor_offset]] _calls_
- [[nodes/ggml_nbytes]] _calls_
- [[nodes/get_mul_mat_vec_pipeline]] _calls_
- [[nodes/get_mul_mat_fast_pipeline]] _calls_
- [[nodes/get_mul_mat_id_vec_pipeline]] _calls_
- [[nodes/ggml_webgpu_tensor_align_offset]] _calls_
- [[nodes/ggml_webgpu_tensor_binding_size]] _calls_
- [[nodes/get_mul_mat_id_gather_pipeline]] _calls_
- [[nodes/get_mul_mat_id_pipeline]] _calls_
- [[nodes/ggml_webgpu_flash_attn_float_vec4_aligned]] _calls_

## Used By

- [[nodes/ggml_webgpu_upscale]] _calls_
