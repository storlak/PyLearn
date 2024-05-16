# creating arrays
import numpy as np

arr = np.zeros(4)
print(arr)  # [0. 0. 0. 0.]
arr1 = np.ones((5, 5))
print(arr1)  # [[1. 1. 1. 1. 1.]
arr2 = np.full((5, 5), 7)
print(arr2)  # [[7 7 7 7 7]
# generates evenly spaced numbers
some_nums = np.linspace(0, 10, 5)
print(some_nums)  # [ 0.  2.5  5.  7.5 10.]
# random in numpy
np.random.random((5, 5))
np.randint(1, 100, (5, 5))
