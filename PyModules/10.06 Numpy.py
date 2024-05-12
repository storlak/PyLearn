import numpy as np

# reshaping arrays
arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
newarr = arr.reshape(4, 3)  # 1D to 2D. 4 rows and 3 columns.
newarr2 = arr.reshape(2, 3, 2)  # 1D to 3D. 2 arrays of 3 rows and 2 columns.

# flatten array
arr = np.array([[1, 2, 3], [4, 5, 6]])
newarr = arr.reshape(-1)
