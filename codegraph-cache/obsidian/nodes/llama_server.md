---
name: "llama_server"
type: "function"
file: "tools/server/server.cpp"
community: "tools"
---

# llama_server

**Type:** `function`  **File:** `tools/server/server.cpp`

**Community:** [[communities/tools]]

## Depends On

- [[nodes/common_init]] _calls_
- [[nodes/server_stream_session_manager_start]] _calls_
- [[nodes/common_params_parse]] _calls_
- [[nodes/llama_backend_init]] _calls_
- [[nodes/llama_numa_init]] _calls_
- [[nodes/common_models_handler_init]] _calls_
- [[nodes/common_models_handler_is_preset_repo]] _calls_
- [[nodes/common_models_handler_apply]] _calls_
- [[nodes/common_params_print_info]] _calls_
- [[nodes/init]] _calls_
- [[nodes/ex_wrapper]] _calls_
- [[nodes/server_stream_make_get_handler]] _calls_
- [[nodes/server_stream_make_lookup_handler]] _calls_
- [[nodes/server_stream_make_delete_handler]] _calls_
- [[nodes/safe_json_to_str]] _calls_
- [[nodes/setup]] _calls_
- [[nodes/size]] _calls_
- [[nodes/server_stream_session_manager_stop]] _calls_
- [[nodes/has_value]] _calls_
- [[nodes/llama_backend_free]] _calls_
- [[nodes/join]] _calls_
- [[nodes/terminate]] _calls_
- [[nodes/load_model]] _calls_
- [[nodes/sigaction]] _calls_
- [[nodes/signal_handler]] _calls_
- [[nodes/string_ends_with]] _calls_
- [[nodes/common_memory_breakdown_print]] _calls_

## Used By

- [[nodes/main]] _calls_
- [[nodes/signal_handler]] _calls_
