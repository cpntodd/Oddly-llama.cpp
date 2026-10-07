---
name: "init_softmax_ctx"
type: "function"
file: "ggml/src/ggml-hexagon/htp/softmax-ops.c"
community: "ggml"
---

# init_softmax_ctx

**Type:** `function`  **File:** `ggml/src/ggml-hexagon/htp/softmax-ops.c`

**Community:** [[communities/ggml]]

## Depends On

- [[nodes/init_fastdiv_values]] _calls_
- [[nodes/hvx_vec_splat_f32]] _calls_

## Used By

- [[nodes/execute_op_softmax_f32]] _calls_
