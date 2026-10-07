---
name: "make_context"
type: "function"
file: "tests/test-alloc.cpp"
community: "tests"
---

# make_context

**Type:** `function`  **File:** `tests/test-alloc.cpp`

**Community:** [[communities/tests]]

## Depends On

- [[nodes/ggml_tensor_overhead]] _calls_
- [[nodes/ggml_graph_overhead]] _calls_
- [[nodes/ggml_init]] _calls_
- [[nodes/ggml_new_graph]] _calls_
- [[nodes/ggml_set_input]] _calls_

## Used By

- [[nodes/dsv4_make_k_only]] _calls_
- [[nodes/test_max_size_too_many_tensors]] _calls_
- [[nodes/test_max_size_tensor_too_large]] _calls_
- [[nodes/test_tensor_larger_than_max_size]] _calls_
- [[nodes/test_not_enough_chunks]] _calls_
- [[nodes/test_fill_leftover_space]] _calls_
- [[nodes/test_view_inplace]] _calls_
- [[nodes/test_reuse_and_free]] _calls_
- [[nodes/test_merge_free_block]] _calls_
- [[nodes/test_prefer_already_allocated_memory]] _calls_
- [[nodes/test_multiple_buffer_types]] _calls_
- [[nodes/test_buffer_size_zero]] _calls_
- [[nodes/test_reallocation]] _calls_
