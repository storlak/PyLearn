# if the inner func captures from the scope of outer it is a closure
# closures are important for decorators in Python


def outer(a, b):
    sum_ = a + b

    def inner():
        prod = a * b
        print(a, b, sum_, prod)
        return "You just called a closure"

    return inner


func = outer(2, 3)
print(func())  # since func is a reference to a function it is callable
