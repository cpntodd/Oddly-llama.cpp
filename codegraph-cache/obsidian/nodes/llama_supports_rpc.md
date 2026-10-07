---
name: "llama_supports_rpc"
type: "function"
file: "src/llama.cpp"
community: "ggml"
---

# llama_supports_rpc

**Type:** `function`  **File:** `src/llama.cpp`

**Community:** [[communities/ggml]]

## Depends On

- [[nodes/ggml_backend_reg_count]] _calls_
- [[nodes/ggml_backend_load_all]] _calls_
- [[nodes/ggml_backend_reg_by_name]] _calls_

## Used By

- [[nodes/print_usage]] _calls_
- [[nodes/parse_cmd_params]] _calls_
- [[nodes/llama_supports_gpu_offload]] _calls_
- [[nodes/common_params_parser_init]] _calls_
