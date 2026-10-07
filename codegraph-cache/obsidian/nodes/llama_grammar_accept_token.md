---
name: "llama_grammar_accept_token"
type: "function"
file: "src/llama-grammar.cpp"
community: "src"
---

# llama_grammar_accept_token

**Type:** `function`  **File:** `src/llama-grammar.cpp`

**Community:** [[communities/src]]

## Depends On

- [[nodes/decode_utf8]] _calls_
- [[nodes/size]] _calls_
- [[nodes/empty]] _calls_
- [[nodes/llama_grammar_is_end_of_sequence]] _calls_
- [[nodes/push_back]] _calls_

## Used By

- [[nodes/llama_grammar_accept_impl]] _calls_
- [[nodes/match_string]] _calls_
