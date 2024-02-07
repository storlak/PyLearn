import csv

with open("names.csv", "r") as my_file:
    csv_reader = csv.reader(my_file)  # csv reader expects commas to read!
    with open("new_names.csv", "w") as my_scd_file:
        csv_writer = csv.writer(my_scd_file, delimiter="\t")

        for line in csv_reader:
            csv_writer.writerow(line)
