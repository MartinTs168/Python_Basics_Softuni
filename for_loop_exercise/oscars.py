name_actor = input()
points_academy = float(input())
num_judges = int(input())
actors_points = points_academy

for _ in range(num_judges):
    name_judge = input()
    points_judge = float(input())
    actors_points += (points_judge * len(name_judge)) / 2
    if actors_points >= 1250.5:
        print(f"Congratulations, {name_actor} got a nominee for leading role with {actors_points:.1f}!")
        break
if actors_points < 1250.5:
    needed_points = 1250.5 - actors_points
    print(f"Sorry, {name_actor} you need {needed_points:.1f} more!" )

