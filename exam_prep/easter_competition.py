import  sys
best_points = - sys.maxsize
best_chef_name = ""
number_of_ester_breads = int(input())
for _ in range(number_of_ester_breads):
    bakers_total_points = 0
    baker_name = input()
    bakers_points = input()
    while not bakers_points == "Stop":
        points = int(bakers_points)
        bakers_total_points += points
        bakers_points = input()
    print(f"{baker_name} has {bakers_total_points} points.")
    if bakers_total_points > best_points:
        best_points = bakers_total_points
        print(f"{baker_name} is the new number 1!")
        best_chef_name = baker_name
print(f"{best_chef_name} won competition with {best_points} points!")



