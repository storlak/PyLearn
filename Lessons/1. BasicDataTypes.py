# integer
print(1)

# float
print(1.0)

# float ile gözüken sayı aynısı değil, py yuvarlıyor. Örnek aşağıda. Gözüken 0.1 ama gerçek:
print(format(0.1, ".25f"))
print(0.1 == 0.1000000000000000055511151)  # not equal or same but still True veriyor!
print(0.1 + 0.1 + 0.1 == 0.3)  # false veriyor!!!
print(
    abs(0.1 + 0.1 + 0.1 - 0.3)
)  # abs absolute value. Böylece aradaki farkı görebiliriz!
print(format(0.1 + 0.1 + 0.1, ".25f"))
print(0.1 + 0.1 + 0.1 == 0.3000000000000000444089210)  # == True!!!

# Booleans
print(True)
print(False)
