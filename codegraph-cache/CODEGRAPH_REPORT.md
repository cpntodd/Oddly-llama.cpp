# CodeGraph Report
_Generated: 2026-10-07T04:40:36.637929Z_

**21478 nodes** · **29639 edges** · **10689 communities**

## God Nodes

_Highest-degree concepts everything flows through:_

- **Keys** `gguf-py/gguf/constants.py` — 432 connections
- **slice** `common/jinja/value.cpp` — 332 connections
- **map** `examples/llama.android/lib/src/main/java/com/arm/aichat/internal/gguf/GgufMetadataReaderImpl.kt` — 326 connections
- **types** `examples/llama.android/lib/src/main/java/com/arm/aichat/internal/gguf/GgufMetadataReaderImpl.kt` — 272 connections
- **jinja** `common/jinja/string.cpp` — 263 connections

## Community Clusters

### common (249 nodes)
Members: llama_download, is_string, arg_removed, common_models_handler_apply, common_models_handler_init …

### tools (236 nodes)
Members: assert_fail, set_error_handler, token, common_chat_get_asr_prompt, is_lfm2_template …

### common (215 nodes)
Members: clean_file_name, common_params_parse, common_chat_templates_source, common_chat_templates_was_explicit, common_batch_clear …

### src (213 nodes)
Members: decode_utf8, get_n_tokens, ggml_backend_alloc_ctx_tensors_from_buft, ggml_backend_alloc_ctx_tensors_from_buft_size, ggml_gallocr_get_buffer_size …

### build-sycl-2025 (206 nodes)
Members: command, colorizeFaviconSvg, padFaviconSvg, writeThemeFavicons, parseGrepLine …

### build-vulkan-gcc (203 nodes)
Members: accessors, getHastNodeId, BlockIdGenerator, Window, Window …

### ggml (195 nodes)
Members: diag.comp.cpp, fill.comp.cpp, im2col.comp.cpp, repeat_back.comp.cpp, solve_tri.comp.cpp …

### tools (185 nodes)
Members: ToolResultContentItem, ToolsService, fakeFetch, is401, expectUpright …

### tools (180 nodes)
Members: info, warn, darkImageResolver, buildInfoPlugin, nerdamerPlugin …

### tests (180 nodes)
Members: print_tensor_info, ggml_backend_meta_buffer_type_alloc_buffer, ggml_backend_tensor_set, ggml_is_view_op, op …

## Surprising Connections

- **TOKENIZER_TYPE** →(imports)→ **ai_should_log**
- **TOKENIZER_TYPE** →(imports)→ **os.h**
- **TOKENIZER_TYPE** →(imports)→ **common_json_item**
- **split_str_to_n_bytes** →(imports)→ **ai_should_log**
- **split_str_to_n_bytes** →(imports)→ **os.h**
- **split_str_to_n_bytes** →(imports)→ **gguf.py**
- **GGMLFormat** →(imports)→ **ai_should_log**
- **GGMLFormat** →(imports)→ **os.h**

## Suggested Questions

- What does Keys depend on?
- What uses Keys?
- What is the relationship between TOKENIZER_TYPE and other modules?
- What is the relationship between GGMLFormat and other modules?
- Which files have the most connections?

## Confidence Breakdown

- **EXTRACTED**: 15585 edges
- **INFERRED**: 14054 edges

## Knowledge Gaps

**Isolated nodes** (10180 with no edges):
  - `ty.toml` in `ty.toml`
  - `AGENTS.md` in `AGENTS.md`
  - `CONTRIBUTING.md` in `CONTRIBUTING.md`
  - `pyproject.toml` in `pyproject.toml`
  - `Makefile` in `Makefile`
  - `CLAUDE.md` in `CLAUDE.md`
  - `pyrightconfig.json` in `pyrightconfig.json`
  - `CMakeLists.txt` in `CMakeLists.txt`
  - …and 10172 more

**Thin communities** (10180 single-node clusters):
  - `.pre-commit-config.yaml` in `.pre-commit-config.yaml`
  - `AGENTS.md` in `AGENTS.md`
  - `CLAUDE.md` in `CLAUDE.md`
  - `CMakeLists.txt` in `CMakeLists.txt`
  - `CMakePresets.json` in `CMakePresets.json`
  - …and 10175 more

_No ambiguous edges._
