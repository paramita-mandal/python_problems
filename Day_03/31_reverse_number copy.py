# Reverse a number 

num = int(input("Enter a number: "))

reverse = 0      #'reverse' stores the final reversed number, starting at 0. 
temp = num       #'temp' is a copy of num so we don't lose the original number.

while temp != 0:                   #The loop keeps running as long as temp is not zero 
    digit = temp % 10              # % 10 : picks the last digit
    reverse = reverse * 10 + digit
    temp = temp // 10               #'//' is floor division: it removes the last digit

print(f"Reverse of {num} is {reverse}")
