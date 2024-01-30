# Filtering names starting with "A" from a dictionary:
names = {"Alice": 25, "Bob": 30, "Charlie": 28, "David": 32, "Emily": 29}
a_names = dict(filter(lambda item: item[0].startswith("A"), names.items()))
print(a_names)
