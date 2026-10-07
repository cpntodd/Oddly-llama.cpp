---
name: "build_sdpa"
type: "function"
file: "ggml/src/ggml-sycl/fattn-onednn.cpp"
community: "ggml"
---

# build_sdpa

**Type:** `function`  **File:** `ggml/src/ggml-sycl/fattn-onednn.cpp`

**Community:** [[communities/ggml]]

## Depends On

- [[nodes/op]] _calls_
- [[nodes/add_op]] _calls_
- [[nodes/engine_dnnl]] _calls_
- [[nodes/stream_dnnl]] _calls_
- [[nodes/pool]] _calls_
- [[nodes/ggml_sycl_get_device]] _calls_
- [[nodes/kernel]] _calls_
- [[nodes/ggml_sycl_flash_attn_ext_tile]] _calls_
