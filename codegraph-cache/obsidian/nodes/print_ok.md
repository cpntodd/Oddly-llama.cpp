---
name: "print_ok"
type: "function"
file: "tests/test-opt.cpp"
community: "ggml"
---

# print_ok

**Type:** `function`  **File:** `tests/test-opt.cpp`

**Community:** [[communities/ggml]]

## Depends On

- [[nodes/ggml_opt_dataset_shuffle]] _calls_
- [[nodes/data]] _calls_
- [[nodes/ggml_nelements]] _calls_
- [[nodes/ggml_opt_dataset_get_batch]] _calls_
- [[nodes/ggml_backend_tensor_get]] _calls_
- [[nodes/ggml_nbytes]] _calls_
- [[nodes/helper_free_ctx_data]] _calls_
- [[nodes/ggml_opt_alloc]] _calls_
- [[nodes/ggml_backend_tensor_set]] _calls_
- [[nodes/ggml_opt_eval]] _calls_
- [[nodes/ggml_opt_result_ndata]] _calls_
- [[nodes/ggml_opt_result_loss]] _calls_
- [[nodes/ggml_opt_result_accuracy]] _calls_
- [[nodes/almost_equal]] _calls_
- [[nodes/ggml_opt_reset]] _calls_
- [[nodes/ggml_opt_result_reset]] _calls_

## Used By

- [[nodes/helper_get_regression_opt_pars]] _calls_
- [[nodes/main]] _calls_
