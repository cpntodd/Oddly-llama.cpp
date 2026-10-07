---
name: "ggml_is_quantized"
type: "function"
file: "ggml/src/ggml.c"
community: "ggml"
---

# ggml_is_quantized

**Type:** `function`  **File:** `ggml/src/ggml.c`

**Community:** [[communities/ggml]]

## Used By

- [[nodes/merge_tensor]] _calls_
- [[nodes/fa_init_uniform]] _calls_
- [[nodes/llama_model_get_tok_embd]] _calls_
- [[nodes/ggml_gen_hadamard]] _calls_
- [[nodes/set_input_kq_mask_impl]] _calls_
- [[nodes/category_is_attn_v]] _calls_
- [[nodes/llama_tensor_get_type]] _calls_
- [[nodes/llama_model_quantize_impl]] _calls_
- [[nodes/ctx_type_to_graph_type]] _calls_
- [[nodes/llama_context_default_params]] _calls_
- [[nodes/llm_graph_context]] _calls_
- [[nodes/common_debug_cb_eval]] _calls_
- [[nodes/build_context]] _calls_
- [[nodes/ggml_get_tensor]] _calls_
- [[nodes/ggml_threadpool_resume]] _calls_
- [[nodes/ggml_backend_cpu_device_supports_op]] _calls_
- [[nodes/ggml_backend_cpu_kleidiai_buffer_type_get_alloc_size]] _calls_
- [[nodes/ggml_backend_rpc_buffer_init_tensor]] _calls_
- [[nodes/ggml_backend_rpc_buffer_type_get_alloc_size]] _calls_
- [[nodes/ggml_webgpu_pad]] _calls_
- [[nodes/ggml_backend_webgpu_device_supports_op]] _calls_
- [[nodes/ggml_webgpu_flash_attn_v_direct]] _calls_
- [[nodes/get_set_rows_pipeline]] _calls_
- [[nodes/get_mul_mat_fast_pipeline]] _calls_
- [[nodes/get_mul_mat_id_pipeline]] _calls_
- [[nodes/ggml_backend_cann_buffer_init_tensor]] _calls_
- [[nodes/ggml_backend_cann_buffer_type_get_alignment]] _calls_
- [[nodes/ggml_backend_cann_free]] _calls_
- [[nodes/ggml_metal_op_get_rows]] _calls_
- [[nodes/ggml_metal_op_set]] _calls_
