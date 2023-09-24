kg_dog_food_bought = int(input())
dog_food_bought_grams = kg_dog_food_bought * 1000
command = input()
grams_food_eaten = 0
while not command == "Adopted":
    current_meal_weight = int(command)
    grams_food_eaten += current_meal_weight
    command = input()
leftover_food = dog_food_bought_grams - grams_food_eaten
if leftover_food >= 0:
    print(f"Food is enough! Leftovers: {leftover_food} grams.")
else:
    print(f"Food is not enough. You need {abs(leftover_food)} grams more.")
