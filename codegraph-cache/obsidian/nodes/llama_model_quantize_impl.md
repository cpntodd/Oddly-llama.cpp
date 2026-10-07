---
name: "llama_model_quantize_impl"
type: "function"
file: "src/llama-quant.cpp"
community: "ggml"
---

# llama_model_quantize_impl

**Type:** `function`  **File:** `src/llama-quant.cpp`

**Community:** [[communities/ggml]]

## Depends On

- [[nodes/llama_ftype_get_default_type]] _calls_
- [[nodes/format]] _calls_
- [[nodes/llama_model_default_params]] _calls_
- [[nodes/load_hparams]] _calls_
- [[nodes/size]] _calls_
- [[nodes/push_back]] _calls_
- [[nodes/gguf_set_kv]] _calls_
- [[nodes/gguf_set_val_u32]] _calls_
- [[nodes/llm_kv]] _calls_
- [[nodes/gguf_remove_key]] _calls_
- [[nodes/gguf_set_val_f32]] _calls_
- [[nodes/gguf_set_val_bool]] _calls_
- [[nodes/gguf_set_val_str]] _calls_
- [[nodes/remap_layer]] _calls_
- [[nodes/empty]] _calls_
- [[nodes/ggml_set_name]] _calls_
- [[nodes/ggml_get_name]] _calls_
- [[nodes/metadata]] _calls_
- [[nodes/init_quantize_state_counters]] _calls_
- [[nodes/tensor_allows_quantization]] _calls_
- [[nodes/llama_tensor_get_type]] _calls_
- [[nodes/tensor_requires_imatrix]] _calls_
- [[nodes/remap_imatrix]] _calls_
- [[nodes/ggml_type_name]] _calls_
- [[nodes/gguf_set_val_u16]] _calls_
- [[nodes/gguf_set_val_i32]] _calls_
- [[nodes/gguf_get_meta_size]] _calls_
- [[nodes/gguf_get_meta_data]] _calls_
- [[nodes/llama_path_max]] _calls_
- [[nodes/zeros]] _calls_

## Used By

- [[nodes/llama_model_quantize_default_params]] _calls_
