# Extract digits from a string

# Step 1: Take input from the user
text = input("Enter a string: ")

# Step 2: Create an empty string to store digits
digits = ""

# Step 3: Loop through each character and check if it's a digit
for char in text:
    if char.isdigit():
        digits += char

# Step 4: Check if any digits were found
if digits == "":
    print("\n No digits found in the string!")
else:
    # Step 5: Print the results
    print("\n--- Results ---")
    print("Original string :", text)
    print("Extracted digits:", digits)
    print("Total digits    :", len(digits))