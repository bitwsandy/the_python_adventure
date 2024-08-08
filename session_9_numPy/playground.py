import numpy as np

array2d = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(array2d)

stride = array2d[0:3:2, ::2]  # Rows from index 0 to 2 step 2, all columns step 2
print("\n",stride)

