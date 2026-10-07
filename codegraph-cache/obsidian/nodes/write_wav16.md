---
name: "write_wav16"
type: "function"
file: "tools/mtmd/mtmd-helper-gen.cpp"
community: "tools"
---

# write_wav16

**Type:** `function`  **File:** `tools/mtmd/mtmd-helper-gen.cpp`

**Community:** [[communities/tools]]

## Depends On

- [[nodes/mtmd_gen_audio_pipeline]] _calls_
- [[nodes/vocab]] _calls_
- [[nodes/llama_model_n_embd]] _calls_
- [[nodes/info]] _calls_
- [[nodes/mtmd_gen_audio_get_info]] _calls_
- [[nodes/ensure_cache]] _calls_
- [[nodes/tts_resolve_lang]] _calls_
- [[nodes/find_special_token]] _calls_
- [[nodes/encode_speaker]] _calls_
- [[nodes/string]] _calls_
- [[nodes/llama_model_rope_type]] _calls_
- [[nodes/decode_embd_batch]] _calls_
- [[nodes/mtmd_gen_inp_default]] _calls_
- [[nodes/get_view]] _calls_
- [[nodes/llama_vocab_is_eog]] _calls_
- [[nodes/mtmd_gen_audio_process]] _calls_
- [[nodes/flush_gen_wav]] _calls_
- [[nodes/assign]] _calls_

## Used By

- [[nodes/pockettts_pack]] _calls_
