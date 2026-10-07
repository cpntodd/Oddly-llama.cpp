---
name: "llama_batched_bench"
type: "function"
file: "tools/batched-bench/batched-bench.cpp"
community: "common"
---

# llama_batched_bench

**Type:** `function`  **File:** `tools/batched-bench/batched-bench.cpp`

**Community:** [[communities/common]]

## Depends On

- [[nodes/common_init]] _calls_
- [[nodes/common_params_parse]] _calls_
- [[nodes/llama_backend_init]] _calls_
- [[nodes/llama_numa_init]] _calls_
- [[nodes/common_model_params_to_llama]] _calls_
- [[nodes/common_context_params_to_llama]] _calls_
- [[nodes/llama_model_free]] _calls_
- [[nodes/llama_vocab_n_tokens]] _calls_
- [[nodes/llama_get_memory]] _calls_
- [[nodes/llama_n_ctx]] _calls_
- [[nodes/llama_batch_init]] _calls_
- [[nodes/llama_synchronize]] _calls_
- [[nodes/decode_helper]] _calls_
- [[nodes/llama_free]] _calls_
- [[nodes/common_batch_clear]] _calls_
- [[nodes/llama_memory_clear]] _calls_
- [[nodes/ggml_time_us]] _calls_
- [[nodes/llama_perf_context_print]] _calls_
- [[nodes/llama_batch_free]] _calls_
- [[nodes/llama_backend_free]] _calls_

## Used By

- [[nodes/main]] _calls_
- [[nodes/print_usage]] _calls_
