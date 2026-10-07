---
name: "ggml_backend_cpu_buffer_type"
type: "function"
file: "ggml/src/ggml-backend.cpp"
community: "src"
---

# ggml_backend_cpu_buffer_type

**Type:** `function`  **File:** `ggml/src/ggml-backend.cpp`

**Community:** [[communities/src]]

## Depends On

- [[nodes/ggml_backend_reg_dev_get]] _calls_
- [[nodes/ggml_backend_cpu_reg]] _calls_

## Used By

- [[nodes/to_llama_mparams]] _calls_
- [[nodes/select_weight_buft]] _calls_
- [[nodes/hparams]] _calls_
- [[nodes/llama_prepare_model_devices]] _calls_
- [[nodes/dsv4_make_k_only]] _calls_
- [[nodes/make_cpu_buft_list]] _calls_
- [[nodes/ggml_gen_hadamard]] _calls_
- [[nodes/needs_raw_logits]] _calls_
- [[nodes/llm_ffn_exps_cpu_override]] _calls_
- [[nodes/common_params_parser_init]] _calls_
- [[nodes/test_backends]] _calls_
- [[nodes/ggml_opt_build]] _calls_
- [[nodes/ggml_backend_zendnn_device_get_buffer_type]] _calls_
- [[nodes/ggml_backend_cpu_device_get_buffer_type]] _calls_
- [[nodes/ggml_backend_cpu_repack_buffer_type_alloc_buffer]] _calls_
- [[nodes/ggml_backend_cpu_kleidiai_buffer_type_alloc_buffer]] _calls_
- [[nodes/ggml_backend_cann_host_buffer_free]] _calls_
- [[nodes/ggml_backend_cann_host_buffer_type]] _calls_
- [[nodes/ggml_backend_et_device_get_host_buffer_type]] _calls_
- [[nodes/ggml_backend_blas_device_get_buffer_type]] _calls_
- [[nodes/ggml_backend_sycl_host_buffer_type_alloc_buffer]] _calls_
- [[nodes/ggml_backend_sycl_host_buffer_type_for_device]] _calls_
