# Use lambda functions when an anonymous function is required for a short period of time.
x = lambda a: a + 10
print(x(5))

x = lambda a, b, c: a + b + c
print(x(6, 7, 1))


# The power of lambda is better shown when you use them as an anonymous function inside another function.
def myfunc(n):
    return lambda a: a * n


mydoubler = myfunc(2)

print(mydoubler(11))

# we can assign lambda to a variable
f = lambda z, y: y * z * 2
print(f(3, 7))
