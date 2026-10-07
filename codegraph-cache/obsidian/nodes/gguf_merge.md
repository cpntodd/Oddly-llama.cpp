---
name: "gguf_merge"
type: "function"
file: "tools/gguf-split/gguf-split.cpp"
community: "ggml"
---

# gguf_merge

**Type:** `function`  **File:** `tools/gguf-split/gguf-split.cpp`

**Community:** [[communities/ggml]]

## Depends On

- [[nodes/gguf_find_key]] _calls_
- [[nodes/gguf_free]] _calls_
- [[nodes/ggml_free]] _calls_
- [[nodes/gguf_get_val_u16]] _calls_
- [[nodes/gguf_set_val_u16]] _calls_
- [[nodes/gguf_set_kv]] _calls_
- [[nodes/gguf_get_n_tensors]] _calls_
- [[nodes/ggml_get_tensor]] _calls_
- [[nodes/gguf_get_meta_size]] _calls_
- [[nodes/zeros]] _calls_
- [[nodes/ggml_nbytes]] _calls_
- [[nodes/gguf_get_data_offset]] _calls_
- [[nodes/gguf_get_tensor_offset]] _calls_
- [[nodes/read]] _calls_
- [[nodes/write]] _calls_
- [[nodes/gguf_get_meta_data]] _calls_

## Used By

- [[nodes/main]] _calls_
