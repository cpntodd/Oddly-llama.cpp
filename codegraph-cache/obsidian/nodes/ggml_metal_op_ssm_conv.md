---
name: "ggml_metal_op_ssm_conv"
type: "function"
file: "ggml/src/ggml-metal/ggml-metal-ops.cpp"
community: "ggml"
---

# ggml_metal_op_ssm_conv

**Type:** `function`  **File:** `ggml/src/ggml-metal/ggml-metal-ops.cpp`

**Community:** [[communities/ggml]]

## Depends On

- [[nodes/can_fuse]] _calls_
- [[nodes/ggml_get_unary_op]] _calls_
- [[nodes/ggml_is_contiguous]] _calls_
- [[nodes/ggml_are_same_shape]] _calls_
- [[nodes/ggml_metal_op_concurrency_check]] _calls_
- [[nodes/ggml_metal_op_concurrency_reset]] _calls_
- [[nodes/ggml_metal_library_get_pipeline_ssm_conv_batched]] _calls_
- [[nodes/ggml_metal_get_buffer_id]] _calls_
- [[nodes/ggml_metal_library_get_pipeline_ssm_conv]] _calls_

## Used By

- [[nodes/ggml_metal_op_encode_impl]] _calls_
