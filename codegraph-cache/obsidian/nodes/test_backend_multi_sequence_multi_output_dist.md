---
name: "test_backend_multi_sequence_multi_output_dist"
type: "function"
file: "tests/test-backend-sampler.cpp"
community: "tests"
---

# test_backend_multi_sequence_multi_output_dist

**Type:** `function`  **File:** `tests/test-backend-sampler.cpp`

**Community:** [[communities/tests]]

## Depends On

- [[nodes/llama_vocab_n_tokens]] _calls_
- [[nodes/llama_sampler_chain_default_params]] _calls_
- [[nodes/llama_sampler_chain_add]] _calls_
- [[nodes/llama_vocab_bos]] _calls_
- [[nodes/llama_vocab_eos]] _calls_
- [[nodes/llama_batch_init]] _calls_
- [[nodes/llama_sampler_sample]] _calls_
- [[nodes/llama_get_sampled_logits_count_ith]] _calls_
- [[nodes/llama_get_sampled_probs_count_ith]] _calls_
- [[nodes/llama_batch_free]] _calls_
