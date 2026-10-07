---
name: "test_seq_cp_host"
type: "function"
file: "tests/test-save-load-state.cpp"
community: "tests"
---

# test_seq_cp_host

**Type:** `function`  **File:** `tests/test-save-load-state.cpp`

**Community:** [[communities/tests]]

## Depends On

- [[nodes/common_context_params_to_llama]] _calls_
- [[nodes/llama_sampler_chain_default_params]] _calls_
- [[nodes/llama_sampler_chain_add]] _calls_
- [[nodes/llama_state_load_file]] _calls_
- [[nodes/data]] _calls_
- [[nodes/common_replay_last_token]] _calls_
- [[nodes/llama_state_seq_get_size]] _calls_
- [[nodes/llama_state_seq_get_data]] _calls_
- [[nodes/llama_memory_clear]] _calls_
- [[nodes/llama_get_memory]] _calls_
- [[nodes/llama_state_seq_set_data]] _calls_
- [[nodes/generate_tokens]] _calls_

## Used By

- [[nodes/main]] _calls_
