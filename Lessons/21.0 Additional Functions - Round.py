# python rounds to even. 13.5 rounds to 14 while 12.5 rounds to 12.
# round(value, exponent)

mynum = 3.928374
rounded_num = round(mynum, 2)
print(rounded_num)

print(round(3.325))
print(round(12345, -1))
print(round(12345, -2))
print(round(12345, -3))

# floats do not have exact representation
print(round(0.325, 2))
