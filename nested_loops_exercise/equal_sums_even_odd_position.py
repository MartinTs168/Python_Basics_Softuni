num1 = int(input())
num2 = int(input())
for number in range(num1, num2 + 1):
    number_to_str = str(number)
    sum_odd_pos = 0
    sum_even_pos = 0
    for index, digit in enumerate(number_to_str):
        if index % 2 == 0:
            sum_odd_pos += int(digit)
        else:
            sum_even_pos += int(digit)
    if sum_even_pos == sum_odd_pos:
        print(number, end=' ')