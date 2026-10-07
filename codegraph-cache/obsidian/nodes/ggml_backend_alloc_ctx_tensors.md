---
name: "ggml_backend_alloc_ctx_tensors"
type: "function"
file: "ggml/src/ggml-alloc.c"
community: "ggml"
---

# ggml_backend_alloc_ctx_tensors

**Type:** `function`  **File:** `ggml/src/ggml-alloc.c`

**Community:** [[communities/ggml]]

## Depends On

- [[nodes/ggml_backend_alloc_ctx_tensors_from_buft]] _calls_
- [[nodes/ggml_backend_get_default_buffer_type]] _calls_

## Used By

- [[nodes/merge_tensor]] _calls_
- [[nodes/print_debug_tensor]] _calls_
- [[nodes/get_random_gguf_context]] _calls_
- [[nodes/helper_get_test_opt_pars]] _calls_
- [[nodes/helper_get_regression_opt_pars]] _calls_
- [[nodes/ggml_backend_graph_copy]] _calls_
- [[nodes/ggml_opt_build]] _calls_
- [[nodes/if]] _calls_
- [[nodes/matches_filter]] _calls_
- [[nodes/eval_perf]] _calls_
- [[nodes/eval_grad]] _calls_
