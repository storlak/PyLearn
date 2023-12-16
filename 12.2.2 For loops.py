data = [10.5, 11.2, 9.8, None, 11.5, None]
count = 0
total = 0

for i in range(len(data)):
    if data[i] is not None:
        count = count + 1
        total = total + data[i]
avarage = total / count
print(avarage)