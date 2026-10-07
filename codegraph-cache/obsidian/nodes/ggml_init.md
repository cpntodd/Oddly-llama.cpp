---
name: "ggml_init"
type: "function"
file: "ggml/src/ggml.c"
community: "ggml"
---

# ggml_init

**Type:** `function`  **File:** `ggml/src/ggml.c`

**Community:** [[communities/ggml]]

## Depends On

- [[nodes/ggml_critical_section_start]] _calls_
- [[nodes/ggml_time_init]] _calls_
- [[nodes/ggml_critical_section_end]] _calls_
- [[nodes/ggml_aligned_malloc]] _calls_

## Used By

- [[nodes/all_finite]] _calls_
- [[nodes/base_model]] _calls_
- [[nodes/merge_tensor]] _calls_
- [[nodes/main]] _calls_
- [[nodes/clip_image_convert_f32_to_u8]] _calls_
- [[nodes/load_tensors]] _calls_
- [[nodes/print_usage]] _calls_
- [[nodes/save_tensor_for_layer]] _calls_
- [[nodes/print_debug_tensor]] _calls_
- [[nodes/weight_buft_supported]] _calls_
- [[nodes/select_weight_buft]] _calls_
- [[nodes/hparams]] _calls_
- [[nodes/llama_sampler_backend_copy_state]] _calls_
- [[nodes/llama_backend_init]] _calls_
- [[nodes/dsv4_make_k_only]] _calls_
- [[nodes/params]] _calls_
- [[nodes/buft_supported]] _calls_
- [[nodes/llama_adapter_lora_init_impl]] _calls_
- [[nodes/ggml_gen_hadamard]] _calls_
- [[nodes/max_nodes]] _calls_
- [[nodes/needs_raw_logits]] _calls_
- [[nodes/llama_set_param]] _calls_
- [[nodes/gguf_ex_write]] _calls_
- [[nodes/main]] _calls_
- [[nodes/main]] _calls_
- [[nodes/build_mock_tensors]] _calls_
- [[nodes/make_context]] _calls_
- [[nodes/get_random_gguf_context]] _calls_
- [[nodes/main]] _calls_
- [[nodes/test_barrier]] _calls_
