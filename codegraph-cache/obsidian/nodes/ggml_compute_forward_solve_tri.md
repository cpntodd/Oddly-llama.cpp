---
name: "ggml_compute_forward_solve_tri"
type: "function"
file: "ggml/src/ggml-cpu/ops.cpp"
community: "ggml"
---

# ggml_compute_forward_solve_tri

**Type:** `function`  **File:** `ggml/src/ggml-cpu/ops.cpp`

**Community:** [[communities/ggml]]

## Depends On

- [[nodes/ggml_compute_forward_solve_tri_f32]] _calls_
- [[nodes/ggml_get_op_params_i32]] _calls_
- [[nodes/ggml_is_contiguous_rows]] _calls_
- [[nodes/ggml_is_contiguous]] _calls_
- [[nodes/K]] _calls_
- [[nodes/view]] _calls_
- [[nodes/ggml_vec_mul_f32]] _calls_
- [[nodes/ggml_vec_scale_f32]] _calls_
- [[nodes/ggml_vec_dot_f32]] _calls_
- [[nodes/ggml_vec_mad_f32]] _calls_
- [[nodes/ggml_is_numa]] _calls_
- [[nodes/ggml_threadpool_chunk_set]] _calls_
- [[nodes/ggml_barrier]] _calls_
- [[nodes/ggml_threadpool_chunk_add]] _calls_

## Used By

- [[nodes/ggml_compute_forward]] _calls_
