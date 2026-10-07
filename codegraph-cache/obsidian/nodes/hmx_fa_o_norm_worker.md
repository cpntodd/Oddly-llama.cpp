---
name: "hmx_fa_o_norm_worker"
type: "function"
file: "ggml/src/ggml-hexagon/htp/flash-attn-ops.c"
community: "ggml"
---

# hmx_fa_o_norm_worker

**Type:** `function`  **File:** `ggml/src/ggml-hexagon/htp/flash-attn-ops.c`

**Community:** [[communities/ggml]]

## Depends On

- [[nodes/hvx_splat_f16_a]] _calls_
- [[nodes/hvx_vec_f32_to_f16]] _calls_
- [[nodes/alibi_slope]] _calls_
- [[nodes/fastmodulo]] _calls_
- [[nodes/hvx_copy_f16_aa]] _calls_
- [[nodes/dma_queue_push]] _calls_
