---
name: "ggml_graph_overhead_custom"
type: "function"
file: "ggml/src/ggml.c"
community: "ggml"
---

# ggml_graph_overhead_custom

**Type:** `function`  **File:** `ggml/src/ggml.c`

**Community:** [[communities/ggml]]

## Depends On

- [[nodes/ggml_graph_nbytes]] _calls_

## Used By

- [[nodes/llama_sampler_backend_copy_state]] _calls_
- [[nodes/max_nodes]] _calls_
- [[nodes/llama_set_param]] _calls_
- [[nodes/ggml_backend_meta_graph_compute]] _calls_
- [[nodes/ggml_backend_sched_compute_splits]] _calls_
- [[nodes/ggml_backend_graph_copy]] _calls_
- [[nodes/ggml_graph_overhead]] _calls_
- [[nodes/ggml_opt_alloc]] _calls_
- [[nodes/ggml_backend_rpc_get_device_memory]] _calls_
- [[nodes/apir_untrack_backend_buffer]] _calls_
- [[nodes/eval_perf]] _calls_
- [[nodes/eval_support]] _calls_
- [[nodes/eval_grad]] _calls_
