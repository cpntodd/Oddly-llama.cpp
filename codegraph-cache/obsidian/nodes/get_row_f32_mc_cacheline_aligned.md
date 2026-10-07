---
name: "get_row_f32_mc_cacheline_aligned"
type: "function"
file: "ggml/src/ggml-et/et-kernels/src/get_rows_f32.c"
community: "ggml"
---

# get_row_f32_mc_cacheline_aligned

**Type:** `function`  **File:** `ggml/src/ggml-et/et-kernels/src/get_rows_f32.c`

**Community:** [[communities/ggml]]

## Depends On

- [[nodes/get_relative_thread_id]] _calls_
- [[nodes/get_num_threads]] _calls_
- [[nodes/rows]] _calls_
- [[nodes/get_elements_per_work_unit]] _calls_
- [[nodes/copy_row_cache_align]] _calls_
- [[nodes/copy_f16_row]] _calls_
- [[nodes/copy_q8_0_row_cache_aligned]] _calls_
- [[nodes/copy_q4_0_row_cache_aligned]] _calls_
- [[nodes/copy_q4_K_row_cache_aligned]] _calls_

## Used By

- [[nodes/entry_point]] _calls_
