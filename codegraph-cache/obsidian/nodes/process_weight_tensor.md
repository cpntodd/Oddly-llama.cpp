---
name: "process_weight_tensor"
type: "function"
file: "ggml/src/ggml-openvino/ggml-quants.cpp"
community: "ggml"
---

# process_weight_tensor

**Type:** `function`  **File:** `ggml/src/ggml-openvino/ggml-quants.cpp`

**Community:** [[communities/ggml]]

## Depends On

- [[nodes/ggml_nbytes]] _calls_
- [[nodes/ggml_is_quantized]] _calls_
- [[nodes/ggml_type_name]] _calls_
- [[nodes/ggml_openvino_get_extracted_layout]] _calls_
- [[nodes/weights]] _calls_
- [[nodes/tensors]] _calls_
- [[nodes/value]] _calls_
- [[nodes/types]] _calls_
- [[nodes/quantize_q4_0]] _calls_
- [[nodes/quantize_q8_0]] _calls_
- [[nodes/block]] _calls_
- [[nodes/quantize_q8_1]] _calls_

## Used By

- [[nodes/extra_quant_type_name]] _calls_
- [[nodes/is_mul_mat_id_expert_weight]] _calls_
- [[nodes/ggml_backend_openvino_buffer_init_tensor]] _calls_
