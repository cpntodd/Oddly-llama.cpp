---
name: "ggml_backend_graph_compute"
type: "function"
file: "ggml/src/ggml-backend.cpp"
community: "ggml"
---

# ggml_backend_graph_compute

**Type:** `function`  **File:** `ggml/src/ggml-backend.cpp`

**Community:** [[communities/ggml]]

## Depends On

- [[nodes/ggml_backend_graph_compute_async]] _calls_
- [[nodes/ggml_backend_synchronize]] _calls_

## Used By

- [[nodes/merge_tensor]] _calls_
- [[nodes/print_debug_tensor]] _calls_
- [[nodes/time_cell_median]] _calls_
- [[nodes/ggml_backend_compare_graph_backend]] _calls_
- [[nodes/ggml_backend_rpc_get_device_memory]] _calls_
- [[nodes/ggml_et_cpu_compare_init_pre]] _calls_
- [[nodes/eval_perf]] _calls_
- [[nodes/eval_grad]] _calls_
