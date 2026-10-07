---
name: "ggml_backend_supports_op"
type: "function"
file: "ggml/src/ggml-backend.cpp"
community: "ggml"
---

# ggml_backend_supports_op

**Type:** `function`  **File:** `ggml/src/ggml-backend.cpp`

**Community:** [[communities/ggml]]

## Depends On

- [[nodes/ggml_backend_dev_supports_op]] _calls_

## Used By

- [[nodes/reserve_compute_meta]] _calls_
- [[nodes/needs_raw_logits]] _calls_
- [[nodes/main]] _calls_
- [[nodes/ggml_backend_sched_backend_from_buffer]] _calls_
- [[nodes/ggml_backend_sched_backend_id_from_cur]] _calls_
- [[nodes/ggml_backend_sched_set_if_supported]] _calls_
- [[nodes/ggml_backend_sched_split_graph]] _calls_
- [[nodes/matches_filter]] _calls_
- [[nodes/eval_perf]] _calls_
- [[nodes/eval_support]] _calls_
- [[nodes/eval_grad]] _calls_
