data = ["a", "ab", "abc", "abcd"]
lenghts = [len(element) for element in data]
lenghts1 = map(len, data)
print(lenghts)
print(list(lenghts1))  # to print we must use list otherwise it is a iterable.
