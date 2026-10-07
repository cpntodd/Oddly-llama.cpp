---
name: "metadata"
type: "function"
file: "src/llama-model-loader.cpp"
community: "ggml"
---

# metadata

**Type:** `function`  **File:** `src/llama-model-loader.cpp`

**Community:** [[communities/ggml]]

## Depends On

- [[nodes/getenv]] _calls_
- [[nodes/insert]] _calls_
- [[nodes/empty]] _calls_
- [[nodes/format]] _calls_
- [[nodes/llm_kv]] _calls_
- [[nodes/llm_arch_from_string]] _calls_
- [[nodes/ggml_get_first_tensor]] _calls_
- [[nodes/ggml_get_next_tensor]] _calls_
- [[nodes/ggml_get_name]] _calls_
- [[nodes/ggml_nelements]] _calls_
- [[nodes/ggml_nbytes]] _calls_
- [[nodes/size]] _calls_
- [[nodes/gguf_find_key]] _calls_
- [[nodes/gguf_get_val_u16]] _calls_
- [[nodes/gguf_get_n_kv]] _calls_
- [[nodes/gguf_get_version]] _calls_
- [[nodes/ggml_type_name]] _calls_
- [[nodes/llama_format_tensor_shape]] _calls_
- [[nodes/gguf_get_kv_type]] _calls_
- [[nodes/gguf_get_arr_type]] _calls_
- [[nodes/gguf_get_arr_n]] _calls_
- [[nodes/gguf_kv_to_str]] _calls_
- [[nodes/replace_all]] _calls_

## Used By

- [[nodes/server_state_from_str]] _calls_
- [[nodes/makeCircle]] _calls_
- [[nodes/makeCircle]] _calls_
- [[nodes/llama_model_quantize_impl]] _calls_
- [[nodes/llama_quant_free]] _calls_
- [[nodes/main]] _calls_
- [[nodes/makeCircle]] _calls_
- [[nodes/ggml_cann_rope_cache_preload]] _calls_
- [[nodes/makeCircle]] _calls_
