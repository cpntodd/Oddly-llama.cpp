---
name: "fa_q_load_thread"
type: "function"
file: "ggml/src/ggml-hexagon/htp/flash-attn-ops.c"
community: "ggml"
---

# fa_q_load_thread

**Type:** `function`  **File:** `ggml/src/ggml-hexagon/htp/flash-attn-ops.c`

**Community:** [[communities/ggml]]

## Depends On

- [[nodes/rows]] _calls_
- [[nodes/hex_smin]] _calls_
- [[nodes/htp_trace_event_start]] _calls_
- [[nodes/hex_align_up]] _calls_
- [[nodes/hvx_vec_splat_f32]] _calls_
- [[nodes/fastmodulo]] _calls_
- [[nodes/hvx_splat_u8_a]] _calls_
- [[nodes/hvx_splat_f32_a]] _calls_
- [[nodes/atomic_load]] _calls_
- [[nodes/htp_trace_event_stop]] _calls_
- [[nodes/hmx_ceil_div]] _calls_
- [[nodes/work_queue_run]] _calls_
