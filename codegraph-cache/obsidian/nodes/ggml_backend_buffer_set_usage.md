---
name: "ggml_backend_buffer_set_usage"
type: "function"
file: "ggml/src/ggml-backend.cpp"
community: "ggml"
---

# ggml_backend_buffer_set_usage

**Type:** `function`  **File:** `ggml/src/ggml-backend.cpp`

**Community:** [[communities/ggml]]

## Depends On

- [[nodes/ggml_backend_buffer_is_multi_buffer]] _calls_
- [[nodes/ggml_backend_multi_buffer_set_usage]] _calls_

## Used By

- [[nodes/load_tensors]] _calls_
- [[nodes/params]] _calls_
- [[nodes/ggml_backend_multi_buffer_set_usage]] _calls_
- [[nodes/ggml_vbuffer_alloc]] _calls_
- [[nodes/matches_filter]] _calls_
- [[nodes/eval_perf]] _calls_
