---
name: "format_error_response"
type: "function"
file: "tools/server/server-common.cpp"
community: "tools"
---

# format_error_response

**Type:** `function`  **File:** `tools/server/server-common.cpp`

**Community:** [[communities/tools]]

## Depends On

- [[nodes/KeyValuePair]] _imports_
- [[nodes/print_usage]] _imports_
- [[nodes/log.comp.cpp]] _imports_
- [[nodes/llama_update]] _imports_
- [[nodes/mtmd_serialization]] _imports_
- [[nodes/mtmd_helper_video]] _imports_
- [[nodes/ResumableStreamState]] _imports_
- [[nodes/base64_error]] _imports_
- [[nodes/type_traits]] _imports_
- [[nodes/to_json]] _calls_

## Used By

- [[nodes/stop_type_to_str]] _imports_
- [[nodes/server_http_context]] _imports_
- [[nodes/parse_gcp_predict_response]] _calls_
- [[nodes/server_subproc]] _imports_
- [[nodes/router_validate_model]] _calls_
- [[nodes/encode_qs]] _calls_
- [[nodes/class]] _imports_
- [[nodes/make_error_response]] _calls_
- [[nodes/ex_wrapper]] _calls_
- [[nodes/server_model_status]] _imports_
- [[nodes/server_tool]] _imports_
- [[nodes/server_task_type]] _imports_
- [[nodes/json_value]] _calls_
- [[nodes/server_mcp_server_config]] _imports_
- [[nodes/server_output_limits]] _imports_
- [[nodes/impl]] _calls_
- [[nodes/get_res_props]] _calls_
- [[nodes/get_header]] _calls_
- [[nodes/server_chat_convert_responses_to_chatcmpl]] _imports_
- [[nodes/field_eval_context]] _imports_
