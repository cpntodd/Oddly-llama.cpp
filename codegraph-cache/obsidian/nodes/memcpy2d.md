---
name: "memcpy2d"
type: "function"
file: "ggml/src/ggml-cpu/spacemit/rvv_kernels.cpp"
community: "ggml"
---

# memcpy2d

**Type:** `function`  **File:** `ggml/src/ggml-cpu/spacemit/rvv_kernels.cpp`

**Community:** [[communities/ggml]]

## Depends On

- [[nodes/memcpy1d]] _calls_
- [[nodes/flash_attn_ext_supported_shape_vlen1024_vf16]] _calls_
- [[nodes/ggml_type_size]] _calls_
- [[nodes/rvv_zero_f32]] _calls_
- [[nodes/rvv_softcap_tanh_inplace_f32]] _calls_
- [[nodes/rvv_max_f32]] _calls_
- [[nodes/rvv_scale_f32]] _calls_
- [[nodes/rvv_softmax_exp_inplace_f32]] _calls_

## Used By

- [[nodes/q8k_blk_size]] _calls_
