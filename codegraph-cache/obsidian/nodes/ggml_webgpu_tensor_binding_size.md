---
name: "ggml_webgpu_tensor_binding_size"
type: "function"
file: "ggml/src/ggml-webgpu/ggml-webgpu.cpp"
community: "ggml"
---

# ggml_webgpu_tensor_binding_size

**Type:** `function`  **File:** `ggml/src/ggml-webgpu/ggml-webgpu.cpp`

**Community:** [[communities/ggml]]

## Depends On

- [[nodes/ggml_nbytes]] _calls_
- [[nodes/ggml_webgpu_tensor_misalignment]] _calls_
- [[nodes/ggml_webgpu_tensor_align_offset]] _calls_
- [[nodes/ggml_webgpu_tensor_offset]] _calls_
- [[nodes/ggml_type_size]] _calls_
- [[nodes/ggml_webgpu_tensor_buf]] _calls_

## Used By

- [[nodes/ggml_webgpu_pad]] _calls_
- [[nodes/ggml_webgpu_flash_attn_direct]] _calls_
- [[nodes/ggml_webgpu_unary_op]] _calls_
- [[nodes/ggml_webgpu_scale]] _calls_
