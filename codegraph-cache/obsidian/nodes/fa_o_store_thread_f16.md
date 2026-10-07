---
name: "fa_o_store_thread_f16"
type: "function"
file: "ggml/src/ggml-hexagon/htp/flash-attn-ops.c"
community: "ggml"
---

# fa_o_store_thread_f16

**Type:** `function`  **File:** `ggml/src/ggml-hexagon/htp/flash-attn-ops.c`

**Community:** [[communities/ggml]]

## Depends On

- [[nodes/hex_smin]] _calls_
- [[nodes/htp_trace_event_start]] _calls_
- [[nodes/fastdiv]] _calls_
- [[nodes/fastmodulo]] _calls_
- [[nodes/htp_trace_event_stop]] _calls_
- [[nodes/hmx_ceil_div]] _calls_
- [[nodes/work_queue_run]] _calls_
- [[nodes/hex_align_up]] _calls_
- [[nodes/hvx_vec_splat_f16]] _calls_
- [[nodes/hvx_vec_tanh_f16]] _calls_
- [[nodes/hvx_vec_repl_f16]] _calls_
- [[nodes/hvx_vec_reduce_max_f16]] _calls_
- [[nodes/hvx_vec_repl_f32]] _calls_
- [[nodes/hvx_vec_f32_to_f16]] _calls_
- [[nodes/hvx_vec_exp2_f16]] _calls_
- [[nodes/hvx_vec_f16_to_f32_shuff]] _calls_
- [[nodes/hvx_vec_reduce_sum_f32]] _calls_
- [[nodes/hvx_vec_f16_to_f32]] _calls_
- [[nodes/value]] _calls_
