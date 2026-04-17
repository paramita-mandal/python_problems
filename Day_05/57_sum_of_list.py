# Sum of all elements in a list

# Step 1: Take input from the user
user_input = input("Enter numbers separated by spaces: ")

# Step 2: Convert input into a list of numbers
numbers = [int(num) for num in user_input.split()]

# Step 3: Start with a total of zero
total = 0

# Step 4: Loop through each number and add it to total
for num in numbers:
    total += num

# Step 5: Print the results
print("\n--- Results ---")
print("Numbers  :", numbers)
print("Count    :", len(numbers))
print("Sum      :", total)
print("Average  :", total / len(numbers))