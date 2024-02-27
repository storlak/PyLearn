suits = ["Spades", "Hearts", "Diamonds", "Clubs"]
for suit in suits:
    print(suit)

# range function
for i in range(0, 11, 2):
    print(i)

# does the same with range
print(list(range(0, 11, 2)))

for i in range(3):
    for j in range(3):
        print(f"i={i}, j={j}")
    print("-" * 8)

