# stacking arrays
# vstack vertical and hstack horizontal

import numpy as np

# colum numbers are equal so we can stack them(a1, a2)
a1 = np.arange(1, 6)
a2 = np.arange(1, 11).reshape(2, 5)

# stacking arrays vertically
s1 = np.vstack((a1, a2))
print(s1)

# stacking arrays horizontally using hstack
u1 = np.linspace(0, 5, 10).reshape(2, 5)
np.random.seed(0)
u2 = np.random.randint(0, 10, 10).reshape(2, 5)
result = np.hstack((u1, u2))
print(result)
