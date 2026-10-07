---
name: "load_hparams"
type: "function"
file: "tools/mtmd/clip.cpp"
community: "ggml"
---

# load_hparams

**Type:** `function`  **File:** `tools/mtmd/clip.cpp`

**Community:** [[communities/ggml]]

## Depends On

- [[nodes/get_string]] _calls_
- [[nodes/clip_projector_type_from_string]] _calls_
- [[nodes/string_format]] _calls_
- [[nodes/models]] _calls_
- [[nodes/get_u32]] _calls_
- [[nodes/get_f32]] _calls_
- [[nodes/get_i32]] _calls_
- [[nodes/get_arr_int]] _calls_
- [[nodes/get_bool]] _calls_
- [[nodes/get_arr_f32]] _calls_
- [[nodes/set_internvl_dhr_res_candidates]] _calls_
- [[nodes/value]] _calls_
- [[nodes/tokens]] _calls_
- [[nodes/assign]] _calls_
- [[nodes/set_llava_uhd_res_candidates]] _calls_
- [[nodes/ggml_get_mem_size]] _calls_

## Used By

- [[nodes/clip_init]] _calls_
- [[nodes/llama_prepare_model_devices]] _calls_
- [[nodes/params]] _calls_
- [[nodes/llama_model_quantize_impl]] _calls_
