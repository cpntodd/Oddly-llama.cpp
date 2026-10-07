---
name: "ggml_nrows"
type: "function"
file: "ggml/src/ggml.c"
community: "ggml"
---

# ggml_nrows

**Type:** `function`  **File:** `ggml/src/ggml.c`

**Community:** [[communities/ggml]]

## Used By

- [[nodes/all_finite]] _calls_
- [[nodes/if]] _calls_
- [[nodes/llama_sampler_top_p_free]] _calls_
- [[nodes/llama_model_quantize_impl]] _calls_
- [[nodes/gguf_read_emplace_helper]] _calls_
- [[nodes/ggml_set_i32]] _calls_
- [[nodes/ggml_set_f32]] _calls_
- [[nodes/ggml_get_n_tasks]] _calls_
- [[nodes/repack_q4_0_to_q4_0_4_bl]] _calls_
- [[nodes/repack_q4_K_to_q4_K_8_bl]] _calls_
- [[nodes/repack_q4_K_to_q4_K_16_bl]] _calls_
- [[nodes/repack_q2_K_to_q2_K_8_bl]] _calls_
- [[nodes/repack_q2_K_to_q2_K_16_bl]] _calls_
- [[nodes/repack_q4_0_to_q4_0_16_bl]] _calls_
- [[nodes/repack_q6_K_to_q6_K_8_bl]] _calls_
- [[nodes/repack_q4_0_to_q4_0_8_bl]] _calls_
- [[nodes/make_block_q8_0x16]] _calls_
- [[nodes/repack_iq4_nl_to_iq4_nl_4_bl]] _calls_
- [[nodes/repack_iq4_nl_to_iq4_nl_8_bl]] _calls_
- [[nodes/repack_iq4_nl_to_iq4_nl_16_bl]] _calls_
- [[nodes/repack_mxfp4_to_mxfp4_4_bl]] _calls_
- [[nodes/repack_mxfp4_to_mxfp4_8_bl]] _calls_
- [[nodes/forward_mul_mat]] _calls_
- [[nodes/f32_to_f32]] _calls_
- [[nodes/ggml_compute_forward_tri]] _calls_
- [[nodes/rotate_pairs]] _calls_
- [[nodes/ggml_conv_2d_dw_knl_f32]] _calls_
- [[nodes/ggml_wrap_index]] _calls_
- [[nodes/ggml_dsv4_hc_comb_norm_rows]] _calls_
- [[nodes/ggml_compute_forward_opt_step_sgd_f32]] _calls_
