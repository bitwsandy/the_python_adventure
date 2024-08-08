import numpy as np

# Creating a 2D array for demonstration
array2d = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

# Basic indexing: Accessing a specific element (row 1, column 2)
element = array2d[1, 2]
print("Access specific element (row 1, col 2):", element)  # Output: 6

# Slicing: Extracting a row
row = array2d[1, :]  # Second row
print("Extract a row (second row):", row)  # Output: [4 5 6]

# Slicing: Extracting a column
column = array2d[:, 2]  # Third column
print("Extract a column (third column):", column)  # Output: [3 6 9]

# Slicing: Extracting a subarray
subarray = array2d[0:2, 1:3]  # Rows from index 0 to 1, columns from index 1 to 2
print("Extract a subarray:", subarray)
# Output:
# [[2 3]
#  [5 6]]

# Boolean indexing: Filter elements
filtered_array = array2d[array2d > 5]
print("Filter elements greater than 5:", filtered_array)  # Output: [6 7 8 9]

# Fancy indexing: Access multiple elements
fancy_indexing = array2d[[0, 2], [1, 2]]  # Elements at (0,1) and (2,2)
print("Fancy indexing (elements at (0,1) and (2,2)):", fancy_indexing)  # Output: [2 9]

# Advanced slicing: Stride in slicing
stride = array2d[0:3:2, ::2]  # Rows from index 0 to 2 step 2, all columns step 2
print("Advanced slicing with stride:", stride)
# Output:
# [[1 3]
#  [7 9]]

# Modifying an element
array2d[0, 0] = 10
print("Modified array (change element at (0,0) to 10):\n", array2d)
# Output:
# [[10  2  3]
#  [ 4  5  6]
#  [ 7  8  9]]

# Modifying a whole row
array2d[1, :] = [11, 12, 13]
print("Modified array (change second row):\n", array2d)
# Output:
# [[10  2  3]
#  [11 12 13]
#  [ 7  8  9]]

# Modifying a whole column
array2d[:, 2] = [14, 15, 16]
print("Modified array (change third column):\n", array2d)
# Output:
# [[10  2 14]
#  [11 12 15]
#  [ 7  8 16]]
