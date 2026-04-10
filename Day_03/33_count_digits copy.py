# Count the number of digits in a given integer.

number = input("Enter a number: ")

def count_digits_loop(number):
    number = abs(number)        # Handle negative numbers
    count = 0                   # Initialize counter to 0

    if number == 0:             # Special case: 0 has 1 digit
        return 1

    while number > 0:           # Loop until number becomes 0
        number //= 10           # Remove last digit using integer division
        count += 1              # Increment counter

    return count

print("Number of digits (using loop):", count_digits_loop(int(number))) 