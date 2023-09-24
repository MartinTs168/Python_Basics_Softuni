number_of_days = int(input())
room_type = input()
review = input()
price_per_night = 0
discount = 0
total_price = 0
additional_change_price_due_to_review = 0

if room_type == "room for one person":
    price_per_night = 18
elif room_type == "apartment":
    price_per_night = 25
    if number_of_days < 10:
        discount = 0.3
    elif 10 <= number_of_days <= 15:
        discount = 0.35
    else:
        discount = 0.5
elif room_type == "president apartment":
    price_per_night = 35
    if number_of_days < 10:
        discount = 0.1
    elif 10 <= number_of_days <= 15:
        discount = 0.15
    else:
        discount = 0.2
total_price = price_per_night * (number_of_days - 1)
total_price -= total_price * discount

if review == "positive":
    additional_change_price_due_to_review = 0.25
    total_price += total_price * additional_change_price_due_to_review
else:
    additional_change_price_due_to_review = 0.1
    total_price -= total_price * additional_change_price_due_to_review
print(f"{total_price:.2f}")
