command = input()
total_deposit = 0
while command != "NoMoreMoney":
    deposited_money = float(command)
    if deposited_money < 0:
        print("Invalid operation!")
        break
    print(f"Increase: {deposited_money:.2f}")
    total_deposit += deposited_money
    command = input()
print(f"Total: {total_deposit:.2f}")
