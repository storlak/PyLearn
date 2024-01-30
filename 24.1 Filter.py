# Filtering names starting with "A" from a dictionary:
names = {"Alice": 25, "Bob": 30, "Charlie": 28, "David": 32, "Emily": 29}
a_names = dict(filter(lambda item: item[0].startswith("A"), names.items()))
print(a_names)

# filter positive & negative numbers from a list
numbers = [-5, 2, 6, 0, -7, 23, 54]
positives = list(filter(lambda x: x > 0, numbers))
negatives = list(filter(lambda x: x < 0, numbers))
print(f"Positive numbers are: {positives}")
print(f"Negative numbers are: {negatives}")
