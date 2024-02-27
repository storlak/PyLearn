# math module most common functions
import math

power = math.pow(3, 4)
square = math.sqrt(16)
ceil = math.ceil(10.5)
floor = math.floor(4.1)
factorial = math.factorial(5)
math.gcd(10, 20)  # greatest common diviser

# fsum(iterable) it is like sum
my_list = [1, 2, 3, 4]
print(sum(my_list))
# math module fsum works with floats better

# math.prod
values = [1, 2, 3, 4]
print(math.prod(values))  # multiplies all
print(math.prod(values, start=10))  # multiplies all starting from 10
