text = input("Enter a string: ")

reverse = text[::-1]

if text.lower() == reverse.lower():
    print("The string is a palindrome.")
else:
    print("The string is not a palindrome.")

# Sample Input:
# Madam

# Output:
# The string is a palindrome.
