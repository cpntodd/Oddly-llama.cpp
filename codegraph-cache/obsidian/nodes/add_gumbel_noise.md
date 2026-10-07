---
name: "add_gumbel_noise"
type: "function"
file: "examples/diffusion/diffusion.cpp"
community: "tests"
---

# add_gumbel_noise

**Type:** `function`  **File:** `examples/diffusion/diffusion.cpp`

**Community:** [[communities/tests]]

## Depends On

- [[nodes/log.comp.cpp]] _imports_
- [[nodes/fill_templated_filename]] _imports_
- [[nodes/llama_set_causal_attn]] _calls_
- [[nodes/llama_vocab_n_tokens]] _calls_
- [[nodes/llama_sampler_chain_default_params]] _calls_
- [[nodes/llama_sampler_chain_add]] _calls_
- [[nodes/llama_batch_init]] _calls_
- [[nodes/ggml_time_us]] _calls_
- [[nodes/llama_sampler_apply]] _calls_
- [[nodes/llama_batch_free]] _calls_
- [[nodes/llama_sampler_free]] _calls_

## Used By

- [[nodes/callback_data]] _imports_
