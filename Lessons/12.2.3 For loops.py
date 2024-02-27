data = [10.5, 11.2, 9.8, None, 11.5, None]
count = sum(1 for val in data if val is not None)
total = sum(val for val in data if val is not None)
avarage = total / count
data = [val if val is not None else avarage for val in data]
print(data)