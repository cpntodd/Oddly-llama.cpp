---
name: "hvx_vec_exp_f32"
type: "function"
file: "ggml/src/ggml-hexagon/htp/hvx-exp.h"
community: "ggml"
---

# hvx_vec_exp_f32

**Type:** `function`  **File:** `ggml/src/ggml-hexagon/htp/hvx-exp.h`

**Community:** [[communities/ggml]]

## Depends On

- [[nodes/hvx_vec_store_u]] _imports_
- [[nodes/hvx_vec_truncate_f32]] _imports_
- [[nodes/hvx_vec_floor_f32]] _calls_

## Used By

- [[nodes/hvx_vec_exp_f32_guard]] _calls_
- [[nodes/flash_attn_ext_f16_thread]] _calls_
- [[nodes/hvx_vec_fast_sigmoid_f32]] _imports_
- [[nodes/hvx_fast_softmax_f32]] _calls_
- [[nodes/htp_unary_context]] _imports_
- [[nodes/hvx_vec_pow_const_base_f32]] _imports_
