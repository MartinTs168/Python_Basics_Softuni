EXPENSE_PERCENTAGE = 0.35
egg_size = input()
egg_color = input()
number_of_packs = int(input())
price = 0
total_price = 0
if egg_size == "Large":
    if egg_color == "Red":
        price = 16
    elif egg_color == "Green":
        price = 12
    else:
        price = 9
elif egg_size == "Medium":
    if egg_color == "Red":
        price = 13
    elif egg_color == "Green":
        price = 9
    else:
        price = 7
elif egg_size == "Small":
    if egg_color == "Red":
        price = 9
    elif egg_color == "Green":
        price = 8
    else:
        price = 5
total_price = number_of_packs * price
profit = total_price - total_price * EXPENSE_PERCENTAGE
print(f"{profit:.2f} leva.")
