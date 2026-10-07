---
name: "load_vocab"
type: "function"
file: "examples/convert-llama2c-to-ggml/convert-llama2c-to-ggml.cpp"
community: "ggml"
---

# load_vocab

**Type:** `function`  **File:** `examples/convert-llama2c-to-ggml/convert-llama2c-to-ggml.cpp`

**Community:** [[communities/ggml]]

## Depends On

- [[nodes/is_ggml_file]] _calls_
- [[nodes/gguf_find_key]] _calls_
- [[nodes/gguf_get_kv_type]] _calls_
- [[nodes/gguf_get_arr_type]] _calls_
- [[nodes/gguf_get_arr_n]] _calls_
- [[nodes/ggml_free]] _calls_
- [[nodes/gguf_free]] _calls_
- [[nodes/file]] _calls_
- [[nodes/read_u32]] _calls_
- [[nodes/read_f32]] _calls_
- [[nodes/read_string]] _calls_
- [[nodes/llama_escape_whitespaces]] _calls_

## Used By

- [[nodes/llama_prepare_model_devices]] _calls_
- [[nodes/params]] _calls_
- [[nodes/main]] _calls_
