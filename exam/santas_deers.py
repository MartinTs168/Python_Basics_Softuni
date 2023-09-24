from math import floor, ceil

days = int(input())
kg_food = int(input())
first_deer_serving_kg = float(input())
second_deer_serving_kg = float(input())
third_deer_serving_kg = float(input())
total_food_needed = (first_deer_serving_kg + second_deer_serving_kg + third_deer_serving_kg) * days
leftover_food = kg_food - total_food_needed
if leftover_food > 0:
    print(f"{floor(leftover_food)} kilos of food left.")
else:
    leftover_food = abs(leftover_food)
    print(f"{ceil(leftover_food)} more kilos of food are needed.")
