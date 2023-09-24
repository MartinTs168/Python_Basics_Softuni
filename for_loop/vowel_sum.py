word = input()
total = 0
for index in range(len(word)):
    value = 0
    if word[index] == "a":
        value = 1
    elif word[index] == "e":
        value = 2
    elif word[index] == "i":
        value = 3
    elif word[index] == "o":
        value = 4
    elif word[index] == "u":
        value = 5
    total += value
print(total)