---
name: "common_replay_last_token"
type: "function"
file: "common/common.cpp"
community: "tests"
---

# common_replay_last_token

**Type:** `function`  **File:** `common/common.cpp`

**Community:** [[communities/tests]]

## Depends On

- [[nodes/size]] _calls_
- [[nodes/llama_state_save_file]] _calls_
- [[nodes/empty]] _calls_
- [[nodes/clear]] _calls_
- [[nodes/llama_state_seq_get_size_ext]] _calls_
- [[nodes/llama_state_seq_get_data_ext]] _calls_
- [[nodes/llama_state_seq_set_data_ext]] _calls_

## Used By

- [[nodes/llama_completion]] _calls_
- [[nodes/string_find_partial_stop]] _calls_
- [[nodes/test_state_load]] _calls_
- [[nodes/test_seq_cp_host]] _calls_
- [[nodes/test_seq_cp_device]] _calls_
