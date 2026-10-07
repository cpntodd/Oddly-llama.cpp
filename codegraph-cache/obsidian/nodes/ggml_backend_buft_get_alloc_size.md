---
name: "ggml_backend_buft_get_alloc_size"
type: "function"
file: "ggml/src/ggml-backend.cpp"
community: "ggml"
---

# ggml_backend_buft_get_alloc_size

**Type:** `function`  **File:** `ggml/src/ggml-backend.cpp`

**Community:** [[communities/ggml]]

## Depends On

- [[nodes/ggml_nbytes]] _calls_

## Used By

- [[nodes/ggml_backend_meta_buffer_type_get_alloc_size]] _calls_
- [[nodes/ggml_backend_buffer_get_alloc_size]] _calls_
- [[nodes/ggml_gallocr_free_extra_space]] _calls_
- [[nodes/ggml_gallocr_allocate_node]] _calls_
- [[nodes/ggml_gallocr_free_node]] _calls_
- [[nodes/ggml_gallocr_alloc_graph_impl]] _calls_
- [[nodes/ggml_gallocr_init_tensor]] _calls_
- [[nodes/ggml_gallocr_node_needs_realloc]] _calls_
- [[nodes/free_buffers]] _calls_
- [[nodes/ggml_backend_rpc_get_device_memory]] _calls_
- [[nodes/ggml_sycl_topk_moe_fusion]] _calls_
- [[nodes/ggml_backend_cann_buffer_init_tensor]] _calls_
- [[nodes/ggml_mem_range_from_tensor]] _calls_
- [[nodes/ggml_backend_et_buffer_init_tensor]] _calls_
- [[nodes/ggml_backend_buffer_is_sycl]] _calls_
