---
name: "json_value"
type: "function"
file: "tools/server/server-common.h"
community: "tools"
---

# json_value

**Type:** `function`  **File:** `tools/server/server-common.h`

**Community:** [[communities/tools]]

## Depends On

- [[nodes/KeyValuePair]] _imports_
- [[nodes/log.comp.cpp]] _imports_
- [[nodes/llama_update]] _imports_
- [[nodes/ResumableStreamState]] _imports_
- [[nodes/mtmd_serialization]] _imports_
- [[nodes/common_json_item]] _imports_
- [[nodes/jinja]] _imports_
- [[nodes/server_grammar_trigger]] _calls_
- [[nodes/value]] _calls_
- [[nodes/to_json]] _calls_
- [[nodes/format_error_response]] _calls_
- [[nodes/random_string]] _calls_
- [[nodes/gen_chatcmplid]] _calls_
- [[nodes/gen_tool_call_id]] _calls_
- [[nodes/lora_all_alora]] _calls_
- [[nodes/tokens]] _calls_
- [[nodes/server_tokens]] _calls_
- [[nodes/chunk]] _calls_
- [[nodes/serialize]] _calls_
- [[nodes/deserialize]] _calls_
- [[nodes/size]] _calls_
- [[nodes/clear]] _calls_
- [[nodes/clone]] _calls_
- [[nodes/json_is_array_of_numbers]] _calls_
- [[nodes/json_is_array_of_mixed_numbers_strings]] _calls_
- [[nodes/json_is_array_and_contains_numbers]] _calls_
- [[nodes/json_get_nested_values]] _calls_
- [[nodes/tokenize_mixed]] _calls_
- [[nodes/validate_utf8]] _calls_
- [[nodes/process_mtmd_prompt]] _calls_

## Used By

- [[nodes/lora_all_alora]] _calls_
- [[nodes/oaicompat_completion_params_parse]] _calls_
- [[nodes/is_valid_utf8]] _calls_
- [[nodes/wide_to_utf8]] _calls_
- [[nodes/res_err]] _calls_
- [[nodes/encode_qs]] _calls_
- [[nodes/make_error_response]] _calls_
- [[nodes/ex_wrapper]] _calls_
- [[nodes/impl]] _calls_
- [[nodes/error]] _calls_
- [[nodes/get_res_props]] _calls_
- [[nodes/entry_depth]] _calls_
- [[nodes/path_glob_match]] _calls_
- [[nodes/server_chat_convert_responses_to_chatcmpl]] _calls_
- [[nodes/if]] _calls_
- [[nodes/server_chat_convert_anthropic_to_oai]] _calls_
- [[nodes/server_chat_msg_diff_to_json_oaicompat]] _calls_
