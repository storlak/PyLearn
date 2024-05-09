# data types in python

# integer
print(1)

# float
print(1.0)

# string
print("hello")
print("Number 53 is a string.")
print("I am from python".upper())
my_name = input("Enter your name: ")
print(f"Hello {my_name}".capitalize)

# float number is not the same as integer number.Ex:0.1 but it is not:
print(format(0.1, ".25f"))
print(0.1 == 0.1000000000000000055511151)  # not equal or same but still True!
print(0.1 + 0.1 + 0.1 == 0.3)  # false!!!
print(
    abs(0.1 + 0.1 + 0.1 - 0.3)
)  # abs absolute value. So we can see the differnce in the numbers.
print(format(0.1 + 0.1 + 0.1, ".25f"))
print(0.1 + 0.1 + 0.1 == 0.3000000000000000444089210)  # == True!!!

# Booleans
print(True)
print(False)
