import sys

command = input()
max_number = -sys.maxsize
while command != "Stop":
    entered_number = int(command)
    if entered_number > max_number:
        max_number = entered_number
    command = input()
print(max_number)




