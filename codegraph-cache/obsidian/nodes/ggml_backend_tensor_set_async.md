---
name: "ggml_backend_tensor_set_async"
type: "function"
file: "ggml/src/ggml-backend.cpp"
community: "src"
---

# ggml_backend_tensor_set_async

**Type:** `function`  **File:** `ggml/src/ggml-backend.cpp`

**Community:** [[communities/src]]

## Depends On

- [[nodes/ggml_nbytes]] _calls_
- [[nodes/ggml_backend_synchronize]] _calls_
- [[nodes/ggml_backend_tensor_set]] _calls_

## Used By

- [[nodes/select_weight_buft]] _calls_
- [[nodes/ggml_backend_meta_set_tensor_async]] _calls_
- [[nodes/ggml_backend_tensor_get_async]] _calls_
- [[nodes/ggml_backend_sched_compute_splits]] _calls_
