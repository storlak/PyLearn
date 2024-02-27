# CSV dialects
import csv

print(csv.list_dialects())  # default dialects

with open("actors.pdv") as f:
    for row in f:
        print(row.strip())
    print()

with open("actors.pdv") as f:
    reader = csv.reader(
        f, delimiter="|", quotechar="'", escapechar="\\", skipinitialspace=True
    )
    for row in reader:
        print(row)

# registering & using a dialect
csv.register_dialect(
    "pdv", delimiter="|", quotechar="'", escapechar="\\", skipinitialspace=True
)
print(csv.list_dialects())  # print new pdv registered dialects
# now we can use the new registered pdv dialect
with open("actors.pdv") as f:
    reader = csv.reader(f, dialect="pdv")
    for row in reader:
        print(row)
