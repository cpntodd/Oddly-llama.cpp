---
name: "llama_completion"
type: "function"
file: "tools/completion/completion.cpp"
community: "common"
---

# llama_completion

**Type:** `function`  **File:** `tools/completion/completion.cpp`

**Community:** [[communities/common]]

## Depends On

- [[nodes/common_init]] _calls_
- [[nodes/common_params_parse]] _calls_
- [[nodes/init]] _calls_
- [[nodes/cleanup]] _calls_
- [[nodes/llama_backend_init]] _calls_
- [[nodes/llama_numa_init]] _calls_
- [[nodes/common_init_from_params]] _calls_
- [[nodes/sampler]] _calls_
- [[nodes/llama_get_memory]] _calls_
- [[nodes/llama_perf_context_reset]] _calls_
- [[nodes/llama_model_n_ctx_train]] _calls_
- [[nodes/llama_n_ctx]] _calls_
- [[nodes/tokens]] _calls_
- [[nodes/common_chat_templates_was_explicit]] _calls_
- [[nodes/empty]] _calls_
- [[nodes/common_params_get_system_info]] _calls_
- [[nodes/file_exists]] _calls_
- [[nodes/llama_vocab_get_add_bos]] _calls_
- [[nodes/llama_model_has_encoder]] _calls_
- [[nodes/llama_vocab_get_add_eos]] _calls_
- [[nodes/push_back]] _calls_
- [[nodes/string_from]] _calls_
- [[nodes/llama_vocab_bos]] _calls_
- [[nodes/size]] _calls_
- [[nodes/llama_memory_clear]] _calls_
- [[nodes/clear]] _calls_
- [[nodes/common_replay_last_token]] _calls_
- [[nodes/common_token_to_piece]] _calls_
- [[nodes/sigaction]] _calls_
- [[nodes/sigint_handler]] _calls_

## Used By

- [[nodes/main]] _calls_
- [[nodes/sigint_handler]] _calls_
