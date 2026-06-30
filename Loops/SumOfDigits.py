num = int(input("Enter a number: "))

sum_of_digits = 0

while num > 0:
    digit = num % 10
    sum_of_digits += digit
    num = num // 10

print("Sum of Digits =", sum_of_digits)

# Sample Input:
# 1234

# Output:
# Sum of Digits = 10
