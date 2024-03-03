# inheritance
# we can inherit, extend, override
class Employee:
    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary

    def work(self):
        print(f"{self.name} is working...")


class SoftWareEngineer(Employee):  # inheriting from Employee
    def __init__(self, name, age, salary, level):
        super().__init__(name, age, salary)
        self.level = level

    def debug(self):
        print(f"{self.name} is debugging...")


class Designer(Employee):
    def draw(self):
        print(f"{self.name} is drawing...")


se = SoftWareEngineer("Max", 25, 6000, "Junior")
print("**SOFTWARE ENGINEER**")
print(se.name, se.age)
se.work()
print(se.level)
se.debug()
print()
print("**DESIGNER**")
d = Designer("Philippe", 27, 8000)
print(d.name, d.age)
d.work()
d.draw()
