---
name: "ggml_backend_buffer_get_size"
type: "function"
file: "ggml/src/ggml-backend.cpp"
community: "src"
---

# ggml_backend_buffer_get_size

**Type:** `function`  **File:** `ggml/src/ggml-backend.cpp`

**Community:** [[communities/src]]

## Depends On

- [[nodes/ggml_backend_buffer_is_meta]] _calls_
- [[nodes/get_base]] _calls_

## Used By

- [[nodes/hparams]] _calls_
- [[nodes/dsv4_make_k_only]] _calls_
- [[nodes/params]] _calls_
- [[nodes/llama_adapter_lora_init_impl]] _calls_
- [[nodes/ggml_gen_hadamard]] _calls_
- [[nodes/set_input_kq_mask_impl]] _calls_
- [[nodes/ctx_type_to_graph_type]] _calls_
- [[nodes/needs_raw_logits]] _calls_
- [[nodes/allocated_total]] _calls_
- [[nodes/ggml_backend_meta_buffer_type_alloc_buffer]] _calls_
- [[nodes/ggml_backend_meta_graph_compute]] _calls_
- [[nodes/ggml_backend_multi_buffer_alloc_buffer]] _calls_
- [[nodes/ggml_backend_tensor_alloc]] _calls_
- [[nodes/ggml_backend_graph_copy]] _calls_
- [[nodes/ggml_tallocr_alloc]] _calls_
- [[nodes/ggml_vbuffer_chunk_size]] _calls_
- [[nodes/ggml_vbuffer_size]] _calls_
- [[nodes/ggml_backend_rpc_get_device_memory]] _calls_
- [[nodes/apir_untrack_backend_buffer]] _calls_
- [[nodes/ggml_et_cpu_compare_init_pre]] _calls_
