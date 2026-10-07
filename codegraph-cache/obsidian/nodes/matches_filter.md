---
name: "matches_filter"
type: "function"
file: "tests/test-backend-ops.cpp"
community: "ggml"
---

# matches_filter

**Type:** `function`  **File:** `tests/test-backend-ops.cpp`

**Community:** [[communities/ggml]]

## Depends On

- [[nodes/op_desc]] _calls_
- [[nodes/vars]] _calls_
- [[nodes/ggml_tensor_overhead]] _calls_
- [[nodes/ggml_graph_overhead]] _calls_
- [[nodes/use_weight_context]] _calls_
- [[nodes/ggml_init]] _calls_
- [[nodes/ggml_new_graph]] _calls_
- [[nodes/add_sentinel]] _calls_
- [[nodes/check_for_f16_tensor]] _calls_
- [[nodes/ggml_get_first_tensor]] _calls_
- [[nodes/ggml_get_next_tensor]] _calls_
- [[nodes/ggml_backend_supports_op]] _calls_
- [[nodes/string]] _calls_
- [[nodes/print_test_result_locked]] _calls_
- [[nodes/ggml_backend_alloc_ctx_tensors]] _calls_
- [[nodes/ggml_backend_buffer_set_usage]] _calls_
- [[nodes/buf]] _calls_
- [[nodes/ggml_build_forward_expand]] _calls_
- [[nodes/ggml_graph_add_node]] _calls_
- [[nodes/initialize_tensors]] _calls_
- [[nodes/ggml_nbytes]] _calls_
- [[nodes/ggml_backend_tensor_get]] _calls_
- [[nodes/data]] _calls_
- [[nodes/ggml_op_desc]] _calls_
- [[nodes/isinf_or_max]] _calls_
- [[nodes/signbit]] _calls_
- [[nodes/err]] _calls_
- [[nodes/max_err]] _calls_
- [[nodes/run_whole_graph]] _calls_
- [[nodes/ggml_backend_compare_graph_backend]] _calls_

## Used By

- [[nodes/eval_perf]] _calls_
- [[nodes/eval_support]] _calls_
- [[nodes/eval_grad]] _calls_
