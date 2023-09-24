from math import floor
W = 2000
F = 1200
SF = 720
won_tournaments = 0
num_tournaments = int(input())
begining_points = int(input())
points = begining_points
for _ in range(num_tournaments):
    finish = input()
    if finish == "W":
        points += W
        won_tournaments += 1
    elif finish == "F":
        points += F
    elif finish == "SF":
        points += SF
print(f"Final points: {floor(points)}")
print(f"Average points: {floor((points - begining_points )/ num_tournaments)}" )
print(f"{(won_tournaments / num_tournaments) * 100:.2f}%")