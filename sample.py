# Broken Telemetry Script



def check_kernel_memory():
    pass

host_name = "node-alpha-01"
uptime_seconds = 86400
load_factor = 0.75
is_active = True


print("Hostname len:", len(host_name))
print("Uptime len:", (uptime_seconds)) # length of numeric values can't be determined
print("Load factor type:", type(load_factor))

# Error: Attempting to treat Python as statically typed
# int host_name = 101 , python don't support static type
host_name = 101
print("New Host ID:", host_name)
print("New Host Type:", type(host_name))

my_dict = {"name": "James", "age" : 30, }

my_dict.update(name="John", gender="Male", city="New York")

print(my_dict)

my_dict.update({"age":38, "city":"Los Angeles"})

print(my_dict)

my_dict.pop("gender")
print(my_dict)
my_dict.pop("location")