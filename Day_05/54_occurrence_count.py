#Count occurrence of each element 

# Step 1: Take input from the user
user_input = input("Enter numbers separated by spaces: ")

# Step 2: Convert input into a list of numbers
numbers = [int(num) for num in user_input.split()]

# Step 3: Create an empty dictionary to store counts
counts = {}

# Step 4: Loop through each number and count it
for num in numbers:
    if num in counts:
        counts[num] += 1
    else:
        counts[num] = 1

# Step 5: Print the results
print("\n--- Results ---")
print("Original list :", numbers)
print("\nOccurrences:")
for element, count in counts.items():
    print(f"  {element} appears {count} time(s)")