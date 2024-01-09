def say_hello(first_name, last_name):
    def assemble_name():
        return " ".join([first_name, last_name])

    return " ".join(["Hello, ", assemble_name(), "!"])


print(say_hello("Zoltan", "Kulle"))


def add(a, b):
    return a + b


def apply(func, a, b):
    result = func(a, b)
    return result


print(apply(add, 1, 2))
