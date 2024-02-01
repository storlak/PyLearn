# sorted(iterable, key=, reverse) sorted can take 3 args
# sorted returns a new iterable
data = [-6, 1 - 3, 8, -1, 7]
print(sorted(data))
print(sorted(data, key=lambda x: abs(x)))


def key_func(c):
    return abs(c)


print(sorted(data, key=key_func))
