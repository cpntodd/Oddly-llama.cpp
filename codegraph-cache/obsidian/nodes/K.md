---
name: "K"
type: "function"
file: "ggml/src/ggml-sycl/fattn-buffers.hpp"
community: "tests"
---

# K

**Type:** `function`  **File:** `ggml/src/ggml-sycl/fattn-buffers.hpp`

**Community:** [[communities/tests]]

## Depends On

- [[nodes/ggml_sycl_fattn_kv_buffers]] _calls_
- [[nodes/V]] _calls_

## Used By

- [[nodes/ggml_gen_hadamard]] _calls_
- [[nodes/llama_context_default_params]] _calls_
- [[nodes/ggml_calc_pool_output_size]] _calls_
- [[nodes/ggml_compute_forward_solve_tri]] _calls_
- [[nodes/MKL_ACCUM]] _calls_
- [[nodes/ggml_metal_op_flash_attn_ext_use_kv_f16]] _calls_
- [[nodes/entry_point]] _calls_
- [[nodes/try_fuse_node]] _calls_
- [[nodes/flash_attn_ext_f16_thread]] _calls_
- [[nodes/init_set_rows_row_ids]] _calls_
- [[nodes/n_cache_rows]] _calls_
- [[nodes/init_mul_mat_id_tensors]] _calls_
- [[nodes/ggml_sycl_fattn_tile_get_nbatch_K]] _calls_
