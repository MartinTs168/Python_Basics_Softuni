num_groups = int(input())
Musala_climbers = 0
Monblan_climbers = 0
Kilimanjaro_climbers = 0
K2_climbers = 0
Everest_climbers = 0
sum_people = 0
for _ in range(num_groups):
    people_in_group = int(input())
    if people_in_group < 6:
        Musala_climbers += people_in_group
    elif people_in_group < 13:
        Monblan_climbers += people_in_group
    elif people_in_group < 26:
        Kilimanjaro_climbers += people_in_group
    elif people_in_group < 41:
        K2_climbers += people_in_group
    else:
        Everest_climbers += people_in_group
    sum_people += people_in_group
p1 = Musala_climbers / sum_people * 100
p2 = Monblan_climbers / sum_people * 100
p3 = Kilimanjaro_climbers / sum_people * 100
p4 = K2_climbers / sum_people * 100
p5 = Everest_climbers / sum_people * 100

print(f"{p1:.2f}%")
print(f"{p2:.2f}%")
print(f"{p3:.2f}%")
print(f"{p4:.2f}%")
print(f"{p5:.2f}%")

# 10
# 10
# 5
# 1
# 100
# 12
# 26
# 17
# 37
# 40
# 78