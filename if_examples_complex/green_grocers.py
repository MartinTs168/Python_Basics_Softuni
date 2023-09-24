item = input()
type = ""
if item == "banana" or item == "apple" or item == "kiwi" or item == "cherry" \
        or item == "lemon" or item == "grapes":
    type = "fruit"
elif item == "tomato" or item == "cucumber" or item == "pepper" or item == "carrot":
    type = "vegetable"
else:
    type = "unknown"
print(type)