import numpy as np

# rows = axis 0
# columns = axis 1

a = np.array([1, 2, 3, 4, 5])
print(a)
print(type(a))

# 2-D array
arr = np.array([[1, 2, 3], [4, 5, 6]])
print(arr)

# ndim checks the number of dimensions
a = np.array(42)
b = np.array([1, 2, 3, 4, 5])
c = np.array([[1, 2, 3], [4, 5, 6]])
d = np.array([[[1, 2, 3], [4, 5, 6]], [[1, 2, 3], [4, 5, 6]]])

print(a.ndim)
print(b.ndim)
print(c.ndim)
print(d.ndim)
