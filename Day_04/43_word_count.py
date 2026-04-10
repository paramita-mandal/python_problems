# Count words in a string

text = input("Enter a string: ")
# Step 2: Show the original string
print("Original string:", text)

# Step 3: Count the number of words using split()
words = text.split()
word_count = len(words)

print("Number of words:", word_count)
