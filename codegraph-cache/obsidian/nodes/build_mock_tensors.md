---
name: "build_mock_tensors"
type: "function"
file: "tests/test-quant-type-selection.cpp"
community: "ggml"
---

# build_mock_tensors

**Type:** `function`  **File:** `tests/test-quant-type-selection.cpp`

**Community:** [[communities/ggml]]

## Depends On

- [[nodes/ggml_tensor_overhead]] _calls_
- [[nodes/ggml_init]] _calls_
- [[nodes/ggml_set_name]] _calls_
- [[nodes/llama_ftype_get_default_type]] _calls_
- [[nodes/data]] _calls_
- [[nodes/ggml_type_name]] _calls_
- [[nodes/ggml_get_name]] _calls_

## Used By

- [[nodes/run_generate]] _calls_
- [[nodes/run_remote_tests]] _calls_
