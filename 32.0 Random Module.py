import random

for _ in range(5):
    print(random.random())

random.seed(0)  # if we do not set the seed it is the time in comp.
for _ in range(5):
    print(random.randrange(1, 6))

random.seed(0)  # same seed. the output will be same!
for _ in range(5):
    print(random.randint(1, 6))
