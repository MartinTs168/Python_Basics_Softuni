GOAL = 10000
command = input()
total_steps = 0

while not command == "Going home":
    steps_today = int(command)
    total_steps += steps_today
    if total_steps >= GOAL:
        break
    command = input()
if command == "Going home":
    steps_today = int(input())
    total_steps += steps_today
if total_steps >= GOAL:
    over_goal_steps = total_steps - GOAL
    print("Goal reached! Good job!")
    print(f"{over_goal_steps} steps over the goal!")
else:
    steps_needed = GOAL - total_steps
    print(f"{steps_needed} more steps to reach goal.")
