deposited_sum = float(input())
duration_of_deposit = int(input())/100
yearly_interest = float(input())
sum_at_end_of_deposit_duration = deposited_sum + (duration_of_deposit*((deposited_sum*yearly_interest)/12))
print(sum_at_end_of_deposit_duration)