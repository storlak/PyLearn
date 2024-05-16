# creating arrays
import numpy as np

arr = np.zeros(4)  # 1 dimension
print(arr)  # [0. 0. 0. 0.]
arr = np.zeros((5, 5))  # 2 dimension

arr1 = np.ones((5, 5))
print(arr1)  # [[1. 1. 1. 1. 1.]

arr2 = np.full((5, 5), 7)
print(arr2)  # [[7 7 7 7 7]

# generates evenly spaced numbers
some_nums = np.linspace(0, 10, 5)
print(some_nums)  # [ 0.  2.5  5.  7.5 10.]

even_nums = np.linspace(2, 10, num=5)
print(even_nums)  # [ 2.  4.  6.  8. 10.]

# random in numpy
np.random.random((5, 5))
rand_nums = np.random.randint(1, 10, 50)
print(rand_nums)  # 50 random nums 1-10

# range function in numpy
arr3 = np.arange(1, 100, 5)
print(arr3)
