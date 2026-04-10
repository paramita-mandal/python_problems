# Reverse a string 

string = input("Enter a string: ")
reverse = ""      # 'reverse' will hold the final reversed string, starting as an empty string.

for char in string:  # Loop through each character in the input string
    reverse = char + reverse  # Prepend the current character to 'reverse'
print(f"Reverse of '{string}' is '{reverse}'")

