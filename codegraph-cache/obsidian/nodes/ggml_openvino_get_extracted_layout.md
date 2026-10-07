---
name: "ggml_openvino_get_extracted_layout"
type: "function"
file: "ggml/src/ggml-openvino/ggml-openvino-extra.cpp"
community: "ggml"
---

# ggml_openvino_get_extracted_layout

**Type:** `function`  **File:** `ggml/src/ggml-openvino/ggml-openvino-extra.cpp`

**Community:** [[communities/ggml]]

## Depends On

- [[nodes/ggml_is_quantized]] _calls_
- [[nodes/MXFP4]] _calls_
- [[nodes/ggml_nelements]] _calls_
- [[nodes/ggml_nbytes]] _calls_
- [[nodes/value]] _calls_
- [[nodes/format]] _calls_
- [[nodes/weights]] _calls_
- [[nodes/ggml_type_name]] _calls_
- [[nodes/ggml_openvino_tensor_extra]] _calls_

## Used By

- [[nodes/process_weight_tensor]] _calls_
- [[nodes/ggml_backend_openvino_buffer_type_get_max_size]] _calls_
