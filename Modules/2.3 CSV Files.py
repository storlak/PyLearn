# CSV files: Reading data using Dict Reader/Writer
import csv

with open("names.csv", "r") as my_file:
    csv_reader = csv.DictReader(my_file)

    for line in csv_reader:
        # print(line)
        print(line["email"])
