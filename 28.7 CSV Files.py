# read - parse csv files
import csv

with open("names.csv", "r") as my_file:
    csv_reader = csv.reader(my_file)
    for row in csv_reader:
        print(row)  # this will print a [list] of data in csv
        print(row[2])  # we can print any index
