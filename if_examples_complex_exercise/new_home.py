# Роза	Далия	Лале	Нарцис	Гладиола
# 5	   3.80	   2.80	    3	       2.50
price = 0
discount = 0
fine = 0
total_price = 0
type_flower = input()
num_flowers = int(input())
budget = int(input())
if type_flower == "Roses":
    price = 5
    if num_flowers > 80:
        discount = 0.1
elif type_flower == "Dahlias":
    price = 3.8
    if num_flowers > 90:
        discount = 0.15
elif type_flower == "Tulips":
    price = 2.8
    if num_flowers > 80:
        discount = 0.15
elif type_flower == "Narcissus":
    price = 3
    if num_flowers < 120:
        fine = 0.15
elif type_flower == "Gladiolus":
    price = 2.5
    if num_flowers < 80:
        fine = 0.2
total_price = price * num_flowers
total_price = -(total_price * discount) + (total_price * fine) + total_price
leftover_money = budget - total_price
if leftover_money >= 0:
    print(f"Hey, you have a great garden with {num_flowers} {type_flower} and {abs(leftover_money):.2f} leva left.")
else:
    print(f"Not enough money, you need {abs(leftover_money):.2f} leva more.")
