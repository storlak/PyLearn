d = dict.fromkeys(["cntr1", "cntr2", "cntr3"], 0) # fromkeys assng 1 same armngt to all.
z = dict.fromkeys("abc", 1)
print(d)
print(z)

zoo = {}  # empty dict
zoo1 = dict()  # also empty dict

# get method (to avoid any exception)
num = {"length": 10, "width": 20}
num1 = {"height": 30}
print(num.get("length", 0))
print(num.get("height", 0)) # height doesn't exist but thx to get it takes the default value 0.

# update() to merge dictionaries
num.update(num1) # num1 added to num or owerwrites to num. Merged. num is mutated.
print(num)