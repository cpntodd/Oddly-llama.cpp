---
name: "ggml_metal_op_rwkv"
type: "function"
file: "ggml/src/ggml-metal/ggml-metal-ops.cpp"
community: "ggml"
---

# ggml_metal_op_rwkv

**Type:** `function`  **File:** `ggml/src/ggml-metal/ggml-metal-ops.cpp`

**Community:** [[communities/ggml]]

## Depends On

- [[nodes/ggml_metal_library_get_pipeline_rwkv]] _calls_
- [[nodes/ggml_metal_get_buffer_id]] _calls_
- [[nodes/getenv]] _calls_
- [[nodes/ggml_get_op_params_i32]] _calls_
- [[nodes/n_nodes]] _calls_
- [[nodes/rows]] _calls_
- [[nodes/layout]] _calls_
- [[nodes/ggml_type_size]] _calls_
- [[nodes/ggml_nelements]] _calls_
- [[nodes/ggml_is_contiguous]] _calls_

## Used By

- [[nodes/ggml_metal_op_encode_impl]] _calls_
