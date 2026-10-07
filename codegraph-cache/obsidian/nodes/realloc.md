---
name: "realloc"
type: "function"
file: "ggml/src/ggml-cann/ggml-cann.cpp"
community: "ggml"
---

# realloc

**Type:** `function`  **File:** `ggml/src/ggml-cann/ggml-cann.cpp`

**Community:** [[communities/ggml]]

## Depends On

- [[nodes/clear]] _calls_

## Used By

- [[nodes/ggml_backend_sched_split_inputs_grow]] _calls_
- [[nodes/ggml_backend_sched_graph_inputs_grow]] _calls_
- [[nodes/ggml_backend_sched_split_graph]] _calls_
- [[nodes/free_buffers]] _calls_
- [[nodes/weight_format_to_nz]] _calls_
- [[nodes/pool]] _calls_
- [[nodes/ggml_backend_sycl_comm_free]] _calls_
