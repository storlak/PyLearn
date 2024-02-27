# Slicing sets
l = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5]
s = set(l)
s.add(6)

# remove = discard but error difference
s.remove(2)  # generates a key error if nothing to remove
s.discard(5)  # does not generate any error.
print(s)

# Union of 2 sets |
z1 = {2, 4, 6, 8, 10, 12}
z2 = {1, 3, 5, 7, 9, 11}
print(z1 | z2)  # union of z1 and z2

# Intersection of 2 sets &
print(s & z1)

# Difference of 2 sets &
print(z1 - z2)
print(z2 - z1)
print(s - z1)

# Membership testing (in operators) are much faster with sets than lists, tuples!
