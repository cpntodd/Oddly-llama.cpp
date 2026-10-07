---
name: "ggml_is_contiguously_allocated"
type: "function"
file: "ggml/src/ggml.c"
community: "ggml"
---

# ggml_is_contiguously_allocated

**Type:** `function`  **File:** `ggml/src/ggml.c`

**Community:** [[communities/ggml]]

## Depends On

- [[nodes/ggml_nbytes]] _calls_
- [[nodes/ggml_nelements]] _calls_
- [[nodes/ggml_type_size]] _calls_
- [[nodes/ggml_blck_size]] _calls_

## Used By

- [[nodes/ggml_backend_meta_buffer_init_tensor_impl]] _calls_
- [[nodes/ggml_sycl_op_acc]] _calls_
- [[nodes/if]] _calls_
- [[nodes/get_dequantize_V]] _calls_
- [[nodes/if]] _calls_
