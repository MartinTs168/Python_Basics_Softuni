import sys

command = input()
min_number = sys.maxsize
while command != "Stop":
    entered_number = int(command)
    if entered_number < min_number:
        min_number = entered_number
    command = input()
print(min_number)




