number_grades_to_fail = int(input())
problems_count = 0
last_problem = ""
failing_grades = 0
total_grade = 0
done_enough = False
while failing_grades < number_grades_to_fail:
    problem = input()
    if problem == "Enough":
        done_enough = True
        break
    grade = int(input())
    if grade <= 4:
        failing_grades += 1
    total_grade += grade
    problems_count += 1
    last_problem = problem
if done_enough:
    average_grade = total_grade / problems_count
    print(f"Average score: {average_grade:.2f}")
    print(f"Number of problems: {problems_count}")
    print(f"Last problem: {last_problem}")
else:
    print(f"You need a break, {failing_grades} poor grades.")