import numpy as np

# searching arrays
arr = np.array([1, 2, 3, 4, 5, 4, 4])
x = np.where(arr == 4)
print(x)  # the value 4 is present at index 3, 5, and 6.

# find the indices where the values are even
arr = np.array([1, 2, 3, 4, 5, 6, 7, 8])
x = np.where(arr % 2 == 0)
print(x)

# search sorted
arr = np.array([6, 7, 8, 9])
x = np.searchsorted(arr, 7)
print(x)  # only 7 is present at index 1

# search from right
arr = np.array([6, 7, 8, 9])
x = np.searchsorted(arr, 7, side="right")
print(x)

# sort arrays puts in ascending order
arr = np.array([3, 2, 0, 1])
print(np.sort(arr))
