#Sum of digits of 3-digit number
num = int(input("Enter a 3-digit number: "))

#Extract digits

hundreds = num // 100.     #Perform integer division by 100 to extract the hundreds digit (drops remainder).
tens = (num // 10) % 10    #First remove the last digit with // 10, then use % 10 to get the tens digit.
units = num % 10           #use modulo 10 to obtain the ones (units) digit (the remainder after dividing by 10).

#Calculate sum of digits
sum = hundreds + tens + units

print("Sum of digits:", sum)
