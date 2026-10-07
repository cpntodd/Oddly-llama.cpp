---
name: "ggml_sycl_t2_restore_tensor"
type: "function"
file: "ggml/src/ggml-sycl/ggml-sycl.cpp"
community: "ggml"
---

# ggml_sycl_t2_restore_tensor

**Type:** `function`  **File:** `ggml/src/ggml-sycl/ggml-sycl.cpp`

**Community:** [[communities/ggml]]

## Depends On

- [[nodes/ggml_sycl_t2_restore]] _calls_
- [[nodes/queues_wait_and_throw]] _calls_
- [[nodes/mmap]] _calls_

## Used By

- [[nodes/ggml_sycl_is_l0_discrete_gpu]] _calls_
- [[nodes/ggml_sycl_t2_tensor]] _calls_
- [[nodes/ggml_sycl_mul_mat]] _calls_
- [[nodes/ggml_sycl_argmax]] _calls_
- [[nodes/ggml_backend_sycl_free]] _calls_
