---
name: "hvx_mm_qkv_2d"
type: "function"
file: "ggml/src/ggml-hexagon/htp/matmul-ops.c"
community: "ggml"
---

# hvx_mm_qkv_2d

**Type:** `function`  **File:** `ggml/src/ggml-hexagon/htp/matmul-ops.c`

**Community:** [[communities/ggml]]

## Depends On

- [[nodes/dma_queue_push]] _calls_
- [[nodes/hvx_mm_run_quant_task]] _calls_
- [[nodes/dma_queue_pop]] _calls_
- [[nodes/rows]] _calls_
