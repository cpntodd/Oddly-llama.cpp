---
name: "common_print_available_devices"
type: "function"
file: "common/arg.cpp"
community: "ggml"
---

# common_print_available_devices

**Type:** `function`  **File:** `common/arg.cpp`

**Community:** [[communities/ggml]]

## Depends On

- [[nodes/ggml_backend_load_all]] _calls_
- [[nodes/ggml_backend_dev_count]] _calls_
- [[nodes/ggml_backend_dev_get]] _calls_
- [[nodes/ggml_backend_dev_type]] _calls_
- [[nodes/push_back]] _calls_
- [[nodes/empty]] _calls_
- [[nodes/ggml_backend_dev_memory]] _calls_

## Used By

- [[nodes/parse_cmd_params]] _calls_
- [[nodes/common_params_parser_init]] _calls_
