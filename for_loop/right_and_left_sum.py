numbers_to_use = int(input())
total_left = 0
total_right = 0
for numbers in range(2 * numbers_to_use):
    entered_number = int(input())
    if numbers < numbers_to_use:
        total_left += entered_number
    elif numbers >= numbers_to_use:
        total_right += entered_number
if total_right == total_left:
    print(f"Yes, sum = {total_left}")
else:
    difference = abs(total_left - total_right)  # abs always takes the positive value
    print(f"No, diff = {difference}")
