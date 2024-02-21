# choice : single element
# choices: (seq, k=)
import random

l = [1, 2, 3, 4, 5, 6]
l1 = random.choices(l, k=2)
print(l1)
random.shuffle(l)
print(l)

for i in range(5):
    print(random.choice(l))
