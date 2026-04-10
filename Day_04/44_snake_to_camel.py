#Convert snake case to camel case

# Step 1: Take input from the user
text = input("Enter a snake_case string: ")

# Step 2: Split the string by underscore
words = text.split("_")

# Step 3: Capitalize the first letter of each word except the first one
camel_case = words[0] + "".join(word.capitalize() for word in words[1:])

# Step 4: Print the result
print("camelCase result:", camel_case)