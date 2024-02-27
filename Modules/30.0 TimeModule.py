# time module with Youtube
import time

print(time.ctime(0))  # show the eopch time of the computer
print(time.time())  # returns current scds since eopch

time_object = time.localtime()
print(time_object)

local_time = time.strftime("%d.%m.%Y %H:%M:%S", time_object)  # shows local time
print(local_time)
print("And the Oscar goes to...")
time.sleep(3)
print("What Oscar Bro.")
