---
name: "clip_image_convert_f32_to_u8"
type: "function"
file: "tools/mtmd/clip.cpp"
community: "ggml"
---

# clip_image_convert_f32_to_u8

**Type:** `function`  **File:** `tools/mtmd/clip.cpp`

**Community:** [[communities/ggml]]

## Depends On

- [[nodes/get_size]] _calls_
- [[nodes/ggml_backend_init_by_type]] _calls_
- [[nodes/ggml_backend_dev_init]] _calls_
- [[nodes/string_format]] _calls_
- [[nodes/ggml_backend_get_default_buffer_type]] _calls_
- [[nodes/ggml_backend_sched_set_eval_callback]] _calls_
- [[nodes/getenv]] _calls_
- [[nodes/ggml_backend_free]] _calls_
- [[nodes/clip_graph]] _calls_
- [[nodes/proj_type]] _calls_
- [[nodes/nx]] _calls_
- [[nodes/clip_n_mmproj_embd]] _calls_
- [[nodes/ggml_init]] _calls_
- [[nodes/ggml_new_graph_custom]] _calls_
- [[nodes/ggml_format_name]] _calls_
- [[nodes/ggml_set_name]] _calls_
- [[nodes/ggml_row_size]] _calls_
- [[nodes/ggml_set_input]] _calls_
- [[nodes/weights]] _calls_
- [[nodes/ggml_build_forward_order]] _calls_
- [[nodes/ggml_nelements]] _calls_
- [[nodes/clip_model_loader]] _calls_
- [[nodes/fname]] _calls_
- [[nodes/gguf_get_n_tensors]] _calls_
- [[nodes/get_string]] _calls_
- [[nodes/gguf_get_version]] _calls_
- [[nodes/gguf_get_alignment]] _calls_
- [[nodes/gguf_get_n_kv]] _calls_
- [[nodes/get_bool]] _calls_
- [[nodes/gguf_get_tensor_offset]] _calls_
