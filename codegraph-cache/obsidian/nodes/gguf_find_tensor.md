---
name: "gguf_find_tensor"
type: "function"
file: "ggml/src/gguf.cpp"
community: "ggml"
---

# gguf_find_tensor

**Type:** `function`  **File:** `ggml/src/gguf.cpp`

**Community:** [[communities/ggml]]

## Depends On

- [[nodes/gguf_get_n_tensors]] _calls_

## Used By

- [[nodes/read_tensor_data]] _calls_
- [[nodes/main]] _calls_
- [[nodes/load_tensors]] _calls_
- [[nodes/write]] _calls_
- [[nodes/select_weight_buft]] _calls_
- [[nodes/llama_model_saver_supports_arch]] _calls_
- [[nodes/llama_adapter_lora_init_impl]] _calls_
- [[nodes/llama_model_quantize_impl]] _calls_
- [[nodes/handcrafted_check_tensors]] _calls_
- [[nodes/handcrafted_check_tensor_data]] _calls_
- [[nodes/all_tensors_in_other]] _calls_
- [[nodes/gguf_set_kv]] _calls_
- [[nodes/gguf_set_tensor_type]] _calls_
- [[nodes/gguf_set_tensor_data]] _calls_
- [[nodes/common_speculative_type_from_name]] _calls_
