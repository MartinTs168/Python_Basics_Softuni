BONUS_TIME = 15
hour = int(input())
minutes = int(input())
hour *= 60
time = hour + minutes + BONUS_TIME
new_hour = time // 60
new_minutes = time % 60
if new_hour == 24:
    new_hour = 0
if new_minutes < 10:
    print(f"{new_hour}:0{new_minutes}")
else:
    print(f"{new_hour}:{new_minutes}")
