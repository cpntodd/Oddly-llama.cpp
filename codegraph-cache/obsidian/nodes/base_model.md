---
name: "base_model"
type: "function"
file: "tools/export-lora/export-lora.cpp"
community: "ggml"
---

# base_model

**Type:** `function`  **File:** `tools/export-lora/export-lora.cpp`

**Community:** [[communities/ggml]]

## Depends On

- [[nodes/gguf_find_key]] _calls_
- [[nodes/file_input]] _calls_
- [[nodes/check_metadata_lora]] _calls_
- [[nodes/gguf_get_n_tensors]] _calls_
- [[nodes/ggml_tensor_overhead]] _calls_
- [[nodes/ggml_init]] _calls_
- [[nodes/ggml_backend_cpu_init]] _calls_
- [[nodes/ggml_gallocr_new]] _calls_
- [[nodes/ggml_backend_get_default_buffer_type]] _calls_
