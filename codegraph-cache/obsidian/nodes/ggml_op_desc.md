---
name: "ggml_op_desc"
type: "function"
file: "ggml/src/ggml.c"
community: "ggml"
---

# ggml_op_desc

**Type:** `function`  **File:** `ggml/src/ggml.c`

**Community:** [[communities/ggml]]

## Depends On

- [[nodes/ggml_get_unary_op]] _calls_
- [[nodes/ggml_unary_op_name]] _calls_
- [[nodes/ggml_get_glu_op]] _calls_
- [[nodes/ggml_glu_op_name]] _calls_
- [[nodes/ggml_op_name]] _calls_

## Used By

- [[nodes/common_debug_cb_eval]] _calls_
- [[nodes/ggml_backend_sched_backend_from_buffer]] _calls_
- [[nodes/ggml_backend_sched_print_assignments]] _calls_
- [[nodes/ggml_gallocr_alloc_graph_impl]] _calls_
- [[nodes/ggml_backend_zendnn_graph_compute]] _calls_
- [[nodes/backend_backend_graph_compute]] _calls_
- [[nodes/ggml_metal_op_encode_impl]] _calls_
- [[nodes/ggml_metal_op_encode]] _calls_
- [[nodes/ggml_backend_blas_graph_compute]] _calls_
- [[nodes/ggml_hexagon_dump_op_supp]] _calls_
- [[nodes/op_remap_to_htp]] _calls_
- [[nodes/ggml_backend_hexagon_device_supports_op]] _calls_
- [[nodes/op_desc]] _calls_
- [[nodes/matches_filter]] _calls_
- [[nodes/usage]] _calls_
