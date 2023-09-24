start_of_range = int(input())
end_of_range = int(input())
magic_number = int(input())
num_in_order = 0
sum_magic_number_found = False
for number1 in range(start_of_range, end_of_range + 1):
    for number2 in range(start_of_range, end_of_range + 1):
        num_in_order += 1
        if number1 + number2 == magic_number:
            sum_magic_number_found = True
            print(f"Combination N:{num_in_order} ({number1} + {number2} = {magic_number})")
            break
    if sum_magic_number_found:
        break
if not sum_magic_number_found:
    print(f"{num_in_order} combinations - neither equals {magic_number}")