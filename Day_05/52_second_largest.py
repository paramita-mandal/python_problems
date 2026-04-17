# Second largest element in a list

# Step 1: Take input from the user
user_input = input("Enter numbers separated by spaces: ")

# Step 2: Convert input into a list of numbers
numbers = [int(num) for num in user_input.split()]

# Step 3: Check if list has at least 2 numbers
if len(numbers) < 2:
    print("Please enter at least 2 numbers!")
else:
    # Step 4: Set initial values for largest and second largest
    largest        = float('-inf')
    second_largest = float('-inf')

    # Step 5: Loop through the list
    for num in numbers:

        # If current number is greater than largest
        if num > largest:
            second_largest = largest   # old largest becomes second
            largest        = num       # new number becomes largest

        # If current number is between largest and second largest
        elif num > second_largest and num != largest:
            second_largest = num

    # Step 6: Print the results
    print("\n--- Results ---")
    print("Numbers        :", numbers)
    print("Largest        :", largest)
    print("Second Largest :", second_largest)