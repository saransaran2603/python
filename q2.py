num = int(input("Enter a number: "))

num = abs(num)
last = num % 10

while num >= 10:
    num = num // 10

first = num

print("Sum of first and last digit:", first + last)
