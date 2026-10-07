---
name: "init_tensor_kq_mask"
type: "function"
file: "tests/test-backend-ops.cpp"
community: "tests"
---

# init_tensor_kq_mask

**Type:** `function`  **File:** `tests/test-backend-ops.cpp`

**Community:** [[communities/tests]]

## Depends On

- [[nodes/rd]] _calls_
- [[nodes/ggml_fp32_to_fp16_row]] _calls_
- [[nodes/data]] _calls_
- [[nodes/ggml_backend_tensor_set]] _calls_

## Used By

- [[nodes/init_mul_mat_id_tensors]] _calls_
- [[nodes/hsk]] _calls_
- [[nodes/is_non_contiguous]] _calls_
