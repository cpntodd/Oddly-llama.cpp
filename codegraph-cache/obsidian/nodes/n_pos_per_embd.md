---
name: "n_pos_per_embd"
type: "function"
file: "src/llama-batch.cpp"
community: "src"
---

# n_pos_per_embd

**Type:** `function`  **File:** `src/llama-batch.cpp`

**Community:** [[communities/src]]

## Depends On

- [[nodes/llama_ubatch]] _imports_
- [[nodes/no_init]] _imports_
- [[nodes/llama_vocab_pre_type]] _imports_
- [[nodes/llama_ubatch]] _imports_
- [[nodes/getenv]] _calls_
- [[nodes/clear]] _calls_
- [[nodes/size]] _calls_
- [[nodes/insert]] _calls_
- [[nodes/set]] _calls_
- [[nodes/push_back]] _calls_
- [[nodes/empty]] _calls_
- [[nodes/only]] _calls_
- [[nodes/get_n_tokens]] _calls_
- [[nodes/n_remaining]] _calls_

## Used By

- [[nodes/hparams]] _calls_
- [[nodes/ggml_gen_hadamard]] _calls_
- [[nodes/set_input_kq_mask_impl]] _calls_
- [[nodes/max_nodes]] _calls_
- [[nodes/ctx_type_to_graph_type]] _calls_
- [[nodes/needs_raw_logits]] _calls_
