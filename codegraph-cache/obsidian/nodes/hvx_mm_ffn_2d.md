---
name: "hvx_mm_ffn_2d"
type: "function"
file: "ggml/src/ggml-hexagon/htp/matmul-ops.c"
community: "ggml"
---

# hvx_mm_ffn_2d

**Type:** `function`  **File:** `ggml/src/ggml-hexagon/htp/matmul-ops.c`

**Community:** [[communities/ggml]]

## Depends On

- [[nodes/dma_queue_push]] _calls_
- [[nodes/hvx_mm_run_quant_task]] _calls_
- [[nodes/dma_queue_pop]] _calls_
- [[nodes/rows]] _calls_
- [[nodes/htp_trace_event_start]] _calls_
- [[nodes/hex_smin]] _calls_
- [[nodes/htp_trace_event_stop]] _calls_
