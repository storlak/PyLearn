suits = ["spades", "Hearts", "Diamonds", "Clubs"]
for suit in suits:
    print(suit)

for i in range(3):
    for j in range(3):
        print(f"i={i}, j={j}")
    print("-" * 10)

data = [10, 20, 30]
print(list(enumerate(data)))
#inx= index & elmnt = element which enumarte function provides us
for inx, elmnt in enumerate(data):
    print(inx, elmnt)