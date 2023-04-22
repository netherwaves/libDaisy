Import("env")

# CPU
MCU = ["-mthumb", "-mfloat-abi=hard", "-mfpu=fpv5-d16", "-mcpu=cortex-m7"]


# General options that are passed to the C compiler (C only; not C++).
env.Append(
    CFLAGS = [
        "-std=gnu11",
        "-finline-functions"
    ]
)
# General options that are passed to the C and C++ compilers
env.Append(
    CCFLAGS=[
        *MCU,
        
        # C defines
        "-DCORE_CM7",
        "-DSTM32H750xx",
        "-DSTM32H750IB",
        "-DARM_MATH_CM7",
        "-Dflash_layout",
        "-DHSE_VALUE=16000000",
        "-DUSE_HAL_DRIVER",
        "-DUSE_FULL_LL_DRIVER",
        "-DDATA_IN_D2_SRAM",

        # warnings
        "-Wall",
        "-Wno-attributes",
        "-Wno-strict-aliasing",
        "-Wno-maybe-uninitialized",
        "-Wno-missing-attributes",
        "-Wno-stringop-overflow",

        # other
        "-ggdb",
        "-fasm",
        "-fdata-sections",
        "-ffunction-sections"
    ]
)
# General options that are passed to the C++ compiler
env.Append(
    CXXFLAGS=[
        "-std=gnu++14",
        "-Wno-register",
        "-fno-exceptions",  
        "-fno-rtti"
    ]
)
# print("printing env:")
# print(env)
# print(env.Dump())

print("running supplimental libDaisy compilation flag script") 