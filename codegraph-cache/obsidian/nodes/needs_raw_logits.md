---
name: "needs_raw_logits"
type: "function"
file: "src/llama-context.cpp"
community: "src"
---

# needs_raw_logits

**Type:** `function`  **File:** `src/llama-context.cpp`

**Community:** [[communities/src]]

## Depends On

- [[nodes/n_embd_out]] _calls_
- [[nodes/empty]] _calls_
- [[nodes/get_n_tokens]] _calls_
- [[nodes/clear]] _calls_
- [[nodes/ggml_time_us]] _calls_
- [[nodes/llama_sampler_backend_begin]] _calls_
- [[nodes/ctx_type_to_graph_type]] _calls_
- [[nodes/format]] _calls_
- [[nodes/ggml_graph_dump_dot]] _calls_
- [[nodes/ggml_backend_sched_get_tensor_backend]] _calls_
- [[nodes/ggml_backend_tensor_get_async]] _calls_
- [[nodes/models]] _calls_
- [[nodes/size]] _calls_
- [[nodes/swap]] _calls_
- [[nodes/push_back]] _calls_
- [[nodes/ggml_backend_buffer_get_size]] _calls_
- [[nodes/ggml_backend_cpu_buffer_type]] _calls_
- [[nodes/ggml_backend_dev_host_buffer_type]] _calls_
- [[nodes/ggml_backend_buft_alloc_buffer]] _calls_
- [[nodes/ggml_backend_buffer_clear]] _calls_
- [[nodes/ggml_nbytes]] _calls_
- [[nodes/llama_sampler_backend_n_nodes]] _calls_
- [[nodes/get_gf_res_reserve]] _calls_
- [[nodes/ggml_backend_sched_reset]] _calls_
- [[nodes/n_pos_per_embd]] _calls_
- [[nodes/ggml_backend_sched_reserve_size]] _calls_
- [[nodes/ggml_backend_sched_split_graph]] _calls_
- [[nodes/ggml_backend_sched_reserve]] _calls_
- [[nodes/graph_compute]] _calls_
- [[nodes/ggml_backend_dev_backend_reg]] _calls_
