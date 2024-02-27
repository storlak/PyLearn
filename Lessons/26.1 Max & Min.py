# checking max number in a list without using max function
data = [3, 4, -9, 10, 18]
max_num = data[0]
print("Start Max:", max_num)
for number in data:
    print("Checking:", number)
    if number > max_num:
        print("NEW MAX:", number)
        max_num = number
print("Max:", max_num)
