# comprehension way is more readable
numbers = (1, 2, 3, 4, 5)
sq = [number**2 for number in numbers]
print(sq)

# or
sq1 = []
for number in numbers:
    sq1.append(number**2)
print(sq1)
