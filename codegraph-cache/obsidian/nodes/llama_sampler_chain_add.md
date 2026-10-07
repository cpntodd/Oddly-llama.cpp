---
name: "llama_sampler_chain_add"
type: "function"
file: "src/llama-sampler.cpp"
community: "tests"
---

# llama_sampler_chain_add

**Type:** `function`  **File:** `src/llama-sampler.cpp`

**Community:** [[communities/tests]]

## Depends On

- [[nodes/push_back]] _calls_
- [[nodes/size]] _calls_

## Used By

- [[nodes/llama_sampler_chain_reset]] _calls_
- [[nodes/main]] _calls_
- [[nodes/add_gumbel_noise]] _calls_
- [[nodes/main]] _calls_
- [[nodes/main]] _calls_
- [[nodes/llama_batch_add]] _calls_
- [[nodes/main]] _calls_
- [[nodes/main]] _calls_
- [[nodes/test_sampler_chain]] _calls_
- [[nodes/test_baseline]] _calls_
- [[nodes/test_state_load]] _calls_
- [[nodes/test_seq_cp_host]] _calls_
- [[nodes/test_seq_cp_device]] _calls_
- [[nodes/test_backend_greedy_sampling]] _calls_
- [[nodes/test_backend_top_k_sampling]] _calls_
- [[nodes/test_backend_temp_sampling]] _calls_
- [[nodes/test_backend_temp_ext_sampling]] _calls_
- [[nodes/test_backend_min_p_sampling]] _calls_
- [[nodes/test_backend_top_p_sampling]] _calls_
- [[nodes/test_backend_multi_sequence_sampling]] _calls_
- [[nodes/test_backend_dist_sampling]] _calls_
- [[nodes/test_backend_dist_sampling_and_cpu]] _calls_
- [[nodes/test_backend_logit_bias_sampling]] _calls_
- [[nodes/accept_prompt]] _calls_
- [[nodes/find_backend_logit]] _calls_
- [[nodes/test_backend_mixed_sampling]] _calls_
- [[nodes/test_backend_set_sampler]] _calls_
- [[nodes/test_backend_cpu_mixed_batch]] _calls_
- [[nodes/test_backend_multi_output_limit]] _calls_
- [[nodes/test_backend_multi_sequence_multi_output_dist]] _calls_
