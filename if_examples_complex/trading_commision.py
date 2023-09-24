city = input()
sales = float(input())
commission_percentage = 0
commission = 0
if city == "Sofia":
    if sales >= 0 and sales <=500:
        commission_percentage = 0.05
    elif 500 < sales <= 1000:
        commission_percentage = 0.07
    elif sales > 1000 and sales <= 10000:
        commission_percentage = 0.08
    elif sales > 10000:
        commission_percentage = 0.12
elif city == "Varna":
    if sales >= 0 and sales <= 500:
        commission_percentage = 0.045
    elif 500 < sales <= 1000:
        commission_percentage = 0.075
    elif sales > 1000 and sales <= 10000:
        commission_percentage = 0.10
    elif sales > 10000:
        commission_percentage = 0.13
elif city == "Plovdiv":
    if sales >= 0 and sales <= 500:
        commission_percentage = 0.055
    elif 500 < sales <= 1000:
        commission_percentage = 0.08
    elif sales > 1000 and sales <= 10000:
        commission_percentage = 0.12
    elif sales > 10000:
        commission_percentage = 0.145
if commission_percentage == 0:
    print("error")
else:
    commission = sales * commission_percentage
    print(f"{commission:.2f}")


# city = input()
# money = float(input())
# commission = 0
# error = False
# if city == "Sofia":
#     if 0 <= money <= 500:
#         commission = 0.05
#     elif 500 < money <= 1000:
#         commission = 0.07
#     elif 1000 < money <= 10000:
#         commission = 0.08
#     elif money > 10000:
#         commission = 0.12
#     else:
#         print("error")
#         error = True
# elif city == "Varna":
#     if 0 <= money <= 500:
#         commission = 0.045
#     elif 500 < money <= 1000:
#         commission = 0.075
#     elif 1000 < money <= 10000:
#         commission = 0.1
#     elif money > 10000:
#         commission = 0.13
#     else:
#         print("error")
#         error = True
# elif city == "Plovdiv":
#     if 0 <= money <= 500:
#         commission = 0.055
#     elif 500 < money <= 1000:
#         commission = 0.08
#     elif 1000 < money <= 10000:
#         commission = 0.12
#     elif money > 10000:
#         commission = 0.145
#     else:
#         print("error")
#         error = True
# else:
#     print("error")
#     error = True
# if not error:
#     commission = money * commission
#     print(f"{commission:.2f}")