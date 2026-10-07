---
name: "ggml_new_graph_custom"
type: "function"
file: "ggml/src/ggml.c"
community: "ggml"
---

# ggml_new_graph_custom

**Type:** `function`  **File:** `ggml/src/ggml.c`

**Community:** [[communities/ggml]]

## Depends On

- [[nodes/ggml_graph_nbytes]] _calls_
- [[nodes/ggml_new_object]] _calls_
- [[nodes/ggml_hash_size]] _calls_
- [[nodes/ggml_bitset_size]] _calls_
- [[nodes/ggml_hash_set_reset]] _calls_

## Used By

- [[nodes/clip_image_convert_f32_to_u8]] _calls_
- [[nodes/llama_sampler_backend_copy_state]] _calls_
- [[nodes/max_nodes]] _calls_
- [[nodes/ggml_backend_meta_graph_compute]] _calls_
- [[nodes/ggml_backend_graph_copy]] _calls_
- [[nodes/ggml_new_graph]] _calls_
- [[nodes/ggml_graph_dup]] _calls_
- [[nodes/ggml_opt_get_constant_optimizer_params]] _calls_
- [[nodes/ggml_opt_init]] _calls_
- [[nodes/ggml_backend_rpc_get_device_memory]] _calls_
- [[nodes/apir_untrack_backend_buffer]] _calls_
- [[nodes/ggml_et_cpu_compare_init_pre]] _calls_
- [[nodes/eval_perf]] _calls_
- [[nodes/eval_support]] _calls_
- [[nodes/eval_grad]] _calls_
