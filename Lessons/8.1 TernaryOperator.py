"""ask_price = 80
if ask_price > 50:
    volume = 50
else:
    volume = 80"""

# below is the shortway of writing ternary operator
ask_price = 100
volume = 50 if ask_price > 50 else 80
print(volume)
