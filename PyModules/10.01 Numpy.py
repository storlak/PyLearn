import numpy as np

# accessing arrays
arr = np.array([1, 2, 3, 4, 5])
print(arr[0])
print(arr[2] + arr[4])

# 2-D arrays
arr = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])
print("2nd element on 1st row: ", arr[0, 1])
print("5th element on 2nd row: ", arr[1, 4])
# last element from the 2nd dim:
print("Last element from 2nd dim: ", arr[1, -1])

# 3-D arrays
arr = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])
# Access the third element of the second array of the first array:
print(arr[0, 1, 2])
