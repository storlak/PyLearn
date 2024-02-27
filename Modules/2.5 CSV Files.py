import csv

# working & reading csv files
nasdaq = "nasdaq.csv"
with open(nasdaq) as f:
    for _ in range(5):
        row = next(f)
        print(row)

with open(nasdaq) as f:
    reader = csv.reader(f)  # default is excel
    for row in reader:
        print(row)


# floats in the end line are printed as strings.
# to correct this:
def parse_nasdaq(f_name):
    result = []

    with open(f_name) as f:
        reader = csv.reader(f)

        headers = next(reader)
        result.append(headers)

        for row in reader:
            row[-1] = float(row[-1])
            result.append(row)
    return result


parse_nasdaq(nasdaq)
