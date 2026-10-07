---
name: "post_decode"
type: "function"
file: "tools/server/server-context.cpp"
community: "tools"
---

# post_decode

**Type:** `function`  **File:** `tools/server/server-context.cpp`

**Community:** [[communities/tools]]

## Depends On

- [[nodes/iterate]] _calls_
- [[nodes/string_format]] _calls_
- [[nodes/send_partial_response]] _calls_
- [[nodes/send_embedding]] _calls_
- [[nodes/release]] _calls_
- [[nodes/send_rerank]] _calls_
- [[nodes/can_speculate]] _calls_
- [[nodes/common_speculative_begin]] _calls_
- [[nodes/empty]] _calls_
- [[nodes/common_sampler_sample]] _calls_
- [[nodes/common_sampler_accept]] _calls_
- [[nodes/llama_context]] _calls_
- [[nodes/ggml_time_us]] _calls_
- [[nodes/common_token_to_piece]] _calls_
- [[nodes/populate_token_probs]] _calls_
- [[nodes/process_token]] _calls_
- [[nodes/print_timings]] _calls_
- [[nodes/send_final_response]] _calls_
- [[nodes/print_timings_tg]] _calls_
- [[nodes/size]] _calls_
- [[nodes/clear]] _calls_
- [[nodes/llama_n_rs_seq]] _calls_
- [[nodes/tokens]] _calls_
- [[nodes/common_sampler_copy]] _calls_
- [[nodes/common_speculative_accept]] _calls_
- [[nodes/common_speculative_n_max]] _calls_
- [[nodes/n_tokens]] _calls_

## Used By

- [[nodes/update_slots]] _calls_
- [[nodes/pre_decode]] _calls_
