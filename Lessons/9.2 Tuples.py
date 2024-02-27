ev = ("masa", "sofra", "çatal")
print(ev[1])

ofis = ["masa", "sofra", "merdiven"]
ofis = tuple(ofis)  # liste ofisi tuple'a çevirdik.
print(ofis)

numbers = (10, 20, [30, 40])  # 2nd item is a list in a tuple. tuple is immutable but list not. we can not
# modify, change tuple item 2, but we can its objects! example:
numbers[2][1] = 100
print(numbers)