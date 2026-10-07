---
name: "ggml_graph_reset"
type: "function"
file: "ggml/src/ggml.c"
community: "ggml"
---

# ggml_graph_reset

**Type:** `function`  **File:** `ggml/src/ggml.c`

**Community:** [[communities/ggml]]

## Depends On

- [[nodes/ggml_graph_get_grad_acc]] _calls_
- [[nodes/ggml_set_zero]] _calls_
- [[nodes/ggml_is_scalar]] _calls_
- [[nodes/ggml_backend_tensor_set]] _calls_

## Used By

- [[nodes/ggml_opt_build]] _calls_
- [[nodes/ggml_opt_reset]] _calls_
- [[nodes/ggml_opt_alloc]] _calls_
- [[nodes/eval_grad]] _calls_
