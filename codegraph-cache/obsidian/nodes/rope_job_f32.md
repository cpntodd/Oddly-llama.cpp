---
name: "rope_job_f32"
type: "function"
file: "ggml/src/ggml-hexagon/htp/rope-ops.c"
community: "ggml"
---

# rope_job_f32

**Type:** `function`  **File:** `ggml/src/ggml-hexagon/htp/rope-ops.c`

**Community:** [[communities/ggml]]

## Depends On

- [[nodes/fastdiv]] _calls_
- [[nodes/fastmodulo]] _calls_
- [[nodes/dma_queue_depth]] _calls_
- [[nodes/dma_queue_push_vtcm_to_ddr]] _calls_
- [[nodes/dma_queue_push]] _calls_
- [[nodes/block]] _calls_
- [[nodes/dma_queue_pop_nowait]] _calls_
- [[nodes/dma_queue_pop]] _calls_
- [[nodes/rows]] _calls_
- [[nodes/dma_queue_flush]] _calls_
