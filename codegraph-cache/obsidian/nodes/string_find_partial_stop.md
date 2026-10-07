---
name: "string_find_partial_stop"
type: "function"
file: "common/common.h"
community: "common"
---

# string_find_partial_stop

**Type:** `function`  **File:** `common/common.h`

**Community:** [[communities/common]]

## Depends On

- [[nodes/empty]] _calls_
- [[nodes/size]] _calls_
- [[nodes/string_ends_with]] _calls_
- [[nodes/string_parse_kv_override]] _calls_
- [[nodes/string_process_escapes]] _calls_
- [[nodes/string_from]] _calls_
- [[nodes/glob_match]] _calls_
- [[nodes/common_get_env]] _calls_
- [[nodes/common_set_env]] _calls_
- [[nodes/fs_validate_filename]] _calls_
- [[nodes/fs_create_directory_with_parents]] _calls_
- [[nodes/fs_is_directory]] _calls_
- [[nodes/fs_get_cache_directory]] _calls_
- [[nodes/fs_get_cache_file]] _calls_
- [[nodes/fs_get_config_directory]] _calls_
- [[nodes/fs_open_ifstream]] _calls_
- [[nodes/tty_can_use_colors]] _calls_
- [[nodes/sampler]] _calls_
- [[nodes/common_init_from_params]] _calls_
- [[nodes/common_model_params_to_llama]] _calls_
- [[nodes/common_context_params_to_llama]] _calls_
- [[nodes/common_set_adapter_lora]] _calls_
- [[nodes/common_get_model_endpoint]] _calls_
- [[nodes/ggml_threadpool_params_from_cpu_params]] _calls_
- [[nodes/common_threadpools]] _calls_
- [[nodes/init]] _calls_
- [[nodes/decltype]] _calls_
- [[nodes/common_context_can_seq_rm]] _calls_
- [[nodes/common_batch_clear]] _calls_
- [[nodes/common_replay_last_token]] _calls_

## Used By

- [[nodes/find_stopping_strings]] _calls_
