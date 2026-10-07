---
name: "ggml_backend_tensor_get_async"
type: "function"
file: "ggml/src/ggml-backend.cpp"
community: "src"
---

# ggml_backend_tensor_get_async

**Type:** `function`  **File:** `ggml/src/ggml-backend.cpp`

**Community:** [[communities/src]]

## Depends On

- [[nodes/ggml_nbytes]] _calls_
- [[nodes/ggml_backend_synchronize]] _calls_
- [[nodes/ggml_backend_tensor_get]] _calls_
- [[nodes/ggml_backend_tensor_set_async]] _calls_

## Used By

- [[nodes/ctx_type_to_graph_type]] _calls_
- [[nodes/needs_raw_logits]] _calls_
- [[nodes/ggml_backend_meta_get_tensor_async]] _calls_
- [[nodes/ggml_backend_sched_compute_splits]] _calls_
