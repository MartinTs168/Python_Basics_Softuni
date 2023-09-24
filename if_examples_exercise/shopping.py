PRICE_FOR_GPU = 250
budget = float(input())
number_GPU = int(input())
price_CPU = 0.35 * (PRICE_FOR_GPU * number_GPU)
price_RAM = 0.10 * (PRICE_FOR_GPU * number_GPU)
number_CPU = int(input())
number_RAM = int(input())

GPU_order_cost = number_GPU * PRICE_FOR_GPU
CPU_order_cost = number_CPU * price_CPU
RAM_order_cost = number_RAM * price_RAM
total_cost = GPU_order_cost + CPU_order_cost + RAM_order_cost
if number_GPU > number_CPU:
    discount = 0.15
    total_cost = total_cost - total_cost * discount
if budget >= total_cost:
    leftover_money = budget - total_cost
    print(f"You have {leftover_money:.2f} leva left!")
elif budget < total_cost:
    needed_money = total_cost - budget
    print(f"Not enough money! You need {needed_money:.2f} leva more!")