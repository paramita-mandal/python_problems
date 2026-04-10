# Replace a substring with another substring in a string

# Step 1: Take input from the user
sentence = input("Enter a sentence: ")

# Step 2: Ask what to find and what to replace with
old_word = input("Enter the word/phrase to replace: ")
new_word = input("Enter the new word/phrase: ")

# Step 3: Check if the word exists in the sentence
if old_word not in sentence:
    print(f"\n '{old_word}' not found in the sentence!")
else:
    # Step 4: Replace the substring
    result = sentence.replace(old_word, new_word)

    # Step 5: Print the results
    print("\n--- Results ---")
    print("Original  :", sentence)
    print("Replaced  :", result)
    print(f"\n '{old_word}' was replaced with '{new_word}'")