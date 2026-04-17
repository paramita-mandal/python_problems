#Find maximum and minimum element in a list

# Step 1: Take input from the user
user_input = input("Enter numbers separated by spaces: ")

# Step 2: Convert input into a list of numbers
numbers = [int(num) for num in user_input.split()]

# Step 3: Set the first number as both max and min
max_num = numbers[0]
min_num = numbers[0]

# Step 4: Loop through the list and find max and min
for num in numbers:
    if num > max_num:
        max_num = num
    if num < min_num:
        min_num = num

# Step 5: Print the results
print("\n--- Results ---")
print("Numbers entered :", numbers)
print("Maximum value   :", max_num)
print("Minimum value   :", min_num)


