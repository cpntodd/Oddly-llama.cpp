---
name: "ov_graph_compute_dynamic"
type: "function"
file: "ggml/src/ggml-openvino/utils.cpp"
community: "ggml"
---

# ov_graph_compute_dynamic

**Type:** `function`  **File:** `ggml/src/ggml-openvino/utils.cpp`

**Community:** [[communities/ggml]]

## Depends On

- [[nodes/ggml_openvino_getenv_int]] _calls_
- [[nodes/is_model_splitted]] _calls_
- [[nodes/is_naive]] _calls_
- [[nodes/ggml_time_us]] _calls_
- [[nodes/ggml_openvino_weight_buffers_released]] _calls_
- [[nodes/cached]] _calls_
- [[nodes/ggml_openvino_model_cache_dir]] _calls_
- [[nodes/ggml_openvino_model_cache_extra_cfg]] _calls_
- [[nodes/ggml_openvino_model_cache_blob_path]] _calls_
- [[nodes/ggml_openvino_model_cache_manifest_path]] _calls_
- [[nodes/value]] _calls_
- [[nodes/map]] _calls_
- [[nodes/get_node]] _calls_
- [[nodes/get_ov_input_tensor]] _calls_
- [[nodes/print_input_tensor_info]] _calls_
- [[nodes/ggml_nbytes]] _calls_
- [[nodes/print_output_tensor_info]] _calls_
- [[nodes/ggml_openvino_release_weights_enabled]] _calls_
- [[nodes/ggml_openvino_release_weight_buffers]] _calls_

## Used By

- [[nodes/ov_graph_compute]] _calls_
