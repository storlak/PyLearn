import datetime as dt, pytz

# datetime string no timezone
datetime_string = "2022-01-01 12:21:22"
# format we need:
datetime_newyork = dt.datetime.strptime(datetime_string, "%Y-%m-%d %H:%M:%S")

# current and target timezone: converting
currrent_timezone = pytz.timezone("US/Eastern")
target_timezone = pytz.timezone("Europe/Istanbul")

# localized time
localized_newyork = currrent_timezone.localize(datetime_newyork)
datetime_istanbul = localized_newyork.astimezone(target_timezone)

print(datetime_newyork)
print(localized_newyork)
print(datetime_istanbul)  # output prints +03H if we don't want that output:
# without timezone difference ouuput
print(datetime_istanbul.replace(tzinfo=None))
# or printing only time (no date)
print(datetime_istanbul.timetz())
