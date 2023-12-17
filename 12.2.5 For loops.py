# using fmean: converts all the data into float data-type and then computes average of data of an iterable

from statistics import fmean

data = [10.5, 11.2, 9.8, None, 11.5, None]
average = fmean(val for val in data if val is not None)
data = [val if val is not None else average for val in data]
print(data)
