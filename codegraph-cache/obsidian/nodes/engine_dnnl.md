---
name: "engine_dnnl"
type: "function"
file: "ggml/src/ggml-sycl/common.hpp"
community: "ggml"
---

# engine_dnnl

**Type:** `function`  **File:** `ggml/src/ggml-sycl/common.hpp`

**Community:** [[communities/ggml]]

## Depends On

- [[nodes/make_engine]] _calls_
- [[nodes/stream_dnnl]] _calls_
- [[nodes/pool]] _calls_
- [[nodes/stream]] _calls_

## Used By

- [[nodes/ggml_sycl_flash_attn_ext_onednn_supported]] _calls_
- [[nodes/to_dt]] _calls_
