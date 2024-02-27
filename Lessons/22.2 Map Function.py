# map returns an iterator
# Using map function to square numbers
numbers = [1, 2, 3, 4, 5]
squared_numbers = map(lambda x: x**2, numbers)
print(list(squared_numbers))

# Using map function to convert Celsius to Fahreneit
celsius_temps = [0, 10, 20, 30, 40]
fahrenheit_temps = map(lambda x: (9 / 5) * x + 32, celsius_temps)
print(list(fahrenheit_temps))

# Using map function
names = ["Alice", "Bob", "Charlie"]
ages = [25, 30, 22]
combined_info = map(lambda x, y: f"{x} is {y} years old", names, ages)
print(list(combined_info))
