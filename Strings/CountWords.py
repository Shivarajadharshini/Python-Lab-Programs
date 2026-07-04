text = input("Enter a sentence: ")

text = text.strip()

if text == "":
    print("Number of words: 0")
else:
    words = text.split()
    print("Number of words:", len(words))

# Sample Input:
# Python is easy to learn

# Output:
# Number of words: 5
