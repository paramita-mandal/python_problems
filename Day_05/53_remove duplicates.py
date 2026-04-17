# Remove duplicates without using set

# Step 1: Take input from the user
user_input = input("Enter numbers separated by spaces: ")

# Step 2: Convert input into a list of numbers
numbers = [int(num) for num in user_input.split()]

# Step 3: Create an empty list to store unique numbers
unique = []

# Step 4: Loop through each number and check for duplicates
for num in numbers:
    if num not in unique:
        unique.append(num)

# Step 5: Print the results
print("\n--- Results ---")
print("Original list :", numbers)
print("Without dupes :", unique)
print("Removed       :", len(numbers) - len(unique), "duplicate(s)")