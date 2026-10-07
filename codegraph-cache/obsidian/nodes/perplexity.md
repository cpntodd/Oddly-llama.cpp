---
name: "perplexity"
type: "function"
file: "tools/perplexity/perplexity.cpp"
community: "common"
---

# perplexity

**Type:** `function`  **File:** `tools/perplexity/perplexity.cpp`

**Community:** [[communities/common]]

## Depends On

- [[nodes/perplexity_v2]] _calls_
- [[nodes/llama_vocab_get_add_bos]] _calls_
- [[nodes/llama_vocab_get_add_eos]] _calls_
- [[nodes/llama_vocab_n_tokens]] _calls_
- [[nodes/llama_batch_init]] _calls_
- [[nodes/llama_memory_clear]] _calls_
- [[nodes/llama_get_memory]] _calls_
- [[nodes/llama_vocab_bos]] _calls_
- [[nodes/llama_synchronize]] _calls_
- [[nodes/llama_batch_free]] _calls_

## Used By

- [[nodes/llama_perplexity]] _calls_
- [[nodes/common_params_parser_init]] _calls_
