---
name: "llama_fit_params"
type: "function"
file: "tools/fit-params/fit-params.cpp"
community: "common"
---

# llama_fit_params

**Type:** `function`  **File:** `tools/fit-params/fit-params.cpp`

**Community:** [[communities/common]]

## Depends On

- [[nodes/llama_update]] _imports_
- [[nodes/quantize_state_impl]] _imports_
- [[nodes/common_arg]] _imports_
- [[nodes/KeyValuePair]] _imports_
- [[nodes/common_params_fit_status]] _imports_
- [[nodes/log.comp.cpp]] _imports_
- [[nodes/common_init]] _calls_
- [[nodes/common_params_parse]] _calls_
- [[nodes/llama_backend_init]] _calls_
- [[nodes/llama_numa_init]] _calls_
- [[nodes/common_model_params_to_llama]] _calls_
- [[nodes/common_context_params_to_llama]] _calls_
- [[nodes/common_log_flush]] _calls_
- [[nodes/llama_max_devices]] _calls_
- [[nodes/llama_max_tensor_buft_overrides]] _calls_

## Used By

- [[nodes/main]] _calls_
