month = input()
nights_to_spend = int(input())
cost_per_night_apartment = 0
discount_for_apartment = 0
cost_per_night_studio = 0
discount_for_studio = 0

if month == "May" or month == "October":
    cost_per_night_studio = 50
    cost_per_night_apartment = 65
    if nights_to_spend > 14:
        discount_for_studio = 0.30
    elif nights_to_spend > 7:
        discount_for_studio = 0.05
elif month == "June" or month == "September":
    cost_per_night_studio = 75.20
    cost_per_night_apartment = 68.70
    if nights_to_spend > 14:
        discount_for_studio = 0.20
elif month == "July" or month == "August":
    cost_per_night_studio = 76
    cost_per_night_apartment = 77
if nights_to_spend > 14:
    discount_for_apartment = 0.10

apartment_cost = nights_to_spend * cost_per_night_apartment
apartment_cost = apartment_cost - apartment_cost * discount_for_apartment
print(f"Apartment: {apartment_cost:.2f} lv.")

studio_cost = nights_to_spend * cost_per_night_studio
studio_cost = studio_cost - studio_cost * discount_for_studio
print(f"Studio: {studio_cost:.2f} lv.")
