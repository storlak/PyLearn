import pytz
import datetime as dt

# current local time
dt1 = dt.datetime.now()
print(dt1)
# current utc time no consideration of location
dt2 = dt.datetime.now(pytz.utc)
print(dt2)
# current utc time in Istanbul
dt3 = dt.datetime.now(pytz.timezone("Europe/Istanbul"))
print(dt3)
