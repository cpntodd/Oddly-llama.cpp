---
name: "process_single_task"
type: "function"
file: "tools/server/server-context.cpp"
community: "tools"
---

# process_single_task

**Type:** `function`  **File:** `tools/server/server-context.cpp`

**Community:** [[communities/tools]]

## Depends On

- [[nodes/tokenize_cli_input]] _calls_
- [[nodes/is_processing]] _calls_
- [[nodes/size]] _calls_
- [[nodes/launch_slots_with_parent_task]] _calls_
- [[nodes/launch_slot_with_task]] _calls_
- [[nodes/prompt_save]] _calls_
- [[nodes/update]] _calls_
- [[nodes/prompt_clear]] _calls_
- [[nodes/release]] _calls_
- [[nodes/common_sampler_reasoning_budget_force]] _calls_
- [[nodes/push_back]] _calls_
- [[nodes/to_json]] _calls_
- [[nodes/send_error]] _calls_
- [[nodes/ggml_time_us]] _calls_
- [[nodes/serialize]] _calls_
- [[nodes/llama_state_seq_save_file]] _calls_
- [[nodes/data]] _calls_
- [[nodes/llama_state_seq_load_file]] _calls_
- [[nodes/deserialize]] _calls_
- [[nodes/clear]] _calls_
- [[nodes/llama_adapter_get_alora_n_invocation_tokens]] _calls_
- [[nodes/common_token_to_piece]] _calls_

## Used By

- [[nodes/load_model]] _calls_
