---
name: "ggml_backend_sycl_host_buffer_type"
type: "function"
file: "ggml/src/ggml-sycl/ggml-sycl.cpp"
community: "ggml"
---

# ggml_backend_sycl_host_buffer_type

**Type:** `function`  **File:** `ggml/src/ggml-sycl/ggml-sycl.cpp`

**Community:** [[communities/ggml]]

## Depends On

- [[nodes/ggml_backend_sycl_host_buffer_type_for_device]] _calls_
- [[nodes/ggml_sycl_pool_leg]] _calls_
- [[nodes/device]] _calls_
- [[nodes/qptr]] _calls_
- [[nodes/format_slots_in_alloc_order]] _calls_
- [[nodes/ggml_sycl_free_device]] _calls_
- [[nodes/ggml_sycl_pool_vmm]] _calls_
- [[nodes/must]] _calls_
- [[nodes/map]] _calls_
- [[nodes/unmap]] _calls_
- [[nodes/alloc]] _calls_
- [[nodes/ggml_sycl_pool_host]] _calls_
- [[nodes/ggml_sycl_fattn_kv_buffers]] _calls_
- [[nodes/warp_reduce_sum]] _calls_
