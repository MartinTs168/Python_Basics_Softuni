age_Lily = int(input())
washing_machine_price = float(input())
price_of_toy = int(input())
saved_money = 0
money_given = 10
num_toys = 0
for birthday in range(1, age_Lily + 1):
    if birthday % 2 == 0:
        saved_money += money_given
        money_given += 10
        saved_money -= 1
    else:
        num_toys += 1
saved_money += num_toys * price_of_toy
leftover_money = abs(saved_money - washing_machine_price)
if saved_money >= washing_machine_price:
    print(f"Yes! {leftover_money:.2f}")
else:
    print(f"No! {leftover_money:.2f}")