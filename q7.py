n = int(input("Enter a number: "))
sum_divisors = 0

for i in range(1, n):
    if n % i == 0:
        sum_divisors += i

if sum_divisors == n:
    print("Perfect Number")
else:
    print("Not a Perfect Number")
