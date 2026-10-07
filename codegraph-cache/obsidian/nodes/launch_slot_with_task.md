---
name: "launch_slot_with_task"
type: "function"
file: "tools/server/server-context.cpp"
community: "tools"
---

# launch_slot_with_task

**Type:** `function`  **File:** `tools/server/server-context.cpp`

**Community:** [[communities/tools]]

## Depends On

- [[nodes/empty]] _calls_
- [[nodes/size]] _calls_
- [[nodes/clear]] _calls_
- [[nodes/lora_all_alora]] _calls_
- [[nodes/send_error]] _calls_
- [[nodes/llama_adapter_get_alora_n_invocation_tokens]] _calls_
- [[nodes/safe_json_to_str]] _calls_
- [[nodes/to_json]] _calls_
- [[nodes/reset]] _calls_
- [[nodes/llama_set_sampler]] _calls_
- [[nodes/common_sampler_print]] _calls_
- [[nodes/print]] _calls_

## Used By

- [[nodes/oaicompat_completion_params_parse]] _calls_
- [[nodes/launch_slots_with_parent_task]] _calls_
- [[nodes/process_single_task]] _calls_
