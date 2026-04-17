#Reverse list (without reverse())

# Step 1: Take input from the user
user_input = input("Enter numbers separated by spaces: ")

# Step 2: Convert input into a list of numbers
numbers = [int(num) for num in user_input.split()]

# Step 3: Create an empty list to store reversed numbers
reversed_list = []

# Step 4: Loop from the last index to the first
for i in range(len(numbers) - 1, -1, -1):
    reversed_list.append(numbers[i])

# Step 5: Print the results
print("\n--- Results ---")
print("Original list :", numbers)
print("Reversed list :", reversed_list)