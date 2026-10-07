---
name: "ggml_backend_tensor_set"
type: "function"
file: "ggml/src/ggml-backend.cpp"
community: "tests"
---

# ggml_backend_tensor_set

**Type:** `function`  **File:** `ggml/src/ggml-backend.cpp`

**Community:** [[communities/tests]]

## Depends On

- [[nodes/ggml_nbytes]] _calls_

## Used By

- [[nodes/merge_tensor]] _calls_
- [[nodes/load_tensors]] _calls_
- [[nodes/clip_encode]] _calls_
- [[nodes/list_gen_state_slots]] _calls_
- [[nodes/print_debug_tensor]] _calls_
- [[nodes/fa_init_uniform]] _calls_
- [[nodes/fa_init_kq_mask]] _calls_
- [[nodes/select_weight_buft]] _calls_
- [[nodes/llama_sampler_dist_backend_set_input]] _calls_
- [[nodes/llama_sampler_penalties_backend_set_input]] _calls_
- [[nodes/llama_sampler_logit_bias_backend_set_input]] _calls_
- [[nodes/params]] _calls_
- [[nodes/llama_adapter_lora_init_impl]] _calls_
- [[nodes/ggml_gen_hadamard]] _calls_
- [[nodes/dsv4_set_i64]] _calls_
- [[nodes/dsv4_set_i32]] _calls_
- [[nodes/needs_raw_logits]] _calls_
- [[nodes/llama_set_param]] _calls_
- [[nodes/get_random_gguf_context]] _calls_
- [[nodes/set_tensor_data]] _calls_
- [[nodes/if]] _calls_
- [[nodes/helper_get_test_opt_pars]] _calls_
- [[nodes/print_ok]] _calls_
- [[nodes/if]] _calls_
- [[nodes/helper_get_regression_opt_pars]] _calls_
- [[nodes/set_tensor_data]] _calls_
- [[nodes/ggml_backend_meta_buffer_set_tensor]] _calls_
- [[nodes/ggml_backend_tensor_set_async]] _calls_
- [[nodes/ggml_backend_tensor_get]] _calls_
- [[nodes/ggml_backend_tensor_copy]] _calls_
