---
name: "ggml_gemm_q4_K_8x4_q8_K"
type: "function"
file: "ggml/src/ggml-cpu/arch/arm/repack.cpp"
community: "ggml"
---

# ggml_gemm_q4_K_8x4_q8_K

**Type:** `function`  **File:** `ggml/src/ggml-cpu/arch/arm/repack.cpp`

**Community:** [[communities/ggml]]

## Depends On

- [[nodes/vpaddq_s16]] _calls_
- [[nodes/decode_q_Kx8_6bit_scales]] _calls_
- [[nodes/ggml_gemm_q4_K_8x4_q8_K_generic]] _calls_
- [[nodes/ggml_gemm_q5_K_8x4_q8_K_generic]] _calls_
- [[nodes/rows]] _calls_
- [[nodes/ggml_gemm_q4_K_8x8_q8_K_generic]] _calls_
- [[nodes/ggml_gemm_q5_K_8x8_q8_K_generic]] _calls_
- [[nodes/ggml_gemm_q6_K_8x4_q8_K_generic]] _calls_
- [[nodes/block]] _calls_
- [[nodes/ggml_gemm_q6_K_8x8_q8_K_generic]] _calls_
- [[nodes/ggml_q1_0_unpack_pair]] _calls_

## Used By

- [[nodes/repack_mxfp4_to_mxfp4_8_bl]] _calls_
