my_grade = int(input("Enter your grade (0-100) : "))
if my_grade > 100:
    your_grade = "your grade cannot be greater than 100"
elif my_grade >= 90:
    your_grade = "A"
elif my_grade >= 80:
    your_grade = "B"
elif my_grade >= 70:
    your_grade = "C"
elif my_grade >= 60:
    your_grade = "D"
else:
    your_grade = "F"
print(your_grade)
