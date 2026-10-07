---
name: "ggml_backend_dev_by_type"
type: "function"
file: "ggml/src/ggml-backend-reg.cpp"
community: "ggml"
---

# ggml_backend_dev_by_type

**Type:** `function`  **File:** `ggml/src/ggml-backend-reg.cpp`

**Community:** [[communities/ggml]]

## Depends On

- [[nodes/ggml_backend_dev_count]] _calls_
- [[nodes/ggml_backend_dev_get]] _calls_

## Used By

- [[nodes/llama_bench]] _calls_
- [[nodes/rpc_server_params_parse]] _calls_
- [[nodes/select_weight_buft]] _calls_
- [[nodes/llama_supports_gpu_offload]] _calls_
- [[nodes/llama_numa_init]] _calls_
- [[nodes/make_cpu_buft_list]] _calls_
- [[nodes/params]] _calls_
- [[nodes/llama_adapter_lora_init_impl]] _calls_
- [[nodes/ggml_threadpool_params_from_cpu_params]] _calls_
- [[nodes/main]] _calls_
- [[nodes/load_model]] _calls_
- [[nodes/if]] _calls_
- [[nodes/ggml_backend_init_by_type]] _calls_
- [[nodes/ggml_backend_init_best]] _calls_
