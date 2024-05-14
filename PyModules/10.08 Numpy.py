import numpy as np

# array splitting
array = np.array([1, 2, 3, 4, 5, 6])
newarr = np.array_split(array, 3)

print(newarr[0])
print(newarr[1])
print(newarr[2])

# splitting 2D array
arr = np.array([[1, 2], [3, 4], [5, 6], [7, 8], [9, 10], [11, 12]])
newarr = np.array_split(arr, 3)
print(newarr)
