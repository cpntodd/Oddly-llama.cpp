---
name: "ggml_webgpu_flash_attn_direct"
type: "function"
file: "ggml/src/ggml-webgpu/ggml-webgpu.cpp"
community: "ggml"
---

# ggml_webgpu_flash_attn_direct

**Type:** `function`  **File:** `ggml/src/ggml-webgpu/ggml-webgpu.cpp`

**Community:** [[communities/ggml]]

## Depends On

- [[nodes/get_flash_attn_pipeline]] _calls_
- [[nodes/get_flash_attn_vec_pipeline]] _calls_
- [[nodes/ggml_webgpu_flash_attn_vec_nwg]] _calls_
- [[nodes/ggml_webgpu_tensor_offset]] _calls_
- [[nodes/ggml_nbytes]] _calls_
- [[nodes/ggml_webgpu_tensor_buf]] _calls_
- [[nodes/ggml_type_size]] _calls_
- [[nodes/get_flash_attn_blk_pipeline]] _calls_
- [[nodes/ggml_webgpu_tensor_misalignment]] _calls_
- [[nodes/ggml_webgpu_tensor_align_offset]] _calls_
- [[nodes/ggml_webgpu_tensor_binding_size]] _calls_
- [[nodes/get_flash_attn_vec_reduce_pipeline]] _calls_
