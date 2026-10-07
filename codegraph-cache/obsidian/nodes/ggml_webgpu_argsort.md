---
name: "ggml_webgpu_argsort"
type: "function"
file: "ggml/src/ggml-webgpu/ggml-webgpu.cpp"
community: "ggml"
---

# ggml_webgpu_argsort

**Type:** `function`  **File:** `ggml/src/ggml-webgpu/ggml-webgpu.cpp`

**Community:** [[communities/ggml]]

## Depends On

- [[nodes/get_argsort_pipeline]] _calls_
- [[nodes/get_argsort_merge_pipeline]] _calls_
- [[nodes/ggml_nrows]] _calls_
- [[nodes/ggml_webgpu_tensor_offset]] _calls_
- [[nodes/ggml_webgpu_tensor_misalignment]] _calls_
- [[nodes/ggml_type_size]] _calls_
- [[nodes/ggml_webgpu_tensor_align_offset]] _calls_
- [[nodes/compute_2d_workgroups]] _calls_
- [[nodes/ggml_webgpu_tensor_buf]] _calls_

## Used By

- [[nodes/ggml_webgpu_upscale]] _calls_
