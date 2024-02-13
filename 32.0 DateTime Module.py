import datetime

# date object

dt = datetime.date(2024, 2, 13)
dt1 = datetime.date.today()  # this is the local date. Not UTC date
dt2 = datetime.date.fromisoformat("2020-12-31")
print(dt)
print(dt1)
print(dt2)

# time object

t = datetime.time(13, 12, 28)
t1 = datetime.time(0, 0, 0)  # midnight
print(t)
print(t.isoformat())
print(t1)

# datetime object
st = datetime.datetime(2024, 2, 11, 13, 11, 38)
st1 = datetime.datetime.now()  # local
st2 = datetime.datetime.utcnow()  # utc

print(st)
print(st1)
print(st2)

# converting to iso format
s = "2020-04-02T18:30:30-07:00"
dt3 = datetime.datetime.fromisoformat(s)
print(dt3)
