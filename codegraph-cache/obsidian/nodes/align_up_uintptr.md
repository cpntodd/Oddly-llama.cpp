---
name: "align_up_uintptr"
type: "function"
file: "ggml/src/ggml-cpu/spacemit/spine_mem_pool.cpp"
community: "ggml"
---

# align_up_uintptr

**Type:** `function`  **File:** `ggml/src/ggml-cpu/spacemit/spine_mem_pool.cpp`

**Community:** [[communities/ggml]]

## Depends On

- [[nodes/spine_mem_pool_manager]] _calls_
- [[nodes/alloc]] _calls_
- [[nodes/is_power_of_two]] _calls_
- [[nodes/align_up]] _calls_
- [[nodes/try_alloc_locked]] _calls_
- [[nodes/add_chunk_locked]] _calls_
- [[nodes/rollback_allocation_locked]] _calls_
- [[nodes/spine_mem_pool_posix]] _calls_
- [[nodes/release_chunks]] _calls_
- [[nodes/free]] _calls_
- [[nodes/clear_chunk]] _calls_
- [[nodes/spine_mem_pool_transparent_hugepage]] _calls_
- [[nodes/default_chunk_size]] _calls_
- [[nodes/mmap]] _calls_
- [[nodes/spine_mem_pool_hugetlb_1g]] _calls_
- [[nodes/spine_mem_pool_shared_mem]] _calls_

## Used By

- [[nodes/try_alloc_locked]] _calls_
