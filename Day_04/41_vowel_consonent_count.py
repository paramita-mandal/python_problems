# Count vowels and consonants in a string

string = input("Enter a string: ")

# Step 2: Convert to lowercase so 'A' and 'a' are treated the same
normalized = string.lower()

# Step 3: Define all vowels to compare against
vowels = "aeiou"

# Step 4: Initialize counters for vowels and consonants
vowel_count = 0
consonant_count = 0

# Step 5: Loop through each character in the string
for char in normalized:

    # Step 6: Check if the character is a vowel
    if char in vowels:
        vowel_count += 1          # Add 1 to vowel counter

    # Step 7: Check if it's a consonant (letter but NOT a vowel)
    elif char.isalpha():
        consonant_count += 1      # Add 1 to consonant counter

    # Step 8: Skip spaces, numbers, and special characters (no else needed)

# Step 9: Print the final results
print(f"String      : {string}")
print(f"Vowels      : {vowel_count}")
print(f"Consonants  : {consonant_count}")