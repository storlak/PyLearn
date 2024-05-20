# numpy universal functions
import numpy as np

arr_1 = np.array([1, 2, 3, 4, 5])
arr_2 = np.arange(1, 6)

# adding two arrays
arr_3 = arr_1 + arr_2
print(arr_3)
print(np.add(arr_1, arr_2))  # we can add multiple arrays

# this works the same way with other math operators
np.multiply(arr_1, arr_2)
np.subtract(arr_1, arr_2)
floor_division = arr_1 // arr_2
np.floor_divide(arr_1, arr_2)

# power, % and sqrt
np.power(arr_1, arr_2)
np.mod(arr_1, arr_2)
np.sqrt(arr_1)
