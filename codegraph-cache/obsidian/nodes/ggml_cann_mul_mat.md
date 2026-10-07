---
name: "ggml_cann_mul_mat"
type: "function"
file: "ggml/src/ggml-cann/aclnn_ops.cpp"
community: "ggml"
---

# ggml_cann_mul_mat

**Type:** `function`  **File:** `ggml/src/ggml-cann/aclnn_ops.cpp`

**Community:** [[communities/ggml]]

## Depends On

- [[nodes/ggml_cann_mat_mul_fp]] _calls_
- [[nodes/ggml_cann_mul_mat_quant]] _calls_
- [[nodes/ggml_cann_create_int_array]] _calls_
- [[nodes/ggml_cann_create_scalar]] _calls_
- [[nodes/rules]] _calls_
- [[nodes/aclnn_mul]] _calls_
- [[nodes/pool]] _calls_
- [[nodes/alloc]] _calls_
- [[nodes/ggml_cann_type_mapping]] _calls_
- [[nodes/ggml_type_size]] _calls_
- [[nodes/aclnn_div]] _calls_
- [[nodes/swap]] _calls_
- [[nodes/aclnn_sin]] _calls_
- [[nodes/aclnn_cos]] _calls_
- [[nodes/set]] _calls_

## Used By

- [[nodes/ggml_cann_compute_forward]] _calls_
