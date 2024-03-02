# this part is from other sources


# creating the class
class SoftwareEngineer:

    # class attribute
    alias = "Keyboard Magician"

    # instance attributes
    def __init__(self, name, age, level, salary):
        self.name = name
        self.age = age
        self.level = level
        self.salary = salary


# instance
se1 = SoftwareEngineer("Max", 20, "Junior", 5000)
se2 = SoftwareEngineer("Lisa", 25, "Junior", 800)
print(se1.name, se1.age)
print(SoftwareEngineer.alias)  # alias works with both. it is a class attribute
print(se1.alias)
print("*" * 15)
print(se2.alias)
print(SoftwareEngineer.alias)

# Recap
# creating a class
# create an instance (object)
# class vs instance
# instance attributes: defined in __init__(self)
# attribues
