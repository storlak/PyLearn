def multiply(x, y):
    return x * y


print(multiply(2, 4))


# single star / asterix. creates a tuple.
def multiplies(*numbers):
    total = 1
    for number in numbers:
        total *= number
    return total


print(multiplies(2, 3, 4, 5, 6))


# double star / asterix. creates a dictionary.
def save_user(**user):
    print(user)
    print(user["id"])  # we can replace id with name, age etc...


# when using a double asterix, we can pass multiple key,value items or multiple keyword arguments
save_user(id=1, name="john", age=27)
