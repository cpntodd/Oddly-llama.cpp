---
name: "hvx_geglu_f32_aa"
type: "function"
file: "ggml/src/ggml-hexagon/htp/act-ops.c"
community: "ggml"
---

# hvx_geglu_f32_aa

**Type:** `function`  **File:** `ggml/src/ggml-hexagon/htp/act-ops.c`

**Community:** [[communities/ggml]]

## Depends On

- [[nodes/hvx_vec_splat_f32]] _calls_
- [[nodes/hvx_vec_mul_f32_f32]] _calls_
- [[nodes/hvx_vec_add_f32_f32]] _calls_
- [[nodes/hvx_vec_truncate_f32]] _calls_
- [[nodes/sigmoid]] _calls_
- [[nodes/hvx_vec_sub_f32_f32]] _calls_
- [[nodes/hvx_vec_store_a]] _calls_
- [[nodes/dma_queue_push_vtcm_to_ddr]] _calls_
- [[nodes/dma_queue_push]] _calls_
- [[nodes/dma_queue_pop]] _calls_
- [[nodes/htp_trace_event_start]] _calls_
- [[nodes/htp_trace_event_stop]] _calls_
- [[nodes/dma_queue_flush]] _calls_
