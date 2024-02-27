# min, max: (iterable, key=func)
data = [-1, 6, 7, 0, 12, -9]

print(min(data, key=abs))
print(max(data))

divisible_by_2 = [num for num in data if num % 2 == 0]

if divisible_by_2:
    highest = max(divisible_by_2)
    lowest = min(divisible_by_2)
    print(f"Highest number divisible by 2 is {highest}")
    print(f"Lowest number divisible by 2 is {lowest}")
else:
    print("There are no numbers divisible by 2 in the list")
