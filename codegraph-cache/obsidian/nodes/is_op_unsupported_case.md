---
name: "is_op_unsupported_case"
type: "function"
file: "ggml/src/ggml-openvino/ggml-openvino.cpp"
community: "ggml"
---

# is_op_unsupported_case

**Type:** `function`  **File:** `ggml/src/ggml-openvino/ggml-openvino.cpp`

**Community:** [[communities/ggml]]

## Depends On

- [[nodes/is_msa_block_mask_expansion]] _calls_
- [[nodes/has_view_op_input]] _calls_
- [[nodes/ggml_is_quantized]] _calls_
- [[nodes/is_gemma3n_flash_attn_pattern]] _calls_
- [[nodes/is_supported_flash_attn_pattern]] _calls_
- [[nodes/ggml_nelements]] _calls_
- [[nodes/cpy_output_view_is_supported]] _calls_
- [[nodes/mul_mat_id_requires_large_tmp]] _calls_
- [[nodes/ggml_type_name]] _calls_

## Used By

- [[nodes/ggml_backend_openvino_device_supports_op]] _calls_
