# Find all pairs with sum K

# Step 1: Take input
numbers = list(map(int, input("Enter numbers: ").split()))
k = int(input("Enter target sum (K): "))

# Step 2: Create empty list to store pairs
pairs = []

# Step 3: Loop through all pairs
for i in range(len(numbers)):
    for j in range(i + 1, len(numbers)):
        if numbers[i] + numbers[j] == k:
            pairs.append((numbers[i], numbers[j]))

# Step 4: Print result
print("\n--- Results ---")
print("Pairs with sum", k, ":", pairs)