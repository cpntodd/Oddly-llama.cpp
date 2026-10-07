---
name: "ggml_backend_hexagon_graph_compute"
type: "function"
file: "ggml/src/ggml-hexagon/ggml-hexagon.cpp"
community: "ggml"
---

# ggml_backend_hexagon_graph_compute

**Type:** `function`  **File:** `ggml/src/ggml-hexagon/ggml-hexagon.cpp`

**Community:** [[communities/ggml]]

## Depends On

- [[nodes/try_fuse_node]] _calls_
- [[nodes/op_remap_to_htp]] _calls_
- [[nodes/htp_op_is_unary]] _calls_
- [[nodes/flush]] _calls_
