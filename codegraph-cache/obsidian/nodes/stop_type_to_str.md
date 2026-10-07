---
name: "stop_type_to_str"
type: "function"
file: "tools/server/server-task.cpp"
community: "tools"
---

# stop_type_to_str

**Type:** `function`  **File:** `tools/server/server-task.cpp`

**Community:** [[communities/tools]]

## Depends On

- [[nodes/build-info.h]] _imports_
- [[nodes/server-chat.h]] _imports_
- [[nodes/ResumableStreamState]] _imports_
- [[nodes/KeyValuePair]] _imports_
- [[nodes/common_grammar_builder]] _imports_
- [[nodes/llama_update]] _imports_
- [[nodes/ring_buffer]] _imports_
- [[nodes/speculative.md]] _imports_
- [[nodes/format_error_response]] _imports_
- [[nodes/to_json]] _calls_
- [[nodes/validate_utf8]] _calls_
- [[nodes/push_back]] _calls_
- [[nodes/update]] _calls_
- [[nodes/empty]] _calls_
- [[nodes/json_get_nested_values]] _calls_
- [[nodes/size]] _calls_
- [[nodes/server_chat_msg_diff_to_json_oaicompat]] _calls_
- [[nodes/random_string]] _calls_
- [[nodes/models]] _calls_
- [[nodes/parse]] _calls_
- [[nodes/insert]] _calls_
- [[nodes/alloc]] _calls_
- [[nodes/entry]] _calls_
- [[nodes/pop_front]] _calls_
- [[nodes/llama_state_seq_set_data_ext]] _calls_
- [[nodes/data]] _calls_
- [[nodes/clear]] _calls_

## Used By

- [[nodes/server_queue]] _imports_
- [[nodes/task_resets_idle_timer]] _imports_
- [[nodes/server_context_impl]] _imports_
- [[nodes/server_output_limits]] _imports_
- [[nodes/field_eval_context]] _imports_
