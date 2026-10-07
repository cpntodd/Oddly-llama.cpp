---
name: "common_memory_breakdown_print"
type: "function"
file: "common/fit.cpp"
community: "ggml"
---

# common_memory_breakdown_print

**Type:** `function`  **File:** `common/fit.cpp`

**Community:** [[communities/ggml]]

## Depends On

- [[nodes/llama_model_n_devices]] _calls_
- [[nodes/push_back]] _calls_
- [[nodes/llama_model_get_device]] _calls_
- [[nodes/llama_get_memory_breakdown]] _calls_
- [[nodes/size]] _calls_
- [[nodes/ggml_backend_buft_is_host]] _calls_
- [[nodes/insert]] _calls_
- [[nodes/ggml_backend_buft_get_device]] _calls_
- [[nodes/ggml_backend_dev_memory]] _calls_

## Used By

- [[nodes/llama_perplexity]] _calls_
- [[nodes/llama_server]] _calls_
- [[nodes/common_perf_print]] _calls_
