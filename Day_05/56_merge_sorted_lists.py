# Merge two sorted lists 

# Step 1: Take input from the user
input1 = input("Enter first sorted list  (space separated): ")
input2 = input("Enter second sorted list (space separated): ")

# Step 2: Convert inputs into sorted lists of numbers
list1 = [int(num) for num in input1.split()]
list2 = [int(num) for num in input2.split()]

# Step 3: Create an empty list to store merged result
merged = []

# Step 4: Set two pointers for both lists
i = 0   # pointer for list1
j = 0   # pointer for list2

# Step 5: Compare and merge until one list is exhausted
while i < len(list1) and j < len(list2):
    if list1[i] <= list2[j]:
        merged.append(list1[i])
        i += 1
    else:
        merged.append(list2[j])
        j += 1

# Step 6: Add remaining elements from list1
while i < len(list1):
    merged.append(list1[i])
    i += 1

# Step 7: Add remaining elements from list2
while j < len(list2):
    merged.append(list2[j])
    j += 1

# Step 8: Print the results
print("\n--- Results ---")
print("List 1  :", list1)
print("List 2  :", list2)
print("Merged  :", merged)