PUZZLE_PRICE = 2.60
DOLL_PRICE = 3
TEDDY_BEAR_PRICE = 4.10
MINION_PRICE = 8.20
TRUCK_PRICE = 2
DISCOUNT = 0.25
RENT = 0.10

price_of_excursion = float(input())
num_puzzles = int(input())
num_dolls = int(input())
num_teddy_bears = int(input())
num_minions = int(input())
num_trucks = int(input())

price_of_order = num_puzzles * PUZZLE_PRICE + num_dolls * DOLL_PRICE \
                 + num_teddy_bears * TEDDY_BEAR_PRICE + num_minions * MINION_PRICE + num_trucks * TRUCK_PRICE
num_of_toys = num_trucks + num_minions +num_dolls + num_puzzles + num_teddy_bears
if num_of_toys >=50:
    price_of_order = price_of_order - (price_of_order * DISCOUNT)
final_earnings = price_of_order - (price_of_order * RENT)
leftover_money = final_earnings - price_of_excursion
if leftover_money >= 0:

    print(f"Yes! {leftover_money:.2f} lv left.")
else:
    print(f"Not enough money! {-leftover_money:.2f} lv needed.")