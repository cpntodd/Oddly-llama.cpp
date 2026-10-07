---
name: "check_double_bos_eos"
type: "function"
file: "src/llama-vocab.cpp"
community: "src"
---

# check_double_bos_eos

**Type:** `function`  **File:** `src/llama-vocab.cpp`

**Community:** [[communities/src]]

## Depends On

- [[nodes/size]] _calls_
- [[nodes/tokenize]] _calls_
- [[nodes/clear]] _calls_
- [[nodes/unicode_len_utf8]] _calls_
- [[nodes/add_new_bigram]] _calls_
- [[nodes/empty]] _calls_
- [[nodes/pop_move]] _calls_
- [[nodes/push_back]] _calls_
- [[nodes/llm_tokenizer_wpm]] _calls_
- [[nodes/llm_tokenizer_wpm_session]] _calls_
- [[nodes/vocab]] _calls_
- [[nodes/unicode_cpts_from_utf8]] _calls_
- [[nodes/unicode_cpt_flags_from_cpt]] _calls_
- [[nodes/unicode_cpt_to_utf8]] _calls_
- [[nodes/unicode_tolower]] _calls_
- [[nodes/is_chinese_char]] _calls_
- [[nodes/llm_tokenizer_ugm]] _calls_
- [[nodes/insert]] _calls_
- [[nodes/llm_tokenizer_ugm_session]] _calls_
- [[nodes/tokenizer]] _calls_
- [[nodes/normalize]] _calls_
- [[nodes/llm_tokenizer_rwkv]] _calls_
- [[nodes/llm_tokenizer_rwkv_session]] _calls_
- [[nodes/llm_tokenizer_plamo2]] _calls_
- [[nodes/build]] _calls_
- [[nodes/tokens]] _calls_
- [[nodes/llm_tokenizer_hybriddna_session]] _calls_
- [[nodes/emit_dna_kmers]] _calls_
- [[nodes/llm_tokenizer_whitespace_session]] _calls_
- [[nodes/fragment_buffer_variant]] _calls_

## Used By

- [[nodes/llama_decode_text]] _calls_
