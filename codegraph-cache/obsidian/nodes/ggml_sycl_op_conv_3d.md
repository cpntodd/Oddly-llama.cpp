---
name: "ggml_sycl_op_conv_3d"
type: "function"
file: "ggml/src/ggml-sycl/conv3d.cpp"
community: "ggml"
---

# ggml_sycl_op_conv_3d

**Type:** `function`  **File:** `ggml/src/ggml-sycl/conv3d.cpp`

**Community:** [[communities/ggml]]

## Depends On

- [[nodes/ggml_is_contiguous]] _calls_
- [[nodes/ggml_sycl_conv3d_calc_patch_total]] _calls_
- [[nodes/ggml_sycl_conv3d_calc_knl_n_total]] _calls_
- [[nodes/ggml_element_size]] _calls_
- [[nodes/pool]] _calls_
- [[nodes/alloc]] _calls_
- [[nodes/get]] _calls_
- [[nodes/A]] _calls_
- [[nodes/each]] _calls_
- [[nodes/parallel_for]] _calls_
- [[nodes/is]] _calls_
- [[nodes/gemm]] _calls_
- [[nodes/get_value]] _calls_

## Used By

- [[nodes/ggml_sycl_conv_3d]] _calls_
