---
name: "llama_model_saver_supports_arch"
type: "function"
file: "src/llama-model-saver.cpp"
community: "src"
---

# llama_model_saver_supports_arch

**Type:** `function`  **File:** `src/llama-model-saver.cpp`

**Community:** [[communities/src]]

## Depends On

- [[nodes/ggml_graph_next_uid]] _imports_
- [[nodes/gguf.py]] _imports_
- [[nodes/llm_arch]] _imports_
- [[nodes/llama_update]] _imports_
- [[nodes/llama-hparams.cpp]] _imports_
- [[nodes/llama_meta_device_get_split_state]] _imports_
- [[nodes/llama_vocab_pre_type]] _imports_
- [[nodes/jinja]] _imports_
- [[nodes/llama_model_saver]] _calls_
- [[nodes/gguf_free]] _calls_
- [[nodes/gguf_set_val_u32]] _calls_
- [[nodes/gguf_set_val_i32]] _calls_
- [[nodes/gguf_set_val_f32]] _calls_
- [[nodes/gguf_set_val_bool]] _calls_
- [[nodes/gguf_set_val_str]] _calls_
- [[nodes/size]] _calls_
- [[nodes/gguf_set_arr_data]] _calls_
- [[nodes/gguf_set_arr_str]] _calls_
- [[nodes/gguf_find_tensor]] _calls_
- [[nodes/tokens]] _calls_
- [[nodes/llama_rope_scaling_type_name]] _calls_
- [[nodes/string]] _calls_
- [[nodes/gguf_write_to_file]] _calls_
- [[nodes/gguf_write_to_file_ptr]] _calls_

## Used By

- [[nodes/llama_flash_attn_type]] _imports_
- [[nodes/nmse]] _imports_
- [[nodes/llm_arch_all]] _calls_
- [[nodes/test_backends]] _calls_
- [[nodes/set_tensor_data]] _imports_
