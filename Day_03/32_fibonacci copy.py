# Fibonacci Series - First N Terms

n = int(input("Enter the number of terms: "))  # Take input from user

# Initialize the first two terms
a, b = 0, 1

print("Fibonacci Series:")

for i in range(n):           # Loop runs n times
    print(a, end=" ")        # Print current term
    a, b = b, a + b          # Update: a becomes b, b becomes a+b (next term)