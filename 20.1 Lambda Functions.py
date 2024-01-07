f1 = lambda a, b, c: max(a, b, c)
print(f1(24, 34, 12))

# no need to define a def for simple ops. instead we can use lamba.
f2 = lambda x: x + 5
print(f2(10))


# this is more common using a lamba inside a def function
def func(x):
    func2 = lambda x: x + 5
    return func2(x) + 85


print(func(25))

a = [1, 2, 3, 4, 5, 6]
newList = list(filter(lambda x: x % 2 == 0, a))
# filter takes 2 args, a function and an iterable.
print(newList)

# it is ok to call lambda also in a single line
print((lambda y: y**3)(7))
