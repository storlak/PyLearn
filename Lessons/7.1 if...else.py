my_grade = 110

if my_grade >= 90:
    your_grade = "A"
else:
    if my_grade >= 80:
        your_grade = "B"
    else:
        if my_grade >= 70:
            your_grade = "C"
        else:
            if my_grade >= 60:
                your_grade = "D"
            else:
                your_grade = "F"
print(your_grade)
