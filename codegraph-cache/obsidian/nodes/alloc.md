---
name: "alloc"
type: "function"
file: "ggml/src/ggml-hexagon/ggml-hexagon.cpp"
community: "ggml"
---

# alloc

**Type:** `function`  **File:** `ggml/src/ggml-hexagon/ggml-hexagon.cpp`

**Community:** [[communities/ggml]]

## Depends On

- [[nodes/rpcmem_to_fd]] _calls_
- [[nodes/mmap]] _calls_

## Used By

- [[nodes/stop_type_to_str]] _calls_
- [[nodes/prompt_save]] _calls_
- [[nodes/makeCircle]] _calls_
- [[nodes/makeCircle]] _calls_
- [[nodes/makeCircle]] _calls_
- [[nodes/align_up_uintptr]] _calls_
- [[nodes/convert_f32]] _calls_
- [[nodes/MKL_ACCUM]] _calls_
- [[nodes/ggml_sycl_op_out_prod]] _calls_
- [[nodes/ggml_sycl_op_conv_3d]] _calls_
- [[nodes/get_dequantize_V]] _calls_
- [[nodes/ggml_cann_l2_norm]] _calls_
- [[nodes/ggml_cann_dup]] _calls_
- [[nodes/ggml_cann_diag_mask]] _calls_
- [[nodes/ggml_cann_im2col]] _calls_
- [[nodes/ggml_cann_mul_mat_quant]] _calls_
- [[nodes/ggml_cann_mul_mat]] _calls_
- [[nodes/ggml_cann_rope]] _calls_
- [[nodes/ggml_cann_conv_transpose_1d]] _calls_
- [[nodes/ggml_cann_mul_mat_id_quant]] _calls_
- [[nodes/ggml_cann_flash_attn_ext]] _calls_
- [[nodes/ggml_cann_init]] _calls_
- [[nodes/free]] _calls_
- [[nodes/makeCircle]] _calls_
- [[nodes/ggml_sycl_flash_attn_ext_dec]] _calls_
- [[nodes/ggml_sycl_get_device]] _calls_
- [[nodes/pool]] _calls_
- [[nodes/ggml_backend_sycl_host_buffer_type]] _calls_
- [[nodes/format_slots_in_alloc_order]] _calls_
- [[nodes/next_power_of_2]] _calls_
