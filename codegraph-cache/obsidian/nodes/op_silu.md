---
name: "op_silu"
type: "function"
file: "ggml/src/ggml-sycl/element_wise.hpp"
community: "ggml"
---

# op_silu

**Type:** `function`  **File:** `ggml/src/ggml-sycl/element_wise.hpp`

**Community:** [[communities/ggml]]

## Depends On

- [[nodes/op_exp]] _calls_
- [[nodes/ggml_sycl_sqrt]] _calls_
- [[nodes/ggml_sycl_sin]] _calls_
- [[nodes/ggml_sycl_cos]] _calls_
- [[nodes/ggml_sycl_acc]] _calls_
- [[nodes/ggml_sycl_gelu]] _calls_
- [[nodes/ggml_sycl_silu]] _calls_
- [[nodes/ggml_sycl_gelu_quick]] _calls_
- [[nodes/ggml_sycl_swiglu_oai]] _calls_
- [[nodes/ggml_sycl_gelu_erf]] _calls_
- [[nodes/ggml_sycl_tanh]] _calls_
- [[nodes/ggml_sycl_relu]] _calls_
- [[nodes/ggml_sycl_sigmoid]] _calls_
- [[nodes/ggml_sycl_hardsigmoid]] _calls_
- [[nodes/ggml_sycl_hardswish]] _calls_
- [[nodes/ggml_sycl_exp]] _calls_
- [[nodes/ggml_sycl_expm1]] _calls_
- [[nodes/ggml_sycl_log]] _calls_
- [[nodes/ggml_sycl_softplus]] _calls_
- [[nodes/ggml_sycl_neg]] _calls_
- [[nodes/ggml_sycl_step]] _calls_
- [[nodes/ggml_sycl_leaky_relu]] _calls_
- [[nodes/ggml_sycl_sqr]] _calls_
- [[nodes/ggml_sycl_clamp]] _calls_
- [[nodes/ggml_sycl_xielu]] _calls_
- [[nodes/ggml_sycl_sgn]] _calls_
- [[nodes/ggml_sycl_abs]] _calls_
- [[nodes/ggml_sycl_elu]] _calls_
- [[nodes/ggml_sycl_geglu]] _calls_
- [[nodes/ggml_sycl_reglu]] _calls_

## Used By

- [[nodes/ggml_sycl_op_silu]] _calls_
- [[nodes/ggml_sycl_op_swiglu]] _calls_
- [[nodes/dispatch_type]] _calls_
- [[nodes/constexpr]] _calls_
