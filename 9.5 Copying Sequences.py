from copy import deepcopy

# shallow copy & deepcopy
# even they have same collections they are separate objects!
# for deep copy we have to import: from copy import deepcopy
my_list = [1, 2, 3, ]
my_copy = my_list[:]  # or my_copy = my_list.copy()
print(my_copy)
del my_copy[0]

# deepcopy exemple
this_list = [["a", "b"], 2, 3]
my_copy_list = deepcopy(this_list)
print(this_list[0] is my_copy_list[0])  # false bcs deepcopy.
my_copy_list[0].append("c")

# these 2 lists are now different
print(this_list)
print(my_copy_list)
