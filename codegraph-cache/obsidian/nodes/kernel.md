---
name: "kernel"
type: "function"
file: "ggml/src/ggml-cpu/llamafile/sgemm.cpp"
community: "ggml"
---

# kernel

**Type:** `function`  **File:** `ggml/src/ggml-cpu/llamafile/sgemm.cpp`

**Community:** [[communities/ggml]]

## Depends On

- [[nodes/constexpr]] _calls_
- [[nodes/KERNEL_4x8]] _calls_
- [[nodes/KERNEL_8x8]] _calls_
- [[nodes/KERNEL_8x4]] _calls_

## Used By

- [[nodes/KERNEL_Q0]] _calls_
- [[nodes/KERNEL_4x4]] _calls_
- [[nodes/elem_size]] _calls_
- [[nodes/atomic_fetch_add]] _calls_
- [[nodes/ggml_et_memset]] _calls_
- [[nodes/atomic_store_f16]] _calls_
- [[nodes/wrap_around]] _calls_
- [[nodes/op_im2col]] _calls_
- [[nodes/ggml_sycl_flash_attn_ext_onednn_supported]] _calls_
