---
name: "ggml_backend_alloc_ctx_tensors_from_buft"
type: "function"
file: "ggml/src/ggml-alloc.c"
community: "src"
---

# ggml_backend_alloc_ctx_tensors_from_buft

**Type:** `function`  **File:** `ggml/src/ggml-alloc.c`

**Community:** [[communities/src]]

## Depends On

- [[nodes/ggml_backend_buft_is_meta]] _calls_

## Used By

- [[nodes/load_tensors]] _calls_
- [[nodes/hparams]] _calls_
- [[nodes/dsv4_make_k_only]] _calls_
- [[nodes/params]] _calls_
- [[nodes/llama_adapter_lora_init_impl]] _calls_
- [[nodes/ggml_gen_hadamard]] _calls_
- [[nodes/needs_raw_logits]] _calls_
- [[nodes/test_multiple_buffer_types]] _calls_
- [[nodes/ggml_backend_meta_buffer_type_alloc_buffer]] _calls_
- [[nodes/ggml_backend_alloc_ctx_tensors]] _calls_
- [[nodes/ggml_opt_build]] _calls_
