# Factorial of a Number

num = int(input("Enter a number: "))

factorial = 1

if num < 0:                            #Factorial doesn't work for negative numbers, and by rule 0! = 1.
    print("Factorial does not exist for negative numbers")
elif num == 0:
    print("Factorial of 0 is 1")
else:
    for i in range(1, num + 1):        #The loop multiplies numbers from 1 up to `num`
        factorial = factorial * i
    print(f"Factorial of {num} is {factorial}")
