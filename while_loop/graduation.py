name = input()
klass = 1
final_grade = 0
failed = False

while klass <= 12:   # this is an IF
    grade = float(input())
    if grade < 4:
        if failed == True:
            print(f"{name} has been excluded at {klass} grade")
            break
        failed = True
        continue
    final_grade += grade
    klass += 1
else:               #this is the ELSE of the WHILE
    final_grade = final_grade / 12
    print(f"{name} graduated. Average grade: {final_grade:.2f}")

