# List Comprehension: Squares of numbers 

# Step 1: Take input from the user
user_input = input("Enter numbers separated by spaces: ")

# Step 2: Convert input into a list of numbers
numbers = [int(num) for num in user_input.split()]

# Step 3: Create a new list with squares using list comprehension
squares = [num**2 for num in numbers]

# Step 4: Print the results
print("\n--- Results ---")
print("Numbers :", numbers)
print("Squares :", squares)