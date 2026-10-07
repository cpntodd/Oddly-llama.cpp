---
name: "ggml_hexagon_measure_max_vmem"
type: "function"
file: "ggml/src/ggml-hexagon/ggml-hexagon.cpp"
community: "ggml"
---

# ggml_hexagon_measure_max_vmem

**Type:** `function`  **File:** `ggml/src/ggml-hexagon/ggml-hexagon.cpp`

**Community:** [[communities/ggml]]

## Depends On

- [[nodes/ggml_hexagon_shared_buffer]] _calls_
- [[nodes/string]] _calls_
- [[nodes/remote_session_control]] _calls_
- [[nodes/htp_iface_open]] _calls_
- [[nodes/htp_iface_hwinfo]] _calls_
- [[nodes/remote_handle64_control]] _calls_
- [[nodes/dspqueue_export]] _calls_
- [[nodes/htp_iface_etm]] _calls_
- [[nodes/ggml_hexagon_opqueue]] _calls_
- [[nodes/ggml_hexagon_opbatch]] _calls_
- [[nodes/htp_iface_start]] _calls_
- [[nodes/htp_iface_profiler]] _calls_
- [[nodes/release]] _calls_
- [[nodes/htp_iface_stop]] _calls_
- [[nodes/dspqueue_close]] _calls_
- [[nodes/htp_iface_close]] _calls_
- [[nodes/ggml_hexagon_session]] _calls_
- [[nodes/ggml_backend_hexagon_buffer_type_context]] _calls_
- [[nodes/hex_align_up]] _calls_
- [[nodes/hmx_fa_compute_vtcm_usage]] _calls_
- [[nodes/init_fastdiv_values]] _calls_
- [[nodes/hex_round_up]] _calls_
- [[nodes/hvx_fa_compute_vtcm_usage]] _calls_
