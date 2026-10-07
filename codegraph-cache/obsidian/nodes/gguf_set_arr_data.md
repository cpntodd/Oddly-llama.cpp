---
name: "gguf_set_arr_data"
type: "function"
file: "ggml/src/gguf.cpp"
community: "ggml"
---

# gguf_set_arr_data

**Type:** `function`  **File:** `ggml/src/gguf.cpp`

**Community:** [[communities/ggml]]

## Depends On

- [[nodes/gguf_check_reserved_keys]] _calls_
- [[nodes/gguf_remove_key]] _calls_
- [[nodes/gguf_type_size]] _calls_
- [[nodes/empty]] _calls_
- [[nodes/cast]] _calls_

## Used By

- [[nodes/llama_model_saver_supports_arch]] _calls_
- [[nodes/if]] _calls_
- [[nodes/gguf_ex_write]] _calls_
- [[nodes/convert_weights_ak_to_gg]] _calls_
- [[nodes/get_random_gguf_context]] _calls_
- [[nodes/gguf_set_kv]] _calls_
