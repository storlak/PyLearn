# sorted() does not mutate the original list.

l = [1, 10, 2, 9, 3, 8]  # list
t = (1, 10, 2, 9, 3, 8)  # tuple
s = {1, 10, 2, 9, 3, 8}  # set

print(sorted(l))
print(sorted(t))
print(sorted(s))
print(sorted(l, reverse=True))
print(sorted("azbycz"))
