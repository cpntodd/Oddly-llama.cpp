---
name: "ggml_backend_buffer_is_host"
type: "function"
file: "ggml/src/ggml-backend.cpp"
community: "src"
---

# ggml_backend_buffer_is_host

**Type:** `function`  **File:** `ggml/src/ggml-backend.cpp`

**Community:** [[communities/src]]

## Depends On

- [[nodes/ggml_backend_buft_is_host]] _calls_
- [[nodes/ggml_backend_buffer_get_type]] _calls_

## Used By

- [[nodes/all_finite]] _calls_
- [[nodes/parse_k_cache_in_layer]] _calls_
- [[nodes/select_weight_buft]] _calls_
- [[nodes/params]] _calls_
- [[nodes/ggml_gen_hadamard]] _calls_
- [[nodes/set_input_kq_mask_impl]] _calls_
- [[nodes/print_mask]] _calls_
- [[nodes/dsv4_set_i32]] _calls_
- [[nodes/dsv4_can_reuse_tensor_1d]] _calls_
- [[nodes/hparams]] _calls_
- [[nodes/common_debug_cb_eval]] _calls_
- [[nodes/ggml_backend_meta_graph_compute]] _calls_
- [[nodes/ggml_backend_tensor_copy]] _calls_
- [[nodes/if]] _calls_
- [[nodes/ggml_backend_sched_backend_id_from_cur]] _calls_
- [[nodes/ggml_backend_sched_compute_splits]] _calls_
- [[nodes/ggml_backend_cpu_buffer_cpy_tensor]] _calls_
- [[nodes/ggml_backend_amx_buffer_cpy_tensor]] _calls_
- [[nodes/next_power_of_2]] _calls_
- [[nodes/ggml_backend_openvino_buffer_init_tensor]] _calls_
