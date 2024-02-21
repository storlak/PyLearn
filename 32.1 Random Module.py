# random.shuffle: shuffles and modifies the iterable
# choice : single element
# choices: (seq, k=) random.choices(population, weights=None, k=1)
import random

# random.shuffle example:
my_list = [1, 2, 3, 4, 5]
random.shuffle(my_list)
print(my_list)  # Output will be a shuffled version of my_list

# random.shuffle example:
my_string = "hello"
my_list1 = list(my_string)
random.shuffle(my_list1)
shuffled_string = "".join(my_list1)
print(shuffled_string)  # Output will be a shuffled version of the chars in my_string

# random.choice example:
the_list = [1, 2, 3, 4, 5]
chosen_number = random.choice(the_list)
print(chosen_number)

# random.choice() example:
words = "hello"
choose_char = random.choice(words)
print(choose_char)

# random.choices() example
my_nums = [1, 2, 3, 4, 5, 6]
chosen_nums = random.choices(my_nums, k=2)
print(chosen_nums)

# random.choices() example:
my_words = ["win", "lose", "draw"]
weights = [0.5, 0.3, 0.2]  # Higher weight means higher probability of selection
choices = random.choices(my_words, weights=weights, k=5)
print(choices)  # Output:list of 5 randomly chosen outcomes based on specified weights
