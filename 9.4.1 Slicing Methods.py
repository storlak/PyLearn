numbers = [10, 20, 30]
numbers[1] = "Hello"
print(numbers)

# append adds an element.
numbers.append(40)
print(numbers)

# to add multiple elements we use extend
fumbers = [1, 2, 3, 4]
fumbers.extend([5, 6, 7])
print(fumbers)

# we can also insert an element, but it is much slower!!!
# use insert carefully. It is shifting. If possible use append, much faster.
numbers.insert(2, "World")
print(numbers)

mylist = [1, 2, 3, 5, 6, 7, 8, 9]
mylist[0:3] = "a", "b", "c"
print(mylist)

# deleting an element of a list.
del mylist[0]
print(mylist)

# we can delete an entire slice:
del mylist[2:4]
print(mylist)
