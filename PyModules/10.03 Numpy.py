import numpy as np

# Numpy data types
"""
i - integer
b - boolean
u - unsigned integer
f - float
c - complex float
m - timedelta
M - datetime
O - object
S - string
U - unicode string
V - fixed chunk of memory for other type ( void )
"""
arr = np.array([1, 2, 3, 4])
print(arr.dtype)  # checks the data type of the array

# difference between copy and view
arr = np.array([1, 2, 3, 4, 5])
x = arr.copy()
y = arr.view()
arr[0] = 42

print(arr)
print(x)
print(y)
