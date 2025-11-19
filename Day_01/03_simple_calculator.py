# Simple calculator program
# This program performs basic arithmetic operations based on user input
# This program will take 2 numbers, print sum, diff, product, division.

num1 = float(input("Enter first number: "))
operation = input("Enter operation (+, -, *, /): ")
num2 = float(input("Enter second number: ")) 

# Perform the operation and display the result 
#if and elif statements to check the operation and perform the corresponding calculation
if operation == '+':
    result = num1 + num2
    print("The result is ", result)
elif operation == '-':      
    result = num1 - num2
    print("The result is ", result)
elif operation == '*':
    result = num1 * num2
    print("The result is ", result)
elif operation == '/':
    result = num1 / num2
    print("The result is ", result)
else:
    print("Invalid operation. Please enter one of +, -, *, /.") 
    
