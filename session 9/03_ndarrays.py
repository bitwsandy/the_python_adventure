# NumPy arrays, or ndarrays, are the central data structure of the NumPy
# library.
#
# They are homogeneous multidimensional arrays, meaning all elements
# must be of the same type.
#
# They offer efficient storage and operations on data, making them better suited for
# numerical computations than Python's built-in lists.

import numpy as np

# Creating a NumPy array from a Python list
data = [1, 2, 3, 4, 5]
array1 = np.array(data)
print("np.array:", array1)  # Output: [1 2 3 4 5]

# Create an array of zeros with 5 elements
zeros_array = np.zeros(5)
print("np.zeros:", zeros_array)  # Output: [0. 0. 0. 0. 0.]

# Create an array of ones with 5 elements
ones_array = np.ones(5)
print("np.ones:", ones_array)  # Output: [1. 1. 1. 1. 1.]

# Create an array with a range of elements from 0 to 10, step by 2
range_array = np.arange(0, 10, 2)
print("np.arange:", range_array)  # Output: [0 2 4 6 8]

# Create an array with 5 evenly spaced values between 0 and 1
linspace_array = np.linspace(0, 1, 5)
print("np.linspace:", linspace_array)  # Output: [0.   0.25 0.5  0.75 1.  ]

# Printing attributes of the first array (array1)
print("Shape of array1:", array1.shape)  # Output: (5,)
print("Size of array1:", array1.size)  # Total elements: 5
print("Data type of array1:", array1.dtype)  # Data type: int64 (or int32 depending on your system architecture)
print("Number of dimensions of array1:", array1.ndim)  # Dimensions: 1
