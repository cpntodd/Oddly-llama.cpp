---
name: "ggml_op_can_inplace"
type: "function"
file: "ggml/src/ggml-alloc.c"
community: "ggml"
---

# ggml_op_can_inplace

**Type:** `function`  **File:** `ggml/src/ggml-alloc.c`

**Community:** [[communities/ggml]]

## Depends On

- [[nodes/ggml-backend-impl.h]] _imports_
- [[nodes/ggml_graph_next_uid]] _imports_
- [[nodes/ggml_up32]] _imports_
- [[nodes/jinja]] _imports_

## Used By

- [[nodes/tensor_transformation]] _imports_
- [[nodes/clip_logger_state]] _imports_
- [[nodes/llama_ftype]] _imports_
- [[nodes/dummy_backend_context]] _imports_
- [[nodes/can_reuse_memory]] _calls_
- [[nodes/almost_equal]] _imports_
- [[nodes/ggml_hash_find_or_insert]] _calls_
- [[nodes/ggml_backend_meta_device]] _imports_
- [[nodes/ggml_backend_buft_alloc_buffer]] _imports_
- [[nodes/ggml_gallocr_allocate_node]] _calls_
- [[nodes/ggml_opt_dataset]] _imports_
- [[nodes/apir_buffer_context_t]] _imports_
- [[nodes/ggml_context_deleter]] _imports_
- [[nodes/that]] _imports_
