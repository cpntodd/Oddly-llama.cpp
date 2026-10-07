---
name: "ggml_sycl_op_fwht"
type: "function"
file: "ggml/src/ggml-sycl/fwht.cpp"
community: "ggml"
---

# ggml_sycl_op_fwht

**Type:** `function`  **File:** `ggml/src/ggml-sycl/fwht.cpp`

**Community:** [[communities/ggml]]

## Depends On

- [[nodes/fwht.comp.cpp]] _imports_
- [[nodes/ggml_are_same_shape]] _calls_
- [[nodes/ggml_is_contiguous]] _calls_
- [[nodes/ggml_nrows]] _calls_
- [[nodes/getenv]] _calls_

## Used By

- [[nodes/ggml_sycl_mul_mat]] _calls_
