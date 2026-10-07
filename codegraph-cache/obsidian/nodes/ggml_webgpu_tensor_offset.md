---
name: "ggml_webgpu_tensor_offset"
type: "function"
file: "ggml/src/ggml-webgpu/ggml-webgpu.cpp"
community: "ggml"
---

# ggml_webgpu_tensor_offset

**Type:** `function`  **File:** `ggml/src/ggml-webgpu/ggml-webgpu.cpp`

**Community:** [[communities/ggml]]

## Depends On

- [[nodes/webgpu_global_context_struct]] _calls_
- [[nodes/webgpu_context_struct]] _calls_
- [[nodes/ggml_backend_webgpu_buffer_context]] _calls_

## Used By

- [[nodes/ggml_webgpu_tensor_misalignment]] _calls_
- [[nodes/ggml_webgpu_tensor_align_offset]] _calls_
- [[nodes/ggml_webgpu_tensor_binding_size]] _calls_
- [[nodes/ggml_webgpu_pad]] _calls_
- [[nodes/ggml_webgpu_flash_attn_direct]] _calls_
- [[nodes/ggml_webgpu_argsort]] _calls_
- [[nodes/ggml_backend_webgpu_event_wait]] _calls_
- [[nodes/ggml_backend_webgpu_buffer_free_buffer]] _calls_
