---
name: "extract_mxfp4_data"
type: "function"
file: "ggml/src/ggml-openvino/ggml-quants.cpp"
community: "ggml"
---

# extract_mxfp4_data

**Type:** `function`  **File:** `ggml/src/ggml-openvino/ggml-quants.cpp`

**Community:** [[communities/ggml]]

## Depends On

- [[nodes/get_size]] _calls_
- [[nodes/parallel_for]] _calls_
- [[nodes/pack_32_mxfp4_for_openvino]] _calls_
- [[nodes/unpack_32_4]] _calls_

## Used By

- [[nodes/get_scale_min_k4]] _calls_
