# *args allow multiple non-keyword arguments
# **kwargs allow multiple keyword arguments


def sum_(*args):
    total = 0
    for arg in args:
        total += arg
    return total


# we can pass any number of args bs we use * and it'll include all!
print(sum_(1, 2, 3))


# not necesarily args. it can be any word!
def display_name(*names):
    for name in names:
        print(name, end=" ")


display_name("Zoltan", "Kulle", "Wolverin")


def print_adress(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}:{value}")


print_adress(street="123 Bake st.", city="Istanbul", region="North", zipnumber="45672")
