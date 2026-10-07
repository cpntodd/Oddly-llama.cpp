---
name: "ggml_sycl_flash_attn_ext_onednn_supported"
type: "function"
file: "ggml/src/ggml-sycl/fattn-onednn.cpp"
community: "ggml"
---

# ggml_sycl_flash_attn_ext_onednn_supported

**Type:** `function`  **File:** `ggml/src/ggml-sycl/fattn-onednn.cpp`

**Community:** [[communities/ggml]]

## Depends On

- [[nodes/jinja]] _imports_
- [[nodes/fattn-onednn.hpp]] _imports_
- [[nodes/syclex]] _imports_
- [[nodes/dequantize_row_q4_K_sycl_reorder]] _imports_
- [[nodes/dnnl]] _imports_
- [[nodes/types]] _calls_
- [[nodes/ggml_sycl_get_device]] _calls_
- [[nodes/parallel_for]] _calls_
- [[nodes/out]] _calls_
- [[nodes/op]] _calls_
- [[nodes/add_op]] _calls_
- [[nodes/engine_dnnl]] _calls_
- [[nodes/stream_dnnl]] _calls_
- [[nodes/pool]] _calls_
- [[nodes/get]] _calls_
- [[nodes/ggml_sycl_flash_attn_ext_tile]] _calls_
- [[nodes/kernel]] _calls_

## Used By

- [[nodes/ggml_sycl_get_best_fattn_kernel]] _calls_
