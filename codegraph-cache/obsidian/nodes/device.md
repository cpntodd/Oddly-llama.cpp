---
name: "device"
type: "function"
file: "ggml/src/ggml-cann/ggml-cann.cpp"
community: "ggml"
---

# device

**Type:** `function`  **File:** `ggml/src/ggml-cann/ggml-cann.cpp`

**Community:** [[communities/ggml]]

## Depends On

- [[nodes/ggml_backend_cann_buffer_context]] _calls_
- [[nodes/ggml_nbytes]] _calls_

## Used By

- [[nodes/usage]] _calls_
- [[nodes/print_usage]] _calls_
- [[nodes/common_params_parser_init]] _calls_
- [[nodes/serialize_graph]] _calls_
- [[nodes/ggml_backend_rpc_get_device_memory]] _calls_
- [[nodes/qptr]] _calls_
- [[nodes/get_device_backend_and_type]] _calls_
- [[nodes/get_preferred_gpu_platform_name]] _calls_
- [[nodes/if]] _calls_
- [[nodes/compare_backend]] _calls_
- [[nodes/ggml_cann_init]] _calls_
- [[nodes/ggml_et_cpu_compare_init_pre]] _calls_
- [[nodes/ggml_openvino_is_npu]] _calls_
- [[nodes/ggml_sycl_get_device]] _calls_
- [[nodes/free_aligned_mem_host]] _calls_
- [[nodes/ggml_backend_sycl_host_buffer_type]] _calls_
