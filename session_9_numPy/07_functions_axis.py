import numpy as np

# Creating a 2D array for demonstration
array2d = np.array([[1, 4, 7], [2, 5, 8], [3, 6, 9]])

# Sum of all elements in the array
total_sum = np.sum(array2d)
print("Total sum of all elements:", total_sum)  # Output: 45

# Mean of all elements
mean_value = np.mean(array2d)
print("Mean of all elements:", mean_value)  # Output: 5.0

# Maximum value in the array
max_value = np.max(array2d)
print("Maximum value:", max_value)  # Output: 9

# Minimum value in the array
min_value = np.min(array2d)
print("Minimum value:", min_value)  # Output: 1

# Square root of each element in the array
sqrt_values = np.sqrt(array2d)
print("Square root of each element:\n", sqrt_values)
# Output:
# [[1.         2.         2.64575131]
#  [1.41421356 2.23606798 2.82842712]
#  [1.73205081 2.44948974 3.        ]]

# Sorting elements in each row
sorted_array = np.sort(array2d, axis=1)
print("Elements sorted in each row:\n", sorted_array)
# Output:
# [[1 4 7]
#  [2 5 8]
#  [3 6 9]]

# Using the axis parameter:
# Sum of elements along each column (axis 0)
column_sum = np.sum(array2d, axis=0)
print("Sum of elements along each column:", column_sum)  # Output: [6 15 24]

# Mean of elements along each row (axis 1)
row_mean = np.mean(array2d, axis=1)
print("Mean of elements along each row:", row_mean)  # Output: [4. 5. 6.]

# Max value in each row (axis 1)
row_max = np.max(array2d, axis=1)
print("Maximum value in each row:", row_max)  # Output: [7 8 9]

# Min value in each column (axis 0)
column_min = np.min(array2d, axis=0)
print("Minimum value in each column:", column_min)  # Output: [1 4 7]

# Explanation of the 'axis' parameter:
# - axis=0 operates along the vertical direction, aggregating data in each column.
# - axis=1 operates along the horizontal direction, aggregating data in each row.

