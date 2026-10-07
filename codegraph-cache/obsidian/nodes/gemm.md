---
name: "gemm"
type: "function"
file: "ggml/src/ggml-cpu/llamafile/sgemm.cpp"
community: "ggml"
---

# gemm

**Type:** `function`  **File:** `ggml/src/ggml-cpu/llamafile/sgemm.cpp`

**Community:** [[communities/ggml]]

## Depends On

- [[nodes/ggml_threadpool_chunk_set]] _calls_
- [[nodes/ggml_barrier]] _calls_
- [[nodes/BLOC_POS]] _calls_
- [[nodes/constexpr]] _calls_
- [[nodes/ggml_threadpool_chunk_add]] _calls_

## Used By

- [[nodes/repack_mxfp4_to_mxfp4_8_bl]] _calls_
- [[nodes/gemm_bloc_2x1]] _calls_
- [[nodes/A]] _calls_
- [[nodes/gemmMx4]] _calls_
- [[nodes/matmul_tiled]] _calls_
- [[nodes/KERNEL_Q0]] _calls_
- [[nodes/KERNEL_4x4]] _calls_
- [[nodes/MKL_ACCUM]] _calls_
- [[nodes/ggml_sycl_op_out_prod]] _calls_
- [[nodes/ggml_sycl_op_conv_3d]] _calls_
- [[nodes/get_device_backend_and_type]] _calls_
- [[nodes/max]] _calls_
- [[nodes/next_power_of_2]] _calls_
- [[nodes/ggml_sycl_group_norm]] _calls_
- [[nodes/t2_s32]] _calls_
- [[nodes/to_dt]] _calls_
