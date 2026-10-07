---
name: "load_tensors"
type: "function"
file: "tools/mtmd/clip.cpp"
community: "ggml"
---

# load_tensors

**Type:** `function`  **File:** `tools/mtmd/clip.cpp`

**Community:** [[communities/ggml]]

## Depends On

- [[nodes/string_format]] _calls_
- [[nodes/gguf_get_n_tensors]] _calls_
- [[nodes/gguf_get_data_offset]] _calls_
- [[nodes/gguf_get_tensor_offset]] _calls_
- [[nodes/ggml_tensor_overhead]] _calls_
- [[nodes/ggml_init]] _calls_
- [[nodes/ggml_get_tensor]] _calls_
- [[nodes/ggml_dup_tensor]] _calls_
- [[nodes/ggml_set_name]] _calls_
- [[nodes/ggml_backend_get_device]] _calls_
- [[nodes/ggml_nbytes]] _calls_
- [[nodes/gguf_find_tensor]] _calls_
- [[nodes/gguf_get_tensor_type]] _calls_
- [[nodes/ggml_type_name]] _calls_
- [[nodes/gguf_get_tensor_size]] _calls_
- [[nodes/read]] _calls_
- [[nodes/string_ends_with]] _calls_
- [[nodes/string_replace_all]] _calls_
- [[nodes/entry]] _calls_
- [[nodes/ggml_backend_get_default_buffer_type]] _calls_
- [[nodes/ggml_backend_alloc_ctx_tensors_from_buft]] _calls_
- [[nodes/ggml_backend_buffer_set_usage]] _calls_
- [[nodes/ggml_backend_buft_is_host]] _calls_
- [[nodes/ggml_backend_tensor_set]] _calls_

## Used By

- [[nodes/clip_init]] _calls_
- [[nodes/llama_prepare_model_devices]] _calls_
- [[nodes/params]] _calls_
