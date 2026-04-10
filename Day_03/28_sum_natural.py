#Sum of all natural numbers from 1 to n.

n = int(input("enter a number: "))
i = 1
sum = 0
while (i <= n):         # Loop from 1 to n
    sum = sum + i       # Add current number to sum
    i = i + 1           # Increase number by 1 each time
print("The sum is: ", sum)
