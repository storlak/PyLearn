import numpy as np

a = np.amin(np.array([10, 5, 20]))
b = np.max(np.array([10, 5, 20]))
print(a)
print(b)

# amax and amin are similar to min and max
m = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print("Axis min-max values")
c = np.amin(m, axis=0)
d = np.amin(m, axis=1)
e = np.amax(m, axis=0)
f = np.amax(m, axis=1)
print(c)
print(d)
print(e)
print(f)

# median and mean
print(np.median(np.array([10, 5, 20])))  # median is 10
print(np.mean(np.array([10, 5, 20])))  # mean is 10
