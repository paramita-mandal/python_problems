#Find frequency of characters in a string

# Step 1: Take input from the user
text = input("Enter a string: ")

# Step 2: Create an empty dictionary to store character counts
frequency = {}

# Step 3: Loop through each character and count it
for char in text:
    if char in frequency:
        frequency[char] += 1
    else:
        frequency[char] = 1

# Step 4: Print the frequency of each character
print("\nCharacter Frequencies:")
for char, count in frequency.items():
    print(f"  '{char}' → {count}")