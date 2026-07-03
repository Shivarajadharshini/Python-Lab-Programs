text = input("Enter a string: ")

count = 0

for ch in text.lower():
    if ch in "aeiou":
        count += 1

print("Number of vowels:", count)

# Sample Input:
# OpenAI

# Output:
# Number of vowels: 4
