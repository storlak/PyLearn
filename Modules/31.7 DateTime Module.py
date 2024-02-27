from datetime import datetime, date, time

t = time(23, 24, 35)
print(t.strftime("The time is: %I hours, %M minutes, and %S seconds, %p."))

d = date(2020, 5, 15)
print(d.strftime("%B, %d, %Y"))

dt = datetime(2024, 2, 15, 23, 30, 45)
print(dt.strftime("%I:%M %p %B %d, %Y"))
