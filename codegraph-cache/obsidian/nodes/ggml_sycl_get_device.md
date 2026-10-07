---
name: "ggml_sycl_get_device"
type: "function"
file: "ggml/src/ggml-sycl/common.hpp"
community: "ggml"
---

# ggml_sycl_get_device

**Type:** `function`  **File:** `ggml/src/ggml-sycl/common.hpp`

**Community:** [[communities/ggml]]

## Depends On

- [[nodes/get_current_device_id]] _calls_
- [[nodes/crash]] _calls_
- [[nodes/block]] _calls_
- [[nodes/ggml_sycl_pool]] _calls_
- [[nodes/alloc]] _calls_
- [[nodes/ggml_sycl_pool_alloc]] _calls_
- [[nodes/pool]] _calls_
- [[nodes/ggml_sycl_free_device]] _calls_
- [[nodes/release_extra_gpu]] _calls_
- [[nodes/ggml_backend_sycl_context]] _calls_
- [[nodes/device]] _calls_
- [[nodes/warp_reduce_sum]] _calls_
- [[nodes/x]] _calls_

## Used By

- [[nodes/get_dequantize_V]] _calls_
- [[nodes/ggml_sycl_flash_attn_ext_onednn_supported]] _calls_
- [[nodes/ggml_sycl_flash_attn_ext]] _calls_
- [[nodes/launch_fattn_tile_switch_ncols1]] _calls_
- [[nodes/launch_fattn_tile_switch_ncols2]] _calls_
