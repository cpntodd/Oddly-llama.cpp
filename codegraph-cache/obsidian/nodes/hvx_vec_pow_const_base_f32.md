---
name: "hvx_vec_pow_const_base_f32"
type: "function"
file: "ggml/src/ggml-hexagon/htp/hvx-pow.h"
community: "ggml"
---

# hvx_vec_pow_const_base_f32

**Type:** `function`  **File:** `ggml/src/ggml-hexagon/htp/hvx-pow.h`

**Community:** [[communities/ggml]]

## Depends On

- [[nodes/hvx_vec_store_u]] _imports_
- [[nodes/hvx_vec_exp_f32]] _imports_
- [[nodes/hvx_vec_log_f32]] _imports_
- [[nodes/hvx_vec_splat_f32]] _calls_
- [[nodes/hvx_vec_mul_f32_f32]] _calls_
- [[nodes/hvx_vec_exp_f32_guard]] _calls_

## Used By

- [[nodes/alibi_slope]] _calls_
