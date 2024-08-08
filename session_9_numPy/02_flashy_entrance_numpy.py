import numpy as np
import time

# Define the size of the array
size = 100000000

# Create a large array of random numbers
array_np = np.random.rand(size)
array_py = list(array_np)

# Measure time for NumPy operation
start_time_np = time.time()
result_np = np.sum(array_np)
end_time_np = time.time()

# Measure time for Python loop
start_time_py = time.time()
result_py = sum(array_py)
end_time_py = time.time()

# Calculate the time taken by each
time_np = end_time_np - start_time_np
time_py = end_time_py - start_time_py

print(f"Time taken by NumPy: {time_np} seconds")
print(f"Time taken by Python loop: {time_py} seconds")
