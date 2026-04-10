# This code prompts the user for a number and generates its multiplication table from 1 to 10. 

num_str = input("Display multiplication table of? ")

# Convert user input to an integer
num = int(num_str)

# Iterate 10 times from i = 1 to 10
for i in range(1, 11):
    print(f"{num} x {i} = {num * i}") # Using an f-string for formatted output
 
    