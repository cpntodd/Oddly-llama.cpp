---
name: "ggml_sycl_init"
type: "function"
file: "ggml/src/ggml-sycl/ggml-sycl.cpp"
community: "ggml"
---

# ggml_sycl_init

**Type:** `function`  **File:** `ggml/src/ggml-sycl/ggml-sycl.cpp`

**Community:** [[communities/ggml]]

## Depends On

- [[nodes/log_to_file_callback]] _imports_
- [[nodes/ggml_graph_next_uid]] _imports_
- [[nodes/ggml_up32]] _imports_
- [[nodes/ptq1-t2.hpp]] _imports_
- [[nodes/ggml-backend-impl.h]] _imports_
- [[nodes/ggml_sycl_add_id]] _imports_
- [[nodes/KeyValuePair]] _imports_
- [[nodes/neg_infinity]] _imports_
- [[nodes/fwht.comp.cpp]] _imports_
- [[nodes/DnnlGemmWrapper]] _imports_
- [[nodes/w8a8.hpp]] _imports_
- [[nodes/ggml_sycl_op_get_rows]] _imports_
- [[nodes/norm.comp.cpp]] _imports_
- [[nodes/presets.hpp]] _imports_
- [[nodes/must]] _imports_
- [[nodes/repeat_back.comp.cpp]] _imports_
- [[nodes/utils]] _imports_
- [[nodes/sycl]] _imports_
- [[nodes/dsv4-hc.hpp]] _imports_
- [[nodes/lightning-indexer.hpp]] _imports_
- [[nodes/conv2d_params]] _imports_
- [[nodes/conv2d_dw_params]] _imports_
- [[nodes/conv2d-transpose.hpp]] _imports_
- [[nodes/ssm_conv.comp.cpp]] _imports_
- [[nodes/syclex]] _imports_
- [[nodes/ssm_scan.comp.cpp]] _imports_
- [[nodes/fill.comp.cpp]] _imports_
- [[nodes/cumsum.comp.cpp]] _imports_
- [[nodes/diag.comp.cpp]] _imports_
- [[nodes/opt-step.hpp]] _imports_

## Used By

- [[nodes/main]] _imports_
- [[nodes/fs]] _imports_
- [[nodes/syclexp]] _imports_
- [[nodes/DnnlGemmWrapper]] _imports_
