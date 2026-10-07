---
name: "htp_iface_start"
type: "function"
file: "ggml/src/ggml-hexagon/htp/main.c"
community: "ggml"
---

# htp_iface_start

**Type:** `function`  **File:** `ggml/src/ggml-hexagon/htp/main.c`

**Community:** [[communities/ggml]]

## Depends On

- [[nodes/hex_align_up]] _calls_
- [[nodes/work_queue_alignof]] _calls_
- [[nodes/work_queue_sizeof]] _calls_
- [[nodes/dma_queue_alignof]] _calls_
- [[nodes/dma_queue_sizeof]] _calls_
- [[nodes/dma_queue_alias_sizeof]] _calls_
- [[nodes/hmx_queue_alignof]] _calls_
- [[nodes/hmx_queue_sizeof]] _calls_
- [[nodes/dspqueue_close]] _calls_
- [[nodes/vtcm_alloc]] _calls_
- [[nodes/htp_iface_stop]] _calls_
- [[nodes/hmx_queue_init]] _calls_
- [[nodes/init_fastdiv_values]] _calls_
- [[nodes/dma_queue_init]] _calls_
- [[nodes/dma_queue_alias_init]] _calls_
- [[nodes/work_queue_init]] _calls_
- [[nodes/atomic_store]] _calls_

## Used By

- [[nodes/ggml_hexagon_measure_max_vmem]] _calls_
