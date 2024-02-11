from datetime import datetime

x = datetime.now()
print(x.year)
print(x.strftime("%A"))


current_datetime = datetime.now()
formatted_datetime = current_datetime.strftime("%d.%m.%Y %H:%M:%S")
print("Formatted current date and time:", formatted_datetime)
