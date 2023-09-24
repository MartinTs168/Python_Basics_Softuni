goal = int(input())
type_of_service = input()
profit = 0
reached_goal = False
while not type_of_service == "closed":
    if type_of_service == "haircut":
        type_of_haircut = input()
        if type_of_haircut == "mens":
            profit += 15
        elif type_of_haircut == "ladies":
            profit += 20
        elif type_of_haircut == "kids":
            profit += 10
    elif type_of_service == "color":
        type_coloring = input()
        if type_coloring == "touch up":
            profit += 20
        elif type_coloring == "full color":
            profit += 30
    if profit >= goal:
        reached_goal = True
        break
    type_of_service = input()
if reached_goal:
    print("You have reached your target for the day!")
else:
    money_needed = goal - profit
    print(f"Target not reached! You need {money_needed}lv. more.")
print(f"Earned money: {profit}lv.")
