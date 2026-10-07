---
name: "ggml_backend_sched_compute_splits"
type: "function"
file: "ggml/src/ggml-backend.cpp"
community: "src"
---

# ggml_backend_sched_compute_splits

**Type:** `function`  **File:** `ggml/src/ggml-backend.cpp`

**Community:** [[communities/src]]

## Depends On

- [[nodes/ggml_backend_event_synchronize]] _calls_
- [[nodes/ggml_backend_synchronize]] _calls_
- [[nodes/ggml_backend_sched_get_tensor_backend]] _calls_
- [[nodes/ggml_backend_tensor_copy]] _calls_
- [[nodes/ggml_backend_event_wait]] _calls_
- [[nodes/ggml_backend_buffer_get_usage]] _calls_
- [[nodes/ggml_backend_buffer_is_host]] _calls_
- [[nodes/ggml_nbytes]] _calls_
- [[nodes/ggml_backend_tensor_get_async]] _calls_
- [[nodes/clear]] _calls_
- [[nodes/ggml_bitset_size]] _calls_
- [[nodes/ggml_bitset_set]] _calls_
- [[nodes/ggml_backend_tensor_set_async]] _calls_
- [[nodes/ggml_bitset_get]] _calls_
- [[nodes/ggml_backend_graph_compute_async]] _calls_
- [[nodes/ggml_graph_view]] _calls_
- [[nodes/ggml_backend_event_record]] _calls_
- [[nodes/ggml_backend_dev_type]] _calls_
- [[nodes/ggml_backend_get_device]] _calls_
- [[nodes/getenv]] _calls_
- [[nodes/ggml_hash_set_new]] _calls_
- [[nodes/ggml_graph_overhead_custom]] _calls_
- [[nodes/ggml_backend_get_default_buffer_type]] _calls_
- [[nodes/ggml_backend_supports_buft]] _calls_
- [[nodes/ggml_backend_event_new]] _calls_
- [[nodes/ggml_gallocr_new_n]] _calls_
- [[nodes/ggml_backend_sched_reset]] _calls_

## Used By

- [[nodes/ggml_backend_sched_graph_compute_async]] _calls_
