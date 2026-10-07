---
name: "set_tensor_data"
type: "function"
file: "tests/test-kv-mean-center.cpp"
community: "src"
---

# set_tensor_data

**Type:** `function`  **File:** `tests/test-kv-mean-center.cpp`

**Community:** [[communities/src]]

## Depends On

- [[nodes/KeyValuePair]] _imports_
- [[nodes/kv_mean_collector]] _imports_
- [[nodes/log.comp.cpp]] _imports_
- [[nodes/llama_update]] _imports_
- [[nodes/llama_model_deleter]] _imports_
- [[nodes/quantize_state_impl]] _imports_
- [[nodes/llm_arch]] _imports_
- [[nodes/llama_cparams]] _imports_
- [[nodes/llama_model_saver_supports_arch]] _imports_
- [[nodes/jinja]] _imports_
- [[nodes/hasher]] _calls_
- [[nodes/ggml_nelements]] _calls_
- [[nodes/ggml_backend_tensor_set]] _calls_
- [[nodes/data]] _calls_
- [[nodes/ggml_nbytes]] _calls_
