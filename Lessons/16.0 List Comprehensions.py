# List comprehension: more readable
numbers = (1, 2, 3, 4, 5)
sq = [number**2 for number in numbers]
print(sq)

# or below method is also correct
sq1 = []
for number in numbers:
    sq1.append(number**2)
print(sq1)
