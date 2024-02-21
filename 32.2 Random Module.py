# sampling: pick rndm element from an iterable without replacement
import random

# random.sample example
my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
sample = random.sample(my_list, 3)
print("my sample:", sample)  # Output will be a random sample of 3 elements from my_list

# random.sample example 2
my_string = "abcdefghijklmnopqrstuvwxyz"
sample1 = random.sample(my_string, 5)
print(sample1)  # Output will be a random sample of 5 characters from my_string

# random.sample example 3
my_set = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
sample2 = random.sample(my_set, 4)
print(sample2)  # Output will be a random sample of 4 num from the set.
