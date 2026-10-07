---
name: "parse_k_cache_in_layer"
type: "function"
file: "tools/kv-mean-center/kv-mean-center.cpp"
community: "ggml"
---

# parse_k_cache_in_layer

**Type:** `function`  **File:** `tools/kv-mean-center/kv-mean-center.cpp`

**Community:** [[communities/ggml]]

## Depends On

- [[nodes/tensor_has_k_rot_ancestor]] _calls_
- [[nodes/ggml_is_contiguous]] _calls_
- [[nodes/ggml_backend_buffer_is_host]] _calls_
- [[nodes/ggml_nbytes]] _calls_
- [[nodes/ggml_backend_tensor_get]] _calls_
- [[nodes/assign]] _calls_
- [[nodes/ggml_fp16_to_fp32_row]] _calls_
- [[nodes/ggml_bf16_to_fp32_row]] _calls_
