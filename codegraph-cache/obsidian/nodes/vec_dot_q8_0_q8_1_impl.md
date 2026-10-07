---
name: "vec_dot_q8_0_q8_1_impl"
type: "function"
file: "ggml/src/ggml-sycl/vecdotq.hpp"
community: "ggml"
---

# vec_dot_q8_0_q8_1_impl

**Type:** `function`  **File:** `ggml/src/ggml-sycl/vecdotq.hpp`

**Community:** [[communities/ggml]]

## Depends On

- [[nodes/ggml_sycl_dp4a]] _calls_
- [[nodes/dp4a]] _calls_
- [[nodes/x]] _calls_
- [[nodes/block]] _calls_
- [[nodes/ggml_sycl_ptq1_0_trit]] _calls_
- [[nodes/get_int_b1]] _calls_
- [[nodes/ggml_sycl_e8m0_to_fp32]] _calls_
- [[nodes/get_int_b4]] _calls_
- [[nodes/ggml_sycl_ue4m3_to_fp32]] _calls_
- [[nodes/float]] _calls_
- [[nodes/get_int_from_int8]] _calls_
- [[nodes/bad_arch]] _calls_

## Used By

- [[nodes/byte_sub_4]] _calls_
