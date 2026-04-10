# Clean text data by removing punctuation, converting to lowercase, and removing stop words.

# Step 1: Import the string module
import string

# Step 2: Take input from the user
text = input("Enter a string: ")

# Step 3: Convert to lowercase
lowered = text.lower()

# Step 4: Remove punctuation
cleaned = ""
for char in lowered:
    if char not in string.punctuation:
        cleaned += char

# Step 5: Remove extra spaces
cleaned = cleaned.strip()

# Step 6: Print the results
print("\n--- Results ---")
print("Original :", text)
print("Cleaned  :", cleaned)