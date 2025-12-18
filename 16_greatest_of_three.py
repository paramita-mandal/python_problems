#Detect greatest of three numbers
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
num3 = float(input("Enter third number: "))

# Using conditional statements to find the greatest number
#if-elif-else structure to compare the three numbers
if num1 >= num2 and num1 >= num3:
    print("Greatest number =", num1)
elif num2 >= num1 and num2 >= num3:
    print("Greatest number =", num2)
else:
    print("Greatest number =",num3)