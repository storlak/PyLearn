person = {"first_name": "Zoltan", "last_name": "Kulle", "year_born": 1989}
print(person["year_born"])
person["year_born"] = 1888  # replaced in the dictionary
print(person)
person["month_born"] = "April"  # added to the dictionary
print(person)

# get gives the key. if Python can't find it it returns None.
print(person.get("first_name"))
