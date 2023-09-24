name = input()
klass = 1
final_grade = 0
bad_grades = 0
failed = False

while klass <= 12:
    grade = float(input())
    if grade < 4:
        bad_grades += 1
        if bad_grades > 1:
            failed = True
            break
        continue
    final_grade += grade
    klass += 1
if failed == True:
    print(f"{name} has been excluded at {klass} grade")
else:
    final_grade = final_grade / 12
    print(f"{name} graduated. Average grade: {final_grade:.2f}")

