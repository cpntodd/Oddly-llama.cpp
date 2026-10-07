---
name: "category_is_attn_v"
type: "function"
file: "src/llama-quant.cpp"
community: "src"
---

# category_is_attn_v

**Type:** `function`  **File:** `src/llama-quant.cpp`

**Community:** [[communities/src]]

## Depends On

- [[nodes/quantize_state_impl]] _calls_
- [[nodes/params]] _calls_
- [[nodes/size]] _calls_
- [[nodes/ggml_get_type_traits]] _calls_
- [[nodes/ggml_is_quantized]] _calls_
- [[nodes/format]] _calls_
- [[nodes/ggml_type_name]] _calls_
- [[nodes/ggml_fp16_to_fp32_row]] _calls_
- [[nodes/ggml_bf16_to_fp32_row]] _calls_
- [[nodes/ggml_blck_size]] _calls_
- [[nodes/ggml_type_size]] _calls_
- [[nodes/clear]] _calls_

## Used By

- [[nodes/llama_tensor_get_type_impl]] _calls_
- [[nodes/init_quantize_state_counters]] _calls_
