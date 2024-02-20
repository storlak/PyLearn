# writing CSV files
import csv

data = [
    ["First Name", "Last Name", "DOB", "Sketches"],
    [
        "John",
        "Cleese",
        "10/27/39",
        "The Cheese Shop, Ministry of Silly Walks, It's the Arts",
    ],
    ["Eric", "Idle", "3/29/43", 'The Cheese Shop, Nudge Nudge, "Spam"'],
    ["Peter", "O'Toole", "8/2/32", "Lawrence of Arabia"],
]

with open("test.csv", "w") as f:
    writer = csv.writer(f)
    for row in data:
        writer.writerow(row)

with open("test.csv") as f:
    for row in f:
        print(row, end=" ")
