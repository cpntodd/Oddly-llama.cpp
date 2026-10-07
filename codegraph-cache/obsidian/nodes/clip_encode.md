---
name: "clip_encode"
type: "function"
file: "tools/mtmd/clip.cpp"
community: "tools"
---

# clip_encode

**Type:** `function`  **File:** `tools/mtmd/clip.cpp`

**Community:** [[communities/tools]]

## Depends On

- [[nodes/clip_model_n_temporal_merge]] _calls_
- [[nodes/warmup]] _calls_
- [[nodes/ggml_backend_sched_reset]] _calls_
- [[nodes/ggml_backend_sched_alloc_graph]] _calls_
- [[nodes/nx]] _calls_
- [[nodes/ggml_graph_get_tensor]] _calls_
- [[nodes/ggml_nelements]] _calls_
- [[nodes/ggml_backend_tensor_set]] _calls_
- [[nodes/ggml_nbytes]] _calls_
- [[nodes/can_batch_with]] _calls_
- [[nodes/clip_n_mmproj_embd]] _calls_
- [[nodes/out]] _calls_
- [[nodes/fill]] _calls_
- [[nodes/set]] _calls_
- [[nodes/proj_type]] _calls_
- [[nodes/to_string]] _calls_
- [[nodes/ggml_backend_tensor_get]] _calls_
- [[nodes/clip_n_output_tokens]] _calls_
- [[nodes/ggml_backend_cpu_set_n_threads]] _calls_
- [[nodes/ggml_backend_get_device]] _calls_
- [[nodes/ggml_backend_dev_backend_reg]] _calls_
- [[nodes/ggml_backend_sched_graph_compute]] _calls_
- [[nodes/ggml_graph_node]] _calls_
- [[nodes/list_gen_state_slots]] _calls_

## Used By

- [[nodes/mtmd_gen_audio_process_impl]] _calls_
- [[nodes/clip_image_batch_encode]] _calls_
- [[nodes/list_c2w_state_slots]] _calls_
