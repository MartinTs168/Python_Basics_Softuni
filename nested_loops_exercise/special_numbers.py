number = int(input())
for special_num in range(1111, 9999):
    number_to_str = str(special_num)
    counter_digits = 0
    for index, digit in enumerate(number_to_str):
        if int(digit) == 0:
            continue
        if number % int(digit) == 0:
            counter_digits += 1
    if counter_digits == 4:
        print(special_num, end=" ")

