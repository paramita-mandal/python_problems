# List all prime numbers in a given range

start = int(input("Enter the start of the range: "))
end = int(input("Enter the end of the range: "))  
  
# Function to check if a number is prime
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True
print(f"Prime numbers between {start} and {end}:")
for num in range(start, end + 1):
    if is_prime(num):
        print(num)
        