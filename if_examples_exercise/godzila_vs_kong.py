VALUE_OF_DECOR = 0.10 #ten percent of budget
budget = float(input())
num_of_statists = int(input())
price_of_clothes_for_single_statist = float(input())
price_of_decor = budget * VALUE_OF_DECOR
price_of_clothes = price_of_clothes_for_single_statist * num_of_statists
if num_of_statists >= 150:
    price_of_clothes = price_of_clothes - price_of_clothes * 0.10
expense = price_of_decor + price_of_clothes
if budget < expense:
    money_needed = expense - budget
    print("Not enough money!")
    print(f"Wingard needs {money_needed:.2f} leva more.")
elif budget >= expense:
    money_left = budget - expense
    print("Action!")
    print(f"Wingard starts filming with {money_left:.2f} leva left.")

