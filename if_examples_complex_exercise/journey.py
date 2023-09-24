budget = float(input())
season = input()
destination = ""
cost = 0
type_vacation = ""
if budget <= 100:
    destination = "Bulgaria"
    if season == "summer":
        cost = budget * 0.3
        type_vacation = "Camp"
    else:
        cost = budget * 0.7
        type_vacation = "Hotel"
elif budget <= 1000:
    destination = "Balkans"
    if season == "summer":
        cost = budget * 0.4
        type_vacation = "Camp"
    else:
        cost = budget * 0.8
        type_vacation = "Hotel"
elif budget > 1000:
    destination = "Europe"
    type_vacation = "Hotel"
    cost = budget * 0.9
print(f"Somewhere in {destination}")
print(f"{type_vacation} - {cost:.2f}")