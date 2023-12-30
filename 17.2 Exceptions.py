# not completed: raise, try, except, finally

from statistics import fmean

data = [10, 20, 10, 10, 5, 10]
print(fmean(data))

data1 = []

try:
    if len(data1) == 0:
        average = 0
        print(average)
    else:
        print(fmean(data1))
except StatisticsError as ex:
    print("Error:", ex)
