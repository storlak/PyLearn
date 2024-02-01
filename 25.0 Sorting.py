data = [-6, 1 - 3, 8, -1, 7]
print(sorted(data))
print(sorted(data, key=lambda x: abs(x)))


def key_func(c):
    return abs(x)


print(sorted(data, key=key_func))
