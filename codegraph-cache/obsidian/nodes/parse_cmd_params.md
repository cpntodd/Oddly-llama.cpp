---
name: "parse_cmd_params"
type: "function"
file: "tools/llama-bench/llama-bench.cpp"
community: "ggml"
---

# parse_cmd_params

**Type:** `function`  **File:** `tools/llama-bench/llama-bench.cpp`

**Community:** [[communities/ggml]]

## Depends On

- [[nodes/getenv]] _calls_
- [[nodes/print_usage]] _calls_
- [[nodes/ggml_type_from_name]] _calls_
- [[nodes/common_print_available_devices]] _calls_
- [[nodes/llama_supports_rpc]] _calls_
- [[nodes/register_rpc_server_list]] _calls_
- [[nodes/value]] _calls_
- [[nodes/llama_max_devices]] _calls_
- [[nodes/ggml_backend_dev_count]] _calls_
- [[nodes/ggml_backend_dev_get]] _calls_
- [[nodes/ggml_backend_dev_buffer_type]] _calls_
- [[nodes/output_format_from_str]] _calls_
- [[nodes/common_models_handler_init]] _calls_
- [[nodes/common_models_handler_apply]] _calls_
- [[nodes/test]] _calls_
- [[nodes/get_cpu_info]] _calls_
- [[nodes/get_gpu_info]] _calls_
- [[nodes/llama_model_desc]] _calls_
- [[nodes/llama_model_size]] _calls_
- [[nodes/llama_model_n_params]] _calls_
- [[nodes/printer]] _calls_

## Used By

- [[nodes/llama_bench]] _calls_
