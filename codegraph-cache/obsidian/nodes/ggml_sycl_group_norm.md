---
name: "ggml_sycl_group_norm"
type: "function"
file: "ggml/src/ggml-sycl/ggml-sycl.cpp"
community: "ggml"
---

# ggml_sycl_group_norm

**Type:** `function`  **File:** `ggml/src/ggml-sycl/ggml-sycl.cpp`

**Community:** [[communities/ggml]]

## Depends On

- [[nodes/ggml_sycl_op_group_norm]] _calls_
- [[nodes/ggml_is_permuted]] _calls_
- [[nodes/ggml_backend_buffer_is_sycl_split]] _calls_
- [[nodes/ggml_is_transposed]] _calls_
- [[nodes/ggml_is_contiguous]] _calls_
- [[nodes/ggml_type_size]] _calls_
- [[nodes/ggml_is_contiguous_2]] _calls_
- [[nodes/pool]] _calls_
- [[nodes/alloc]] _calls_
- [[nodes/ggml_get_to_fp16_sycl]] _calls_
- [[nodes/get]] _calls_
- [[nodes/ggml_nelements]] _calls_
- [[nodes/ggml_get_to_fp16_nc_sycl]] _calls_
- [[nodes/gemm]] _calls_
- [[nodes/parallel_for]] _calls_

## Used By

- [[nodes/ggml_sycl_argmax]] _calls_
