import numpy as np

arr = np.arange(10, 100, 10)
# first, third, fourth elements
sub = np.array([arr[0], arr[2], arr[3]])  # this is a numpy array
sub1 = arr[np.array([0, 2, 3])]  # this is a numpy array. fancy indexing
sub2 = arr[[0, 2, 3]]  # this is a python list
print(sub)
print(sub1)

arr = np.arange(1, 10)
arr[np.array([0, 1, 1, 5])]  # we can repeat elements
print(arr)

# using fancy indexing in multi dimensional arrays
m = np.arange(25).reshape(5, 5)
print(m[[0, 1, 3]])
print(m[[0, 1, 3], 2])
