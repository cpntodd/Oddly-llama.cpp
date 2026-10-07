---
name: "ggml_get_unary_op"
type: "function"
file: "ggml/src/ggml.c"
community: "ggml"
---

# ggml_get_unary_op

**Type:** `function`  **File:** `ggml/src/ggml.c`

**Community:** [[communities/ggml]]

## Depends On

- [[nodes/ggml_get_op_params_i32]] _calls_

## Used By

- [[nodes/ggml_op_desc]] _calls_
- [[nodes/ggml_hash_map_free]] _calls_
- [[nodes/ggml_build_forward_order]] _calls_
- [[nodes/ggml_get_n_tasks]] _calls_
- [[nodes/ggml_wrap_index]] _calls_
- [[nodes/if]] _calls_
- [[nodes/ggml_sycl_topk_moe_fusion]] _calls_
- [[nodes/ggml_sycl_op_unary_mul_fused]] _calls_
- [[nodes/dispatch_type]] _calls_
- [[nodes/ggml_webgpu_unary_op]] _calls_
- [[nodes/ggml_backend_webgpu_device_supports_op]] _calls_
- [[nodes/get_unary_pipeline]] _calls_
- [[nodes/ggml_cann_compute_forward]] _calls_
- [[nodes/ggml_backend_cann_supports_op]] _calls_
- [[nodes/ggml_metal_library_get_pipeline_unary]] _calls_
- [[nodes/ggml_metal_op_unary]] _calls_
- [[nodes/ggml_metal_op_ssm_conv]] _calls_
- [[nodes/ggml_backend_et_device_supports_op]] _calls_
- [[nodes/ggml_et_op_unary]] _calls_
- [[nodes/op_remap_to_htp]] _calls_
- [[nodes/ggml_backend_hexagon_device_supports_op]] _calls_
- [[nodes/show_test_coverage]] _calls_
- [[nodes/ggml_sycl_argmax]] _calls_
- [[nodes/ggml_backend_sycl_graph_compute_impl]] _calls_
- [[nodes/do_ggml_backend_sycl_device_supports_op]] _calls_
- [[nodes/print_tensor_address_map]] _calls_
- [[nodes/ggml_backend_openvino_device_supports_op]] _calls_
