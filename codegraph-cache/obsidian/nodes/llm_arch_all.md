---
name: "llm_arch_all"
type: "function"
file: "tests/test-llama-archs.cpp"
community: "tests"
---

# llm_arch_all

**Type:** `function`  **File:** `tests/test-llama-archs.cpp`

**Community:** [[communities/tests]]

## Depends On

- [[nodes/moe_implemented]] _calls_
- [[nodes/moe_mandatory]] _calls_
- [[nodes/llama_model_saver_supports_arch]] _calls_
- [[nodes/arch_supported]] _calls_
- [[nodes/get_gguf_ctx]] _calls_
- [[nodes/llama_model_save_to_file]] _calls_
- [[nodes/llama_log_set]] _calls_

## Used By

- [[nodes/arch]] _calls_
- [[nodes/test_backends]] _calls_
