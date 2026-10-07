---
name: "llama_adapter_lora_init_impl"
type: "function"
file: "src/llama-adapter.cpp"
community: "ggml"
---

# llama_adapter_lora_init_impl

**Type:** `function`  **File:** `src/llama-adapter.cpp`

**Community:** [[communities/ggml]]

## Depends On

- [[nodes/no_init]] _imports_
- [[nodes/llama_format_win_err]] _imports_
- [[nodes/llama_meta_device_get_split_state]] _imports_
- [[nodes/map]] _imports_
- [[nodes/gguf_get_n_kv]] _calls_
- [[nodes/gguf_get_kv_type]] _calls_
- [[nodes/format]] _calls_
- [[nodes/gguf_get_arr_type]] _calls_
- [[nodes/gguf_get_arr_n]] _calls_
- [[nodes/gguf_kv_to_str]] _calls_
- [[nodes/size]] _calls_
- [[nodes/replace_all]] _calls_
- [[nodes/gguf_find_key]] _calls_
- [[nodes/gguf_get_val_f32]] _calls_
- [[nodes/get_kv_str]] _calls_
- [[nodes/llm_arch_from_string]] _calls_
- [[nodes/get_kv_f32]] _calls_
- [[nodes/gguf_get_n_tensors]] _calls_
- [[nodes/ggml_tensor_overhead]] _calls_
- [[nodes/ggml_init]] _calls_
- [[nodes/ggml_get_first_tensor]] _calls_
- [[nodes/ggml_get_next_tensor]] _calls_
- [[nodes/name]] _calls_
- [[nodes/llama_adapter_lora_weight]] _calls_
- [[nodes/ggml_backend_dev_by_type]] _calls_
- [[nodes/ggml_backend_dev_backend_reg]] _calls_
- [[nodes/ggml_backend_buffer_get_type]] _calls_
- [[nodes/types]] _calls_
- [[nodes/ggml_backend_dev_buffer_type]] _calls_
- [[nodes/ggml_dup_tensor]] _calls_

## Used By

- [[nodes/llama_model]] _imports_
- [[nodes/ggml_cgraph]] _imports_
