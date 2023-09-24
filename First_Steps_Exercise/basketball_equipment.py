yearly_price = int(input())
shoes = yearly_price - (yearly_price * 0.40)
jersey = shoes - (shoes * 0.20)
ball = jersey / 4
accessories = ball / 5
total_price = yearly_price + shoes + jersey + ball + accessories
print(total_price)
