---
name: "llama_bench"
type: "function"
file: "tools/llama-bench/llama-bench.cpp"
community: "tests"
---

# llama_bench

**Type:** `function`  **File:** `tools/llama-bench/llama-bench.cpp`

**Community:** [[communities/tests]]

## Depends On

- [[nodes/ggml_backend_load_all]] _calls_
- [[nodes/parse_cmd_params]] _calls_
- [[nodes/ggml_backend_dev_by_type]] _calls_
- [[nodes/ggml_backend_dev_backend_reg]] _calls_
- [[nodes/decltype]] _calls_
- [[nodes/llama_log_set]] _calls_
- [[nodes/llama_backend_init]] _calls_
- [[nodes/llama_numa_init]] _calls_
- [[nodes/set_process_priority]] _calls_
- [[nodes/print_header]] _calls_
- [[nodes/to_llama_mparams]] _calls_
- [[nodes/to_llama_cparams]] _calls_
- [[nodes/llama_max_devices]] _calls_
- [[nodes/llama_max_tensor_buft_overrides]] _calls_
- [[nodes/llama_model_free]] _calls_
- [[nodes/llama_model_default_params]] _calls_
- [[nodes/equal_mparams]] _calls_
- [[nodes/llama_memory_clear]] _calls_
- [[nodes/llama_get_memory]] _calls_
- [[nodes/ggml_threadpool_params_default]] _calls_
- [[nodes/parse_cpu_mask]] _calls_
- [[nodes/llama_free]] _calls_
- [[nodes/test_prompt]] _calls_
- [[nodes/test_gen]] _calls_
- [[nodes/llama_state_seq_set_data]] _calls_
- [[nodes/llama_state_seq_get_size]] _calls_
- [[nodes/llama_state_seq_get_data]] _calls_
- [[nodes/get_time_ns]] _calls_
- [[nodes/llama_perf_context_print]] _calls_
- [[nodes/print_footer]] _calls_

## Used By

- [[nodes/main]] _calls_
- [[nodes/get_sql_field_type]] _calls_
- [[nodes/llama_null_log_callback]] _calls_
