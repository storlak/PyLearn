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

    # instance method
    def code(self):
        print(f"{self.name} is writing code...")

    def code_in_language(self, language):
        print(f"{self.name} is writing code in {language}...")

    def information(self):  # using return in Class
        information = f"Employee: {self.name}, {self.age}, {self.level}"
        return information


# instance
se1 = SoftwareEngineer("Max", 20, "Junior", 5000)
se2 = SoftwareEngineer("Lisa", 25, "Junior", 800)

print(se1.information())
se1.code()
print("*" * 5)
se2.code_in_language("Python")

# Recap
# instance method (self)
# can take arguments and can return values
