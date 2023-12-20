person = {
    "first_name": "Zoltan",
    "last_name": "Kulle",
    "year_born": 1989
}

# iterating in dictionaries
for y in person:  # default is keys. it will iterate keys
    print(y)
for x in person.values():  # this will iterate values and print values.
    print(x)
for z in person.items():  # items will print keys & values (pairs) in a tuple.
    print(z)
for k, v in person.items():  # possible to unpack dictionaries.
    print(f"{k} = {v}")
