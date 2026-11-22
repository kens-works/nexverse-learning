def capture_os_metrics():
    pass

def check_kernel_memory():
    pass

kernel_version = "linux_4.3"
pid_limit = 111 
threshold = 0.5
debug_flag = False
#Initial assignment
print("Kernel version type : ", type(kernel_version))
print("PID limit type : ", type(pid_limit))
print("threshold type : ", type(threshold))
print("debug flag type : ", type(debug_flag))

print("Kernel version length :", len(kernel_version))

#Result after dynamic typing
debug_flag = 1
print("debug flag : ", debug_flag)
print("debug flag type : ", type(debug_flag))

