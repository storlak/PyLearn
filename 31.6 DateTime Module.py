from datetime import datetime, timedelta

s = "2023-04-12T13:30:00-03:00"
print(datetime.fromisoformat(s))
td = timedelta(days=1, seconds=61200)
print(td.total_seconds())
