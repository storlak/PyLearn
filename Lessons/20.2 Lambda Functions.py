numbers = [1, 2, 3, 4, 5]

# Use map to square each number
squared_numbers = list(map(lambda x: x**2, numbers))
print(squared_numbers)

# Use filter to square each number
squared_numbers2 = list(filter(lambda x: x**2, numbers))
print(squared_numbers2)
