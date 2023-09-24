attended_students = int(input())
top_grade_count = 0
really_good_grade_count = 0
good_grade_count = 0
failing_grade_count = 0
sum_of_grades = 0
for _ in range(attended_students):
    grade = float(input())
    sum_of_grades += grade
    if grade >= 5:
        top_grade_count += 1
    elif 4 <= grade <= 4.99:
        really_good_grade_count += 1
    elif 3 <= grade <= 3.99:
        good_grade_count += 1
    elif 2 <= grade <= 2.99:
        failing_grade_count += 1
top_grade_percentage = (top_grade_count / attended_students * 100)
really_good_grade_percentage = (really_good_grade_count / attended_students * 100)
good_grade_percentage = (good_grade_count / attended_students * 100)
failing_grade_percentage = (failing_grade_count / attended_students * 100)
average_grade = sum_of_grades / attended_students

print(f"Top students: {top_grade_percentage:.2f}%")
print(f"Between 4.00 and 4.99: {really_good_grade_percentage:.2f}%")
print(f"Between 3.00 and 3.99: {good_grade_percentage:.2f}%")
print(f"Fail: {failing_grade_percentage:.2f}%")
print(f"Average: {average_grade:.2f}")
