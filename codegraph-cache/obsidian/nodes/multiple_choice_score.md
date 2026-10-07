---
name: "multiple_choice_score"
type: "function"
file: "tools/perplexity/perplexity.cpp"
community: "common"
---

# multiple_choice_score

**Type:** `function`  **File:** `tools/perplexity/perplexity.cpp`

**Community:** [[communities/common]]

## Depends On

- [[nodes/deserialize]] _calls_
- [[nodes/counter]] _calls_
- [[nodes/multiple_choice_prepare_one_task]] _calls_
- [[nodes/llama_n_ctx]] _calls_
- [[nodes/llama_vocab_n_tokens]] _calls_
- [[nodes/llama_n_seq_max]] _calls_
- [[nodes/llama_batch_init]] _calls_
- [[nodes/common_batch_clear]] _calls_
- [[nodes/value]] _calls_
- [[nodes/llama_batch_add]] _calls_
- [[nodes/llama_memory_clear]] _calls_
- [[nodes/llama_get_memory]] _calls_
- [[nodes/decode_helper]] _calls_
- [[nodes/llama_batch_free]] _calls_

## Used By

- [[nodes/llama_perplexity]] _calls_
