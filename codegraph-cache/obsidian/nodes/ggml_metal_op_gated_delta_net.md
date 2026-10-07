---
name: "ggml_metal_op_gated_delta_net"
type: "function"
file: "ggml/src/ggml-metal/ggml-metal-ops.cpp"
community: "ggml"
---

# ggml_metal_op_gated_delta_net

**Type:** `function`  **File:** `ggml/src/ggml-metal/ggml-metal-ops.cpp`

**Community:** [[communities/ggml]]

## Depends On

- [[nodes/mark_fused_set_rows]] _calls_
- [[nodes/ggml_metal_op_concurrency_reset]] _calls_
- [[nodes/ggml_metal_op_concurrency_add]] _calls_
- [[nodes/ggml_metal_library_get_pipeline_gated_delta_net]] _calls_
- [[nodes/ggml_metal_get_buffer_id]] _calls_
- [[nodes/rows]] _calls_

## Used By

- [[nodes/ggml_metal_op_encode_impl]] _calls_
