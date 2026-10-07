---
name: "pre_decode"
type: "function"
file: "tools/server/server-context.cpp"
community: "tools"
---

# pre_decode

**Type:** `function`  **File:** `tools/server/server-context.cpp`

**Community:** [[communities/tools]]

## Depends On

- [[nodes/iterate]] _calls_
- [[nodes/n_tokens]] _calls_
- [[nodes/process_token]] _calls_
- [[nodes/send_error]] _calls_
- [[nodes/release]] _calls_
- [[nodes/size]] _calls_
- [[nodes/clear]] _calls_
- [[nodes/can_batch_with]] _calls_
- [[nodes/push_back]] _calls_
- [[nodes/get_n_draft_max]] _calls_
- [[nodes/can_speculate]] _calls_
- [[nodes/empty]] _calls_
- [[nodes/llama_get_memory]] _calls_
- [[nodes/common_speculative_draft]] _calls_
- [[nodes/llama_n_rs_seq]] _calls_
- [[nodes/ggml_time_us]] _calls_
- [[nodes/handle_last_sampled_token]] _calls_
- [[nodes/llama_n_batch]] _calls_
- [[nodes/llama_n_ubatch]] _calls_
- [[nodes/is_processing]] _calls_
- [[nodes/tokens]] _calls_
- [[nodes/common_token_to_piece]] _calls_
- [[nodes/print_timings]] _calls_
- [[nodes/send_final_response]] _calls_
- [[nodes/can_split]] _calls_
- [[nodes/string_format]] _calls_
- [[nodes/llama_memory_can_shift]] _calls_
- [[nodes/common_speculative_set_state]] _calls_
- [[nodes/data]] _calls_
- [[nodes/send_partial_response]] _calls_

## Used By

- [[nodes/update_slots]] _calls_
