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




#  1D Arrays (One-Dimensional Arrays)
# - What it is: Imagine a single row of boxes. Each box can hold a number, and all the boxes are in a straight line.
# - Example: `[1, 2, 3, 4]`
# - How to think of it: It's like a list of items in a straight line, like a list of grocery items.
# - Use: You can store a sequence of numbers or items in a single line.
#


#  2D Arrays (Two-Dimensional Arrays)
# - What it is: Now imagine a grid, like a chessboard. It has rows and columns, so you can organize numbers in both directions: across and down.
# - Example:
#
#   [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9]
#   ]
#
# - How to think of it: It's like a table or a spreadsheet with rows and
#   columns. You have a box at each intersection of a row and a column.
# - Use: Useful for representing things like a matrix or a table of data.


#  3D Arrays (Three-Dimensional Arrays)
# - What it is: Now imagine a cube, like a Rubik's Cube. It has multiple
#   layers of grids stacked on top of each other. Each grid (like the 2D
#   array) is a slice, and you have several slices stacked up.
# - Example:
#
#   [
#     [
#       [1, 2],
#       [3, 4]
#     ],
#     [
#       [5, 6],
#       [7, 8]
#     ]
#   ]
#
# - How to think of it: It's like several sheets of paper stacked on
#   top of each other, where each sheet is a 2D array.
# - Use: Useful for representing more complex structures like a collection
#   of images, where each image is a 2D array,
#   and you have multiple images.
#
#  Key Differences
# - 1D Array: Just a single line of data.
# - 2D Array: A grid with rows and columns.
# - 3D Array: Multiple grids stacked on top of each other.

# 4D Arrays (Four-Dimensional Arrays)
# - What it is: Imagine a collection of cubes. Just as a 3D array is a
#   stack of 2D grids (like layers in a Rubik's Cube), a 4D array is a
#   collection of these cubes.
# - Example:
#
#   [
#     [
#       [
#         [1, 2],
#         [3, 4]
#       ],
#       [
#         [5, 6],
#         [7, 8]
#       ]
#     ],
#     [
#       [
#         [9, 10],
#         [11, 12]
#       ],
#       [
#         [13, 14],
#         [15, 16]
#       ]
#     ]
#   ]
#
# - How to think of it: Imagine you have multiple 3D cubes, and you’re
#   stacking these cubes into a line. Each cube is a 3D array,
#   and the entire line of cubes forms a 4D array.
# - Use: Useful in scenarios like representing a series of 3D objects
#   over time (e.g., multiple 3D models in a video game, where each
#   frame is a 3D array).


