---
name: "create_webgpu_device"
type: "function"
file: "ggml/src/ggml-webgpu/ggml-webgpu.cpp"
community: "ggml"
---

# create_webgpu_device

**Type:** `function`  **File:** `ggml/src/ggml-webgpu/ggml-webgpu.cpp`

**Community:** [[communities/ggml]]

## Depends On

- [[nodes/ggml_backend_webgpu_request_adapter]] _calls_
- [[nodes/ggml_backend_webgpu_get_command_submit_batch_size]] _calls_
- [[nodes/ggml_backend_webgpu_get_max_inflight_batches]] _calls_
- [[nodes/string]] _calls_
- [[nodes/ggml_webgpu_init_memset_pipeline]] _calls_

## Used By

- [[nodes/ggml_backend_webgpu_reg_get_device]] _calls_
