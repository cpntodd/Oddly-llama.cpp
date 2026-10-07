---
name: "test_barrier"
type: "function"
file: "tests/test-barrier.cpp"
community: "ggml"
---

# test_barrier

**Type:** `function`  **File:** `tests/test-barrier.cpp`

**Community:** [[communities/ggml]]

## Depends On

- [[nodes/ggml_graph_next_uid]] _imports_
- [[nodes/ggml_arm_arch_features_type]] _imports_
- [[nodes/ggml_init]] _calls_
- [[nodes/ggml_new_graph]] _calls_
- [[nodes/ggml_build_forward_expand]] _calls_
- [[nodes/ggml_graph_n_nodes]] _calls_
- [[nodes/ggml_threadpool_params_default]] _calls_
- [[nodes/ggml_threadpool_new]] _calls_
- [[nodes/data]] _calls_
- [[nodes/ggml_graph_print]] _calls_
- [[nodes/ggml_graph_compute]] _calls_
- [[nodes/ggml_threadpool_free]] _calls_
- [[nodes/ggml_free]] _calls_

## Used By

- [[nodes/main]] _calls_
