---
name: "print_debug_tensor"
type: "function"
file: "tools/cvector-generator/pca.hpp"
community: "ggml"
---

# print_debug_tensor

**Type:** `function`  **File:** `tools/cvector-generator/pca.hpp`

**Community:** [[communities/ggml]]

## Depends On

- [[nodes/KeyValuePair]] _imports_
- [[nodes/llama_update]] _imports_
- [[nodes/ggml_graph_next_uid]] _imports_
- [[nodes/ggml-cuda.h]] _imports_
- [[nodes/ggml_backend_metal_buffer_shared_free_buffer]] _imports_
- [[nodes/jinja]] _imports_
- [[nodes/ggml_type_name]] _calls_
- [[nodes/ggml_get_f32_nd]] _calls_
- [[nodes/pca_model]] _calls_
- [[nodes/ggml_backend_metal_init]] _calls_
- [[nodes/ggml_backend_cpu_init]] _calls_
- [[nodes/ggml_tensor_overhead]] _calls_
- [[nodes/ggml_init]] _calls_
- [[nodes/ggml_set_name]] _calls_
- [[nodes/ggml_backend_alloc_ctx_tensors]] _calls_
- [[nodes/ggml_backend_tensor_set]] _calls_
- [[nodes/ggml_nbytes]] _calls_
- [[nodes/ggml_nelements]] _calls_
- [[nodes/ggml_free]] _calls_
- [[nodes/ggml_backend_buffer_free]] _calls_
- [[nodes/ggml_backend_free]] _calls_
- [[nodes/ggml_graph_overhead]] _calls_
- [[nodes/buf]] _calls_
- [[nodes/ggml_new_graph]] _calls_
- [[nodes/ggml_format_name]] _calls_
- [[nodes/ggml_build_forward_expand]] _calls_
- [[nodes/ggml_gallocr_alloc_graph]] _calls_
- [[nodes/ggml_backend_is_cpu]] _calls_
- [[nodes/ggml_backend_cpu_set_n_threads]] _calls_
- [[nodes/ggml_backend_graph_compute]] _calls_

## Used By

- [[nodes/Iter]] _imports_
- [[nodes/save_tensor_for_layer]] _calls_
- [[nodes/build_v_diff]] _calls_
- [[nodes/export_gguf]] _calls_
