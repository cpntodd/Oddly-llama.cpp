---
name: "get_tensor_ov_name"
type: "function"
file: "ggml/src/ggml-openvino/ggml-decoder.cpp"
community: "ggml"
---

# get_tensor_ov_name

**Type:** `function`  **File:** `ggml/src/ggml-openvino/ggml-decoder.cpp`

**Community:** [[communities/ggml]]

## Depends On

- [[nodes/ggml_hash_find]] _calls_
- [[nodes/ggml_bitset_get]] _calls_
- [[nodes/string]] _calls_
- [[nodes/decltype]] _calls_
- [[nodes/value]] _calls_
- [[nodes/ggml_is_contiguous]] _calls_
- [[nodes/view]] _calls_
- [[nodes/ggml_nelements]] _calls_
- [[nodes/is_same_shape]] _calls_
- [[nodes/is_conv_state_writeback]] _calls_
- [[nodes/is_conv_states_all_tensor]] _calls_
- [[nodes/is_moe_expert_sum_add]] _calls_
- [[nodes/ggml_backend_openvino_buffer_get_ctx_id]] _calls_
- [[nodes/ggml_type_size]] _calls_
- [[nodes/is_inplace_op]] _calls_
- [[nodes/ggml_nbytes]] _calls_

## Used By

- [[nodes/is_mul_mat_id_expert_weight]] _calls_
- [[nodes/print_tensor_address_map]] _calls_
