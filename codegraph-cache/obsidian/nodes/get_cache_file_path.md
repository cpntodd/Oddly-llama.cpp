---
name: "get_cache_file_path"
type: "function"
file: "tests/gguf-model-data.cpp"
community: "tests"
---

# get_cache_file_path

**Type:** `function`  **File:** `tests/gguf-model-data.cpp`

**Community:** [[communities/tests]]

## Depends On

- [[nodes/sanitize_for_path]] _calls_
- [[nodes/read_file]] _calls_
- [[nodes/fs_create_directory_with_parents]] _calls_
- [[nodes/get_default_cache_dir]] _calls_
- [[nodes/value]] _calls_
- [[nodes/ggml_get_first_tensor]] _calls_
- [[nodes/ggml_get_next_tensor]] _calls_
- [[nodes/gguf_set_val_u16]] _calls_
