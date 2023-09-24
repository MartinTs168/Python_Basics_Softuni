nylon_price_per_square_meter = 1.50
paint_price_per_liter = 14.50
paint_thinner_price_per_liter = 5.00
plastic_bags_price = 0.40
nylon_needed = int(input()) + 2
paint_needed = int(input())
paint_needed = paint_needed + (paint_needed * 0.10)
paint_thinner_needed = int(input())
working_hours_for_worker = int(input())

total_price = nylon_price_per_square_meter * nylon_needed + \
              paint_price_per_liter * paint_needed + \
              paint_thinner_price_per_liter * paint_thinner_needed + \
              plastic_bags_price

total_price = total_price + (total_price * 0.30) * working_hours_for_worker
print(total_price)
