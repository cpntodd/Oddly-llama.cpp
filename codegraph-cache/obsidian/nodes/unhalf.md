---
name: "unhalf"
type: "function"
file: "ggml/src/ggml-cpu/llamafile/sgemm.cpp"
community: "ggml"
---

# unhalf

**Type:** `function`  **File:** `ggml/src/ggml-cpu/llamafile/sgemm.cpp`

**Community:** [[communities/ggml]]

## Depends On

- [[nodes/ggml_up32]] _imports_
- [[nodes/ggml_compute_params]] _imports_
- [[nodes/ggml-quants.h]] _imports_
- [[nodes/ggml_lookup_fp16_to_fp32]] _imports_
- [[nodes/type_traits]] _imports_

## Used By

- [[nodes/ggml_arm_arch_features_type]] _imports_
- [[nodes/A]] _calls_
- [[nodes/gemm4xN]] _calls_
- [[nodes/gemmMx4]] _calls_
- [[nodes/packNormalInt4]] _calls_
- [[nodes/KERNEL_Q0]] _calls_
