# Check if a character is a vowel or consonant

char = input("Enter a single alphabet character: ") 

# Convert it to lowercase to make checking easier
ch = char.lower()

# Check if character is a vowel
if char in ('a', 'e', 'i', 'o', 'u'):
    print("It is a Vowel")

# If not vowel, check if it's an alphabet
elif char.isalpha():
    print("It is a Consonant")

# If it's not a letter at all
else:
    print("Not an Alphabet")
