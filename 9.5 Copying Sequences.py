from copy import deepcopy

# shallow copy & deepcopy

my_list = [1, 2, 3, 4]
my_copy = my_list[:]  # or my_copy = my_list.copy()
del my_list[0]
print(my_copy)
print(my_list)

# deepcopy exemple
this_list = [["a", "b"], 2, 3]
my_copy_list = deepcopy(this_list)
print(this_list[0] is my_copy_list[0])  # false bcs deepcopy.
my_copy_list[0].append("c")

# these 2 lists are now different
print(this_list)
print(my_copy_list)
