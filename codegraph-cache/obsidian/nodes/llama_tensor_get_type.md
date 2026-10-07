---
name: "llama_tensor_get_type"
type: "function"
file: "src/llama-quant.cpp"
community: "ggml"
---

# llama_tensor_get_type

**Type:** `function`  **File:** `src/llama-quant.cpp`

**Community:** [[communities/ggml]]

## Depends On

- [[nodes/tensor_allows_quantization]] _calls_
- [[nodes/ggml_is_quantized]] _calls_
- [[nodes/empty]] _calls_
- [[nodes/ggml_type_name]] _calls_
- [[nodes/llama_tensor_get_type_impl]] _calls_
- [[nodes/tensor_type_fallback]] _calls_

## Used By

- [[nodes/llama_model_quantize_impl]] _calls_
- [[nodes/llama_quant_free]] _calls_
