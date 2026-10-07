---
name: "llama_decode_text"
type: "function"
file: "src/llama-vocab.cpp"
community: "src"
---

# llama_decode_text

**Type:** `function`  **File:** `src/llama-vocab.cpp`

**Community:** [[communities/src]]

## Depends On

- [[nodes/unicode_cpts_from_utf8]] _calls_
- [[nodes/unicode_cpt_to_utf8]] _calls_
- [[nodes/unicode_utf8_to_byte]] _calls_
- [[nodes/format]] _calls_
- [[nodes/tokenize]] _calls_
- [[nodes/empty]] _calls_
- [[nodes/push_back]] _calls_
- [[nodes/llama_escape_whitespace]] _calls_
- [[nodes/size]] _calls_
- [[nodes/append_bos]] _calls_
- [[nodes/append]] _calls_
- [[nodes/append_eos]] _calls_
- [[nodes/check_double_bos_eos]] _calls_
- [[nodes/llama_unescape_whitespace]] _calls_
