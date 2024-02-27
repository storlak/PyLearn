# create a new exception object
# then raise an exception object
# ex = ValueError()
# ex = ValueError("Name must be at least min 5 char long")

name = input("Enter name (5 chars min): ")
if len(name) < 5:
    raise ValueError(f"{name} is not 5 chars or more...")
print(f"Hello {name}!")
