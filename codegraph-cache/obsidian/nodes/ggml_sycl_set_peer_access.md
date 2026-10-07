---
name: "ggml_sycl_set_peer_access"
type: "function"
file: "ggml/src/ggml-sycl/ggml-sycl.cpp"
community: "ggml"
---

# ggml_sycl_set_peer_access

**Type:** `function`  **File:** `ggml/src/ggml-sycl/ggml-sycl.cpp`

**Community:** [[communities/ggml]]

## Depends On

- [[nodes/ggml_nrows]] _calls_
- [[nodes/ggml_backend_buffer_is_sycl_split]] _calls_
- [[nodes/ggml_type_size]] _calls_
- [[nodes/ggml_blck_size]] _calls_
- [[nodes/ggml_is_contiguous]] _calls_
- [[nodes/get_row_rounding]] _calls_
- [[nodes/alloc]] _calls_
- [[nodes/pool]] _calls_
- [[nodes/ggml_nbytes]] _calls_
- [[nodes/ggml_nelements]] _calls_

## Used By

- [[nodes/ggml_sycl_argmax]] _calls_
