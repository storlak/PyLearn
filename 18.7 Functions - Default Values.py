def func(a, b=2, c=30):
    return a, b, c


print(func(1))  # will print 1 for a and default values for b,c
print(func(3, 4))  # will print 3 for a and 4 for b and default value for c)
