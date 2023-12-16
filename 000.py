data = [10, 20, 30, -10, 40, -5]
for number in enumerate(data):
    place, element = number
    if element < 0:
        data[place] = 0
        print(data)