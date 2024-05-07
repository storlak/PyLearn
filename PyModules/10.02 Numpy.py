# slicing arrays

import numpy as np

arr = np.array([1, 2, 3, 4, 5, 6, 7])
print(arr[1:5])
# negative indexing
print(arr[-3:-1])

# slicing 2D arrays
arr = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])
print(arr[1, 1:4])  # 1 is dimension, 1 is row, 4 is column
print(arr[0:2, 2])  # returns index 2 from both rows
print(arr[0:2, 1:4])  # slices 1:4 from both rows
