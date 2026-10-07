---
name: "ggml_backend_meta_graph_compute"
type: "function"
file: "ggml/src/ggml-backend-meta.cpp"
community: "ggml"
---

# ggml_backend_meta_graph_compute

**Type:** `function`  **File:** `ggml/src/ggml-backend-meta.cpp`

**Community:** [[communities/ggml]]

## Depends On

- [[nodes/ggml_backend_meta_n_backends]] _calls_
- [[nodes/ggml_backend_buffer_is_meta]] _calls_
- [[nodes/ggml_reset]] _calls_
- [[nodes/get]] _calls_
- [[nodes/clear]] _calls_
- [[nodes/ggml_backend_buffer_is_host]] _calls_
- [[nodes/ggml_node_get_use_count]] _calls_
- [[nodes/ggml_backend_meta_get_split_state]] _calls_
- [[nodes/ggml_are_same_shape]] _calls_
- [[nodes/max]] _calls_
- [[nodes/ggml_nbytes]] _calls_
- [[nodes/ggml_backend_alloc_buffer]] _calls_
- [[nodes/ggml_graph_overhead_custom]] _calls_
- [[nodes/ggml_tensor_overhead]] _calls_
- [[nodes/ggml_init]] _calls_
- [[nodes/ggml_new_graph_custom]] _calls_
- [[nodes/ggml_hash_set_reset]] _calls_
- [[nodes/ggml_hash_find]] _calls_
- [[nodes/ggml_hash_insert]] _calls_
- [[nodes/ggml_graph_next_uid]] _calls_
- [[nodes/ggml_backend_buffer_get_size]] _calls_
- [[nodes/ggml_set_op_params_f32]] _calls_
- [[nodes/ggml_backend_graph_compute_async]] _calls_
- [[nodes/ggml_is_contiguous]] _calls_
- [[nodes/ggml_backend_tensor_copy_async]] _calls_
- [[nodes/ggml_backend_view_init]] _calls_
