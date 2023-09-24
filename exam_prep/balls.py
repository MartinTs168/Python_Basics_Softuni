points = 0
red_ball_counter = 0
orange_ball_counter = 0
yellow_ball_counter = 0
white_ball_counter = 0
black_ball_counter = 0
another_color_ball = 0
balls_to_draw = int(input())
for _ in range(balls_to_draw):
    ball_color = input()
    if ball_color == "red":
        points += 5
        red_ball_counter += 1
    elif ball_color == "orange":
        points += 10
        orange_ball_counter += 1
    elif ball_color == "yellow":
        points += 15
        yellow_ball_counter += 1
    elif ball_color == "white":
        points += 20
        white_ball_counter += 1
    elif ball_color == "black":
        points //= 2
        black_ball_counter += 1
    else:
        another_color_ball += 1
        continue
print(f"Total points: {points}")
print(f"Red balls: {red_ball_counter}")
print(f"Orange balls: {orange_ball_counter}")
print(f"Yellow balls: {yellow_ball_counter}")
print(f"White balls: {white_ball_counter}")
print(f"Other colors picked: {another_color_ball}")
print(f"Divides from black balls: {black_ball_counter}")
