---
name: "pool"
type: "function"
file: "ggml/src/ggml-sycl/common.hpp"
community: "ggml"
---

# pool

**Type:** `function`  **File:** `ggml/src/ggml-sycl/common.hpp`

**Community:** [[communities/ggml]]

## Depends On

- [[nodes/ggml_sycl_pool_alloc]] _calls_
- [[nodes/alloc]] _calls_
- [[nodes/realloc]] _calls_
- [[nodes/get]] _calls_

## Used By

- [[nodes/ggml_new_object]] _calls_
- [[nodes/convert_f32]] _calls_
- [[nodes/MKL_ACCUM]] _calls_
- [[nodes/ggml_sycl_op_out_prod]] _calls_
- [[nodes/ggml_sycl_op_conv_3d]] _calls_
- [[nodes/get_dequantize_V]] _calls_
- [[nodes/ggml_sycl_cross_entropy_loss]] _calls_
- [[nodes/ggml_cann_geglu]] _calls_
- [[nodes/ggml_cann_argsort]] _calls_
- [[nodes/ggml_cann_l2_norm]] _calls_
- [[nodes/ggml_cann_cross_entropy_loss]] _calls_
- [[nodes/ggml_cann_group_norm]] _calls_
- [[nodes/ggml_cann_solve_tri]] _calls_
- [[nodes/ggml_cann_max_pool2d]] _calls_
- [[nodes/ggml_cann_dup]] _calls_
- [[nodes/ggml_cann_diag_mask]] _calls_
- [[nodes/ggml_cann_im2col]] _calls_
- [[nodes/ggml_cann_timestep_embedding]] _calls_
- [[nodes/aclnn_pow_tensor_tensor]] _calls_
- [[nodes/ggml_cann_softmax]] _calls_
- [[nodes/ggml_cann_get_rows]] _calls_
- [[nodes/ggml_cann_set_rows]] _calls_
- [[nodes/ggml_cann_mul_mat_quant]] _calls_
- [[nodes/ggml_cann_mul_mat]] _calls_
- [[nodes/ggml_cann_rope]] _calls_
- [[nodes/ggml_cann_conv_transpose_1d]] _calls_
- [[nodes/ggml_cann_count_equal]] _calls_
- [[nodes/ggml_cann_mul_mat_id_fp]] _calls_
- [[nodes/ggml_cann_mul_mat_id_quant]] _calls_
- [[nodes/ggml_cann_flash_attn_ext]] _calls_
