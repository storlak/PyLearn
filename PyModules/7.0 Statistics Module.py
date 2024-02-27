# mean, fmean: art avearge of an iterable
import statistics as stats

data = list(range(1, 11))
data1 = list(range(1, 100, 3))
print(stats.mean(data))
print(stats.fmean(data))  # using fmean is faster than mean
print(stats.median(data1))
print(stats.median_low(data1))  # low, left side of the num
print(stats.median_high(data1))  # high, right side of the num

# mode: the most frequently occurring value
data2 = [1, 2, 3, 4, 4, 5, 5, 5, 6]
mode_value = stats.mode(data2)
print("Mode of the dataset:", mode_value)

# mode & multimode works also with strings
data = ["apple", "banana", "apple", "orange", "banana", "apple"]
mode_value = stats.mode(data)
print("Mode of the dataset:", mode_value)
modes = stats.multimode(data)
print("Modes of the dataset:", modes)
