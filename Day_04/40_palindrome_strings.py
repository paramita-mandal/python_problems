# Check if a string is a palindrome

string = input("Enter a string: ")

# Remove all spaces and convert to lowercase for a clean comparison
cleaned = string.replace(" ", "").lower()

# Compare the cleaned string with its reverse ([::-1] reverses it)
if cleaned == cleaned[::-1]:
    print(f"'{string}' is a Palindrome!")
else:
    print(f"'{string}' is NOT a Palindrome!")