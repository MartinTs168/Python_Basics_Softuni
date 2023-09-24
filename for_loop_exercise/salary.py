FINE_FACEBOOK = 150
FINE_INSTAGRAM = 100
FINE_REDDIT = 50
num_tabs = int(input())
salary = float(input())
sum_fine = 0 # another way: don't use this variable just write salary -= Fine... in if clauses
for _ in range(num_tabs): # when you use " _ " in loop you are saying that it won't be used
    tab_name = input()
    if tab_name == "Facebook":
        sum_fine += FINE_FACEBOOK
    elif tab_name == "Instagram":
        sum_fine += FINE_INSTAGRAM
    elif tab_name == "Reddit":
        sum_fine += FINE_REDDIT
    if salary <= sum_fine:
        print("You have lost your salary.")
        break
if salary > sum_fine:
    salary -= sum_fine
    print(int(salary))