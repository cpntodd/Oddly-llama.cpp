---
name: "buf"
type: "function"
file: "ggml/src/gguf.cpp"
community: "ggml"
---

# buf

**Type:** `function`  **File:** `ggml/src/gguf.cpp`

**Community:** [[communities/ggml]]

## Depends On

- [[nodes/gguf_writer_buf]] _calls_
- [[nodes/write]] _calls_
- [[nodes/ggml_is_contiguous]] _calls_
- [[nodes/ggml_nbytes]] _calls_
- [[nodes/ggml_backend_tensor_get]] _calls_
- [[nodes/pad]] _calls_

## Used By

- [[nodes/merge_tensor]] _calls_
- [[nodes/get_server_exec_path]] _calls_
- [[nodes/add_media]] _calls_
- [[nodes/clip_log_internal]] _calls_
- [[nodes/print_debug_tensor]] _calls_
- [[nodes/format]] _calls_
- [[nodes/llama_model_get_tok_embd]] _calls_
- [[nodes/string_format]] _calls_
- [[nodes/common_chat_extra_context]] _calls_
- [[nodes/file]] _calls_
- [[nodes/get_device_backend_and_type]] _calls_
- [[nodes/max]] _calls_
- [[nodes/init_tensor_tril]] _calls_
- [[nodes/matches_filter]] _calls_
- [[nodes/eval_perf]] _calls_
- [[nodes/eval_grad]] _calls_
