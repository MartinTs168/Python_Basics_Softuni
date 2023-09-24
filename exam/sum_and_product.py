n = int(input())
sum_of_digits = 0
product_of_digits = 0
found = False
string_number = ""
condition = False
for a in range(1, 9):
    for b in range(9, a, -1):
        for c in range(0, 9):
            for d in range(9, c, -1):
                sum_of_digits = a + b + c + d
                product_of_digits = a * b * c * d
                if sum_of_digits == product_of_digits:
                    string_n = str(n)
                    for index, digit in enumerate(string_n):
                        if int(index) == 2 and int(digit) == 5:
                            condition = True
                            break
                    if condition:
                        string_number = str(a) + str(b) + str(c) + str(d)
                        found = True
                        break
                elif product_of_digits // sum_of_digits == 3 and n % 3 == 0:
                    string_number = str(d) + str(c) + str(b) + str(a)
                    found = True
                    break
            if found:
                break
        if found:
            break
    if found:
        break
if found:
    print(string_number)
else:
    print("Nothing found")






