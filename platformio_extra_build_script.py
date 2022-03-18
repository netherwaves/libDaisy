Import("env")

# General options that are passed to the C compiler (C only; not C++).
env.Append(
    CFLAGS = [
        "-std=gnu11"
    ]
)
# General options that are passed to the C and C++ compilers
env.Append(
    CCFLAGS=[
        "-finline-functions",
        "-DCORE_CM7",
        "-DSTM32H750xx",
        "-DSTM32H750IB",
        "-DARM_MATH_CM7",
        "-Dflash_layout",
        "-DHSE_VALUE=16000000",
        "-DUSE_HAL_DRIVER",
        "-DUSE_FULL_LL_DRIVER"
    ]
)
# General options that are passed to the C++ compiler
env.Append(
    CXXFLAGS=[
        "-std=gnu++14",
        "-fno-exceptions",  
        "-fno-rtti"
    ]
)
# print("printing env:")
# print(env)
# print(env.Dump())

print("running supplimental libDaisy compilation flag script")   