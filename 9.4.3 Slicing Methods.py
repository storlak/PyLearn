my_list = [1, 2, 3, 4, 5]
my_list[0:3] = ["a", "b"]
del my_list[1]
print(my_list[::-1])

# Example with a list
original_list = [1, 2, 3, 4, 5]
reversed_list = list(reversed(original_list))

print("Original list:", original_list)
print("Reversed list:", reversed_list)

# Example with a string
original_string = "Hello, World!"
reversed_string = ''.join(reversed(original_string))

print("Original string:", original_string)
print("Reversed string:", reversed_string)
