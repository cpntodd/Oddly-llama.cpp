---
name: "tensor_is_contiguous"
type: "function"
file: "tests/test-quantize-stats.cpp"
community: "ggml"
---

# tensor_is_contiguous

**Type:** `function`  **File:** `tests/test-quantize-stats.cpp`

**Community:** [[communities/ggml]]

## Depends On

- [[nodes/ggml_type_size]] _calls_
- [[nodes/ggml_blck_size]] _calls_
- [[nodes/ggml_get_f32_1d]] _calls_
- [[nodes/ggml_get_data_f32]] _calls_
- [[nodes/update_error_stats]] _calls_
- [[nodes/ggml_nelements]] _calls_
- [[nodes/data]] _calls_
- [[nodes/combine_error_stats]] _calls_
- [[nodes/compute]] _calls_
- [[nodes/print_error_stats]] _calls_
