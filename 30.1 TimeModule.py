from time import perf_counter, sleep, strftime

# perf_counter calculates...
start = perf_counter()
sleep(1)
end = perf_counter()
elapsed_time = end - start
print(elapsed_time)

# strftime
print(strftime("%A is the best day of the week."))
print(strftime("Today's date is: %d.%m.%Y"))
print("What time is it?")
print(strftime("It is %H:%M:%S"))
