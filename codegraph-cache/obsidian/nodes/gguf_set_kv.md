---
name: "gguf_set_kv"
type: "function"
file: "ggml/src/gguf.cpp"
community: "ggml"
---

# gguf_set_kv

**Type:** `function`  **File:** `ggml/src/gguf.cpp`

**Community:** [[communities/ggml]]

## Depends On

- [[nodes/gguf_get_n_kv]] _calls_
- [[nodes/gguf_set_val_u8]] _calls_
- [[nodes/gguf_set_val_i8]] _calls_
- [[nodes/gguf_set_val_u16]] _calls_
- [[nodes/gguf_set_val_i16]] _calls_
- [[nodes/gguf_set_val_u32]] _calls_
- [[nodes/gguf_set_val_i32]] _calls_
- [[nodes/gguf_set_val_f32]] _calls_
- [[nodes/gguf_set_val_u64]] _calls_
- [[nodes/gguf_set_val_i64]] _calls_
- [[nodes/gguf_set_val_f64]] _calls_
- [[nodes/gguf_set_val_bool]] _calls_
- [[nodes/gguf_set_val_str]] _calls_
- [[nodes/get_ne]] _calls_
- [[nodes/gguf_set_arr_data]] _calls_
- [[nodes/gguf_set_arr_str]] _calls_
- [[nodes/gguf_find_tensor]] _calls_
- [[nodes/empty]] _calls_
- [[nodes/ggml_nbytes]] _calls_

## Used By

- [[nodes/run_merge]] _calls_
- [[nodes/zeros]] _calls_
- [[nodes/gguf_merge]] _calls_
- [[nodes/llama_model_quantize_impl]] _calls_
- [[nodes/same_tensor_data]] _calls_
