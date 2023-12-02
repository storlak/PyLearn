my_grade = int(98)
grade_letter = "a"  # tanımlamak gerekir öncesinde!

if my_grade > 100 or my_grade < 0:
    grade_letter = "Invalid"
elif 90 <= my_grade <= 100:
    grade_letter = "A"
elif 80 <= my_grade < 90:
    grade_letter = "B"
elif 70 <= my_grade < 80:
    grade_letter = "C"
elif 60 <= my_grade < 70:
    grade_letter = "D"
else:
    grade_letter = "F"
print(grade_letter)
