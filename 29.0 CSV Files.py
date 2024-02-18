# Working with CSV files
# csv: comma seperated values. tabular data (rownd & columns)
import csv

with open("actors.csv") as f:
    for row in f:
        print(row)

with open("actors.csv") as f:
    for row in f:
        row = row.strip()
        fields = row.split(",")
        print(fields)
# reading with csv
with open("actors.csv") as f:
    reader = csv.reader(f, delimiter=",", quotechar='"')
    for row in reader:
        print(row)
