SPENDING_COMMAND = "spend"
SAVING_COMMAND = "save"
money_needed_excursion = float(input())
saved_money = float(input())
spending_counter = 0
days_counter = 0
not_able_to_save = False
while saved_money < money_needed_excursion:
    command = input()
    money = float(input())
    if command == SPENDING_COMMAND:
        saved_money -= money
        spending_counter += 1
        if money > saved_money:
            saved_money = 0
    elif command == SAVING_COMMAND:
        saved_money += money
        spending_counter = 0
    days_counter += 1
    if spending_counter == 5:
        not_able_to_save = True
        break
if not_able_to_save:
    print("You can't save the money.")
    print(days_counter)
else:
    print(f"You saved the money for {days_counter} days.")
