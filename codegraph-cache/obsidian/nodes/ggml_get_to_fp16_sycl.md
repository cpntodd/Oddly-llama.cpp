---
name: "ggml_get_to_fp16_sycl"
type: "function"
file: "ggml/src/ggml-sycl/convert.cpp"
community: "ggml"
---

# ggml_get_to_fp16_sycl

**Type:** `function`  **File:** `ggml/src/ggml-sycl/convert.cpp`

**Community:** [[communities/ggml]]

## Depends On

- [[nodes/ggml_type_name]] _calls_

## Used By

- [[nodes/convert_f32]] _calls_
- [[nodes/mkl_fa_make_desc]] _calls_
- [[nodes/get_dequantize_V]] _calls_
- [[nodes/if]] _calls_
- [[nodes/next_power_of_2]] _calls_
- [[nodes/ggml_sycl_group_norm]] _calls_
