---
name: "common_sampler_sample"
type: "function"
file: "common/sampling.cpp"
community: "common"
---

# common_sampler_sample

**Type:** `function`  **File:** `common/sampling.cpp`

**Community:** [[communities/common]]

## Depends On

- [[nodes/llama_synchronize]] _calls_
- [[nodes/tm]] _calls_
- [[nodes/set_logits]] _calls_
- [[nodes/llama_get_sampled_token_ith]] _calls_
- [[nodes/llama_sampler_apply]] _calls_
- [[nodes/grammar_should_apply]] _calls_
- [[nodes/grammar]] _calls_
- [[nodes/size]] _calls_
- [[nodes/common_sampler_accept]] _calls_
- [[nodes/push_back]] _calls_

## Used By

- [[nodes/llama_completion]] _calls_
- [[nodes/post_decode]] _calls_
- [[nodes/generate_response]] _calls_
- [[nodes/main]] _calls_
- [[nodes/is_valid_utf8]] _calls_
- [[nodes/main]] _calls_
- [[nodes/main]] _calls_
- [[nodes/main]] _calls_
- [[nodes/main]] _calls_
- [[nodes/main]] _calls_
- [[nodes/common_speculative_get_devices_str]] _calls_
- [[nodes/flush_deferred]] _calls_
