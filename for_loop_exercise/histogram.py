count_of_numbers = int(input())
num_under_200 = 0
num_between_200_399 = 0
num_between_400_599 = 0
num_between_600_799 = 0
num_bigger_or_equal_800 = 0

for i in range(count_of_numbers):
    number = int(input())
    if number < 200:
        num_under_200 += 1
    elif 200 <= number <= 399:
        num_between_200_399 += 1
    elif 400 <= number <= 599:
        num_between_400_599 += 1
    elif 600 <= number <= 799:
        num_between_600_799 += 1
    else:
        num_bigger_or_equal_800 += 1
p1 = num_under_200 / count_of_numbers * 100
p2 = num_between_200_399 / count_of_numbers * 100
p3 = num_between_400_599 / count_of_numbers * 100
p4 = num_between_600_799 / count_of_numbers * 100
p5 = num_bigger_or_equal_800 / count_of_numbers * 100

print(f"{p1:.2f}%")
print(f"{p2:.2f}%")
print(f"{p3:.2f}%")
print(f"{p4:.2f}%")
print(f"{p5:.2f}%")