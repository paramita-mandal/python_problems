# Find longest word in a list of words

# Step 1: Take input from the user
sentence = input("Enter a sentence: ")

# Step 2: Split the sentence into words
words = sentence.split()

# Step 3: Remove punctuation from each word
import string
cleaned_words = []
for word in words:
    cleaned = ""
    for char in word:
        if char not in string.punctuation:
            cleaned += char
    cleaned_words.append(cleaned)

# Step 4: Find the longest word
longest = ""
for word in cleaned_words:
    if len(word) > len(longest):
        longest = word

# Step 5: Print the result
print("\n--- Results ---")
print("Sentence     :", sentence)
print("All words    :", cleaned_words)
print("Longest word :", longest)
print("Its length   :", len(longest), "letters")