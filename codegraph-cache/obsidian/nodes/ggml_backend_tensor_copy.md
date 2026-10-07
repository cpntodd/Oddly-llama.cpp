---
name: "ggml_backend_tensor_copy"
type: "function"
file: "ggml/src/ggml-backend.cpp"
community: "src"
---

# ggml_backend_tensor_copy

**Type:** `function`  **File:** `ggml/src/ggml-backend.cpp`

**Community:** [[communities/src]]

## Depends On

- [[nodes/ggml_are_same_layout]] _calls_
- [[nodes/ggml_backend_buffer_is_host]] _calls_
- [[nodes/ggml_backend_tensor_set]] _calls_
- [[nodes/ggml_nbytes]] _calls_

## Used By

- [[nodes/print_debug_tensor]] _calls_
- [[nodes/dsv4_make_k_only]] _calls_
- [[nodes/ggml_gen_hadamard]] _calls_
- [[nodes/needs_raw_logits]] _calls_
- [[nodes/ggml_backend_tensor_copy_async]] _calls_
- [[nodes/ggml_backend_sched_compute_splits]] _calls_
- [[nodes/graph_copy_init_tensor]] _calls_
