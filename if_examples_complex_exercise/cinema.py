type_of_projection = input()
row_num = int(input())
col_num = int(input())
price_per_ticket = 0
total_price = 0
if type_of_projection == "Premiere":
    price_per_ticket = 12
elif type_of_projection == "Normal":
    price_per_ticket = 7.50
elif type_of_projection == "Discount":
    price_per_ticket = 5
total_price = (row_num * col_num) * price_per_ticket
print(f"{total_price:.2f} leva")