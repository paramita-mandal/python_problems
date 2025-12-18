# # Password strength checker

# Rules we will check:
# Length must be 8 characters or more
# Must contain at least one digit (0–9)
# Must contain at least one uppercase letter (A–Z)
# Must contain at least one lowercase letter (a–z)

# Step 1: Take password input from the user
password = input("Enter your password: ")

# Step 2: Check minimum length
if len(password) < 8:
    print("Weak Password: Must be at least 8 characters long")

# Step 3: Check if password has a digit
elif not any(char.isdigit() for char in password):
    print("Weak Password: Must contain at least one number")

# Step 4: Check if password has an uppercase letter
elif not any(char.isupper() for char in password):
    print("Weak Password: Must contain at least one uppercase letter")

# Step 5: Check if password has a lowercase letter
elif not any(char.islower() for char in password):
    print("Weak Password: Must contain at least one lowercase letter")

# Step 6: If all conditions are satisfied → Strong password
else:
    print("Strong Password!")
