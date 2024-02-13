from datetime import date, datetime

today = date.today()
print("Today is:", today)
print("Day:", today.day)
print("Month:", today.month)
print("Year:", today.year)

# local date format for TR
print(today.strftime("%d.%m.%Y"))

zoltan = date(1980, 5, 11)
print("Zoltan Kulle was born on", zoltan)

# datetime deals with date&time together
now = datetime.now()
print("Now it is", now)
