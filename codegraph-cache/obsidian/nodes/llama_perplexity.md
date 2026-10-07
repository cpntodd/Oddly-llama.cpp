---
name: "llama_perplexity"
type: "function"
file: "tools/perplexity/perplexity.cpp"
community: "common"
---

# llama_perplexity

**Type:** `function`  **File:** `tools/perplexity/perplexity.cpp`

**Community:** [[communities/common]]

## Depends On

- [[nodes/common_init]] _calls_
- [[nodes/common_params_parse]] _calls_
- [[nodes/llama_backend_init]] _calls_
- [[nodes/llama_numa_init]] _calls_
- [[nodes/common_init_from_params]] _calls_
- [[nodes/llama_model_n_ctx_train]] _calls_
- [[nodes/tokens]] _calls_
- [[nodes/common_params_get_system_info]] _calls_
- [[nodes/hellaswag_score]] _calls_
- [[nodes/winogrande_score]] _calls_
- [[nodes/multiple_choice_score]] _calls_
- [[nodes/kl_divergence]] _calls_
- [[nodes/perplexity]] _calls_
- [[nodes/llama_perf_context_print]] _calls_
- [[nodes/common_memory_breakdown_print]] _calls_
- [[nodes/llama_backend_free]] _calls_

## Used By

- [[nodes/main]] _calls_
- [[nodes/kl_divergence]] _calls_
- [[nodes/main]] _calls_
