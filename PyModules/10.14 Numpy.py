# masking in numpy
import numpy as np

m = np.array([-1, 1, -2, 2, -3, 3])
new_m = np.less(m, 0)  # less function returns a boolean array
print(new_m)

m < 0  # this is also a boolean array
print(m < 0)

mask = m > 0  # this is a boolean array
print(mask)

print(m[mask])  # masking the array

m1 = np.array([1, 2, 3, 4, 5, 6])
print(m1[m > 0])  # masking the array
