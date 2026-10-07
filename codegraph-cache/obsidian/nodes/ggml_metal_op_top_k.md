---
name: "ggml_metal_op_top_k"
type: "function"
file: "ggml/src/ggml-metal/ggml-metal-ops.cpp"
community: "ggml"
---

# ggml_metal_op_top_k

**Type:** `function`  **File:** `ggml/src/ggml-metal/ggml-metal-ops.cpp`

**Community:** [[communities/ggml]]

## Depends On

- [[nodes/ggml_is_contiguous_rows]] _calls_
- [[nodes/ggml_metal_library_get_pipeline_top_k]] _calls_
- [[nodes/ggml_metal_get_buffer_id]] _calls_
- [[nodes/ggml_nelements]] _calls_
- [[nodes/swap]] _calls_
- [[nodes/ggml_metal_library_get_pipeline_top_k_merge]] _calls_
- [[nodes/ggml_metal_op_concurrency_reset]] _calls_

## Used By

- [[nodes/ggml_metal_op_encode_impl]] _calls_
