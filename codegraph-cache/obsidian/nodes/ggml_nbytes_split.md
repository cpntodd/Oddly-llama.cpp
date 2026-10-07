---
name: "ggml_nbytes_split"
type: "function"
file: "ggml/src/ggml-sycl/ggml-sycl.cpp"
community: "ggml"
---

# ggml_nbytes_split

**Type:** `function`  **File:** `ggml/src/ggml-sycl/ggml-sycl.cpp`

**Community:** [[communities/ggml]]

## Depends On

- [[nodes/ggml_row_size]] _calls_
- [[nodes/ggml_backend_sycl_split_buffer_context]] _calls_
- [[nodes/release_extra_gpu]] _calls_

## Used By

- [[nodes/ggml_backend_sycl_split_buffer_free_buffer]] _calls_
- [[nodes/ggml_backend_sycl_split_buffer_type_get_alloc_size]] _calls_
