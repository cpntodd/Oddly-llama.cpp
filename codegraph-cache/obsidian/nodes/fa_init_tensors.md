---
name: "fa_init_tensors"
type: "function"
file: "tools/tuning/fa-vec.cpp"
community: "tests"
---

# fa_init_tensors

**Type:** `function`  **File:** `tools/tuning/fa-vec.cpp`

**Community:** [[communities/tests]]

## Depends On

- [[nodes/fa_cell_seed]] _calls_
- [[nodes/ggml_get_first_tensor]] _calls_
- [[nodes/ggml_get_next_tensor]] _calls_
- [[nodes/fa_init_kq_mask]] _calls_
- [[nodes/fa_init_uniform]] _calls_

## Used By

- [[nodes/tuner_fa_vec_run]] _calls_
