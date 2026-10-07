---
name: "hmx_flash_attn_ext"
type: "function"
file: "ggml/src/ggml-hexagon/htp/flash-attn-ops.c"
community: "ggml"
---

# hmx_flash_attn_ext

**Type:** `function`  **File:** `ggml/src/ggml-hexagon/htp/flash-attn-ops.c`

**Community:** [[communities/ggml]]

## Depends On

- [[nodes/allocation]] _calls_
- [[nodes/hex_round_up]] _calls_
- [[nodes/hmx_init_column_scales]] _calls_
- [[nodes/hvx_vec_splat_f16]] _calls_
- [[nodes/hex_smin]] _calls_
- [[nodes/fastmodulo]] _calls_
- [[nodes/hex_align_up]] _calls_
- [[nodes/fastdiv]] _calls_
- [[nodes/dma_queue_push]] _calls_
- [[nodes/hex_smax]] _calls_
- [[nodes/dma_queue_pop]] _calls_
- [[nodes/htp_trace_event_start]] _calls_
- [[nodes/htp_trace_event_stop]] _calls_
- [[nodes/fa_phase_k_interleave]] _calls_
- [[nodes/hmx_ceil_div]] _calls_
- [[nodes/hmx_queue_push]] _calls_
- [[nodes/hmx_queue_make_desc]] _calls_
- [[nodes/fa_pop_mask_dma_gqa]] _calls_
- [[nodes/hmx_queue_pop]] _calls_
- [[nodes/hex_swap_ptr]] _calls_

## Used By

- [[nodes/op_flash_attn_ext]] _calls_
