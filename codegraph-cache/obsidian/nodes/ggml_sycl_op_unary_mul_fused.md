---
name: "ggml_sycl_op_unary_mul_fused"
type: "function"
file: "ggml/src/ggml-sycl/element_wise.cpp"
community: "ggml"
---

# ggml_sycl_op_unary_mul_fused

**Type:** `function`  **File:** `ggml/src/ggml-sycl/element_wise.cpp`

**Community:** [[communities/ggml]]

## Depends On

- [[nodes/ggml_can_fuse]] _calls_
- [[nodes/ggml_are_same_shape]] _calls_
- [[nodes/ggml_is_contiguous_1]] _calls_
- [[nodes/ggml_is_contiguous]] _calls_
- [[nodes/stream]] _calls_
- [[nodes/ggml_nelements]] _calls_
- [[nodes/unary_mul_sycl]] _calls_
- [[nodes/ggml_type_name]] _calls_
- [[nodes/ggml_get_unary_op]] _calls_

## Used By

- [[nodes/op_silu]] _calls_
- [[nodes/ggml_backend_sycl_graph_compute_impl]] _calls_
