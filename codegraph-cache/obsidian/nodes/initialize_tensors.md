---
name: "initialize_tensors"
type: "function"
file: "tests/test-backend-ops.cpp"
community: "tests"
---

# initialize_tensors

**Type:** `function`  **File:** `tests/test-backend-ops.cpp`

**Community:** [[communities/tests]]

## Depends On

- [[nodes/ggml_get_first_tensor]] _calls_
- [[nodes/ggml_get_next_tensor]] _calls_
- [[nodes/init_tensor_uniform]] _calls_

## Used By

- [[nodes/print_test_result_locked]] _calls_
- [[nodes/matches_filter]] _calls_
- [[nodes/eval_perf]] _calls_
- [[nodes/eval_grad]] _calls_
- [[nodes/op]] _calls_
- [[nodes/init_set_rows_row_ids]] _calls_
- [[nodes/type_src]] _calls_
- [[nodes/ne]] _calls_
- [[nodes/total_elements]] _calls_
- [[nodes/tensor_range]] _calls_
- [[nodes/n_cache_rows]] _calls_
- [[nodes/blk]] _calls_
- [[nodes/init_mul_mat_id_tensors]] _calls_
- [[nodes/hsk]] _calls_
- [[nodes/is_non_contiguous]] _calls_
- [[nodes/hp]] _calls_
