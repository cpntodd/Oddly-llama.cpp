---
name: "tokenize_input_subprompt"
type: "function"
file: "tools/server/server-common.cpp"
community: "tools"
---

# tokenize_input_subprompt

**Type:** `function`  **File:** `tools/server/server-common.cpp`

**Community:** [[communities/tools]]

## Depends On

- [[nodes/is_string]] _calls_
- [[nodes/json_is_array_of_mixed_numbers_strings]] _calls_
- [[nodes/tokenize_mixed]] _calls_
- [[nodes/server_tokens]] _calls_
- [[nodes/json_is_array_of_numbers]] _calls_
- [[nodes/base64_decode]] _calls_
- [[nodes/process_mtmd_prompt]] _calls_
- [[nodes/json_is_array_and_contains_numbers]] _calls_
- [[nodes/size]] _calls_

## Used By

- [[nodes/is_valid_utf8]] _calls_
