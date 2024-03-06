# pytz module used for dealing timezones, aware datetime obj with timezone
# naming convention: Area/Location: Europe/Paris
# pip install pytz
import pytz
from datetime import datetime, time

for tz in pytz.all_timezones:
    print(tz)

tz_Chicago = pytz.timezone("America/Chicago")
tz_Chicago = pytz.timezone("America/Chicago")

print(tz_Chicago)
print(tz_Chicago)  # pytz.UTC easier to write
print(tz_Chicago.zone)  # gives name of timezone

# naive datetime: no info about timezon, daylight
dt_naive = datetime(2020, 5, 15, 10, 0, 0)  # no timezone info
print(dt_naive)
# adding tz info. pytz makes DTS calculations auto
dt_chicago = tz_Chicago.localize(dt_naive)
print(dt_chicago)
print(dt_naive.replace(tzinfo=tz_Chicago))
