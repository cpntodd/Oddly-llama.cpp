---
name: "apir_untrack_backend_buffer"
type: "function"
file: "ggml/src/ggml-virtgpu/backend/apir_cs_ggml-rpc-back.cpp"
community: "ggml"
---

# apir_untrack_backend_buffer

**Type:** `function`  **File:** `ggml/src/ggml-virtgpu/backend/apir_cs_ggml-rpc-back.cpp`

**Community:** [[communities/ggml]]

## Depends On

- [[nodes/ggml_nbytes]] _calls_
- [[nodes/ggml_backend_buffer_get_size]] _calls_
- [[nodes/ggml_set_name]] _calls_
- [[nodes/ggml_tensor_overhead]] _calls_
- [[nodes/ggml_graph_overhead_custom]] _calls_
- [[nodes/ggml_init]] _calls_
- [[nodes/ggml_new_graph_custom]] _calls_

## Used By

- [[nodes/backend_buffer_free_buffer]] _calls_
- [[nodes/apir_backend_deinit]] _calls_
