---
name: "ggml_backend_openvino_device_supports_op"
type: "function"
file: "ggml/src/ggml-openvino/ggml-openvino.cpp"
community: "ggml"
---

# ggml_backend_openvino_device_supports_op

**Type:** `function`  **File:** `ggml/src/ggml-openvino/ggml-openvino.cpp`

**Community:** [[communities/ggml]]

## Depends On

- [[nodes/string]] _calls_
- [[nodes/ggml_op_name]] _calls_
- [[nodes/ggml_unary_op_name]] _calls_
- [[nodes/ggml_glu_op_name]] _calls_
- [[nodes/ggml_get_unary_op]] _calls_
- [[nodes/ggml_get_glu_op]] _calls_
- [[nodes/has_view_op_input]] _calls_
- [[nodes/ggml_type_name]] _calls_
- [[nodes/has_strides_on_element_grid]] _calls_
- [[nodes/ggml_is_quantized]] _calls_
- [[nodes/is_op_unsupported_case]] _calls_
