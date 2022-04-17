import psutil

print(f"Virtual Memory: {psutil.virtual_memory()} Units")
print(f"CPU Percentage: {psutil.cpu_percent()}%")
print(f"Memory Usage: {psutil.virtual_memory()[2]}%")
