---
name: "hvx_vec_cos_f32"
type: "function"
file: "ggml/src/ggml-hexagon/htp/hvx-sin-cos.h"
community: "ggml"
---

# hvx_vec_cos_f32

**Type:** `function`  **File:** `ggml/src/ggml-hexagon/htp/hvx-sin-cos.h`

**Community:** [[communities/ggml]]

## Depends On

- [[nodes/hvx_vec_store_u]] _imports_
- [[nodes/hvx_vec_truncate_f32]] _imports_
- [[nodes/hvx_vec_splat_f32]] _calls_
- [[nodes/hvx_vec_floor_f32]] _calls_
- [[nodes/hvx_vec_add_f32_f32]] _calls_
- [[nodes/hvx_vec_mul_f32_f32]] _calls_
- [[nodes/hvx_vec_sub_f32_f32]] _calls_

## Used By

- [[nodes/rope_yarn_ramp]] _calls_
