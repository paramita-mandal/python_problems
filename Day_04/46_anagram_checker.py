# Anagram Checker 
# An anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

# Step 1: Take input from the user
word1 = input("Enter first word: ").lower().strip()
word2 = input("Enter second word: ").lower().strip()

# Step 2: Check if lengths are equal
if len(word1) != len(word2):
    print("Not an Anagram — different lengths!")
else:
    # Step 3: Sort both words and compare
    if sorted(word1) == sorted(word2):
        print(f" '{word1}' and '{word2}' ARE Anagrams!")
    else:
        print(f" '{word1}' and '{word2}' are NOT Anagrams!")