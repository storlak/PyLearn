# timedelta: subtracting or adding date/time from another
import datetime

dt1 = datetime.datetime.now()
dt2 = datetime.datetime.fromisoformat("1977-04-12T00:00:00")
td = dt1 - dt2
print(td)

# Define two datetime objects
start_time = datetime(2024, 2, 10, 8, 0, 0)
end_time = datetime(2024, 2, 13, 14, 30, 0)

# Calculate the duration between the two datetime objects
duration = end_time - start_time
print(duration)  # Output: 3 days, 6:30:00
