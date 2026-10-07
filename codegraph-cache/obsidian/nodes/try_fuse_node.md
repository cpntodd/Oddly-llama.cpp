---
name: "try_fuse_node"
type: "function"
file: "ggml/src/ggml-hexagon/ggml-hexagon.cpp"
community: "ggml"
---

# try_fuse_node

**Type:** `function`  **File:** `ggml/src/ggml-hexagon/ggml-hexagon.cpp`

**Community:** [[communities/ggml]]

## Depends On

- [[nodes/ggml_can_fuse]] _calls_
- [[nodes/add_fused]] _calls_
- [[nodes/is_mergeable_mul_mat]] _calls_
- [[nodes/is_qkv_mergeable]] _calls_
- [[nodes/K]] _calls_
- [[nodes/V]] _calls_
- [[nodes/is_mergeable_mul_mat_pair]] _calls_

## Used By

- [[nodes/ggml_backend_hexagon_graph_compute]] _calls_
