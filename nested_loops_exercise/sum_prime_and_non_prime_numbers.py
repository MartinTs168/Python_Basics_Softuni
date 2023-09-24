command = input()
prime_sum = 0
non_prime_sum = 0
while command != "stop":
    number = int(command)
    if number < 0:
        print("Number is negative.")
        command = input()
        continue
    if number > 1:
        for i in range(2, int(number/2) + 1):
            if (number % i) == 0:
                non_prime_sum += number
                break
        else:
            prime_sum += number

    else:
        non_prime_sum += number
    command = input()
print(f"Sum of all prime numbers is: {prime_sum}")
print(f"Sum of all non prime numbers is: {non_prime_sum}")