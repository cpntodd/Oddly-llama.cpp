---
name: "n_embd_out"
type: "function"
file: "tools/mtmd/mtmd.cpp"
community: "tools"
---

# n_embd_out

**Type:** `function`  **File:** `tools/mtmd/mtmd.cpp`

**Community:** [[communities/tools]]

## Depends On

- [[nodes/clip_n_mmproj_embd]] _calls_
- [[nodes/clip_free]] _calls_

## Used By

- [[nodes/mtmd_encode_impl]] _calls_
- [[nodes/mtmd_encode_chunk_impl]] _calls_
- [[nodes/mtmd_batch_encode]] _calls_
- [[nodes/params]] _calls_
- [[nodes/llama_model_n_embd_out]] _calls_
- [[nodes/ctx_type_to_graph_type]] _calls_
- [[nodes/needs_raw_logits]] _calls_
- [[nodes/llm_graph_context]] _calls_
- [[nodes/build_dspark_markov_head]] _calls_
- [[nodes/dsv4_elem_offset]] _calls_
