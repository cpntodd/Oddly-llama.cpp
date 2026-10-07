---
name: "flash_attn_ext_f16_thread"
type: "function"
file: "ggml/src/ggml-hexagon/htp/flash-attn-ops.c"
community: "ggml"
---

# flash_attn_ext_f16_thread

**Type:** `function`  **File:** `ggml/src/ggml-hexagon/htp/flash-attn-ops.c`

**Community:** [[communities/ggml]]

## Depends On

- [[nodes/fastdiv]] _calls_
- [[nodes/fastmodulo]] _calls_
- [[nodes/dma_queue_push]] _calls_
- [[nodes/hvx_vec_splat_f32]] _calls_
- [[nodes/hvx_splat_f32_a]] _calls_
- [[nodes/dma_queue_pop]] _calls_
- [[nodes/hvx_copy_f16_f32_aa]] _calls_
- [[nodes/hvx_vec_splat_f16]] _calls_
- [[nodes/htp_trace_event_start]] _calls_
- [[nodes/hvx_vec_f32_to_f16]] _calls_
- [[nodes/hvx_vec_tanh_f16]] _calls_
- [[nodes/hvx_vec_reduce_max_f16]] _calls_
- [[nodes/hvx_vec_f16_to_f32]] _calls_
- [[nodes/htp_trace_event_stop]] _calls_
- [[nodes/K]] _calls_
- [[nodes/V]] _calls_
- [[nodes/hvx_vec_exp2_f16]] _calls_
- [[nodes/hvx_scale_vec_f32_aa]] _calls_
- [[nodes/hvx_vec_reduce_sum_f32]] _calls_
- [[nodes/hvx_vec_repl_f16]] _calls_
- [[nodes/hvx_mad_f32_f16_aa_vec]] _calls_
- [[nodes/block]] _calls_
- [[nodes/hvx_vec_get_f32]] _calls_
- [[nodes/hvx_vec_exp_f32]] _calls_
- [[nodes/hvx_scale_f32_aa]] _calls_
- [[nodes/hvx_copy_f32_ua]] _calls_
- [[nodes/hvx_copy_f16_f32_ua]] _calls_
