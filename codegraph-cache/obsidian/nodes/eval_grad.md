---
name: "eval_grad"
type: "function"
file: "tests/test-backend-ops.cpp"
community: "ggml"
---

# eval_grad

**Type:** `function`  **File:** `tests/test-backend-ops.cpp`

**Community:** [[communities/ggml]]

## Depends On

- [[nodes/ggml_tensor_overhead]] _calls_
- [[nodes/ggml_graph_overhead_custom]] _calls_
- [[nodes/ggml_init]] _calls_
- [[nodes/ggml_new_graph_custom]] _calls_
- [[nodes/matches_filter]] _calls_
- [[nodes/print_operation]] _calls_
- [[nodes/test_operation_info]] _calls_
- [[nodes/op_desc]] _calls_
- [[nodes/vars]] _calls_
- [[nodes/string]] _calls_
- [[nodes/ggml_get_first_tensor]] _calls_
- [[nodes/ggml_get_next_tensor]] _calls_
- [[nodes/ggml_backend_supports_op]] _calls_
- [[nodes/ggml_nelements]] _calls_
- [[nodes/grad_nmax]] _calls_
- [[nodes/info]] _calls_
- [[nodes/set_large_tensor_skip]] _calls_
- [[nodes/ggml_is_scalar]] _calls_
- [[nodes/ggml_set_name]] _calls_
- [[nodes/ggml_set_loss]] _calls_
- [[nodes/ggml_build_forward_expand]] _calls_
- [[nodes/ggml_graph_cpy]] _calls_
- [[nodes/ggml_graph_n_nodes]] _calls_
- [[nodes/ggml_graph_get_grad]] _calls_
- [[nodes/buf]] _calls_
- [[nodes/ggml_backend_alloc_ctx_tensors]] _calls_
- [[nodes/set_error]] _calls_
- [[nodes/initialize_tensors]] _calls_
- [[nodes/tensors]] _calls_
- [[nodes/ggml_graph_reset]] _calls_

## Used By

- [[nodes/run_fa_vec_slice]] _calls_
