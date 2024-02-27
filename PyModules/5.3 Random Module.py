# weights in random module
"""In the random module in Python, the concept of "weights" refers to assigning probabilities to individual elements in a population. 
These weights determine the likelihood of each element being selected when making random choices."""
import random

# equal weights
population = ["A", "B", "C", "D"]
weights = [1, 1, 1, 1]  # Equal weights
choices = random.choices(population, weights=weights, k=5)
print(choices)
# Output:list of 5 randomly chosen elements from population with equal probability

# unequal wieghts
population = ["Red", "Blue", "Green"]
weights = [3, 2, 1]  # Higher weight for 'Red', medium for 'Blue', lower for 'Green'
choices = random.choices(population, weights=weights, k=10)
print(choices)
# Output:list of 10 randomly chosen elements from the population with different probabilities based on the weights
