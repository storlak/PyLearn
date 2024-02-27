def hello(greeting, title, first, last):
    print(f"{greeting} {title} {first} {last}")


hello("Hello", "Mr.", "Zoltan", "Kulle")


def get_phone(country, area, threedig, twodig, twodig1):
    phone_num = f"+{country}({area}) {threedig} {twodig} {twodig1}"
    return phone_num


phone_num = get_phone(country=90, area=216, threedig=23, twodig=456, twodig1=89)
print(phone_num)
