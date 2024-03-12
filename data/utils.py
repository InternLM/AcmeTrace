cluster_metric_header = [
    "NODE_CPU_UTILIZATION",
    "NODE_MEMORY_UTILIZATION",
    "NODE_IB_SEND",
    "NODE_IB_RECEIVE",
]

dcgm_metric_header = [
    "XID_ERRORS",
    "GPU_TEMP",
    "MEMORY_TEMP",
    "MEM_CLOCK",
    "MEM_COPY_UTIL",
    "FB_FREE",
    "FB_USED",
    "DRAM_ACTIVE",
    "POWER_USAGE",
    "GPU_UTIL",
    "PIPE_TENSOR_ACTIVE",
    "SM_ACTIVE",
    "SM_OCCUPANCY",
]

dcgm_full = [
    "DCGM_FI_DEV_CORRECTABLE_REMAPPED_ROWS",  # 可纠正错误的重新映射行数 Number of remapped rows for correctable errors.
    "DCGM_FI_DEV_DEC_UTIL",  # GPU 解码器利用率（单位：%）
    "DCGM_FI_DEV_ECC_DBE_AGG_TOTAL",  # 双位聚合（持久）ECC 错误总数 (Total double bit aggregate (persistent) ECC errors) 注：单调递增。
    "DCGM_FI_DEV_ECC_DBE_VOL_TOTAL",  # 双位易失性 ECC 错误总数。(Total double bit volatile ECC errors)
    "DCGM_FI_DEV_ECC_SBE_AGG_TOTAL",  # 单位聚合（持久）ECC 错误总数 注：单调递增。
    "DCGM_FI_DEV_ECC_SBE_VOL_TOTAL",  # 单位易失性 ECC 错误总数。
    "DCGM_FI_DEV_ENC_UTIL",  # GPU 编码器利用率（单位：%）
    "DCGM_FI_DEV_FB_FREE",  # GPU 帧缓存剩余量（单位：MiB）
    "DCGM_FI_DEV_FB_USED",  # GPU 帧缓存使用量（单位：MiB） (该值与nvidia-smi命令中memory-usage的已使用值对应)
    "DCGM_FI_DEV_GPU_TEMP",  # GPU 当前温度（单位：℃）
    "DCGM_FI_DEV_GPU_UTIL",  # GPU 利用率（单位：%）
    "DCGM_FI_DEV_MEMORY_TEMP",  # 显存当前温度（单位：℃）
    "DCGM_FI_DEV_MEM_CLOCK",  # GPU 内存时钟（单位：MHZ）
    "DCGM_FI_DEV_MEM_COPY_UTIL",  # GPU 内存带宽利用率（单位：%）
    "DCGM_FI_DEV_NVLINK_BANDWIDTH_TOTAL",  # GPU 所有通道的 NVLink 带宽计数器总数
    "DCGM_FI_DEV_PCIE_REPLAY_COUNTER",  # GPU PCIE 重试次数
    "DCGM_FI_DEV_POWER_USAGE",  # GPU 当前使用功率（单位：W)
    "DCGM_FI_DEV_ROW_REMAP_FAILURE",  # Whether remapping of rows has failed
    "DCGM_FI_DEV_SM_CLOCK",  # GPU SM 时钟（单位：MHZ）
    "DCGM_FI_DEV_TOTAL_ENERGY_CONSUMPTION",  # GPU 启动以来的总能耗（单位：mJ）
    "DCGM_FI_DEV_UNCORRECTABLE_REMAPPED_ROWS",  # Number of remapped rows for uncorrectable errors.
    "DCGM_FI_DEV_VGPU_LICENSE_STATUS",  # vGPU 许可证状态
    "DCGM_FI_DEV_XID_ERRORS",  # XID errors
    "DCGM_FI_PROF_DRAM_ACTIVE",  # 内存接口主动发送或接收数据的周期比率 (The ratio of cycles the device memory interface is active sending or receiving data)
    "DCGM_FI_PROF_GR_ENGINE_ACTIVE",  # Profiling Fields. These all start with DCGM_FI_PROF_* Ratio of time the graphics engine is active. The graphics engine is active if a graphics/compute context is bound and the graphics pipe or compute pipe is busy.
    "DCGM_FI_PROF_PCIE_RX_BYTES",  # GPU PCIE 接收字节总数（单位：字节）
    "DCGM_FI_PROF_PCIE_TX_BYTES",  # GPU PCIE 发送字节总数（单位：字节）
    "DCGM_FI_PROF_PIPE_TENSOR_ACTIVE",  # The ratio of cycles the any tensor pipe is active (off the peak sustained elapsed cycles)
    "DCGM_FI_PROF_SM_ACTIVE",  # The ratio of cycles an SM has at least 1 warp assigned (computed from the number of cycles and elapsed cycles)
    "DCGM_FI_PROF_SM_OCCUPANCY",  # The ratio of number of warps resident on an SM.
]

table_dcgm_fatal_header = [
    "DCGM_FI_DEV_XID_ERRORS",
    "DCGM_FI_DEV_GPU_TEMP",
    "DCGM_FI_DEV_MEMORY_TEMP",
    "DCGM_FI_DEV_MEM_CLOCK",
    "DCGM_FI_DEV_MEM_COPY_UTIL",
    "DCGM_FI_DEV_FB_FREE",
    "DCGM_FI_DEV_FB_USED",
    "DCGM_FI_PROF_DRAM_ACTIVE",
    "DCGM_FI_DEV_POWER_USAGE",
    "DCGM_FI_DEV_GPU_UTIL",
    "DCGM_FI_PROF_PIPE_TENSOR_ACTIVE",
    "DCGM_FI_PROF_SM_ACTIVE",
    "DCGM_FI_PROF_SM_OCCUPANCY",
    "DCGM_FI_DEV_SM_CLOCK",
]

converted_dcgm_fatal_table_header = [
    "XID_ERRORS",
    "GPU_TEMP",
    "MEMORY_TEMP",
    "MEM_CLOCK",
    "MEM_COPY_UTIL",
    "FB_FREE",
    "FB_USED",
    "DRAM_ACTIVE",
    "POWER_USAGE",
    "GPU_UTIL",
    "PIPE_TENSOR_ACTIVE",
    "SM_ACTIVE",
    "SM_OCCUPANCY",
    "SM_CLOCK",
]

# node_infiniband_physical_state_id:
# (0: no change, 1: sleep, 2: polling, 3: disable, 4: shift, 5: link up, 6: link error recover, 7: phytest)
IB_PHYSICAL_STATE_MAP = {
    "0": "no change",
    "1": "sleep",
    "2": "polling",
    "3": "disable",
    "4": "shift",
    "5": "link up",
    "6": "link error recover",
    "7": "phytest",
}


# node_infiniband_state_id: (0: no change, 1: down, 2: init, 3: armed, 4: active, 5: act defer)
IB_STATE_MAP = {"0": "no change", "1": "down", "2": "init", "3": "armed", "4": "active", "5": "act defer"}
