---
name: "llama_supports_gpu_offload"
type: "function"
file: "src/llama.cpp"
community: "ggml"
---

# llama_supports_gpu_offload

**Type:** `function`  **File:** `src/llama.cpp`

**Community:** [[communities/ggml]]

## Depends On

- [[nodes/ggml_backend_reg_count]] _calls_
- [[nodes/ggml_backend_load_all]] _calls_
- [[nodes/ggml_backend_dev_by_type]] _calls_
- [[nodes/llama_supports_rpc]] _calls_

## Used By

- [[nodes/params]] _calls_
- [[nodes/common_params_parser_init]] _calls_
