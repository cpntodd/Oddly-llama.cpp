---
name: "run_remote_tests"
type: "function"
file: "tests/test-quant-type-selection.cpp"
community: "ggml"
---

# run_remote_tests

**Type:** `function`  **File:** `tests/test-quant-type-selection.cpp`

**Community:** [[communities/ggml]]

## Depends On

- [[nodes/model_name_from_repo]] _calls_
- [[nodes/value]] _calls_
- [[nodes/llama_model_quantize_default_params]] _calls_
- [[nodes/build_mock_tensors]] _calls_
- [[nodes/snapshot_file_from_name]] _calls_
- [[nodes/parse_snapshot_file]] _calls_
- [[nodes/llama_quant_free]] _calls_
- [[nodes/llama_model_free]] _calls_
- [[nodes/run_test_section]] _calls_

## Used By

- [[nodes/main]] _calls_
