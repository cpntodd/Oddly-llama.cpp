---
name: "common_imatrix_load"
type: "function"
file: "common/imatrix-loader.cpp"
community: "ggml"
---

# common_imatrix_load

**Type:** `function`  **File:** `common/imatrix-loader.cpp`

**Community:** [[communities/ggml]]

## Depends On

- [[nodes/common_imatrix_load_legacy]] _calls_
- [[nodes/gguf_get_n_tensors]] _calls_
- [[nodes/gguf_free]] _calls_
- [[nodes/ggml_free]] _calls_
- [[nodes/gguf_find_key]] _calls_
- [[nodes/gguf_get_kv_type]] _calls_
- [[nodes/gguf_get_arr_type]] _calls_
- [[nodes/gguf_get_arr_n]] _calls_
- [[nodes/size]] _calls_
- [[nodes/push_back]] _calls_
- [[nodes/gguf_get_val_u32]] _calls_
- [[nodes/ggml_get_first_tensor]] _calls_
- [[nodes/ggml_get_next_tensor]] _calls_
- [[nodes/empty]] _calls_
- [[nodes/string_remove_suffix]] _calls_
- [[nodes/ggml_nelements]] _calls_

## Used By

- [[nodes/load_imatrix]] _calls_
- [[nodes/all_finite]] _calls_
