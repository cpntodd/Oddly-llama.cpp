---
name: "weight_format_to_nz"
type: "function"
file: "ggml/src/ggml-cann/ggml-cann.cpp"
community: "ggml"
---

# weight_format_to_nz

**Type:** `function`  **File:** `ggml/src/ggml-cann/ggml-cann.cpp`

**Community:** [[communities/ggml]]

## Depends On

- [[nodes/realloc]] _calls_
- [[nodes/tensors]] _calls_
- [[nodes/ggml_cann_set_device]] _calls_
- [[nodes/parse_bool]] _calls_
- [[nodes/need_transform]] _calls_
- [[nodes/is_matmul_weight]] _calls_
- [[nodes/ggml_nbytes]] _calls_
- [[nodes/ggml_backend_cann_transform]] _calls_
- [[nodes/remove_tracker]] _calls_
- [[nodes/ggml_backend_cann_transform_back]] _calls_
- [[nodes/ggml_backend_buft_is_cann]] _calls_
