# 'a / b = (result)' and b != 0
a = 3.141592653589793
b = 6
# with fstring
result = f"{a:.4f}, {b:.4f} = {a / b:.4f}"
print(result)
# with format
result = "{:.4f}, {:.4f}, {:.4f}".format(a, b, a / b)
print(result)
