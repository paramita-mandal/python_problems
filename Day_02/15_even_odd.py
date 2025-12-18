# Checking is a number is even or odd
number = int(input("Enter a number: "))

# Using modulo operator (%) to determine even or odd.
#(%:mathematical operation that returns the remainder of a division between two numbers)
# If the remainder when divided by 2 is 0, it's even; otherwise, it's odd.
if number % 2 == 0:
    print(number," is an even number.")
else:
    print(number," is an odd number.")    
    
# "," or "+" are used to concatenate strings and variables in the print function.