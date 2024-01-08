# sorted() Numbers
# sorted by default ascending order
# sorted alywas returns a new list so original iterable never mutated
# for strings Upper case sorted before lower case
nums = [42, 67, 12, 43, 29, 9, 1]
new_nums = sorted(nums)
print(new_nums)

t = (1, 5, 3, 7, 4, 9, 60)
print(sorted(t))  # t is tuple but sorted returns a new list
print(sorted(t, reverse=True))  # reverses in descending order

# sorted() Strings
print(sorted(["Boy", "baby"]))  # capital B first
