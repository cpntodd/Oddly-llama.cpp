---
name: "ggml_sycl_flash_attn_ext"
type: "function"
file: "ggml/src/ggml-sycl/fattn.cpp"
community: "ggml"
---

# ggml_sycl_flash_attn_ext

**Type:** `function`  **File:** `ggml/src/ggml-sycl/fattn.cpp`

**Community:** [[communities/ggml]]

## Depends On

- [[nodes/ggml_sycl_get_env]] _calls_
- [[nodes/ggml_sycl_get_best_fattn_kernel]] _calls_
- [[nodes/ggml_sycl_get_device]] _calls_
- [[nodes/ggml_sycl_flash_attn_ext_dec]] _calls_
- [[nodes/ggml_sycl_flash_attn_ext_tile]] _calls_
- [[nodes/ggml_sycl_flash_attn_ext_vec]] _calls_
- [[nodes/ggml_sycl_flash_attn_ext_mkl]] _calls_
- [[nodes/fingerprint]] _calls_
- [[nodes/stream]] _calls_
- [[nodes/ggml_type_name]] _calls_

## Used By

- [[nodes/ggml_sycl_argmax]] _calls_
