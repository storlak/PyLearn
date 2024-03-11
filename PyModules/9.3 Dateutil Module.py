from dateutil import parser
from datetime import datetime

my_date = datetime.strptime("2020-01-01T10:30:00", "%Y-%m-%dT%H:%M:%S")
print(my_date)
my_date1 = parser.parse("2020-01-01T10:30:00 pm+1:00")
print(my_date1)

# dateutil recognizes which is mont or day
my_date2 = parser.parse("12 / 31 / 2020")
print(my_date2)

# parser do not recognize the below string but:
s = "Today is May the 23, 2020 at 3pm UTC"
try:
    parser.parse(s)
except Exception as ex:
    print(type(ex), ex)
# fuzzy with tokens helps to parse
print(parser.parse(s, fuzzy_with_tokens=True))
