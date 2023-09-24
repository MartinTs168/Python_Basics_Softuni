import sys

numbers_to_write = int(input())
max_number = - sys.maxsize
min_number = sys.maxsize
for number in range(numbers_to_write):
    number = int(input())
    if max_number <= number:
        max_number = number
    if min_number >= number:
        min_number = number
print(f"Max number: {max_number}")
print(f"Min number: {min_number}")
