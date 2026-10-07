---
name: "test_backends"
type: "function"
file: "tests/test-llama-archs.cpp"
community: "tests"
---

# test_backends

**Type:** `function`  **File:** `tests/test-llama-archs.cpp`

**Community:** [[communities/tests]]

## Depends On

- [[nodes/llama_log_get]] _calls_
- [[nodes/llama_log_set]] _calls_
- [[nodes/device_config]] _calls_
- [[nodes/ggml_backend_dev_count]] _calls_
- [[nodes/ggml_backend_dev_get]] _calls_
- [[nodes/ggml_backend_dev_buffer_type]] _calls_
- [[nodes/ggml_backend_cpu_buffer_type]] _calls_
- [[nodes/llm_arch_all]] _calls_
- [[nodes/string]] _calls_
- [[nodes/to_string]] _calls_
- [[nodes/common_log_flush]] _calls_
- [[nodes/moe_implemented]] _calls_
- [[nodes/moe_mandatory]] _calls_
- [[nodes/get_gguf_ctx]] _calls_
- [[nodes/gguf_remove_key]] _calls_
- [[nodes/arch_supported]] _calls_
- [[nodes/llm_arch_supports_sm_tensor]] _calls_
- [[nodes/llama_model_saver_supports_arch]] _calls_
- [[nodes/llama_model_saver]] _calls_

## Used By

- [[nodes/main]] _calls_
