---
name: "flush_deferred"
type: "function"
file: "common/speculative.cpp"
community: "common"
---

# flush_deferred

**Type:** `function`  **File:** `common/speculative.cpp`

**Community:** [[communities/common]]

## Depends On

- [[nodes/common_batch_clear]] _calls_
- [[nodes/common_speculative_impl_draft_mtp]] _calls_
- [[nodes/common_speculative_impl]] _calls_
- [[nodes/llama_model_n_embd_out]] _calls_
- [[nodes/llama_model_n_layer_nextn]] _calls_
- [[nodes/ggml_type_name]] _calls_
- [[nodes/common_speculative_get_devices_str]] _calls_
- [[nodes/llama_n_batch]] _calls_
- [[nodes/llama_batch_init]] _calls_
- [[nodes/reset]] _calls_
- [[nodes/assign]] _calls_
- [[nodes/llama_sampler_chain_default_params]] _calls_
- [[nodes/llama_sampler_chain_add]] _calls_
- [[nodes/llama_set_sampler]] _calls_
- [[nodes/llama_sampler_free]] _calls_
- [[nodes/llama_set_embeddings_nextn]] _calls_
- [[nodes/size]] _calls_
- [[nodes/clear]] _calls_
- [[nodes/llama_batch_free]] _calls_
- [[nodes/llama_get_memory]] _calls_
- [[nodes/it]] _calls_
- [[nodes/can_defer]] _calls_
- [[nodes/empty]] _calls_
- [[nodes/llama_set_nextn_layer_offset]] _calls_
- [[nodes/common_speculative_mtp_first_decode_fits]] _calls_
- [[nodes/common_sampler_reset]] _calls_
- [[nodes/common_sampler_sample]] _calls_
- [[nodes/common_token_to_piece]] _calls_
- [[nodes/llama_vocab_n_tokens]] _calls_
- [[nodes/vocab]] _calls_
