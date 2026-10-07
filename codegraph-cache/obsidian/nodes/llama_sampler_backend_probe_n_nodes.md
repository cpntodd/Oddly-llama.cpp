---
name: "llama_sampler_backend_probe_n_nodes"
type: "function"
file: "src/llama-sampler.cpp"
community: "tests"
---

# llama_sampler_backend_probe_n_nodes

**Type:** `function`  **File:** `src/llama-sampler.cpp`

**Community:** [[communities/tests]]

## Depends On

- [[nodes/ggml_get_first_tensor]] _calls_
- [[nodes/ggml_get_next_tensor]] _calls_
- [[nodes/ggml_graph_n_nodes]] _calls_
- [[nodes/ggml_backend_buft_get_device]] _calls_
- [[nodes/ggml_graph_node]] _calls_
- [[nodes/ggml_backend_dev_supports_op]] _calls_
- [[nodes/ggml_op_name]] _calls_
- [[nodes/name]] _calls_

## Used By

- [[nodes/llama_sampler_chain_free]] _calls_
