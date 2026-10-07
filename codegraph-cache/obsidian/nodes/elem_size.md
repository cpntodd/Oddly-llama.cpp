---
name: "elem_size"
type: "function"
file: "ggml/src/ggml-sycl/concat.cpp"
community: "ggml"
---

# elem_size

**Type:** `function`  **File:** `ggml/src/ggml-sycl/concat.cpp`

**Community:** [[communities/ggml]]

## Depends On

- [[nodes/ggml_graph_next_uid]] _imports_
- [[nodes/concat.comp.cpp]] _imports_
- [[nodes/ggml_type_size]] _calls_
- [[nodes/ggml_blck_size]] _calls_
- [[nodes/parallel_for]] _calls_
- [[nodes/kernel]] _calls_

## Used By

- [[nodes/concat_impl_sycl]] _calls_
