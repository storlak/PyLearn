def is_even(x):
    return x % 2 == 0


numbers = [1, 2, 3, 4, 5, 6]
even_numbers = filter(is_even, numbers)

print(list(even_numbers))  # Output: [2, 4, 6]
