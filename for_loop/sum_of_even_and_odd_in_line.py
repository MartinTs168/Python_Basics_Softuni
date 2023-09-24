numbers_to_use = int(input())
total_even = 0
total_odd = 0
for numbers in range(numbers_to_use):
    entered_number = int(input())
    if numbers % 2 == 0:
        total_even += entered_number
    elif numbers % 2 != 0:
        total_odd += entered_number
if total_odd == total_even:
    print("Yes")
    print(f"Sum = {total_even}")
else:

    difference = abs(total_even - total_odd)  # abs always takes the positive value
    print("No")
    print(f"Diff = {difference}")
