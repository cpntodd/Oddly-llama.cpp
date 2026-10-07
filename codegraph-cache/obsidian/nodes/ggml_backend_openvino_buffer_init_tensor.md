---
name: "ggml_backend_openvino_buffer_init_tensor"
type: "function"
file: "ggml/src/ggml-openvino/ggml-openvino.cpp"
community: "ggml"
---

# ggml_backend_openvino_buffer_init_tensor

**Type:** `function`  **File:** `ggml/src/ggml-openvino/ggml-openvino.cpp`

**Community:** [[communities/ggml]]

## Depends On

- [[nodes/is_stateful_enabled]] _calls_
- [[nodes/ggml_backend_openvino_buffer_context]] _calls_
- [[nodes/ggml_is_quantized]] _calls_
- [[nodes/ggml_openvino_get_cl_queue]] _calls_
- [[nodes/ggml_openvino_get_clEnqueueMemFillINTEL]] _calls_
- [[nodes/ggml_nbytes]] _calls_
- [[nodes/process_weight_tensor]] _calls_
- [[nodes/ggml_openvino_quantized_weight_extra]] _calls_
- [[nodes/extra_quant_type_name]] _calls_
- [[nodes/value]] _calls_
- [[nodes/ggml_nelements]] _calls_
- [[nodes/ggml_openvino_weight_extra]] _calls_
- [[nodes/ggml_openvino_weight_buffers_released]] _calls_
- [[nodes/ggml_openvino_register_weight_buffer]] _calls_
- [[nodes/ggml_openvino_get_clEnqueueMemcpyINTEL]] _calls_
- [[nodes/ggml_backend_buffer_is_host]] _calls_
- [[nodes/ggml_backend_buffer_is_openvino]] _calls_
