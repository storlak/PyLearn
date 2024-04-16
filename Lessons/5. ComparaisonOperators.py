# Value and Identity equality
a = 10
b = 10
c = 10.0
print(id(a))
print(a == b)
print(a is b)
print(a == c)  # in terms of value it is True
print(a is c)  # in terms ofidentity it is False


class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        if isinstance(other, Vector):
            return Vector(self.x + other.x, +self.y + other.y)

    def __repr__(self):
        return f"Vector ({self.x}, {self.y})"


v1 = Vector(1, 1)
v2 = Vector(1, 1)
v3 = Vector(2, 3)
