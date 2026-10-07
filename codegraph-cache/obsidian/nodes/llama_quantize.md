---
name: "llama_quantize"
type: "function"
file: "tools/quantize/quantize.cpp"
community: "tools"
---

# llama_quantize

**Type:** `function`  **File:** `tools/quantize/quantize.cpp`

**Community:** [[communities/tools]]

## Depends On

- [[nodes/usage]] _calls_
- [[nodes/llama_model_quantize_default_params]] _calls_
- [[nodes/llama_backend_init]] _calls_
- [[nodes/try_parse_ftype]] _calls_
- [[nodes/llama_time_us]] _calls_
- [[nodes/llama_backend_free]] _calls_

## Used By

- [[nodes/main]] _calls_
- [[nodes/parse_layer_prune]] _calls_
