# decimal precision is 28
import decimal
from decimal import Decimal

d = Decimal(100)
print(d)
print(Decimal(0.1))  # returns the float representation of 0.1

# example
a = 0.25
b = 0.1
c = 0.1
print(a + b + c)

# with decimal we'll get the correct result
a = Decimal(" 0.25")
b = Decimal("0.1")
c = Decimal("0.1")
print(a + b + c)
