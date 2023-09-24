n1 = int(input())
n2 = int(input())
symbol = input()
if symbol == "+":
    result = n1 + n2
    if result % 2 == 0:
        print(f"{n1} {symbol} {n2} = {result} - even")
    else:
        print(f"{n1} {symbol} {n2} = {result} - odd")
elif symbol == "*":
    result = n1 * n2
    if result % 2 == 0:
        print(f"{n1} {symbol} {n2} = {result} - even")
    else:
        print(f"{n1} {symbol} {n2} = {result} - odd")
elif symbol == "-":
    result = n1 - n2
    if result % 2 == 0:
        print(f"{n1} {symbol} {n2} = {result} - even")
    else:
        print(f"{n1} {symbol} {n2} = {result} - odd")
elif symbol == "/":
    if n2 == 0:
        print(f"Cannot divide {n1} by zero")
    else:
        result = n1 / n2
        print(f"{n1} {symbol} {n2} = {result:.2f}")
elif symbol == "%":
    if n2 == 0:
        print(f"Cannot divide {n1} by zero")
    else:
        result = n1 % n2
        print(f"{n1} {symbol} {n2} = {result}")