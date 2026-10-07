---
name: "repack"
type: "function"
file: "ggml/src/ggml-cpu/kleidiai/kleidiai.cpp"
community: "ggml"
---

# repack

**Type:** `function`  **File:** `ggml/src/ggml-cpu/kleidiai/kleidiai.cpp`

**Community:** [[communities/ggml]]

## Depends On

- [[nodes/align_up]] _calls_
- [[nodes/kleidiai_collect_f32_chain]] _calls_
- [[nodes/kleidiai_collect_q8_chain]] _calls_
- [[nodes/kleidiai_collect_q4_chain]] _calls_
- [[nodes/kleidiai_pack_fallback_allowed]] _calls_

## Used By

- [[nodes/repack_mxfp4_to_mxfp4_8_bl]] _calls_
- [[nodes/forward_mul_mat_id]] _calls_
- [[nodes/ggml_backend_cpu_repack_buffer_init_tensor]] _calls_
- [[nodes/ggml_backend_cpu_kleidiai_buffer_init_tensor]] _calls_
- [[nodes/convert_mxfp4_to_5bit]] _calls_
- [[nodes/block_type_has_zp]] _calls_
- [[nodes/forward_mul_mat_id]] _calls_
- [[nodes/forward_flash_attn_ext_f16]] _calls_
- [[nodes/ggml_backend_riscv64_spacemit_buffer_clear]] _calls_
