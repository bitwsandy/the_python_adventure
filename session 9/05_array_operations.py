import numpy as np

# Creating two arrays for demonstration
array1 = np.array([1, 2, 3, 4, 5])
array2 = np.array([5, 4, 3, 2, 1])

# Element-wise addition
addition = array1 + array2
print("Addition:", addition)  # Output: [6 6 6 6 6]

# Element-wise subtraction
subtraction = array1 - array2
print("Subtraction:", subtraction)  # Output: [-4 -2 0 2 4]

# Element-wise multiplication
multiplication = array1 * array2
print("Multiplication:", multiplication)  # Output: [5 8 9 8 5]

# Element-wise division
division = array1 / array2
print("Division:", division)  # Output: [0.2 0.5 1.  2.  5.]

# Broadcasting: Adding a scalar to an array
scalar_addition = array1 + 10
print("Scalar Addition:", scalar_addition)  # Output: [11 12 13 14 15]

# More complex operations - Squaring each element
squared = array1 ** 2
print("Squared:", squared)  # Output: [ 1  4  9 16 25]

# Using conditions to filter elements - Boolean indexing
filtered = array1[array1 > 3]
print("Filtered Elements (>3):", filtered)  # Output: [4 5]

# Sum of all elements in the array
total_sum = np.sum(array1)
print("Sum of all elements:", total_sum)  # Output: 15

# Cumulative sum of elements
cumulative_sum = np.cumsum(array1)
print("Cumulative Sum:", cumulative_sum)  # Output: [ 1  3  6 10 15]

# Mean of the array
mean_value = np.mean(array1)
print("Mean of the elements:", mean_value)  # Output: 3.0

# Standard deviation of the array
std_deviation = np.std(array1)
print("Standard Deviation:", std_deviation)  # Output: 1.4142135623730951

# Dot product of two arrays
dot_product = np.dot(array1, array2)
print("Dot Product:", dot_product)  # Output: 35

# Reshape the array into a 2x3 matrix, if applicable
# Here, using an example array to demonstrate reshape
example_array = np.arange(1, 7)  # Generates array [1, 2, 3, 4, 5, 6]
reshaped_array = example_array.reshape((2, 3))
print("Reshaped Array:\n", reshaped_array)
# Output:
# [[1 2 3]
#  [4 5 6]]
