# A very simple Python code for ATM Cash Withdrawal Rules

# This code checks if a withdrawal request can be processed
# based on the account balance and withdrawal amount.       

print("Hi! Welcome to Python Bank. \nHow much would you like to withdraw?")

balance = int(input("Enter your account balance: "))
amount = int(input("Enter amount to withdraw: "))

# Withdrawal rules:
# 1. Minimum withdrawal amount is 100
# 2. Withdrawal amount should not exceed the account balance    
if amount < 100:
    print("Amount must be at least 100")
elif amount > balance:
    print("Insufficient balance")
else:
    balance -= amount
    print("Withdrawal Successful!")
    print("Remaining Balance:", balance)
