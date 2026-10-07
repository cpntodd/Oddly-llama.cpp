---
name: "ggml_webgpu_scale"
type: "function"
file: "ggml/src/ggml-webgpu/ggml-webgpu.cpp"
community: "ggml"
---

# ggml_webgpu_scale

**Type:** `function`  **File:** `ggml/src/ggml-webgpu/ggml-webgpu.cpp`

**Community:** [[communities/ggml]]

## Depends On

- [[nodes/get_scale_pipeline]] _calls_
- [[nodes/ggml_webgpu_tensor_misalignment]] _calls_
- [[nodes/ggml_type_size]] _calls_
- [[nodes/ggml_nelements]] _calls_
- [[nodes/ggml_webgpu_u32_from_f32]] _calls_
- [[nodes/ggml_get_op_params_f32]] _calls_
- [[nodes/compute_2d_workgroups]] _calls_
- [[nodes/get_soft_max_pipeline]] _calls_
- [[nodes/ggml_webgpu_tensor_buf]] _calls_
- [[nodes/ggml_webgpu_tensor_align_offset]] _calls_
- [[nodes/ggml_webgpu_tensor_binding_size]] _calls_
- [[nodes/ggml_nrows]] _calls_

## Used By

- [[nodes/ggml_webgpu_upscale]] _calls_
