num = int(input("Enter the number of terms: "))

first = 0
second = 1

print("Fibonacci Series:")

for i in range(num):
    print(first, end=" ")
    next_term = first + second
    first = second
    second = next_term

# Sample Input:
# 7

# Output:
# Fibonacci Series:
# 0 1 1 2 3 5 8
