fat_percentage = int(input())
protein_percentage = int(input())
carbs_percentage = int(input())
total_calories = int(input())
water_percentage =int(input())

grams_of_fat = (fat_percentage * total_calories) / 9
grams_of_carbs = (carbs_percentage * total_calories) / 4
grams_of_protein = (protein_percentage * total_calories) / 4
food_weight = grams_of_fat + grams_of_protein + grams_of_carbs
calories_per_gram_food = total_calories / food_weight
calories_per_gram_food *= (100 - water_percentage)
#calories_per_gram_food *= 100
print(f"{calories_per_gram_food:.4f}")