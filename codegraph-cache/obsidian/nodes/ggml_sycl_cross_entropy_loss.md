---
name: "ggml_sycl_cross_entropy_loss"
type: "function"
file: "ggml/src/ggml-sycl/cross_entropy_loss.cpp"
community: "ggml"
---

# ggml_sycl_cross_entropy_loss

**Type:** `function`  **File:** `ggml/src/ggml-sycl/cross_entropy_loss.cpp`

**Community:** [[communities/ggml]]

## Depends On

- [[nodes/cross_entropy_loss.hpp]] _imports_
- [[nodes/ggml_is_contiguous]] _calls_
- [[nodes/ggml_are_same_shape]] _calls_
- [[nodes/ggml_is_scalar]] _calls_
- [[nodes/ggml_nrows]] _calls_
- [[nodes/pool]] _calls_
- [[nodes/get]] _calls_
- [[nodes/block]] _calls_
- [[nodes/parallel_for]] _calls_

## Used By

- [[nodes/ggml_sycl_argmax]] _calls_
