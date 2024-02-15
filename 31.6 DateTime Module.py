from datetime import datetime, timedelta, timezone

s = "2020-03-15T13:30:00-07:00"
print(datetime.fromisoformat(s))
td = timedelta(days=-1, seconds=61200)
print(td.total_seconds())
print(td.total_seconds() // 60 // 60)

tz_EDT = timezone(timedelta(hours=-4), "EDT")
tz_CDT = timezone(timedelta(hours=-5), "CDT")
dt = datetime(year=2024, month=4, day=12, hour=22, minute=28, tzinfo=tz_EDT)
print(dt)

# converting EDT to CDT
dt = dt.astimezone(tz_CDT)
print(dt)
