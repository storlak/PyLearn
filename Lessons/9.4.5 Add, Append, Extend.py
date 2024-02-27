my_list = [1, 2, 3, 4, 5, 6, 7, 8]
# add multiple elements to the end of list
my_list.extend(["a", "b", "c"])
# add single element to the end of the list
my_list.append("d")
print(my_list)
# insert method: to be used carefully. It is slower.
my_list.insert(0, 0)
print(my_list)
print(my_list[:-3:-1])
my_list[:-3:-1] = 100, 200
print(my_list)