---
name: "ggml_metal_op_flash_attn_ext"
type: "function"
file: "ggml/src/ggml-metal/ggml-metal-ops.cpp"
community: "ggml"
---

# ggml_metal_op_flash_attn_ext

**Type:** `function`  **File:** `ggml/src/ggml-metal/ggml-metal-ops.cpp`

**Community:** [[communities/ggml]]

## Depends On

- [[nodes/ggml_are_same_shape]] _calls_
- [[nodes/ggml_metal_get_buffer_id]] _calls_
- [[nodes/ggml_nbytes]] _calls_
- [[nodes/ggml_metal_op_flash_attn_ext_extra_pad]] _calls_
- [[nodes/ggml_metal_op_flash_attn_ext_extra_blk]] _calls_
- [[nodes/ggml_metal_op_flash_attn_ext_extra_tmp]] _calls_
- [[nodes/ggml_metal_op_flash_attn_ext_use_kv_f16]] _calls_
- [[nodes/ggml_metal_op_flash_attn_ext_extra_kv_f16]] _calls_
- [[nodes/ggml_metal_op_flash_attn_ext_v_is_view_of_k]] _calls_
- [[nodes/ggml_blck_size]] _calls_
- [[nodes/ggml_metal_op_flash_attn_ext_kv_f16_k_size]] _calls_
- [[nodes/V]] _calls_
- [[nodes/ggml_metal_op_concurrency_reset]] _calls_
- [[nodes/ggml_metal_op_flash_attn_ext_use_vec]] _calls_
- [[nodes/ggml_is_quantized]] _calls_
- [[nodes/fa_vec_pick]] _calls_
- [[nodes/fa_vec_baseline_cfg]] _calls_

## Used By

- [[nodes/ggml_metal_op_encode_impl]] _calls_
