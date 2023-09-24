import sys

count_of_numbers = int(input())
max_number = - sys.maxsize
sum_numbers = 0
for number in range(count_of_numbers):
    num = int(input())
    if num > max_number:
        max_number = num
    sum_numbers += num
if max_number == sum_numbers - max_number:
    print("Yes")
    print(f"Sum = {max_number}")
else:
    print("No")
    sum_numbers = sum_numbers - max_number - max_number
    print(f"Diff = {abs(sum_numbers)}")