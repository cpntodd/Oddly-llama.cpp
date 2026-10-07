---
name: "all_finite"
type: "function"
file: "tools/imatrix/imatrix.cpp"
community: "ggml"
---

# all_finite

**Type:** `function`  **File:** `tools/imatrix/imatrix.cpp`

**Community:** [[communities/ggml]]

## Depends On

- [[nodes/filter_tensor_name]] _calls_
- [[nodes/ggml_backend_buffer_is_host]] _calls_
- [[nodes/ggml_nbytes]] _calls_
- [[nodes/ggml_backend_tensor_get]] _calls_
- [[nodes/ggml_element_size]] _calls_
- [[nodes/ggml_nrows]] _calls_
- [[nodes/to_string]] _calls_
- [[nodes/out]] _calls_
- [[nodes/write]] _calls_
- [[nodes/string_ends_with]] _calls_
- [[nodes/ggml_tensor_overhead]] _calls_
- [[nodes/ggml_init]] _calls_
- [[nodes/gguf_set_val_str]] _calls_
- [[nodes/gguf_set_arr_str]] _calls_
- [[nodes/gguf_set_val_u32]] _calls_
- [[nodes/ggml_format_name]] _calls_
- [[nodes/gguf_write_to_file]] _calls_
- [[nodes/gguf_free]] _calls_
- [[nodes/ggml_free]] _calls_
- [[nodes/load_imatrix]] _calls_
- [[nodes/common_imatrix_load]] _calls_

## Used By

- [[nodes/if]] _calls_
