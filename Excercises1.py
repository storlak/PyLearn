seconds_in_minutes = 60
seconds_in_hour = 60 * seconds_in_minutes
seconds_in_day = 24 * seconds_in_hour
seconds_in_week = 7 * seconds_in_day

elapsed = 23 # secds

if elapsed < seconds_in_minutes:
    magnitude = "seconds"
elif elapsed < seconds_in_hour:
    magnitude = "minutes"
elif elapsed < seconds_in_day:
    magnitude = "hours"
elif elapsed < seconds_in_week:
    magnitude = "days"
else:
    magnitude = "weeks"
print(magnitude)
