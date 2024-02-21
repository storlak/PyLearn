import random

# random.randint example:
num = random.randint(1, 10)
print(num)  # Output will be a random integer between 1 and 10, inclusive

# random.random() example:
num = random.random()
print(num)  # Output will be a random float between 0.0 and 1.0

#  random.randrange(start, stop, step)
num = random.randrange(1, 10, 2)
print(num)  # Output will be a random odd integer between 1 and 9

# various examples:
for _ in range(5):
    print(random.random())

random.seed(0)  # if we do not set the seed it is the time in comp.
for _ in range(5):
    print(random.randrange(1, 6))

random.seed(0)  # same seed. the output will be same!
for _ in range(5):
    print(random.randint(1, 6))
