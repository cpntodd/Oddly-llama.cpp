---
name: "generate_response"
type: "function"
file: "tools/mtmd/mtmd-cli.cpp"
community: "common"
---

# generate_response

**Type:** `function`  **File:** `tools/mtmd/mtmd-cli.cpp`

**Community:** [[communities/common]]

## Depends On

- [[nodes/common_sampler_sample]] _calls_
- [[nodes/push_back]] _calls_
- [[nodes/common_sampler_accept]] _calls_
- [[nodes/llama_vocab_is_eog]] _calls_
- [[nodes/check_antiprompt]] _calls_
- [[nodes/common_token_to_piece]] _calls_
- [[nodes/common_batch_clear]] _calls_
- [[nodes/common_detokenize]] _calls_

## Used By

- [[nodes/main]] _calls_
