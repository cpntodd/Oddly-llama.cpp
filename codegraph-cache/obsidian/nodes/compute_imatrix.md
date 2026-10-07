---
name: "compute_imatrix"
type: "function"
file: "tools/imatrix/imatrix.cpp"
community: "common"
---

# compute_imatrix

**Type:** `function`  **File:** `tools/imatrix/imatrix.cpp`

**Community:** [[communities/common]]

## Depends On

- [[nodes/llama_vocab_get_add_bos]] _calls_
- [[nodes/llama_vocab_get_add_eos]] _calls_
- [[nodes/llama_vocab_n_tokens]] _calls_
- [[nodes/llama_batch_init]] _calls_
- [[nodes/llama_memory_clear]] _calls_
- [[nodes/llama_get_memory]] _calls_
- [[nodes/common_batch_clear]] _calls_
- [[nodes/llama_vocab_bos]] _calls_
- [[nodes/when]] _calls_
- [[nodes/llama_batch_free]] _calls_
- [[nodes/llama_synchronize]] _calls_

## Used By

- [[nodes/main]] _calls_
