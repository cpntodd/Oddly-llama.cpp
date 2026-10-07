---
name: "update_slots"
type: "function"
file: "tools/server/server-context.cpp"
community: "tools"
---

# update_slots

**Type:** `function`  **File:** `tools/server/server-context.cpp`

**Community:** [[communities/tools]]

## Depends On

- [[nodes/ggml_time_us]] _calls_
- [[nodes/is_processing]] _calls_
- [[nodes/metrics_flush_idle]] _calls_
- [[nodes/t]] _calls_
- [[nodes/pre_decode]] _calls_
- [[nodes/render]] _calls_
- [[nodes/abort_all_slots]] _calls_
- [[nodes/size]] _calls_
- [[nodes/common_set_adapter_lora]] _calls_
- [[nodes/llama_set_embeddings]] _calls_
- [[nodes/need_embd]] _calls_
- [[nodes/llama_n_batch]] _calls_
- [[nodes/decode]] _calls_
- [[nodes/get_view]] _calls_
- [[nodes/llama_synchronize]] _calls_
- [[nodes/post_decode]] _calls_

## Used By

- [[nodes/task_resets_idle_timer]] _calls_
- [[nodes/load_model]] _calls_
