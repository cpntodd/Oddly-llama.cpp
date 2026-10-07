---
name: "next_power_of_2"
type: "function"
file: "ggml/src/ggml-sycl/ggml-sycl.cpp"
community: "ggml"
---

# next_power_of_2

**Type:** `function`  **File:** `ggml/src/ggml-sycl/ggml-sycl.cpp`

**Community:** [[communities/ggml]]

## Depends On

- [[nodes/get]] _calls_
- [[nodes/parallel_for]] _calls_
- [[nodes/ggml_backend_buffer_is_host]] _calls_
- [[nodes/ggml_backend_buffer_is_sycl]] _calls_
- [[nodes/ggml_backend_buffer_is_sycl_split]] _calls_
- [[nodes/get_current_device_id]] _calls_
- [[nodes/ggml_type_size]] _calls_
- [[nodes/ggml_blck_size]] _calls_
- [[nodes/ggml_is_contiguous]] _calls_
- [[nodes/pool]] _calls_
- [[nodes/ggml_get_to_bf16_sycl]] _calls_
- [[nodes/ggml_is_quantized]] _calls_
- [[nodes/ggml_get_to_fp16_sycl]] _calls_
- [[nodes/alloc]] _calls_
- [[nodes/gemm]] _calls_
- [[nodes/ggml_get_to_fp32_sycl]] _calls_
- [[nodes/get_value]] _calls_
