# timezone. naive and aware timzone
# timezone (hours=, and optional name of timezone)
import datetime
from time import perf_counter

start = perf_counter()

d1 = datetime.datetime.fromisoformat("2024-05-15T13:30:00-04:00")
tz_CDT = datetime.timezone(datetime.timedelta(hours=-5), "CDT")
d2 = d1.astimezone(tz_CDT)  # convert to CDT timezone
print(d2)
d3 = d1.astimezone(datetime.timezone.utc)  # convert to UTC timezone
print(d3)

end = perf_counter()
elapsed_time = end - start
print("elapsed time is:", elapsed_time)
