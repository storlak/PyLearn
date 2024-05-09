# shape of array

import numpy as np

arr = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])
# this will print (2, 4)--> the array has 2 dimensions, where the first dimension has 2 elements and the second has 4.
print(arr.shape)

# reshaping arrays
arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
newarr = arr.reshape(4, 3)
print(newarr)
