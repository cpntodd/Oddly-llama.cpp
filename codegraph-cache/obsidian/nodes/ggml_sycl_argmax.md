---
name: "ggml_sycl_argmax"
type: "function"
file: "ggml/src/ggml-sycl/ggml-sycl.cpp"
community: "ggml"
---

# ggml_sycl_argmax

**Type:** `function`  **File:** `ggml/src/ggml-sycl/ggml-sycl.cpp`

**Community:** [[communities/ggml]]

## Depends On

- [[nodes/ggml_is_contiguous]] _calls_
- [[nodes/ggml_sycl_op_argmax]] _calls_
- [[nodes/get_current_device_id]] _calls_
- [[nodes/check_allow_gpu_index]] _calls_
- [[nodes/get_device_info]] _calls_
- [[nodes/ggml_backend_buffer_is_sycl_split]] _calls_
- [[nodes/ggml_sycl_set_peer_access]] _calls_
- [[nodes/ggml_sycl_t2_restore_tensor]] _calls_
- [[nodes/ggml_sycl_op_conv2d]] _calls_
- [[nodes/ggml_sycl_op_conv2d_dw]] _calls_
- [[nodes/ggml_sycl_conv_3d]] _calls_
- [[nodes/ggml_sycl_op_conv_transpose_1d]] _calls_
- [[nodes/ggml_sycl_op_conv2d_transpose]] _calls_
- [[nodes/ggml_sycl_repeat]] _calls_
- [[nodes/ggml_sycl_repeat_back]] _calls_
- [[nodes/ggml_sycl_get_rows]] _calls_
- [[nodes/ggml_sycl_op_set]] _calls_
- [[nodes/ggml_sycl_op_set_rows]] _calls_
- [[nodes/ggml_sycl_op_dsv4_hc_pre]] _calls_
- [[nodes/ggml_sycl_op_dsv4_hc_comb]] _calls_
- [[nodes/ggml_sycl_op_dsv4_hc_post]] _calls_
- [[nodes/ggml_sycl_op_lightning_indexer]] _calls_
- [[nodes/ggml_sycl_dup]] _calls_
- [[nodes/ggml_sycl_add]] _calls_
- [[nodes/ggml_sycl_add_id]] _calls_
- [[nodes/ggml_sycl_sub]] _calls_
- [[nodes/ggml_sycl_count_equal]] _calls_
- [[nodes/ggml_sycl_acc]] _calls_
- [[nodes/ggml_sycl_mul]] _calls_
- [[nodes/ggml_sycl_log]] _calls_
