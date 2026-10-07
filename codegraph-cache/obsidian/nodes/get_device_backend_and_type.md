---
name: "get_device_backend_and_type"
type: "function"
file: "ggml/src/ggml-sycl/dpct/helper.hpp"
community: "ggml"
---

# get_device_backend_and_type

**Type:** `function`  **File:** `ggml/src/ggml-sycl/dpct/helper.hpp`

**Community:** [[communities/ggml]]

## Depends On

- [[nodes/get_device_type_name]] _calls_
- [[nodes/get_version]] _calls_
- [[nodes/generic_error_type]] _calls_
- [[nodes/dim3]] _calls_
- [[nodes/pitched_data]] _calls_
- [[nodes/constexpr]] _calls_
- [[nodes/get_major_version]] _calls_
- [[nodes/get_minor_version]] _calls_
- [[nodes/get_device_info]] _calls_
- [[nodes/set_major_version]] _calls_
- [[nodes/set_minor_version]] _calls_
- [[nodes/has]] _calls_
- [[nodes/set_max_clock_frequency]] _calls_
- [[nodes/device_ext]] _calls_
- [[nodes/device]] _calls_
- [[nodes/clear_queues]] _calls_
- [[nodes/init_queues]] _calls_
- [[nodes/get_device_id]] _calls_
- [[nodes/max]] _calls_
- [[nodes/mem_mgr]] _calls_
- [[nodes/mmap]] _calls_
- [[nodes/buf]] _calls_
- [[nodes/allocation]] _calls_
- [[nodes/get_pitch]] _calls_
- [[nodes/get_y]] _calls_
- [[nodes/get_offset]] _calls_
- [[nodes/host_buffer]] _calls_
- [[nodes/get_ptr]] _calls_
- [[nodes/get_size]] _calls_
- [[nodes/dpct_free]] _calls_

## Used By

- [[nodes/compare_backend]] _calls_
- [[nodes/print_device_opt_feature]] _calls_
- [[nodes/ggml_backend_sycl_print_sycl_devices]] _calls_
