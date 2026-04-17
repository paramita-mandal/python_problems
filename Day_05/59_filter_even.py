#Filter even numbers using list comprehension

# Step 1: Take input from the user
user_input = input("Enter numbers separated by spaces: ")

# Step 2: Convert input into a list of numbers
numbers = [int(num) for num in user_input.split()]

# Step 3: Filter even numbers using list comprehension
even_numbers = [num for num in numbers if num % 2 == 0]

# Step 4: Create squares of even numbers (combined logic)
even_squares = [num**2 for num in numbers if num % 2 == 0]

# Step 5: Print the results
print("\n--- Results ---")
print("Original Numbers :", numbers)
print("Even Numbers     :", even_numbers)
print("Count of Evens   :", len(even_numbers))
print("Sum of Evens     :", sum(even_numbers))
print("Even Squares     :", even_squares)
