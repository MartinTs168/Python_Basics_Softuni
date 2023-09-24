num_jury = int(input())
presentation_name = input()
all_grades_given = 0
sum_grades = 0
while not presentation_name == "Finish":
    average_grade = 0
    for _ in range(num_jury):
        grade = float(input())
        all_grades_given += 1
        average_grade += grade
        sum_grades += grade
    average_grade = average_grade / num_jury
    print(f"{presentation_name} - {average_grade:.2f}.")
    presentation_name = input()
final_assessment = sum_grades / all_grades_given
print(f"Student's final assessment is {final_assessment:.2f}.")
