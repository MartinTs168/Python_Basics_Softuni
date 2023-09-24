package_weight = float(input())
type_of_delivery = input()
distance_km = int(input())
price_per_km = 0
added_cost = 0
if type_of_delivery == "standard" or type_of_delivery == "express":
    if package_weight < 1:
        price_per_km = 0.03
        if type_of_delivery == "express":
            added_cost = (price_per_km * 0.8) * distance_km * package_weight
    elif 1 <= package_weight < 10:
        price_per_km = 0.05
        if type_of_delivery == "express":
            added_cost = (price_per_km * 0.4) * distance_km * package_weight
    elif 10 <= package_weight < 40:
        price_per_km = 0.1
        if type_of_delivery == "express":
            added_cost = (price_per_km * 0.05) * distance_km * package_weight
    elif 40 <= package_weight < 90:
        price_per_km = 0.15
        if type_of_delivery == "express":
            added_cost = (price_per_km * 0.02) * distance_km * package_weight
    elif 90 <= package_weight < 150:
        price_per_km = 0.2
        if type_of_delivery == "express":
            added_cost = (price_per_km * 0.01) * distance_km * package_weight
total_price = (distance_km * price_per_km) + added_cost
print(f"The delivery of your shipment with weight of {package_weight:.3f} kg. would cost {total_price:.2f} lv.")
