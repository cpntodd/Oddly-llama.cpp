---
name: "backends"
type: "function"
file: "ggml/src/ggml-rpc/ggml-rpc.cpp"
community: "ggml"
---

# backends

**Type:** `function`  **File:** `ggml/src/ggml-rpc/ggml-rpc.cpp`

**Community:** [[communities/ggml]]

## Depends On

- [[nodes/rpc_server]] _calls_
- [[nodes/get_alignment]] _calls_
- [[nodes/get_max_size]] _calls_
- [[nodes/copy_tensor]] _calls_
- [[nodes/graph_compute]] _calls_
- [[nodes/get_device_memory]] _calls_

## Used By

- [[nodes/ctx_type_to_graph_type]] _calls_
- [[nodes/ggml_backend_sched_split_graph]] _calls_
