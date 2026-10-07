---
name: "init_kleidiai_context"
type: "function"
file: "ggml/src/ggml-cpu/kleidiai/kleidiai.cpp"
community: "ggml"
---

# init_kleidiai_context

**Type:** `function`  **File:** `ggml/src/ggml-cpu/kleidiai/kleidiai.cpp`

**Community:** [[communities/ggml]]

## Depends On

- [[nodes/ggml_critical_section_start]] _calls_
- [[nodes/getenv]] _calls_
- [[nodes/ggml_feats_get_arch64_runtime]] _calls_
- [[nodes/parse_uint_env]] _calls_
- [[nodes/detect_num_smcus]] _calls_
- [[nodes/is_sme_family]] _calls_
- [[nodes/ggml_critical_section_end]] _calls_

## Used By

- [[nodes/ggml_backend_cpu_kleidiai_buffer_type]] _calls_
